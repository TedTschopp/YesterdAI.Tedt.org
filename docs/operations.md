# Publishing operations

## Two independent producers

- The standalone Codex task begins editorial production at 5 a.m. America/Los_Angeles daily, using the configured gpt-6.1-sol model and max reasoning. Its durable instructions are `prompts/daily-edition.md`.
- `Refresh live news` runs at minute 27 of each hour in GitHub Actions. It records every successful check separately from content-change time, fetches both feeds, preserves upstream ranking and ratings, excludes malformed individual links with an exclusion record, and replaces last-known-good data only after both feeds validate. No model API is used.

`Build and publish` validates editorial content, runs Python/JavaScript tests, builds Jekyll and Pagefind, checks rendered links/feeds, then runs browser/accessibility and fixed-content visual checks before deployment to GitHub Pages. Pull requests validate without deployment. Bot refreshes explicitly dispatch deployment; they do not depend on a bot commit starting another workflow.

## Local setup and checks

Use Ruby 3.2.9, Bundler, Python 3.13+, and Node 22+. `make setup` installs dependencies; `make check` runs the required checks; `make serve` serves a local preview at http://127.0.0.1:4173. `python scripts/research.py history --date YYYY-MM-DD --days 7` caches historical feeds for reconstruction. Cached full source text stays under ignored `.cache/`.

## Failures

The current verified public site remains available after a failed build, feed fetch, or image generation. A failed feed is not an empty-news day. Reuse completed editions and images after an interruption. `python scripts/publish.py ship` requires clean committed editorial work and permits only editorial paths; it fetches and rebases before pushing. A rebase conflict needs resolution before retrying; never force-push.

The computer and ChatGPT/Codex desktop app must be available for project-based scheduled editorial work. GitHub Pages and the hourly GitHub refresh continue independently. Inspect Scheduled for editorial outcomes and GitHub Actions for import/build/deployment failures.

## Corrections and rollback

Correct the article in place, preserve its stable URL, set `modified_at`, and describe the correction in the text and run record. A substantive new development can have a new article with `update_of` and a concrete `substantive_update` explanation.

To roll back a bad publication, revert its source commit in GitHub, run checks, and deploy the reverted main branch. Do not delete historical articles or rewrite repository history. For a cutover failure, remove only the dedicated legacy-newsletter Cloudflare redirect rule and restore the old newsletter page/workflow from Git history.

## Hosting

Canonical URL: https://yesterdai.tedt.org. GitHub Pages uses an Actions build. The Cloudflare CNAME is DNS-only and points to tedtschopp.github.io. GitHub supplies the origin certificate and enforces HTTPS once provisioning completes. The legacy tedt.org newsletter redirects only after the new publication is verified.

The daily standalone schedule is `publish-yesterday-in-ai`, configured at 5 a.m. in the computer’s America/Los_Angeles local timezone. The floating local-time schedule follows its daylight-saving transition; the edition validator independently enforces the Pacific cutoff. Keep the computer’s timezone Pacific. The first unattended run follows launch; the isolated-worktree publisher was exercised separately during launch.

The Cloudflare record ID is `0ab2e56ab41753a5a29baef7cab18417`. The dedicated redirect lives in zone ruleset `2087d71c5be749d097a13a869aef0485`, rule `19bdf4fb4323434f9620a613c08f5107`, reference `yesterdai_legacy_newsletter`. It matches only the three `/Daily-Report/AI` variants on tedt.org and www.tedt.org, returns 301, and preserves query strings. Do not remove other zone rules during rollback.

TedT.org migration PR [#244](https://github.com/TedTschopp/tedt.org/pull/244) removes the source and compiled legacy newsletter workflows and adds a source-level fallback. The pre-migration source revision is `506148a84f60dc7e8d38008bed5bb998f65432e0`; migration commit is `041f823e783c19deb74034e22d2511bcf995d73d`. Restore those specific files from Git history if rollback becomes necessary, rather than resetting the whole repository.

## Reader-contract rollout and regression checks

Version 2.0.0 is defined in docs/reader-contract.md. New formats are backward compatible; original publication dates, identities, source records, heading anchors, and article hero bytes are protected. Revisions use modified_at. Existing source passages remain verbatim; do not import later developments into historical coverage.

Local publication checks are make check: Python tests, editorial validation, Jekyll, Pagefind, rendered-contract checks, JavaScript state tests, and static publication smoke. Local interactive review uses CUA. GitHub is the interactive deployment gate, with Chromium and WebKit checks and fixed-content visual baselines. The editor does not need to install or control a local browser through a shell script.

Build fixtures with python scripts/build_fixtures.py. They live under ignored test-results/ and are never deployed. Fixtures cover eight stories, all sections, briefs/analyses, native-ratio images, long headings, Quick Hits, and a verified-quiet-day presentation. Initial CI snapshots must be reviewed and committed explicitly. Normal CI compares against them; daily writers cannot update them. Intentional app design changes require a reviewed baseline update.

Publication health runs hourly at minute 47 and checks deployed status.json. Before 7 a.m. Pacific, the preceding day is acceptable; at 7 a.m. the current edition is required. A successful feed check must be no more than three hours old. Unchanged upstream content with a recent check is healthy. A failed check exits nonzero and records required action in Actions; scripts do not send external messages.

Publication performance runs weekly and on demand. It uses pinned Lighthouse tooling, three cold simulated-mobile navigations for the homepage, Kapitsa article, and search, and reports median LCP/CLS/TBT. Budgets are 2.5s, 0.1, and 200ms. TBT does not establish field INP. Target field INP remains 200ms at the 75th percentile when real-reader data becomes available; no field compliance is claimed at launch.

Application PRs check the candidate static build using the same lab method. A failed build never replaces the existing Pages artifact. Roll back through a reviewed source revert and successful deployment, preserving article URLs and Git history.
