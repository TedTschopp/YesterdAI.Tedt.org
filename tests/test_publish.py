import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from publish import canonical_url, clean_title, cutoff_for, in_window, normalized_wire, parse_time, refresh, story_id, validate_feed


def feed():
    return {'version': 'https://jsonfeed.org/version/1.1', 'items': [
        {'id': '1', 'url': 'https://example.com/news?utm_source=feed', 'title': 'A useful model [ ! ] [ ◼ ]', 'content_text': 'A supplied summary.', 'date_published': '2026-10-23T12:00:00Z'}]}


class WindowTests(unittest.TestCase):
    def test_boundaries_are_inclusive_and_exact(self):
        cutoff = cutoff_for('2026-10-24')
        start = cutoff.astimezone(timezone.utc) - timedelta(hours=36)
        self.assertTrue(in_window(start.isoformat(), cutoff))
        self.assertTrue(in_window(cutoff.isoformat(), cutoff))
        self.assertFalse(in_window((start - timedelta(seconds=1)).isoformat(), cutoff))
        self.assertFalse(in_window((cutoff + timedelta(seconds=1)).isoformat(), cutoff))

    def test_dst_always_means_36_elapsed_hours(self):
        for day in ['2026-03-08', '2026-11-01']:
            cutoff = cutoff_for(day)
            start = cutoff.astimezone(timezone.utc) - timedelta(hours=36)
            self.assertTrue(in_window(start.isoformat(), cutoff))
            self.assertFalse(in_window((start - timedelta(seconds=1)).isoformat(), cutoff))
            self.assertEqual(cutoff.hour, 5)

    def test_partial_date_at_boundary_is_excluded(self):
        self.assertFalse(in_window('2026-10-22T00:00:00-07:00', cutoff_for('2026-10-24'), 'day'))
        self.assertTrue(in_window('2026-10-23T00:00:00-07:00', cutoff_for('2026-10-24'), 'day'))

    def test_missing_timezone_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_time('2026-10-23T12:00:00')


class FeedTests(unittest.TestCase):
    def test_tracking_links_share_identity(self):
        self.assertEqual(canonical_url('https://example.com/a/?utm_source=x#part'), 'https://example.com/a')
        self.assertEqual(story_id('https://example.com/a?utm_source=x'), story_id('https://example.com/a'))
        self.assertNotEqual(story_id('https://example.com/a?v=1'), story_id('https://example.com/a?v=2'))

    def test_rating_markers_are_preserved_as_fields(self):
        self.assertEqual(clean_title('A useful model [ ! ] [ ◼ ]'), ('A useful model', 'Essential', 'Important'))

    def test_wire_deduplicates_without_reranking(self):
        data = feed()
        second = {**data['items'][0], 'id': '2', 'url': 'https://example.com/news#fragment'}
        data['items'].append(second)
        wire = normalized_wire(data, '2026-10-24T12:00:00Z')
        self.assertEqual(len(wire['items']), 1)
        self.assertEqual(wire['items'][0]['id'], '1')
        self.assertEqual(wire['items'][0]['rating'], 'Essential')

    def test_bad_individual_link_is_recorded_and_excluded(self):
        data = feed()
        data['items'].append({**data['items'][0], 'id': 'bad', 'url': 'javascript:alert(1)'})
        result = validate_feed(data, 'test')
        self.assertEqual(len(result['items']), 1)
        self.assertEqual(result['_excluded_items'][0]['id'], 'bad')

    def test_empty_malformed_or_all_invalid_feed_fails_closed(self):
        for data in [{}, {'version': 'https://jsonfeed.org/version/1.1', 'items': []}, {**feed(), 'items': [{**feed()['items'][0], 'url': 'bad'}]}]:
            with self.assertRaises(ValueError):
                validate_feed(data, 'test')

    def test_failure_of_second_feed_preserves_both_snapshots(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / '_data').mkdir()
            for name in ['wire.json', 'discovery.json']:
                (root / '_data' / name).write_text('{"last_good":true}')
            with patch('publish.get_json', side_effect=[feed(), ValueError('unavailable')]):
                with self.assertRaises(ValueError):
                    refresh(root)
            for name in ['wire.json', 'discovery.json']:
                self.assertEqual((root / '_data' / name).read_text(), '{"last_good":true}')

    def test_unchanged_refresh_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch('publish.get_json', return_value=feed()):
                refresh(root)
                before = (root / '_data/wire.json').read_bytes()
                refresh(root)
                self.assertEqual(before, (root / '_data/wire.json').read_bytes())


if __name__ == '__main__':
    unittest.main()
