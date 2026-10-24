---
test_id: ted-voice-full-publication-2026-10-24
state: complete
edition_date: '2026-10-24'
article_id: art_51c071c2515ec8fe
article_slug: kapitsa-local-inference-operations
completed_at: '2026-10-24T23:54:36.124675Z'
content_commit: 68a264b95bf2b808a1242702a8af0dfaf279d671
deployment_run_url: https://github.com/TedTschopp/YesterdAI.Tedt.org/actions/runs/40144486458
public_verified_at: '2026-10-24T23:53:59.942989Z'
word_count: 915
---

# October 24 Full-Publication Test

Published one new 915-word analysis and one new original hero. The exact content commit passed GitHub Pages build and deployment, and all public checks passed. The one-time request is complete and cannot authorize another article or illustration.

The worktree started clean at `origin/main` 6733a3bd0b3cd4be9e727cca6e592b7892bcd97d in `/Users/tedtschopp/Developer/yesterdai-publication-20261024`. The main checkout was preserved. The request was pending and neither its article nor hero existed. No new edition was created.

## Research and Selection

Both current discovery feeds were fetched through the normal importer at 2026-10-24T23:47:37.006099Z: 235 curated entries and 76 ranked entries, with 76 normalized wire entries. Historical ranked snapshot 923ac0dcbfb49c724e6e7a304bd5cf1f5d920ee3 contains 80 entries; the actual Kapitsa title, summary, and both Important ratings were preserved in the article and compact evidence record. The feed's launch wording is an attributed input, not the article's claim.

One story was selected under the one-article authorization. All seven available editions, October 18–24, and all 22 existing articles were checked for prior coverage: zero Kapitsa matches. Other current feed entries were outside this bounded request, not adjudicated as ineligible. New complete articles: 1. Preserved October 24 articles: 2. Total edition articles: 3; site total: 23 across 7 editions. No Quick Hits added.

The original GitHub release API reverified v0.2.15 publication at 2026-10-23T22:59:15Z, with an update at 23:01:34Z. Both fall inside the unchanged window from 2026-10-23T00:00:00Z to 2026-10-24T12:00:00Z, the 5 a.m. PDT cutoff. Annotated tag 2cbe658e52c9d910e81725d92427a3437719b107 resolves to 5c489cc69b397d2088aa165f9017129b4a724b7a, dated 2026-10-23T22:35:46Z. The release notes and README, usage, KFlash, and benchmark documentation were read at that source commit. Documentation source dates identify the pinned commit snapshot, not independent file-publication times.

Excluded source versions: v0.2.16 and v0.2.17, published after the cutoff. Current main-branch documentation was also excluded. No inaccessible source underpins the article; a web-renderer cache miss for the pinned usage page was resolved through GitHub's file connector at the exact commit. Kapitsa was not installed or executed; the publication made no independent performance or output-equivalence claim.

## Prose and Editing Pass

Applied `ted-writing-style` 1.0.0 in technology/strategy mode, including its style profile and calibration examples. A plain opening about a laptop server leads to the switchboard model: physical location, access, input behavior, performance, retained state, then the person responsible. Questions are answered in the surrounding reasoning. Human consequences include the developer waiting for an answer, the operator investigating failure, and the user whose conversation persists. The ending returns to the switchboard and an accountable owner.

The continuous-prose editing pass removed filler, shortened the KFlash explanation, replaced a semicolon with direct sentences, and made cache permissions precise. Release and vendor performance claims remain attributed; practical pilot advice is editorial interpretation. No first-person testimony, invented experiences, Ted opinions, or claim of Ted's review appears. The publication byline, AI-assisted-analysis label, site assistance disclosure, and generated-illustration caption remain intact.

The repository word counter reports **915 words**, within 800–1,200. The optional body-only style diagnostic found no generic phrase flags, no exclamations or em dashes, and zero first-person usage. Its tokenization differs from the repository counter and was treated as guidance.

## Original Hero Checkpoint

Generated once during this run with the built-in `image_gen` tool at 2026-10-24T23:48:32.368740Z. The visual was inspected before and after WebP optimization. It shows an inference core and operator controls inside a workstation boundary, with an orange gate connecting two peer machines. It has no embedded headline or logo and is an editorial illustration.

- Saved asset: `assets/images/kapitsa-local-inference-operations.webp`
- Actual dimensions: 1,734 × 907; bytes: 16,164
- WebP SHA-256: `45b905c593a8e8c822174ecb6d3c1ff11214451ce9f2dbba8721b635a309e9e3`
- Original generated PNG SHA-256: `553f6288565ddbc1acaf6c2a61080f87a2ff5d65af4a0e2a84bf4e3299e0e267`
- Exact prompt: `docs/runs/2026-10-24-kapitsa-hero-prompt.txt`, also in article metadata
- Compact source evidence: `docs/runs/2026-10-24-kapitsa-evidence.json`

## Validation and Preservation

All four required checks passed before the ready checkpoint:

- `.venv/bin/python -m unittest discover -s tests`: 24 tests passed.
- `.venv/bin/python scripts/publish.py validate`: 7 editions, 23 complete articles and heroes.
- `bundle exec jekyll build --strict_front_matter`: passed with Ruby 3.2.9 selected through rbenv shims.
- `.venv/bin/python scripts/check_site.py`: 36 HTML pages, internal links, accessibility metadata, feeds, and sitemap checked; 1.4 MB.

Additional inspection confirmed the new homepage and edition article links, archive edition link, RSS and JSON entries, canonical URL, and publication disclosures. Both prior October 24 articles and heroes are byte-identical to the base revision. The original retrospective flag, preparation timestamp, cutoff, window start, and prior source notes are preserved. The edition has an actual modification time and a dated addition note. All tracked changes are confined to allowed editorial paths.

## Publication and Public Verification

Intended article: https://yesterdai.tedt.org/articles/kapitsa-local-inference-operations/

Edition: https://yesterdai.tedt.org/editions/2026-10-24/

Hero: https://yesterdai.tedt.org/assets/images/kapitsa-local-inference-operations.webp

The ready checkpoint was committed as `68a264b95bf2b808a1242702a8af0dfaf279d671` and published through `scripts/publish.py ship`, which repeated the four checks and safely reconciled with origin/main without a force-push. GitHub Actions [Build and publish run 40144486458](https://github.com/TedTschopp/YesterdAI.Tedt.org/actions/runs/40144486458) completed successfully at 2026-10-24T23:53:07Z for that exact commit; both build and deploy jobs succeeded. No deployment retry was needed.

Public verification completed at 2026-10-24T23:53:59.942989Z. Ten requested URLs returned HTTP 200. The new article’s live prose matches the local built article, with its canonical URL, source links, byline, AI disclosures, generated-image dimensions, and publication metadata intact. Homepage and edition link directly to it. The archive displays the updated three-analysis edition and navigates through that edition to the article, following the existing archive design. RSS, JSON Feed, and sitemap contain the article. The new and both preserved heroes match the repository assets byte for byte. The article remains 915 words and all cited source timestamps precede the historical cutoff. Results and exact public URLs are saved in `docs/runs/2026-10-24-full-publication-verification.json`.

Request marked complete at 2026-10-24T23:54:36.124675Z. This final audit and completed request are shipped as a separate editorial commit through the same guarded workflow; its exact workflow outcome is checked before the Scheduled result and automation memory are finalized. No additional content is authorized by this test.

## Material Omissions

This is the authorized single-story addition, not an attempt to replace the edition or cover all current feed entries. Earlier edition exclusions remain in its preserved source notes. Later Kapitsa releases, unverified GPU behavior, and independent benchmark reproduction are not presented as established findings.
