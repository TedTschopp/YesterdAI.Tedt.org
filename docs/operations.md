# Publishing operations

## Two independent producers

- The standalone Codex task begins editorial production at 5 a.m. America/Los_Angeles daily, using the configured gpt-6.1-sol model and max reasoning. Its durable instructions are `prompts/daily-edition.md`.
- `Refresh live news` runs at minute 27 of each hour in GitHub Actions. It fetches both feeds, preserves upstream ranking and ratings, excludes malformed individual links with an exclusion record, and replaces last-known-good data only after both feeds validate. No model API is used.

`Build and publish` validates editorial content, runs tests, builds Jekyll, checks rendered links and feeds, and deploys only successful builds to GitHub Pages. Pull requests validate without deployment. Bot refreshes explicitly dispatch deployment; they do not depend on a bot commit starting another workflow.

## Local setup and checks

Use Ruby 3.2.9, Bundler, and Python 3.13 or newer. `make setup` installs dependencies; `make check` runs the required checks; `make serve` serves a local preview at http://127.0.0.1:4173. `python scripts/research.py history --date YYYY-MM-DD --days 7` caches historical feeds for reconstruction. Cached full source text stays under ignored `.cache/`.

## Failures

The current verified public site remains available after a failed build, feed fetch, or image generation. A failed feed is not an empty-news day. Reuse completed editions and images after an interruption. `python scripts/publish.py ship` requires clean committed editorial work and permits only editorial paths; it fetches and rebases before pushing. A rebase conflict needs resolution before retrying; never force-push.

The computer and ChatGPT/Codex desktop app must be available for project-based scheduled editorial work. GitHub Pages and the hourly GitHub refresh continue independently. Inspect Scheduled for editorial outcomes and GitHub Actions for import/build/deployment failures.

## Corrections and rollback

Correct the article in place, preserve its stable URL, set `modified_at`, and describe the correction in the text and run record. A substantive new development can have a new article with `update_of` and a concrete `substantive_update` explanation.

To roll back a bad publication, revert its source commit in GitHub, run checks, and deploy the reverted main branch. Do not delete historical articles or rewrite repository history. For a cutover failure, remove only the dedicated legacy-newsletter Cloudflare redirect rule and restore the old newsletter page/workflow from Git history.

## Hosting

Canonical URL: https://yesterdai.tedt.org. GitHub Pages uses an Actions build. The Cloudflare CNAME is DNS-only and points to tedtschopp.github.io. GitHub supplies the origin certificate and enforces HTTPS once provisioning completes. The legacy tedt.org newsletter redirects only after the new publication is verified.
