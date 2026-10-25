# Reader experience and publishing contract v2

Status: implementation candidate; remote browser/performance checks and clock-triggered acceptance remain pending.

## Approved intent

Progress from a five-minute leadership briefing to a balanced daily edition and practitioner detail. Preserve the design system and scheduled publication. Remove Looking Ahead, public editor/source-record panels, reconstruction/cutoff paragraphs, and expandable upstream-summary records. Keep ordinary Sources, publication ownership, truthful dates, and necessary AI disclosure.

## Preserved baseline

The archive baseline is revision 0d8bc54c20672932909d716da8fe7c42937ccb65. The feature branch also includes the later hourly feed refresh at 70f288b. tests/fixtures/preservation-baseline.json records all 23 article identities, source records, original dates, body anchors, attributed source passages, hero metadata/hashes, seven edition windows, and original logo hashes.

All 23 bodies are revised: six analyses and 17 briefs. Attributed source passages remain verbatim; original facts, scope qualifications, source URLs, dates, article URLs, and hero bytes remain protected. Original removed heading IDs are retained as aliases. New modification timestamps record these revisions without changing publication timestamps. No later developments are added to historical reporting.

## Implementation

- Explicit editorial lead and linked takeaways; homepage previews emphasize leadership decisions.
- Dated newspaper sections preserve order and source access, with previous/next navigation and no changing live-news rail.
- Article takeaways, practitioner sections, restrained illustrations, Sources, related coverage, and topic links.
- Compact full-text Pagefind search with stable-ID joins, bookmarked section/subject filters, pagination, empty states, and reduced-search fallback.
- Month-grouped archive and six subject pages.
- Native image ratios and larger wrapping thumbnails; responsive stacking; default body corrected to 18px.
- Existing outlined logos/colors/type roles retained. The four existing font families are pinned under OFL with source/hash manifests.
- Page-specific social images, original feed identifiers/dates, update timestamps, matching RSS/JSON full content, and sitemap rules.
- Backward-compatible brief/analysis contracts; isolated editorial ship now checks static search and publication state.
- Separate successful feed-check/content-change timestamps, independent health workflow, and restrained stale notices.
- Chromium/WebKit reader and accessibility checks, frozen eight-story/quiet-day layout fixtures, and explicit reviewed visual baselines.
- Pinned Lighthouse mobile lab tooling for application candidates and weekly public measurements.

## Local verification

35 Python tests, four JavaScript state tests, seven editions/23 researched stories, 43 generated HTML pages, internal links/anchors, source/image preservation, feed consistency, Pagefind indexing, and pinned font hashes pass locally.

CUA confirms 18px body type, native-ratio 352px desktop thumbnails, a first article link in the initial desktop view, and a working full-text search for PubMed that resolves to the correct article.

## Remaining acceptance

Review remote browser/accessibility/performance results and initial visual candidates before deployment. Update the existing standalone Codex task to read the v2 repository contract while retaining model/reasoning and 5 a.m. Pacific cadence. Exercise a bounded new researched analysis, original generated hero, and ordinary ship/deployment path. Verify an actual 5 a.m. run and two hourly refreshes; a manual run does not establish clock-triggered execution.

DNS, GitHub Pages domain/HTTPS, and legacy redirect rules are unchanged.
