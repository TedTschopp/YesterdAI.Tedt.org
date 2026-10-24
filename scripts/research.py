#!/usr/bin/env python3
"""Cache historical feed snapshots and read public source metadata for Codex.

Full source text stays in ignored .cache; only short evidence records are published.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import subprocess
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from publish import ROOT, PACIFIC, FEEDS, cutoff_for, canonical_url, atomic_json, utc_now

CACHE = ROOT / '.cache'


def fetch(url):
    with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; YesterdayInAI/1.0; +https://yesterdai.tedt.org/about/)'}), timeout=35) as r:
        return r.read(6_000_000).decode('utf-8', errors='replace')


def history(last_day, days):
    CACHE.mkdir(exist_ok=True)
    for offset in reversed(range(days)):
        day = (datetime.fromisoformat(last_day).date() - timedelta(days=offset)).isoformat()
        end = cutoff_for(day)
        dest = CACHE / 'history' / (day + '.json')
        if dest.exists():
            continue
        query = f'repos/TedTschopp/rss.tedt.org/commits?path=feeds/top.json&until={end.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")}&per_page=1'
        result = subprocess.run(['gh', 'api', query, '--jq', '.[0].sha'], check=True, text=True, capture_output=True)
        sha = result.stdout.strip()
        if len(sha) != 40:
            raise ValueError(f'No historical snapshot for {day}')
        feeds = {}
        for name, path in [('curated', 'ai_rss_feed.json'), ('top', 'feeds/top.json')]:
            feeds[name] = json.loads(fetch(f'https://raw.githubusercontent.com/TedTschopp/rss.tedt.org/{sha}/{path}'))
        data = {'edition_date': day, 'cutoff': end.isoformat(), 'window_start': (end.astimezone(timezone.utc) - timedelta(hours=36)).isoformat(), 'snapshot': sha, 'feeds': feeds}
        atomic_json(dest, data)
        print(f'{day}: {sha[:10]} · curated {len(feeds["curated"]["items"])} · ranked {len(feeds["top"]["items"])}', flush=True)


def read_source(url):
    key = hashlib.sha256(url.encode()).hexdigest()[:20]
    path = CACHE / 'sources' / (key + '.json')
    if path.exists():
        return json.loads(path.read_text())
    try:
        html = fetch(url)
        soup = BeautifulSoup(html, 'html.parser')
        metadata = [{'property': x.get('property', x.get('name')), 'content': x.get('content')} for x in soup.find_all('meta') if any(k in str(x.get('property', x.get('name', ''))).lower() for k in ('date', 'time', 'title', 'description', 'published', 'modified'))]
        ld = []
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                ld.append(json.loads(script.get_text()))
            except ValueError:
                pass
        times = [{'datetime': x.get('datetime'), 'text': x.get_text(' ', strip=True)} for x in soup.find_all('time')]
        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'noscript', 'svg']):
            tag.decompose()
        article = soup.find('article') or soup.find('main') or soup.body or soup
        data = {'url': url, 'retrieved_at': utc_now(), 'title': soup.title.get_text(' ', strip=True) if soup.title else '', 'metadata': metadata, 'jsonld': ld, 'times': times, 'text': article.get_text('\n', strip=True)[:90000]}
    except Exception as e:
        data = {'url': url, 'error': str(e)}
    atomic_json(path, data)
    return data


def candidates():
    for path in sorted((CACHE / 'history').glob('*.json')):
        data = json.loads(path.read_text())
        start, end = data['window_start'][:10], data['cutoff'][:10]
        print('\n' + data['edition_date'] + ' · ' + data['snapshot'][:10])
        seen = set()
        for name in ['curated', 'top']:
            count = 0
            for item in data['feeds'][name]['items']:
                if start <= item['date_published'][:10] <= end and item['url'] not in seen:
                    seen.add(item['url'])
                    print(f'{name}: {item["date_published"]} | {item["title"]} | {item["url"]}')
                    count += 1
                    if name == 'top' and count >= 25:
                        break


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('command', choices=['history', 'candidates', 'read'])
    p.add_argument('--date', default=str(datetime.now(PACIFIC).date()))
    p.add_argument('--days', type=int, default=7)
    p.add_argument('urls', nargs='*')
    a = p.parse_args()
    if a.command == 'history':
        history(a.date, a.days)
    elif a.command == 'candidates':
        candidates()
    else:
        with ThreadPoolExecutor(max_workers=6) as pool:
            for result in pool.map(read_source, a.urls):
                print(json.dumps({k: v for k, v in result.items() if k != 'text'}, ensure_ascii=False))
