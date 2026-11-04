# November 4 Daily Editorial Run

## Contract, Clock and Scope

Reader contract **2.0.3**, article metadata contract **2**, `ted-writing-style` **1.0.0**, technology/strategy mode including the editing pass. The current explicit user request selects **AP sentence-style publication headlines**. Existing policy files, design and published content remain unchanged.

Clean background worktree: `/Users/tedtschopp/Developer/yesterdai-daily-20261104`, branch `codex/daily-2026-11-04`, based on freshly fetched `origin/main` **f53cd7fee8eac540d330516e8c9d7306555daed8**. The original checkout remains clean and unmoved at **09cda671f74aeabaa26fcb65734d2b1909c204ff**. Dependencies are reused within ignored directories. Tracked writes stay within the editorial paths; there are no application, fixture, approved screenshot, policy, DNS, workflow, schedule or model changes.

Cutoff: **2026-11-04T05:00:00-08:00 / 13:00 UTC**. Exact 36-hour start: **2026-11-03T01:00:00Z**. Actual preparation: **2026-11-04T13:08:31.452921Z**. The cutoff command accounts for daylight-saving changes. Preparation and the reporting anchor do not establish an observed deployment time.

## Discovery and Exclusions

Both feeds succeeded at **2026-11-04T13:04:08.178057Z**: **229 curated and 198 ranked usable records**, with **one malformed curated and two malformed ranked ingestion exclusions**. The initial sandbox GitHub DNS error was resolved using authorized network access. No feed failure or source failure was called quiet news.

The preceding **seven editions, 22 articles and zero Quick Hits** supplied deduplication evidence. Research covered **17 distinct candidates**: all **12 newest curated** and **five ranked** originals. Dispositions: **three selected; seven outside-window originals (including one modification without an established substantive change); two access failures; three unverified original dates; one conflicting original date; and one editorial-priority exclusion**. Individual original-date evidence and reasons are retained in `2026-11-04-source-audit.json`.

- Microsoft’s Copilot Cowork account, HBR’s essay and Anthropic’s provable-inference original are November 2. Anthropic’s November 3 modification has no verified substantive change here. BCG’s available dates are October 28–30, Uber’s redlining article is October 8, The Commanding Heights is October 29, and the Postman issue was opened October 25. New feed entries do not reset these dates.
- Seeking Alpha returned 403 and VentureBeat returned 429. DXC and Hydrogen-1.0 lack verified original dates. Prime Intellect supplies only a day without an evidenced timezone.
- Glow’s same original page displays November 2 and November 3 while its JSON-LD gives November 3. The unresolved boundary case is excluded. Its claimed findings were not independently reproduced.
- Addy Osmani’s accessible November 3 practitioner essay was lower priority than the selected immediate decisions; that is not an eligibility rejection.

Research continued until three distinct developments supported complete articles. **Target: 3–5; selected: three; shortfall: zero.** The remaining feed records were not all individually verified, and no exhaustion claim is made. No padding, split development, relaxed reporting window or quiet-day label.

## Evidence, Formats and Editing

- **Menlo, Big Moves and explicit lead:** JSON-LD, metadata and visible date establish **November 3 14:00Z**. The full report and methodology were read after the first extraction captured only a navigation fragment. The brief preserves annualized revenue modeling, reclassified prior-year figures, the U.S. buyer sample, investor interests, and the difference between mean and median spending. Market expenditure is not presented as measured customer productivity.
- **OpenAI, Enterprise Ops:** Official OpenAI news RSS gives **November 3 12:00Z** for the exact original. Direct HTTP returned 403; the web reader supplied the complete November 3 announcement. The article preserves human review, tolerances, assembly iterations and vendor-reporting limits. A device design interval, prototype manufacturing interval and research collaboration are distinct; no independent test or vehicle-safety result is invented.
- **Google, Vendors:** Original JSON-LD and `published_time` agree on **November 3 14:00Z**, corroborated by the visible date. Complete direct retrieval succeeded despite web-reader failure. The article separates announced future account controls, the current global Classroom launch, and a limited U.S. Search pilot later in November. It does not invent an exact controls effective date, toggle design or universal Search-pilot access.

Formats were chosen **before drafting**: three focused **briefs of 287, 283 and 289 words**. No analyses, new heroes or generation attempts. All **97 prior article, edition and image files**, including **25 attached article heroes**, remain byte-identical to the base. Existing alt text, captions, provenance and the publication share image are preserved.

The source/voice editing pass reviewed every factual claim, original date, denominator, reporting period, announcement-versus-result distinction and reader implication. Concrete openings lead through visible reasoning to separate budget, manufacturing and school-access consequences. Continuous-prose editing removes repetitive advice and unsupported certainty; body-only style diagnostics supplement that judgment. Publication byline and footer/About AI disclosure remain intact, with no invented Ted experience, opinion, review or hands-on test.

The explicit lead is **art_7aa60ae025d525c4**. Every TL;DR entry links to a member article. The fixed section order and page jobs remain, with empty sections omitted. Article metadata describes that article, while homepage metadata describes the publication. No public production log, cutoff/preparation paragraph, Looking Ahead, Editor’s note or expandable feed-summary record is added.

## Preparation Checkpoint

Complete articles and edition are retained for retry. Deterministic preflight, committed guarded shipping, hosted gates and public readback are pending at this checkpoint. Preserve the last successful site on a required-stage failure.

Publication URLs:

- https://yesterdai.tedt.org/editions/2026-11-04/
- https://yesterdai.tedt.org/articles/menlo-enterprise-ai-spending-run-rate/
- https://yesterdai.tedt.org/articles/openai-physical-engineering-manufacturing-review/
- https://yesterdai.tedt.org/articles/google-school-search-ai-access-controls/

**Required action at this checkpoint:** complete all six deterministic stages, commit, run `scripts/publish.py ship`, and verify the exact pushed commit’s Pages deployment and public URLs automatically. Record the observed outcome after verification.

## Deterministic Preflight Passed

All six required stages passed: **44 Python tests**, validation of **18 editions / 57 complete articles**, strict-front-matter Jekyll, Pagefind indexing of **57 articles**, site checks across **88 HTML pages**, and four JavaScript tests plus publication smoke checks. Full outputs and toolchain versions are recorded in the source audit. Completed content is ready for commit and guarded shipping; deployment and public readback remain pending.
