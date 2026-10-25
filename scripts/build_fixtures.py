#!/usr/bin/env python3
"""Build frozen layout cases separately from the deployable site."""
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'test-results/fixture-source'
DESTINATION = ROOT / 'test-results/fixture-site'

def build():
    for directory in (SOURCE, DESTINATION):
        if directory.exists():
            shutil.rmtree(directory)
    SOURCE.mkdir(parents=True)
    for name in ('_config.yml', '_layouts', '_includes', '_plugins', 'assets', 'index.html', 'live.html',
                 'archive.html', 'search.html', 'topics.html', 'about.md', '404.html', 'feed.xml', 'feed.json',
                 'search-index.json', 'sitemap.xml', 'robots.txt', 'status.json'):
        item = ROOT / name
        if item.is_dir():
            shutil.copytree(item, SOURCE / name)
        else:
            shutil.copyfile(item, SOURCE / name)
    shutil.copytree(ROOT / 'tests/fixtures/site', SOURCE, dirs_exist_ok=True)
    shutil.copyfile(ROOT / '_data/topics.yml', SOURCE / '_data/topics.yml')
    subprocess.run(['bundle', 'exec', 'jekyll', 'build', '--config', str(SOURCE / '_config.yml'),
                    '--source', str(SOURCE), '--destination', str(DESTINATION), '--strict_front_matter'], cwd=ROOT, check=True)
    subprocess.run([str(ROOT / 'node_modules/.bin/pagefind'), '--site', str(DESTINATION),
                    '--glob', 'articles/**/index.html'], cwd=ROOT, check=True)

if __name__ == '__main__':
    build()
