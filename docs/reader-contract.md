# Reader and publishing contract

Version 2.0.1. Approved October 24, 2026; headline, metadata, and caption preferences refined by Ted the same day.

This document and the checked-in brand/voice policy define the publication. Daily producers fill the content contracts; they do not redesign templates, change typography, or update visual baselines.

## Reading levels

| Surface | Reader job | Required behavior |
| --- | --- | --- |
| Homepage | Identify important enterprise AI changes and a useful decision in five minutes | Explicit editorial lead, linked takeaways, up to five concise story previews, complete-edition link. At most 850 editorial words; never pad to a minimum. |
| Edition | Understand the day across business and technical concerns | All selected stories, established section order, direct sources, previous/next editions. Historical editions contain dated coverage rather than a changing live-news rail. |
| Article | Understand a claim, consequence, and practical applicability | Concise takeaways, attributed evidence, useful interpretation, limitations, practitioner detail, sources, related coverage. |
| Live news | Scan the wider landscape | Preserve upstream order and ratings; identify feed-provided summaries and link directly to original material. |
| Archive | Recover coverage by date | Month grouping, dated editions, representative linked headlines. |
| Search/topics | Find an answer or follow an idea | Article-only full-text search, stable IDs/URLs, date and format context, section/subject filters, empty-state recovery. |
| About/corrections | Establish responsibility and report an error | Ownership, editorial standards, truthful AI disclosure, correction route. |
| Feeds | Read in another tool | Stable GUIDs, original publication dates, update dates, matching full article content. |
| Navigation/404 | Orient and recover | Accessible predictable links, working recovery, visible keyboard focus. |

## Editorial section jobs

Maintain this order and omit empty sections.

- **TL;DR:** consequential developments, each linked to its article. One item is sufficient on a one-story day; no padding.
- **Big Moves:** changes affecting enterprise strategy, investment, or the wider market.
- **Enterprise Ops:** changes to running AI services and completing real work.
- **Vendors:** capabilities, availability, costs, terms, and useful comparisons.
- **Security:** evidenced exposure, affected boundaries, and supported responses.
- **Policy:** applicable rules, jurisdictions, obligations, and effective dates. Avoid stretching unrelated research into regulatory news.
- **Quick Hits:** focused developments with verified original dates and direct sources.

Looking Ahead, Editor's notes and source record, reconstruction paragraphs, machine cutoffs, preparation logs, and expandable upstream-summary records do not render on public pages. Production evidence remains in GitHub. Keep plain reader dates and a discreet Retrospective label where appropriate. Ordinary citations appear under Sources.

## Article contracts

Existing records without a format remain analyses. New and revised records declare:

- format: brief (200–400 words) or analysis (600–1,200 words), including subheads and practitioner detail in the body count.
- takeaways: one to three concise, specific points separating the finding from its implication.
- topics: one to three slugs from _data/topics.yml.
- evidence_type: preprint, vendor, reporting, research, or practitioner. Source-level kind may provide more specificity.
- reader_job: the concrete question the story helps answer.
- editorial_contract: 2, the existing writing-style fields, and reading_minutes computed at 220 words/minute.
- The existing identity, edition, source, eligibility, feed-input, and role-action metadata.

Choose length from evidence and reader job, with no analysis quota. A focused announcement or narrow finding usually merits a brief. Analysis earns extra length through distinct mechanisms, consequences, limitations, and practical detail. A small source count is not itself a defect; corroborate claims that require it.

Every new analysis has its own built-in generated hero. New briefs may omit one. Preserve existing attached heroes during reclassification and reuse completed assets on retries. An image failure never authorizes silently relabeling an analysis as a brief.

Use AP sentence-style headline capitalization, preserving proper names and acronyms and capitalizing the first word after a colon. Do not automatically title-case or lowercase headlines. Match article search/social titles to the reviewed headline. Homepage search/social title, description, and image describe Yesterday in AI as a publication; article metadata describes the article; edition metadata describes that dated edition.

Image captions explain the visible composition’s relationship to the story. Prefer one sentence, with a maximum of two. Generic generation or illustration credits are not captions. Preserve the existing image bytes, alt text, and generation provenance while updating the caption; keep AI-assistance disclosure in the footer and About page.

Keep sourced facts and qualifications intact. Report preprints with experimental scope, vendor benchmarks as claims, and hypothetical application examples as examples. Never imply hands-on testing or personal review that did not occur. Use Ted's technology/strategy voice without invented biography.

Keep inline attributed source passages in the preserved launch archive. Its original dates, source records, URLs, heading anchors, logos, and hero hashes have regression checks. Later developments belong in a new dated article; archive revisions must not import hindsight.

## Edition contracts

Up to eight researched stories, from the same two discovery feeds, with verified original publication or substantive-update times in the preceding 36 elapsed hours at 5 a.m. America/Los_Angeles. Preserve seven-day deduplication and historical cutoffs.

lead_article_id identifies editorial importance independently of section order. tldr entries use {article_id, text}. Legacy text-only entries still render with article links. A verified quiet day can use text explaining successful discovery without inventing a story.

A retrospective label describes the edition; actual article publication and revision timestamps remain truthful. Do not backdate publication or change a historical reporting window.

## Repeatable presentation

Use the checked-in logos, fonts, color roles, spacing, focus treatment, and recipes. Headlines precede list illustrations. Images retain native proportions. Large thumbnails float only when their story column has room; sidebars collapse below 1,100px. Preserve an 18px default body with user-controlled scaling.

The homepage emphasizes leadership implications. Deeper pages provide practitioner detail. Avoid repeating the same actions in several sections.

Pagefind indexes article bodies after every Jekyll build. Existing q and topic search URLs remain valid; tag selects a subject. Search failure leaves a useful static list and an honest reduced-search state.

## Health and failure behavior

Daily Codex starts at 5 a.m. Pacific using the existing model and reasoning. Hourly GitHub refresh is independent. The host computer and app remain prerequisites for local editorial production.

Keep successful feed-check time separate from content-change time. An unchanged feed with a recent successful check is healthy. An independent hourly GitHub check fails when an edition is missing after 7 a.m. Pacific or a feed check is over three hours old. Public notices appear only for material staleness on the latest briefing/live page.

Use isolated editorial worktrees and the bounded ship command. No force pushes. Reuse completed articles and images; validate a completed edition and no-op on reruns. A source, generation, validation, or deployment failure preserves the last successful publication and reports required action in Scheduled/Actions.

Application changes pass fixed-content visual review and meaningful browser tests. Daily production cannot update approved fixture snapshots. Dynamic editions get structural, accessibility, and overflow checks.
