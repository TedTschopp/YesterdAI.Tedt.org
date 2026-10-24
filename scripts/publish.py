#!/usr/bin/env python3
"""Deterministic feed ingestion, editorial validation, and safe publication.

Research and image generation are performed by Codex, never by a paid API here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import struct
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

import yaml

ROOT = Path(__file__).resolve().parents[1]
PACIFIC = ZoneInfo('America/Los_Angeles')
FEEDS = {'curated': 'https://rss.tedt.org/ai_rss_feed.json', 'top': 'https://rss.tedt.org/feeds/top.json'}
SECTIONS = {'Big Moves', 'Enterprise Ops', 'Vendors', 'Security', 'Policy'}
EDITORIAL_PATHS = ('_articles/', '_editions/', '_data/', 'assets/images/', 'docs/runs/')
PRIORITY = {'!': 'Essential', '*': 'Important', '~': 'Optional'}
TECH = {'◻': 'Informational', '◼': 'Important', '⬢': 'Transformational'}


def utc_now():
    return datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')


def parse_time(value):
    dt = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    if dt.tzinfo is None:
        raise ValueError(f'Timezone required: {value}')
    return dt


def cutoff_for(day):
    return datetime.fromisoformat(str(day)).replace(hour=5, tzinfo=PACIFIC)


def in_window(value, cutoff, precision='second'):
    end = parse_time(cutoff) if not isinstance(cutoff, datetime) else cutoff
    # Timedeltas must use UTC to represent exactly 36 elapsed hours across DST.
    start = end.astimezone(timezone.utc) - timedelta(hours=36)
    if precision == 'day':
        # A date-only original source needs an explicitly evidenced timezone.
        beginning = parse_time(value)
        finish = (beginning.replace(tzinfo=None) + timedelta(days=1)).replace(tzinfo=beginning.tzinfo)
        return start <= beginning and finish <= end
    moment = parse_time(value)
    return start <= moment <= end


def canonical_url(value):
    u = urlsplit(value)
    if u.scheme != 'https' or not u.hostname or u.username or u.password:
        raise ValueError(f'Public HTTPS URL required: {value}')
    if u.hostname in {'localhost', '127.0.0.1', '::1'}:
        raise ValueError('Local URLs are not public source evidence')
    query = [(k, v) for k, v in parse_qsl(u.query, keep_blank_values=True)
             if not k.lower().startswith('utm_') and k.lower() not in {'fbclid', 'gclid', 'mc_cid', 'mc_eid'}]
    return urlunsplit(('https', u.netloc.lower(), u.path.rstrip('/') or '/', urlencode(sorted(query)), ''))


def story_id(url):
    return 'art_' + hashlib.sha256(canonical_url(url).encode()).hexdigest()[:16]


def clean_title(title):
    markers = re.findall(r'\[\s*([!*~◻◼⬢])\s*\]', title)
    return re.sub(r'\s*\[\s*[!*~◻◼⬢]\s*\]', '', title).strip(), next((PRIORITY[m] for m in markers if m in PRIORITY), ''), next((TECH[m] for m in markers if m in TECH), '')


def atomic_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, delete=False, encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
        temp = f.name
    os.replace(temp, path)


def get_json(url):
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={'User-Agent': 'YesterdayInAI/1.0 (+https://yesterdai.tedt.org/about/)', 'Cache-Control': 'no-cache'}), timeout=45) as response:
                raw = response.read(8_000_001)
                if len(raw) > 8_000_000:
                    raise ValueError('Feed exceeds 8 MB limit')
                return json.loads(raw)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(attempt + 1)


def validate_feed(feed, label):
    if not isinstance(feed, dict) or feed.get('version') not in {'https://jsonfeed.org/version/1', 'https://jsonfeed.org/version/1.1'}:
        raise ValueError(f'{label}: invalid JSON Feed')
    if not isinstance(feed.get('items'), list) or not feed['items']:
        raise ValueError(f'{label}: unexpectedly empty or missing items; preserve previous snapshot')
    seen, valid, excluded = set(), [], []
    for item in feed['items']:
        try:
            if not isinstance(item, dict) or any(not isinstance(item.get(k), str) or not item[k].strip() for k in ('id', 'url', 'title', 'content_text', 'date_published')):
                raise ValueError('malformed item fields')
            canonical_url(item['url'])
            parse_time(item['date_published'])
            if item['id'] in seen:
                raise ValueError('duplicate feed ID')
            seen.add(item['id'])
            valid.append(item)
        except ValueError as error:
            excluded.append({'id': item.get('id') if isinstance(item, dict) else None, 'reason': str(error)})
    if not valid:
        raise ValueError(f'{label}: no usable feed items; preserve previous snapshot')
    return {**feed, 'items': valid, '_excluded_items': feed.get('_excluded_items', []) + excluded}


def normalized_wire(feed, fetched_at):
    feed = validate_feed(feed, 'top')
    items, seen = [], set()
    for original in feed['items']:
        url = canonical_url(original['url'])
        if url in seen:
            continue
        seen.add(url)
        title, rating, technical = clean_title(original['title'])
        items.append({'id': original['id'], 'url': original['url'], 'canonical_url': url, 'title': title,
                      'summary': original['content_text'], 'publisher': urlsplit(url).hostname.removeprefix('www.'),
                      'date_published': original['date_published'],
                      'date_precision': 'day' if 'T00:00:00' in original['date_published'] else 'second',
                      'rating': rating, 'technical_rating': technical})
    return {'source_url': FEEDS['top'], 'last_success_at': fetched_at, 'items': items}


def refresh(root=ROOT):
    # Read and validate both feeds before replacing either last-known-good file.
    raw = {name: validate_feed(get_json(url), name) for name, url in FEEDS.items()}
    wire_path = root / '_data/wire.json'
    wire = normalized_wire(raw['top'], utc_now())
    previous = json.loads(wire_path.read_text()) if wire_path.exists() else None
    if previous and previous.get('items') == wire['items']:
        wire['last_success_at'] = previous['last_success_at']
    discovery_path = root / '_data/discovery.json'
    discovery = {'feeds': raw}
    if not wire_path.exists() or previous != wire:
        atomic_json(wire_path, wire)
    if not discovery_path.exists() or json.loads(discovery_path.read_text()) != discovery:
        atomic_json(discovery_path, discovery)
    print(json.dumps({'curated': len(raw['curated']['items']), 'top': len(raw['top']['items']), 'wire': len(wire['items']), 'checked_at': utc_now()}))


def read_document(path):
    raw = Path(path).read_text(encoding='utf-8')
    parts = raw.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError(f'{path}: missing front matter')
    metadata = yaml.safe_load(parts[1])
    if not isinstance(metadata, dict):
        raise ValueError(f'{path}: front matter must be a mapping')
    return metadata, parts[2].strip()


def word_count(body):
    body = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', body)
    body = re.sub(r'<[^>]*>', '', body)
    return len(re.findall(r"\b[\w]+(?:[’'–-][\w]+)*\b", body))


def image_dimensions(path):
    data = Path(path).read_bytes()
    if data[:4] != b'RIFF' or data[8:12] != b'WEBP':
        raise ValueError('Not a WebP image')
    offset = 12
    while offset + 8 <= len(data):
        kind = data[offset:offset + 4]
        size = int.from_bytes(data[offset + 4:offset + 8], 'little')
        chunk = data[offset + 8:offset + 8 + size]
        if kind == b'VP8X' and len(chunk) >= 10:
            return int.from_bytes(chunk[4:7], 'little') + 1, int.from_bytes(chunk[7:10], 'little') + 1
        if kind == b'VP8 ' and len(chunk) >= 10 and chunk[3:6] == b'\x9d\x01\x2a':
            return struct.unpack('<H', chunk[6:8])[0] & 0x3fff, struct.unpack('<H', chunk[8:10])[0] & 0x3fff
        if kind == b'VP8L' and len(chunk) >= 5 and chunk[0] == 0x2f:
            bits = int.from_bytes(chunk[1:5], 'little')
            return (bits & 0x3fff) + 1, ((bits >> 14) & 0x3fff) + 1
        offset += 8 + size + (size % 2)
    raise ValueError('WebP dimensions unavailable')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(root=ROOT, allow_empty=False):
    articles, editions = {}, {}
    for file in sorted((root / '_editions').glob('*.md')):
        ed, body = read_document(file)
        label = f'Edition {file.stem}'
        require(str(ed.get('edition_date')) == file.stem, f'{label}: edition date / filename mismatch')
        expected = cutoff_for(file.stem)
        require(parse_time(ed['cutoff']) == expected, f'{label}: cutoff must be 5 a.m. Pacific')
        require(parse_time(ed['window_start']) == expected.astimezone(timezone.utc) - timedelta(hours=36), f'{label}: exact 36-hour window required')
        require(isinstance(ed.get('article_ids'), list) and len(ed['article_ids']) <= 8, f'{label}: at most eight articles')
        require(len(ed['article_ids']) == len(set(ed['article_ids'])), f'{label}: repeated article ID')
        require(isinstance(ed.get('tldr'), list) and len(ed['tldr']) > 0, f'{label}: TL;DR required')
        require(ed['article_ids'] or ed.get('quiet_day') is True, f'{label}: empty edition needs verified quiet_day flag')
        require(ed.get('source_snapshot') or not ed.get('retrospective'), f'{label}: retrospective snapshot required')
        require(parse_time(ed['prepared_at']) >= expected, f'{label}: cannot claim preparation before cutoff')
        editions[file.stem] = ed
    require(allow_empty or editions, 'No editions available for publication')
    for file in sorted((root / '_articles').glob('*.md')):
        a, body = read_document(file)
        label = f'Article {file.stem}'
        for key in ('article_id', 'title', 'summary', 'section', 'edition_date', 'published_at', 'eligibility', 'sources', 'hero', 'leader_action', 'individual_action', 'feed_summary', 'feed_name'):
            require(a.get(key), f'{label}: {key} required')
        require(a['article_id'] not in articles, f'{label}: duplicate ID')
        require(a['section'] in SECTIONS, f'{label}: invalid section')
        ed = editions.get(str(a['edition_date']))
        require(ed is not None and a['article_id'] in ed['article_ids'], f'{label}: edition membership missing')
        require(800 <= word_count(body) <= 1200, f'{label}: {word_count(body)} words, expected 800–1,200')
        require(len(a['title'].split()) <= 12, f'{label}: headline exceeds 12 words')
        require(not any(c in a['title'] for c in '<>'), f'{label}: headline must be plain text')
        require(not re.search(r'<\s*(script|iframe|object|style)\b', body, re.I), f'{label}: active HTML is not permitted in editorial content')
        require(parse_time(a['published_at']) >= parse_time(ed['cutoff']), f'{label}: publication date predates coverage cutoff')
        eligibility = a['eligibility']
        require(eligibility.get('verification') in {'jsonld', 'meta', 'visible', 'publisher_api'}, f'{label}: verify original source date, not feed placeholder')
        require(eligibility.get('evidence'), f'{label}: timestamp evidence required')
        require(in_window(eligibility['published_at'], ed['cutoff'], eligibility.get('precision', 'second')), f'{label}: original reporting outside window or uncertain date boundary')
        source_urls = set()
        for source in a['sources']:
            source_urls.add(canonical_url(source['url']))
            require(parse_time(source['published_at']) <= parse_time(ed['cutoff']), f'{label}: source from after historical cutoff')
        require(canonical_url(eligibility['url']) in source_urls, f'{label}: eligibility source missing from citations')
        linked = {canonical_url(u) for u in re.findall(r'\]\((https://[^\s)]+)\)', body)}
        require(linked & source_urls, f'{label}: inline source link required')
        hero = a['hero']
        require(hero.get('alt') and hero.get('prompt') and hero.get('generated_at'), f'{label}: hero alt, prompt, generation date required')
        image = (root / hero['path'].lstrip('/')).resolve()
        require(image.is_relative_to((root / 'assets/images').resolve()) and image.is_file(), f'{label}: missing project hero image')
        require(image.suffix == '.webp' and image.read_bytes()[:4] == b'RIFF', f'{label}: expected real WebP hero')
        require(image.stat().st_size > 1000, f'{label}: hero appears empty')
        require(hero.get('width', 0) >= 1000 and hero.get('height', 0) >= 500, f'{label}: hero dimensions too small')
        require(image_dimensions(image) == (hero['width'], hero['height']), f'{label}: hero dimensions do not match asset')
        parse_time(hero['generated_at'])
        require(hero.get('tool') == 'image_gen', f'{label}: built-in generated image required')
        a['_file'] = str(file)
        a['_canonical'] = canonical_url(eligibility['url'])
        articles[a['article_id']] = a
    for day, ed in editions.items():
        for article_id in ed['article_ids']:
            require(article_id in articles, f'Edition {day}: missing article {article_id}')
    ordered = sorted(articles.values(), key=lambda a: str(a['edition_date']))
    for index, a in enumerate(ordered):
        for prior in ordered[:index]:
            gap = (datetime.fromisoformat(str(a['edition_date'])) - datetime.fromisoformat(str(prior['edition_date']))).days
            repeated = a['_canonical'] == prior['_canonical'] or (a.get('story_key') and a.get('story_key') == prior.get('story_key'))
            if gap <= 7 and repeated:
                require(a.get('update_of') == prior['article_id'] and a.get('substantive_update'), f'{a["_file"]}: duplicate coverage needs a documented substantive update')
    print(f'Validated {len(editions)} editions, {len(articles)} complete researched articles and heroes.')
    return len(editions), len(articles)


def run(*args, cwd=ROOT, capture=False):
    result = subprocess.run(args, cwd=cwd, text=True, check=True, capture_output=capture)
    return result.stdout.strip() if capture else ''


def ship(root=ROOT):
    """Publish only already-committed editorial work; never stage unrelated files."""
    require(not run('git', 'status', '--porcelain', cwd=root, capture=True), 'Commit completed editorial changes before ship; working tree must be clean')
    for attempt in range(3):
        run('git', 'fetch', 'origin', 'main', cwd=root)
        changed = run('git', 'diff', '--name-only', 'origin/main...HEAD', cwd=root, capture=True).splitlines()
        require(changed and all(p.startswith(EDITORIAL_PATHS) for p in changed), 'Ship accepts editorial-only commits')
        run('git', 'rebase', 'origin/main', cwd=root)
        run(sys.executable, str(root / 'scripts/publish.py'), 'validate', cwd=root)
        run(sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', cwd=root)
        run('bundle', 'exec', 'jekyll', 'build', '--strict_front_matter', cwd=root)
        run(sys.executable, str(root / 'scripts/check_site.py'), cwd=root)
        try:
            run('git', 'push', 'origin', 'HEAD:main', cwd=root)
            return
        except subprocess.CalledProcessError:
            if attempt == 2:
                raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['refresh', 'validate', 'ship', 'cutoff'])
    parser.add_argument('--allow-empty', action='store_true')
    parser.add_argument('--date')
    args = parser.parse_args()
    if args.command == 'refresh':
        refresh()
    elif args.command == 'validate':
        validate(allow_empty=args.allow_empty)
    elif args.command == 'ship':
        ship()
    else:
        end = cutoff_for(args.date or datetime.now(PACIFIC).date())
        print(json.dumps({'edition_date': str(end.date()), 'cutoff': end.isoformat(), 'window_start': (end.astimezone(timezone.utc) - timedelta(hours=36)).isoformat()}))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        print(f'Publication stopped: {error}', file=sys.stderr)
        sys.exit(1)
