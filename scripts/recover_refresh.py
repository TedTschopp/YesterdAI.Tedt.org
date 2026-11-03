#!/usr/bin/env python3
"""Record publication timing and recover stale feeds through GitHub Actions."""
import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlencode

from publish import parse_time

ACTIVE = ('queued', 'in_progress', 'waiting', 'pending', 'requested')


def github_api(method, endpoint, payload=None):
    args = ['gh', 'api', '--method', method, endpoint]
    if payload is not None:
        args += ['--input', '-']
    result = subprocess.run(args, input=json.dumps(payload) if payload is not None else None,
                            text=True, capture_output=True, check=True)
    return json.loads(result.stdout) if result.stdout.strip() else None


def run_timing(run):
    return {key: run.get(key) for key in
            ('id', 'html_url', 'status', 'conclusion', 'created_at', 'run_started_at', 'updated_at', 'head_sha')}


def recover(report, repository, api=github_api, now=None):
    """Dispatch at most one refresh per hour; daily editorial failures stay red."""
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('A GitHub owner/repository is required')
    now = now or datetime.now(timezone.utc)
    base = f'repos/{repository}/actions/workflows/'
    latest = {}
    for key, workflow in (('refresh', 'refresh-wire.yml'), ('deployment', 'deploy.yml')):
        query = {'branch': 'main', 'per_page': 1}
        if key == 'deployment':
            query['status'] = 'success'
        rows = api('GET', base + workflow + '/runs?' + urlencode(query))['workflow_runs']
        latest[key] = run_timing(rows[0]) if rows else None
    result = {'observed_at': now.isoformat().replace('+00:00', 'Z'),
              'public_observed_at': report.get('observed_at'),
              'wire_checked_at': report.get('wire_checked_at'),
              'wire_changed_at': report.get('wire_changed_at'),
              'latest_runs': latest, 'dispatched': False}
    checked = report.get('wire_checked_at')
    age = now - parse_time(checked) if checked else None
    if age is not None and age <= timedelta(hours=3):
        result['reason'] = 'feed_is_not_stale'
        return result
    # Query active runs without a creation cutoff: a long-running job must
    # prevent another dispatch even when it started more than an hour ago.
    for status in ACTIVE:
        query = urlencode({'branch': 'main', 'status': status, 'per_page': 1})
        if api('GET', base + 'refresh-wire.yml/runs?' + query)['workflow_runs']:
            result['reason'] = 'refresh_already_active'
            return result
    cutoff = now - timedelta(hours=1)
    query = {'branch': 'main', 'event': 'workflow_dispatch',
             'created': '>=' + cutoff.isoformat().replace('+00:00', 'Z'), 'per_page': 100}
    # Only existence is needed, so pagination cannot hide a recent dispatch.
    recent = api('GET', base + 'refresh-wire.yml/runs?' + urlencode(query))
    if recent['workflow_runs']:
        result['reason'] = 'dispatch_cooldown'
        return result
    api('POST', base + 'refresh-wire.yml/dispatches', {'ref': 'main'})
    result.update(dispatched=True, reason='stale_feed_refresh_requested')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('--repository', default=os.environ.get('GITHUB_REPOSITORY'))
    args = parser.parse_args()
    report = json.loads(args.report.read_text())
    result = recover(report, args.repository or '')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        # Never include gh's captured stdout/stderr, which can contain headers.
        print(json.dumps({'dispatched': False, 'error': str(error)}))
        sys.exit(1)
