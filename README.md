# Yesterday in AI

A daily enterprise AI field guide from Ted Tschopp’s Public Workbench.

**Website:** https://yesterdai.tedt.org · **Source:** https://github.com/TedTschopp/YesterdAI.Tedt.org

Jekyll renders versioned Markdown editions and articles. GitHub Actions validates and deploys them to GitHub Pages. Cloudflare manages DNS. A local Codex scheduled task researches and prepares the 5 a.m. Pacific edition; a separate hourly GitHub workflow refreshes the live news.

## Development

Select Ruby 3.2.9 with rbenv, then run `make setup`, `make check`, and `make serve`. Python dependencies live in `.venv/`. Source page caches and generated build files are ignored by Git. There is no paid model API dependency, database, login system, or email delivery service.

## Editorial contract

The feeds at https://rss.tedt.org/ai_rss_feed.json and https://rss.tedt.org/feeds/top.json supply discovery and attributed summaries. Full articles follow original reporting, verify its publication or substantive update time, and use the 36 hours preceding 5 a.m. Pacific. Each edition includes up to eight distinct 800–1,200 word articles with original generated heroes. Read [the daily production prompt](prompts/daily-edition.md), [brand rules](docs/brand.md), and [operations](docs/operations.md).

The seven launch editions are explicitly retrospective. Their reporting windows and historical feed commits are separate from their actual preparation and article publication dates.

## Content interface

- `_articles/<stable-slug>.md`: article front matter and Markdown analysis; public URL `/articles/<stable-slug>/`.
- `_editions/YYYY-MM-DD.md`: cutoff/window, TL;DR, article IDs, short links, editorial notes; public URL `/editions/YYYY-MM-DD/`.
- `_data/wire.json`: ranked, normalized live stories and the last changed successful snapshot time.
- `_data/discovery.json`: current validated input feeds and item exclusion records.
- `assets/images/`: optimized generated hero images, with their prompts and provenance in the article metadata.
- `docs/runs/`: durable editorial and launch records.

Public pages include `/`, `/live/`, `/archive/`, `/search/` (including topic filters), and `/about/`. Syndication uses `/feed.xml` and `/feed.json`; `/sitemap.xml` lists public pages.
