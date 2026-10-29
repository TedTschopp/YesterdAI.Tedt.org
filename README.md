# Yesterday in AI

A daily enterprise AI field guide from Ted Tschopp’s Public Workbench.

**Website:** https://yesterdai.tedt.org · **Source:** https://github.com/TedTschopp/YesterdAI.Tedt.org

Jekyll renders versioned Markdown editions and articles. GitHub Actions validates and deploys them to GitHub Pages. Cloudflare manages DNS. A local Codex scheduled task researches and prepares the 5 a.m. Pacific edition; a separate hourly GitHub workflow refreshes the live news.

## Development

Select Ruby 3.2.9 with rbenv and Node 22+, then run `make setup`, `make check`, and `make serve`. Python dependencies live in `.venv/`. Source page caches and generated build files are ignored by Git. There is no paid model API dependency, database, login system, or email delivery service.

## Editorial Contract

The feeds at https://rss.tedt.org/ai_rss_feed.json and https://rss.tedt.org/feeds/top.json supply discovery and attributed summaries. Full articles follow original reporting, verify its publication or substantive update time, and use the 36 hours preceding 5 a.m. Pacific. New editions target 3–5 distinct complete articles: 200–400-word briefs or 600–1,200-word analyses. Quick Hits do not count toward that target. Research additional eligible candidates before accepting fewer than three; publish only verified material and report any evidence-based shortfall. New analyses require original generated heroes; briefs may omit illustrations. Existing attached images and published editions are preserved. Read [the reader/section jobs](docs/reader-contract.md), [the daily production prompt](prompts/daily-edition.md), [brand rules](docs/brand.md), and [operations](docs/operations.md).

The seven launch editions are explicitly retrospective. Their reporting windows and historical feed commits are separate from their actual preparation and article publication dates.

New articles use Ted's `ted-writing-style` skill in technology/strategy mode, with the portable [article voice policy](docs/ted-writing-style.md). The publication byline and AI-assistance disclosure remain in place.

Titles and headers, including all h1–h6, use [Ted's selected AP-style title-case rules](docs/title-capitalization.md). This house style overrides sentence-case headline guidance in the writing and design skills.

## Content Interface

- `_articles/<stable-slug>.md`: article front matter and Markdown analysis; public URL `/articles/<stable-slug>/`.
- `_editions/YYYY-MM-DD.md`: cutoff/window, article-linked TL;DR, explicit lead, article IDs, short links, and internal evidence; public URL `/editions/YYYY-MM-DD/`.
- `_data/wire.json`: ranked, normalized live stories and separate successful-check and content-change times.
- `_data/discovery.json`: current validated input feeds and item exclusion records.
- `assets/images/`: optimized generated hero images, with their prompts and provenance in the article metadata.
- `docs/runs/`: durable editorial and launch records.

Public pages: /, /live/, /archive/, /search/, /topics/, and /about/. Syndication uses /feed.xml and /feed.json; /sitemap.xml lists indexable pages.

## Regression Protection

The preserved archive has source/date/identity/anchor/image checks. Pagefind builds after Jekyll. GitHub deployment requires Chromium and WebKit reader/accessibility checks plus reviewed fixed-content visual fixtures at six widths in both themes. Pinned OFL font files keep typography repeatable. Production jobs cannot modify application code or approved visual baselines.

Publication health runs independently on GitHub, checking the 7 a.m. Pacific edition deadline and three-hour feed-check age. Weekly Lighthouse runs record mobile lab measurements; they do not establish field INP. See [operations](docs/operations.md).

## Shared TedT.org Navigation

The global header loads `https://tedt.org/assets/global-header/v1/header.js`. Menu changes belong in the TedT.org repository, rather than in this site. The small local fallback and pre-paint bootstrap keep navigation and appearance usable while loading. The shared `tedt-appearance` cookie and `tedt:theme-change` event synchronize appearance; keep local site navigation and application controls separate. See https://tedt.org/docs/global-header.md for the embed contract.
