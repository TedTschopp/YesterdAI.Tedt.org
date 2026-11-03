from datetime import datetime, timezone
from pathlib import Path
import sys
import unittest
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from recover_refresh import recover


class RecoveryTests(unittest.TestCase):
    now = datetime(2026, 11, 2, 20, tzinfo=timezone.utc)

    def execute(self, checked='2026-11-02T16:59:59Z', active=None, dispatched=False, fail=False, missing=False):
        calls = []

        def api(method, endpoint, payload=None):
            calls.append((method, endpoint, payload))
            if fail:
                raise OSError('GitHub unavailable')
            if method == 'POST':
                return None
            query = parse_qs(urlsplit(endpoint).query)
            rows = []
            if not missing and 'status' not in query and 'event' not in query:
                rows = [{'id': 1, 'status': 'completed', 'conclusion': 'success'}]
            if not missing and query.get('status') == ['success']:
                rows = [{'id': 2, 'status': 'completed', 'conclusion': 'success'}]
            if query.get('status') == [active] or (dispatched and query.get('event') == ['workflow_dispatch']):
                if 'branch' not in query:
                    rows = [{'id': 10, 'created_at': '2026-11-02T10:00:00Z', 'head_branch': 'manual-branch'}]
            return {'workflow_runs': rows, 'total_count': len(rows)}

        report = {'wire_checked_at': checked, 'observed_at': '2026-11-02T20:00:00Z', 'ok': False}
        return recover(report, 'TedTschopp/YesterdAI.Tedt.org', api, self.now), calls

    def test_stale_feed_dispatches_only_main_and_retains_observation(self):
        result, calls = self.execute()
        self.assertTrue(result['dispatched'])
        self.assertEqual([call for call in calls if call[0] == 'POST'],
                         [('POST', 'repos/TedTschopp/YesterdAI.Tedt.org/actions/workflows/refresh-wire.yml/dispatches', {'ref': 'main'})])
        self.assertEqual(result['public_observed_at'], '2026-11-02T20:00:00Z')

    def test_daily_editorial_failure_does_not_refresh_a_healthy_feed(self):
        for checked in ('2026-11-02T17:00:00Z', '2026-11-02T21:00:00Z'):
            with self.subTest(checked=checked):
                result, calls = self.execute(checked)
                self.assertFalse(result['dispatched'])
                self.assertFalse(any(call[0] == 'POST' for call in calls))

    def test_missing_feed_timestamp_can_recover(self):
        self.assertTrue(self.execute(None)[0]['dispatched'])

    def test_all_active_states_block_a_second_run_even_if_old(self):
        for state in ('queued', 'in_progress', 'waiting', 'pending', 'requested'):
            with self.subTest(state=state):
                result, calls = self.execute(active=state)
                self.assertEqual(result['reason'], 'refresh_already_active')
                self.assertFalse(any(call[0] == 'POST' for call in calls))

    def test_recent_manual_or_recovery_dispatch_enforces_one_hour_cooldown(self):
        result, calls = self.execute(dispatched=True)
        self.assertEqual(result['reason'], 'dispatch_cooldown')
        query = parse_qs(urlsplit(calls[-1][1]).query)
        self.assertEqual(query['created'], ['>=2026-11-02T19:00:00Z'])
        self.assertFalse(any(call[0] == 'POST' for call in calls))

    def test_unavailable_history_never_authorizes_dispatch(self):
        with self.assertRaises(OSError):
            self.execute(fail=True)

    def test_empty_history_never_authorizes_dispatch(self):
        result, calls = self.execute(missing=True)
        self.assertEqual(result['reason'], 'workflow_history_missing')
        self.assertFalse(any(call[0] == 'POST' for call in calls))

    def test_invalid_timestamp_and_repository_fail_closed(self):
        with self.assertRaises(ValueError):
            self.execute('invalid')
        with self.assertRaises(ValueError):
            recover({}, '../foreign/repository', now=self.now)


if __name__ == '__main__':
    unittest.main()
