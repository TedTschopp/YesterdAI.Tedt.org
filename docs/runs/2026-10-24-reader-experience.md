# Reader experience and publishing contract v2

Status: the reader redesign is live from 9449e04199ecd37d391aeec4f3616d7ff745d78b. Follow-up headline, metadata, and caption requirements are under verification. The isolated editorial integration test and clock-triggered acceptance remain pending.

## Approved intent

Progress from a five-minute leadership briefing to a balanced daily edition and practitioner detail. Preserve the design system and scheduled publication. Remove Looking Ahead, public editor/source-record panels, reconstruction/cutoff paragraphs, and expandable upstream-summary records. Keep ordinary Sources, publication ownership, truthful dates, and necessary AI disclosure.

## Preserved baseline

The archive baseline is revision 0d8bc54c20672932909d716da8fe7c42937ccb65. The feature branch also includes the later hourly feed refresh at 70f288b. tests/fixtures/preservation-baseline.json records all 23 article identities, source records, original dates, body anchors, attributed source passages, hero metadata/hashes, seven edition windows, and original logo hashes.

All 23 bodies are revised: six analyses and 17 briefs. Two studies move from Policy to Enterprise Ops to match section jobs; the approved mapping is preserved separately from the original baseline. Attributed source passages remain verbatim; original facts, scope qualifications, source URLs, dates, article URLs, and hero bytes remain protected. Original removed heading IDs are retained as aliases. New modification timestamps record these revisions without changing publication timestamps. No later developments are added to historical reporting.

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

The original reader release passed 35 Python tests, four JavaScript state tests, seven editions/23 researched stories, 43 generated HTML pages, internal links/anchors, source/image preservation, feed consistency, Pagefind indexing, and pinned font hashes pass locally.

CUA confirms 18px body type, native-ratio 352px desktop thumbnails, a first article link in the initial desktop view, and a working full-text search for PubMed that resolves to the correct article.

## Remaining acceptance

The reader release passed GitHub run 40158015821: 38 Chromium/WebKit reader/accessibility tests and 36 visual tests against 48 approved screenshots. Three-navigation mobile medians are LCP 2.03s/CLS 0 for the homepage, 2.26s/0 for the article, and 1.95s/0.006 for search, with TBT 0ms. The lab uses pinned tooling, standard launcher flags, and production text compression verified against GitHub Pages. Field INP remains unmeasured. Main deployment 40158373135 succeeded and CUA verified the live redesign.

The existing standalone Codex task now reads the v2 repository contract and retains gpt-6.1-sol, max reasoning, its project, and 5 a.m. Pacific cadence. A new 312-word SWE-Verifier brief and an original 1536×804 WebP are prepared in an isolated worktree for the ordinary ship path. The source appeared in the October 23 historical snapshot and its original October 21 publication lies within that edition’s 36-hour window. This test will add dated retrospective coverage rather than misrepresent an older item as current news.

Actual 5 a.m. execution and two subsequent hourly refreshes remain timed acceptance checks; a manual run does not establish clock-triggered execution.

DNS, GitHub Pages domain/HTTPS, and legacy redirect rules are unchanged.

## Additional user requirements

Ted requested AP headline capitalization, publication-level homepage metadata, article-specific metadata, and explanatory image captions on October 24. Existing article headlines were reviewed in sentence style with proper names/acronyms retained. Headline text is shared consistently across HTML, Open Graph, X cards, and structured article data.

The homepage uses a stable publication title, description, branded social image, and WebSite/Organization data. Articles carry their own headline, summary, canonical URL, image/alt/dimensions, source section/topics, publication/revision dates, and NewsArticle data. Dated editions retain their own identity. Every rendered page is checked for valid matching metadata and JSON-LD.

All 23 captions now explain the visible composition’s relationship to its story in one sentence. The original images, alt text, generation prompts, dimensions, dates, and hashes remain intact. The preservation test permits only the explicitly requested caption replacements. Generic credits and captions exceeding two sentences block publication; the footer/About disclosure remains. The fixed-content captions were updated intentionally, without updating approved screenshot files.

Recent editions’ articles are additionally checked for overflow across all six widths and both themes. Quiet-day fixtures verify both the edition and homepage behavior. Local follow-up validation passes 36 Python tests, four JavaScript state tests, all 43 pages and article-only search indexing.
