from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from publish import ship
from research import read_source


class PublicationFailureTests(unittest.TestCase):
    def test_failed_preflight_never_pushes(self):
        calls = []

        def execute(*args, **kwargs):
            calls.append(args)
            if args[:3] == ('git', 'diff', '--name-only'):
                return '_articles/new.md'
            if len(args) > 2 and args[2] == 'validate':
                raise subprocess.CalledProcessError(1, args)
            return ''

        with patch('publish.run', side_effect=execute):
            with self.assertRaises(subprocess.CalledProcessError):
                ship()
        self.assertFalse(any(c[:2] == ('git', 'push') for c in calls))

    def test_application_change_cannot_use_editorial_ship(self):
        calls = []

        def execute(*args, **kwargs):
            calls.append(args)
            return 'assets/css/site.css' if args[:3] == ('git', 'diff', '--name-only') else ''

        with patch('publish.run', side_effect=execute):
            with self.assertRaisesRegex(ValueError, 'editorial-only'):
                ship()
        self.assertFalse(any(c[:2] == ('git', 'push') for c in calls))

    def test_rejected_push_fetches_and_reconciles_without_force(self):
        calls, pushes = [], []

        def execute(*args, **kwargs):
            calls.append(args)
            if args[:3] == ('git', 'diff', '--name-only'):
                return '_editions/2026-10-25.md'
            if args[:2] == ('git', 'push'):
                pushes.append(args)
                if len(pushes) == 1:
                    raise subprocess.CalledProcessError(1, args)
            return ''

        with patch('publish.run', side_effect=execute):
            ship()
        self.assertEqual(len(pushes), 2)
        self.assertEqual(sum(c[:2] == ('git', 'fetch') for c in calls), 2)
        self.assertEqual(sum(c[:2] == ('git', 'rebase') for c in calls), 2)
        self.assertTrue(all(c == ('git', 'push', 'origin', 'HEAD:main') for c in pushes))

    def test_inaccessible_source_records_failure_without_manufactured_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch('research.CACHE', Path(directory)), patch('research.fetch', side_effect=OSError('source unavailable')):
                result = read_source('https://example.com/unavailable')
                self.assertEqual(result['error'], 'source unavailable')
                self.assertNotIn('text', result)
                self.assertNotIn('metadata', result)


if __name__ == '__main__':
    unittest.main()
