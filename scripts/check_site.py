#!/usr/bin/env python3
"""Check rendered internal links, IDs, metadata, feeds, and image paths offline."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys
import xml.etree.ElementTree as ET
from publish import read_document, word_count, parse_time
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1] / '_site'


def check(root=ROOT):
    errors, pages = [], {}
    for path in root.rglob('*.html'):
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        pages[path] = soup
        if not soup.title or not soup.find('h1') or len(soup.find_all('h1')) != 1:
            errors.append(f'{path.relative_to(root)}: exactly one title and h1 required')
        if not soup.select_one('link[rel="canonical"]') or not soup.select_one('meta[name="description"]'):
            errors.append(f'{path.relative_to(root)}: missing canonical or description')
        forbidden = {'Looking Ahead', 'Editor’s notes and source record', "Editor's notes and source record", 'Sources and editorial record', 'Supplied feed summary and rating'}
        if any(node.get_text(strip=True) in forbidden for node in soup.select('h1,h2,h3,summary')):
            errors.append(f'{path.relative_to(root)}: internal production section is visible')
        if 'Reconstructed from historical feed snapshots.' in soup.get_text() or 'reporting cutoff' in soup.get_text():
            errors.append(f'{path.relative_to(root)}: production timing prose is visible')
        share = soup.select_one('meta[property="og:image"]')
        if not share or not (root / urlsplit(share['content']).path.lstrip('/')).is_file():
            errors.append(f'{path.relative_to(root)}: missing local social image')
        for image in soup.find_all('img'):
            if not all(image.has_attr(key) for key in ('alt', 'width', 'height')):
                errors.append(f'{path.relative_to(root)}: image needs alt, width, height')
        ids = [tag['id'] for tag in soup.select('[id]')]
        if len(ids) != len(set(ids)):
            errors.append(f'{path.relative_to(root)}: duplicate HTML ID')
    for path, soup in pages.items():
        for tag, attr in [('a', 'href'), ('img', 'src'), ('script', 'src'), ('link', 'href')]:
            for node in soup.find_all(tag):
                url = node.get(attr, '')
                parsed = urlsplit(url)
                if parsed.scheme or parsed.netloc or not url:
                    continue
                target = (root / unquote(parsed.path).lstrip('/')) if parsed.path.startswith('/') else path.parent / unquote(parsed.path)
                if not parsed.path:
                    target = path
                if target.is_dir():
                    target /= 'index.html'
                if not target.exists():
                    errors.append(f'{path.relative_to(root)}: broken {attr} {url}')
                elif parsed.fragment and target in pages and not pages[target].find(id=unquote(parsed.fragment)):
                    errors.append(f'{path.relative_to(root)}: missing anchor {url}')
    for name in ('feed.json', 'search-index.json', 'status.json'):
        try:
            json.loads((root / name).read_text())
        except (OSError, ValueError) as error:
            errors.append(f'{name}: {error}')
    for name in ('feed.xml', 'sitemap.xml'):
        try:
            ET.parse(root / name)
        except (OSError, ET.ParseError) as error:
            errors.append(f'{name}: {error}')
    if not (root / 'pagefind/pagefind.js').is_file():
        errors.append('Missing Pagefind search bundle; index after building Jekyll')
    homepage = pages.get(root / 'index.html')
    if homepage:
        briefing = ' '.join(node.get_text(' ', strip=True) for node in homepage.select('.briefing-heading,.briefing-main'))
        if word_count(briefing) > 850:
            errors.append(f'Homepage exceeds five-minute editorial budget: {word_count(briefing)} words')
        if homepage.select('.tldr-panel li') and not homepage.select('.tldr-panel a'):
            # A valid quiet day has text explaining no stories, so only require links when previews exist.
            if homepage.select('.story-row'):
                errors.append('Homepage takeaways must link to researched stories')
    baseline_path = Path(__file__).resolve().parents[1] / 'tests/fixtures/preservation-baseline.json'
    if baseline_path.exists():
        baseline = json.loads(baseline_path.read_text())
        for slug, record in baseline['articles'].items():
            page = pages.get(root / 'articles' / slug / 'index.html')
            if page:
                for anchor in record['anchors'] + ['actions-heading', 'sources-heading']:
                    if not page.find(id=anchor):
                        errors.append(f'articles/{slug}: lost original anchor {anchor}')
    try:
        feed = json.loads((root / 'feed.json').read_text())
        xml = ET.parse(root / 'feed.xml')
        rss = {item.findtext('guid'): item for item in xml.findall('./channel/item')}
        for item in feed['items']:
            target = root / urlsplit(item['url']).path.lstrip('/') / 'index.html'
            page = pages.get(target)
            if page:
                expected = page.select_one('.article-body').get_text(' ', strip=True).split()
                actual = BeautifulSoup(item['content_html'], 'html.parser').get_text(' ', strip=True).split()
                if expected != actual:
                    errors.append(f'{item["url"]}: JSON feed differs from article prose')
            counterpart = rss.get(item['id'])
            if counterpart is None or counterpart.findtext('{http://purl.org/rss/1.0/modules/content/}encoded') != item['content_html']:
                errors.append(f'{item["url"]}: RSS and JSON content differ')
            if parse_time(item['date_modified']) < parse_time(item['date_published']):
                errors.append(f'{item["url"]}: feed update predates publication')
        status = json.loads((root / 'status.json').read_text())
        parse_time(status['wire_checked_at'])
        parse_time(status['wire_changed_at'])
    except (OSError, ValueError, KeyError, TypeError, AttributeError, ET.ParseError) as error:
        errors.append(f'Publication contract: {error}')
    size = sum(path.stat().st_size for path in root.rglob('*') if path.is_file())
    if size > 900_000_000:
        errors.append('Site exceeds 900 MB publication budget')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f'Checked {len(pages)} HTML pages, internal links, accessibility metadata, feeds, and sitemap; {size / 1_000_000:.1f} MB.')


if __name__ == '__main__':
    check()
