import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from health import assess
from publish import ROOT, read_document, reading_minutes


class PreservationTests(unittest.TestCase):
    def test_published_identity_sources_dates_and_art_remain_intact(self):
        baseline = json.loads((ROOT / 'tests/fixtures/preservation-baseline.json').read_text())
        section_changes = json.loads((ROOT / 'tests/fixtures/section-migration.json').read_text())
        captions = json.loads((ROOT / 'tests/fixtures/caption-migration.json').read_text())
        titles = json.loads((ROOT / 'tests/fixtures/title-case-migration.json').read_text())
        protected = ('article_id', 'story_key', 'title', 'summary', 'section', 'edition_date', 'published_at',
                     'retrospective', 'eligibility', 'sources', 'hero', 'feed_name', 'feed_summary', 'rating')
        for slug, record in baseline['articles'].items():
            current, body = read_document(ROOT / f'_articles/{slug}.md')
            for key in protected:
                expected = record['metadata'].get(key)
                if key == 'title' and slug in titles:
                    self.assertEqual(expected, titles[slug]['from'])
                    self.assertEqual(expected.casefold(), titles[slug]['to'].casefold())
                    expected = titles[slug]['to']
                if key == 'section' and slug in section_changes:
                    self.assertEqual(expected, section_changes[slug]['from'])
                    expected = section_changes[slug]['to']
                if key == 'hero':
                    expected = {**expected, 'caption': captions[slug]}
                self.assertEqual(current.get(key), expected, f'{slug}: changed {key}')
            path = ROOT / current['hero']['path'].lstrip('/')
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), record['hero_sha256'], slug)
            for passage in record['attributed_passages']:
                self.assertIn(passage, body, f'{slug}: changed an attributed source passage')
        for day, old in baseline['editions'].items():
            current, _ = read_document(ROOT / f'_editions/{day}.md')
            for key in ('edition_date', 'cutoff', 'window_start', 'prepared_at', 'retrospective', 'source_snapshot'):
                self.assertEqual(current[key], old[key], f'{day}: changed {key}')
            self.assertTrue(set(old['article_ids']).issubset(current['article_ids']))
        for filename, digest in baseline['logos'].items():
            self.assertEqual(hashlib.sha256((ROOT / 'assets/logos' / filename).read_bytes()).hexdigest(), digest)

    def test_reading_time_uses_words_not_a_stored_guess(self):
        self.assertEqual(reading_minutes('word ' * 220), 1)
        self.assertEqual(reading_minutes('word ' * 221), 2)
        self.assertEqual(reading_minutes('[the source](https://example.com/a-long-url) ' * 110), 1)


class HealthTests(unittest.TestCase):
    def good(self, checked='2026-10-24T14:00:00Z', latest='2026-10-24'):
        return {'latest_edition': latest, 'wire_checked_at': checked, 'wire_changed_at': '2026-10-20T12:00:00Z'}

    def test_unchanged_content_is_healthy_after_successful_checks(self):
        result = assess(self.good(), datetime.fromisoformat('2026-10-24T15:00:00+00:00'))
        self.assertTrue(result['ok'])

    def test_daily_grace_period_and_seven_am_deadline(self):
        data = self.good(latest='2026-10-23')
        self.assertTrue(assess(data, datetime.fromisoformat('2026-10-24T13:59:59+00:00'))['ok'])
        self.assertFalse(assess(data, datetime.fromisoformat('2026-10-24T14:00:00+00:00'))['ok'])

    def test_stale_feed_and_future_clock_are_reported(self):
        self.assertFalse(assess(self.good(), datetime.fromisoformat('2026-10-24T17:00:01+00:00'))['ok'])
        self.assertFalse(assess(self.good(), datetime.fromisoformat('2026-10-24T13:54:59+00:00'))['ok'])

    def test_watchdog_deadline_follows_dst(self):
        data = self.good(checked='2026-11-01T14:59:00Z', latest='2026-10-31')
        self.assertTrue(assess(data, datetime.fromisoformat('2026-11-01T14:59:59+00:00'))['ok'])
        self.assertFalse(assess(data, datetime.fromisoformat('2026-11-01T15:00:00+00:00'))['ok'])


if __name__ == '__main__':
    unittest.main()
