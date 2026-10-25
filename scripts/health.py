#!/usr/bin/env python3
"""Read-only publication watchdog, independent of local editorial production."""
import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
from urllib.request import Request, urlopen

from publish import PACIFIC, ROOT, parse_time, read_document


def snapshot(root=ROOT):
    editions = [read_document(path)[0] for path in (root / '_editions').glob('*.md')]
    wire = json.loads((root / '_data/wire.json').read_text())
    return {'version': 1, 'latest_edition': max((str(e['edition_date']) for e in editions), default=None),
            'wire_checked_at': wire.get('last_checked_at', wire.get('last_success_at')),
            'wire_changed_at': wire.get('last_changed_at', wire.get('last_success_at'))}


def assess(data, now=None):
    now = now or datetime.now(timezone.utc)
    local = now.astimezone(PACIFIC)
    expected = local.date() if local.hour >= 7 else local.date() - timedelta(days=1)
    errors = []
    latest = data.get('latest_edition')
    if not latest or datetime.fromisoformat(latest).date() < expected:
        errors.append(f'Expected an edition for {expected}; latest published edition is {latest or "missing"}. Check the 5 a.m. Codex task and host availability.')
    checked = data.get('wire_checked_at')
    if not checked or now - parse_time(checked) > timedelta(hours=3):
        errors.append('No successful live-feed check in three hours. Inspect Refresh live news in GitHub Actions.')
    elif parse_time(checked) - now > timedelta(minutes=5):
        errors.append('Feed-check timestamp is in the future; inspect the producer clock.')
    return {'ok': not errors, 'expected_edition': str(expected), 'latest_edition': latest,
            'wire_checked_at': checked, 'errors': errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--public', action='store_true', help='Check the deployed status.json rather than local source files')
    args = parser.parse_args()
    if args.public:
        request = Request('https://yesterdai.tedt.org/status.json', headers={'User-Agent': 'YesterdayInAI-Health/2.0', 'Cache-Control': 'no-cache'})
        with urlopen(request, timeout=30) as response:
            data = json.load(response)
    else:
        data = snapshot()
    result = assess(data)
    print(json.dumps(result, indent=2))
    return 0 if result['ok'] else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as error:
        print(f'Publication health check failed: {error}', file=sys.stderr)
        sys.exit(1)
