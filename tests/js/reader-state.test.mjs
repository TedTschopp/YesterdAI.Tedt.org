import { test } from 'node:test';
import assert from 'node:assert/strict';
import { publicationNotice } from '../../assets/js/reader-state.js';

test('the current edition stays quiet and the prior one gets a grace period', () => {
  assert.equal(publicationNotice({editionDate:'2026-10-24'}, new Date('2026-10-24T20:00:00Z')), null);
  assert.equal(publicationNotice({editionDate:'2026-10-23'}, new Date('2026-10-24T13:59:59Z')), null);
  assert.equal(publicationNotice({editionDate:'2026-10-23'}, new Date('2026-10-24T14:00:00Z')).href, '/live/');
});

test('the seven-am deadline follows both DST transitions', () => {
  for (const [day,before,after] of [
    ['2026-10-31','2026-11-01T14:59:59Z','2026-11-01T15:00:00Z'],
    ['2026-03-07','2026-03-08T13:59:59Z','2026-03-08T14:00:00Z']
  ]) {
    assert.equal(publicationNotice({editionDate:day},new Date(before)),null);
    assert.ok(publicationNotice({editionDate:day},new Date(after)));
  }
});

test('midnight does not warn about an edition that is not due yet', () => {
  assert.equal(publicationNotice({editionDate:'2026-10-24'},new Date('2026-10-25T07:01:00Z')),null);
});

test('recent successful checks stay quiet even if the content was unchanged', () => {
  assert.equal(publicationNotice({wireChecked:'2026-10-24T12:00:00Z'},new Date('2026-10-24T15:00:00Z')),null);
  assert.match(publicationNotice({wireChecked:'2026-10-24T12:00:00Z'},new Date('2026-10-24T15:00:01Z')).message,/last saved/);
  assert.ok(publicationNotice({wireChecked:'invalid'},new Date('2026-10-24T15:00:00Z')));
});
