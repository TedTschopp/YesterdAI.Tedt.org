#!/usr/bin/env python3
"""Check rendered internal links, IDs, metadata, feeds, and image paths offline."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys
import xml.etree.ElementTree as ET
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
    for name in ('feed.json', 'search-index.json'):
        try:
            json.loads((root / name).read_text())
        except (OSError, ValueError) as error:
            errors.append(f'{name}: {error}')
    for name in ('feed.xml', 'sitemap.xml'):
        try:
            ET.parse(root / name)
        except (OSError, ET.ParseError) as error:
            errors.append(f'{name}: {error}')
    size = sum(path.stat().st_size for path in root.rglob('*') if path.is_file())
    if size > 900_000_000:
        errors.append('Site exceeds 900 MB publication budget')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f'Checked {len(pages)} HTML pages, internal links, accessibility metadata, feeds, and sitemap; {size / 1_000_000:.1f} MB.')


if __name__ == '__main__':
    check()
