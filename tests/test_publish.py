import copy
import contextlib
import io
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import sys
import tempfile
import shutil
import unittest
import yaml
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from publish import ROOT, canonical_url, clean_title, cutoff_for, in_window, normalized_wire, parse_time, read_document, reading_minutes, refresh, story_id, validate, validate_feed


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
            with patch('publish.get_json', return_value=feed()), patch('publish.utc_now', side_effect=['2026-10-24T12:00:00Z', '2026-10-24T13:00:00Z']):
                refresh(root)
                before = json.loads((root / '_data/wire.json').read_text())
                refresh(root)
                after = json.loads((root / '_data/wire.json').read_text())
                self.assertEqual(before['items'], after['items'])
                self.assertEqual(before['last_changed_at'], after['last_changed_at'])
                self.assertEqual(after['last_checked_at'], '2026-10-24T13:00:00Z')


class PublicationTests(unittest.TestCase):
    """Exercise the launch artifact contract, including failures that must block deploy."""

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.article, self.body = read_document(ROOT / '_articles/authorization-agent-boundaries.md')
        self.edition, _ = read_document(ROOT / '_editions/2026-10-21.md')
        self.edition['article_ids'] = [self.article['article_id']]
        self.edition['tldr'] = [{'article_id': self.article['article_id'], 'text': 'A scoped authorization benchmark.'}]
        self.edition['lead_article_id'] = self.article['article_id']
        self.image = self.root / self.article['hero']['path'].lstrip('/')
        self.image.parent.mkdir(parents=True)
        shutil.copyfile(ROOT / self.article['hero']['path'].lstrip('/'), self.image)
        self.write_documents()

    def write_documents(self):
        for name, metadata, body in [('_articles/materials-structure-ml.md', self.article, self.body), ('_editions/2026-10-21.md', self.edition, '')]:
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('---\n' + yaml.safe_dump(metadata, allow_unicode=True) + '---\n\n' + body)

    def check(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return validate(self.root)

    def test_complete_retrospective_artifacts_validate(self):
        self.assertEqual(self.check(), (1, 1))

    def test_missing_or_corrupt_hero_blocks_publication(self):
        self.image.unlink()
        with self.assertRaisesRegex(ValueError, 'missing project hero'):
            self.check()
        self.image.write_bytes(b'not an image' * 200)
        with self.assertRaisesRegex(ValueError, 'real WebP'):
            self.check()

    def test_false_image_dimensions_block_publication(self):
        self.article['hero']['width'] += 1
        self.write_documents()
        with self.assertRaisesRegex(ValueError, 'dimensions do not match'):
            self.check()

    def test_source_from_after_retrospective_cutoff_is_rejected(self):
        self.article['sources'].append({'url': 'https://example.com/later-report', 'published_at': '2026-10-22T12:00:00Z'})
        self.write_documents()
        with self.assertRaisesRegex(ValueError, 'after historical cutoff'):
            self.check()

    def test_feed_timestamp_cannot_verify_an_article(self):
        self.article['eligibility']['verification'] = 'feed'
        self.write_documents()
        with self.assertRaisesRegex(ValueError, 'verify original source'):
            self.check()

    def test_duplicate_coverage_needs_a_later_substantive_development(self):
        later = copy.deepcopy(self.article)
        later.update(article_id='art_distinct_revision', edition_date='2026-10-22', update_of=self.article['article_id'], substantive_update='An asserted update without a new timestamp.')
        later['eligibility']['published_at'] = '2026-10-21T01:00:00Z'
        end = cutoff_for('2026-10-22')
        edition = copy.deepcopy(self.edition)
        edition.update(edition_date='2026-10-22', cutoff=end.isoformat(), window_start=(end.astimezone(timezone.utc) - timedelta(hours=36)).isoformat(), article_ids=[later['article_id']], lead_article_id=later['article_id'], tldr=[{'article_id': later['article_id'], 'text': 'An asserted update.'}], quick_hits=[])
        for path, data, body in [(self.root / '_articles/later.md', later, self.body), (self.root / '_editions/2026-10-22.md', edition, '')]:
            path.write_text('---\n' + yaml.safe_dump(data) + '---\n' + body)
        with self.assertRaisesRegex(ValueError, 'substantive development must follow'):
            self.check()

    def test_quiet_day_requires_successful_discovery(self):
        (self.root / '_articles/materials-structure-ml.md').unlink()
        self.edition.update(article_ids=[], lead_article_id=None, tldr=['A quiet day.'], quick_hits=[], quiet_day=True)
        self.write_documents()
        (self.root / '_articles/materials-structure-ml.md').unlink()
        with self.assertRaisesRegex(ValueError, 'successful discovery'):
            self.check()
        self.edition.update(discovery_status='ok', quiet_day_reason='Both feeds checked; no distinct eligible reporting.')
        self.write_documents()
        (self.root / '_articles/materials-structure-ml.md').unlink()
        self.assertEqual(self.check(), (1, 0))

    def test_stale_quick_hit_is_rejected(self):
        self.edition['quick_hits'] = [{'url': 'https://example.com/stale', 'title': 'Old news', 'summary': 'Already old.', 'source_published_at': '2026-10-01T12:00:00Z', 'verification': 'meta'}]
        self.write_documents()
        with self.assertRaisesRegex(ValueError, 'Quick Hit outside'):
            self.check()

    def test_literal_dashes_in_supplied_summary_are_preserved(self):
        self.article['feed_summary'] = 'A source --- keeps its literal punctuation.'
        self.write_documents()
        self.assertEqual(read_document(self.root / '_articles/materials-structure-ml.md')[0]['feed_summary'], self.article['feed_summary'])
        self.assertEqual(self.check(), (1, 1))

    def test_brief_can_omit_a_hero_without_weakening_source_rules(self):
        self.article['format'] = 'brief'
        self.article.pop('hero')
        self.body = ' '.join(self.body.split()[:260])
        self.article['reading_minutes'] = reading_minutes(self.body)
        self.write_documents()
        self.assertEqual(self.check(), (1, 1))
        self.article['eligibility']['verification'] = 'feed'
        self.write_documents()
        with self.assertRaisesRegex(ValueError, 'verify original source'):
            self.check()

    def test_analysis_cannot_silently_publish_without_its_hero(self):
        self.article.pop('hero')
        self.write_documents()
        with self.assertRaisesRegex(ValueError, 'analysis requires'):
            self.check()

    def test_linked_takeaway_and_explicit_lead_stay_in_the_edition(self):
        self.edition['lead_article_id'] = 'missing'
        self.write_documents()
        with self.assertRaisesRegex(ValueError, 'lead must belong'):
            self.check()
        self.edition['lead_article_id'] = self.article['article_id']
        self.edition['tldr'][0]['article_id'] = 'missing'
        self.write_documents()
        with self.assertRaisesRegex(ValueError, 'TL;DR needs'):
            self.check()

    def test_legacy_text_takeaways_and_implicit_analysis_still_validate(self):
        self.article.pop('format')
        self.edition.pop('lead_article_id')
        self.edition['tldr'] = ['Legacy text-only takeaway.']
        self.write_documents()
        self.assertEqual(self.check(), (1, 1))

    def test_format_length_and_reading_time_are_checked(self):
        self.article['format'] = 'brief'
        self.write_documents()
        with self.assertRaisesRegex(ValueError, 'expected 200–400'):
            self.check()
        self.article['format'] = 'analysis'
        self.article['reading_minutes'] += 1
        self.write_documents()
        with self.assertRaisesRegex(ValueError, 'reading time'):
            self.check()


if __name__ == '__main__':
    unittest.main()
