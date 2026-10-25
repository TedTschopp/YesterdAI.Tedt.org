#!/usr/bin/env python3
"""Check rendered internal links, IDs, metadata, feeds, and image paths offline."""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import sys
import xml.etree.ElementTree as ET
import yaml
from publish import read_document, word_count, parse_time
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1] / '_site'
SOURCE = Path(__file__).resolve().parents[1]


def check_metadata(path, soup, root, config, errors):
    """Verify the rendered search/social contract, including page identity."""
    relative = path.relative_to(root)
    values = {}
    for node in soup.select('meta[content]'):
        key = node.get('property', node.get('name'))
        values.setdefault(key, []).append(node['content'])
    required = ('description', 'author', 'robots', 'og:site_name', 'og:locale', 'og:title',
                'og:description', 'og:url', 'og:type', 'og:image', 'og:image:secure_url',
                'og:image:alt', 'og:image:width', 'og:image:height', 'og:image:type',
                'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image', 'twitter:image:alt')
    for key in required:
        if len(values.get(key, [])) != 1 or not values[key][0].strip():
            errors.append(f'{relative}: exactly one nonempty {key} required')
    meta = lambda key: values.get(key, [None])[0]
    for first, second in [('description', 'og:description'), ('og:title', 'twitter:title'),
                          ('og:description', 'twitter:description'), ('og:image', 'twitter:image'),
                          ('og:image', 'og:image:secure_url'), ('og:image:alt', 'twitter:image:alt')]:
        if meta(first) != meta(second):
            errors.append(f'{relative}: {first} and {second} differ')
    canonical = soup.select_one('link[rel="canonical"]')
    if canonical and (not canonical['href'].startswith(config['url'] + '/') or meta('og:url') != canonical['href']):
        errors.append(f'{relative}: canonical and social URL must identify this HTTPS page')
    graph = []
    try:
        for script in soup.select('script[type="application/ld+json"]'):
            data = json.loads(script.get_text())
            graph.extend(data.get('@graph', [data]) if isinstance(data, dict) else data)
        if not graph:
            raise ValueError('missing JSON-LD')
    except (ValueError, TypeError) as error:
        errors.append(f'{relative}: invalid structured data: {error}')
        return
    if relative == Path('index.html'):
        website = next((n for n in graph if n.get('@type') == 'WebSite'), {})
        if (meta('og:title') != config['home_title'] or soup.title.get_text() != config['home_title']
                or meta('description') != config['description'] or meta('og:type') != 'website'
                or meta('og:image') != config['url'] + config['share_image']['path']
                or website.get('name') != config['title'] or website.get('description') != config['description']):
            errors.append('Homepage metadata must describe the publication, independently of its latest edition')
    elif relative.parts[0] == 'articles':
        record, _ = read_document(SOURCE / '_articles' / (relative.parts[1] + '.md'))
        article = next((n for n in graph if n.get('@type') == 'NewsArticle'), {})
        modified = record.get('modified_at', record['published_at'])
        if (meta('og:title') != record['title'] or meta('description') != record['summary']
                or meta('og:type') != 'article' or meta('article:section') != record['section']
                or meta('article:published_time') != record['published_at']
                or meta('article:modified_time') != modified
                or article.get('headline') != record['title'] or article.get('description') != record['summary']
                or article.get('datePublished') != record['published_at'] or article.get('dateModified') != modified):
            errors.append(f'{relative}: metadata must describe this article and retain its actual dates')
        hero = record.get('hero')
        if hero:
            expected = config['url'] + hero['path']
            if meta('og:image') != expected or article.get('image', [{}])[0].get('url') != expected:
                errors.append(f'{relative}: social/structured image must belong to this article')
            caption = soup.select_one('.article-figure figcaption')
            if hero.get('caption') and (not caption or caption.get_text() != hero['caption']):
                errors.append(f'{relative}: render the story-specific image caption')
        if meta('og:title') != soup.h1.get_text():
            errors.append(f'{relative}: headline capitalization must match across the page and social metadata')


def check(root=ROOT):
    errors, pages = [], {}
    config = yaml.safe_load((SOURCE / '_config.yml').read_text())
    for path in root.rglob('*.html'):
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        pages[path] = soup
        check_metadata(path, soup, root, config, errors)
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
