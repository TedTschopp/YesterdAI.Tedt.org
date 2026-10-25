# Title and Heading Capitalization

Ted requested the linked AP-style title-case rules for h1–h6 and other titles or headers on October 24, 2026. docs/title-capitalization.md records that house style and its precedence over earlier sentence-case guidance. The agent instructions, daily prompt, brand, reader contract 2.0.2, voice policy, and README point to it.

The 24 existing article titles and their authored subheads, seven edition titles, static page titles, topic names, and shared title/header labels use title case. Article titles flow unchanged into search, syndication, social metadata, and NewsArticle data. Names such as AI, LiteLLM, MiniMax, and Yesterday in AI retain their spelling. Quoted source titles, attributed passages, and upstream feed records retain their supplied text.

The changes preserve article/edition URLs, stable IDs, all original rendered IDs across 44 pages, original publication and source dates, reporting windows, edition membership, source records, summaries, body paragraphs, bylines, disclosures, hero bytes, and logos. Revised articles and editions record modified_at without changing publication dates. An audit against the parent commit confirmed that article/edition records differ only in title/subhead capitalization and revision timestamps.

The original archive preservation baseline is unchanged. tests/fixtures/title-case-migration.json records exact old/new headlines for its 23 articles; the existing preservation test checks both the allowed title and unchanged wording. The frozen rendering fixture has the same capitalization-only update; its identities, dates, layout cases, and other content remain fixed.

Local validation passed all six required commands: 36 Python tests, editorial validation, strict Jekyll build, Pagefind indexing, rendered-site checks, and JavaScript/static smoke checks.

## Visual Review

[Candidate run 40164414620](https://github.com/TedTschopp/YesterdAI.Tedt.org/actions/runs/40164414620) for source commit 05b3912f3d34992657ac9b1e12a6ebeeddab0bcd passed the Chromium/WebKit reader, accessibility, and responsive checks, plus mobile performance budgets. The existing baseline-generation path produced 48 candidates through 36 passing visual tests, then stopped for explicit review before accepting them.

Codex reviewed all 48 candidates in light/dark contact sheets and inspected narrow homepage/article and wide story images individually. The changed title wrapping fits the existing columns and retains the mobile navigation, takeaways, paper/slate themes, typography, and illustration proportions. Local CUA review also confirmed the actual homepage/article headings, contents links, and absence of horizontal overflow at the displayed desktop width.

The reviewed Linux PNGs from artifact 12587204402 are committed explicitly for the home, edition, article, and story cases at 320, 390, 768, 1024, 1280, and 1440 pixels in both themes. The subsequent checks on [PR #3](https://github.com/TedTschopp/YesterdAI.Tedt.org/pull/3) compare those committed baselines without accepting new snapshots automatically. The publication workflow and its gates are unchanged.
