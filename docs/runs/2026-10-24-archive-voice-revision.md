---
state: ready
requested_on: '2026-10-24'
writing_style: ted-writing-style
writing_style_version: '1.0.0'
base_commit: 181d9c53fdcc01532f29f787a2282517fbe6655a
---

# October 24 Archive Voice Revision

Ted requested that existing articles use the ted-writing-style skill while preserving facts, sources, dates, and hero images. Reviewed all 23 published articles and revised the 22 earlier pieces. The already-styled Kapitsa article is byte-identical to its baseline.

Applied the skill's technology/strategy mode using its style profile and calibration examples. Each piece received an individual editing pass: concrete openings, visible reasoning, useful questions, plain explanations, and endings grounded in the work people need to do. Comparisons explain mechanisms, including a handoff record, a measuring ruler, a reviewer's desk, and a release authority's key ring. These are explanatory or clearly hypothetical examples, not invented anecdotes about Ted. Publication bylines and AI-assistance disclosures remain in place.

## Preservation

Every original front-matter value remains identical, including headlines, summaries, stable IDs/slugs, edition membership, publication dates, source URLs and dates, timestamp evidence, feed inputs and ratings, action statements, and complete hero metadata. The only added article fields are writing_style and writing_style_version. Original article dates have not been replaced by the voice-revision date; this run record and Git history record the revision separately.

All original inline citation URLs, their order, numeric tokens, and citation-bearing reporting paragraphs are unchanged. All section headings remain unchanged to preserve existing anchors. Reported findings and their qualifications were retained while the surrounding interpretation was revised. The style pass introduces no new reporting or biographical claims.

All seven edition files and all 23 WebP hero assets match their original SHA-256 hashes. Templates, feeds' structure, application code, DNS, workflows, and the daily schedule are unchanged. The existing publication feed IDs and publication dates remain stable.

The companion [preservation record](2026-10-24-archive-voice-preservation.json) contains per-article before/after hashes and word counts, source-paragraph checks, and the original edition/image hashes. Source baseline: 181d9c53fdcc01532f29f787a2282517fbe6655a.

## Validation

- 24 unit tests passed.
- Editorial validation passed: seven editions and 23 complete researched articles and heroes.
- Strict Jekyll build passed with the project's Ruby 3.2.9 selected on PATH.
- Rendered-site checks passed for 36 HTML pages, internal links, metadata, feeds, and sitemap.
- Every revised body remains within 800–1,200 words.
- All changes are confined to articles and the editorial run record.

A first local build selected the system Ruby instead of the project's runtime and stopped before publication. Selecting the installed rbenv shims resolved it; the required build and site checks then passed. Publication uses the guarded editorial ship path and GitHub Actions. Public verification is recorded after deployment.

## Article Word Counts

| Article | Before | After |
| --- | ---: | ---: |
| agent-harness-state | 812 | 903 |
| ai-recommendation-bias | 811 | 899 |
| authorization-agent-boundaries | 821 | 910 |
| calibrated-disposition-drift | 809 | 891 |
| citation-relevance-verification | 825 | 919 |
| context-sensitive-model-boundaries | 810 | 892 |
| cost-aware-ticket-routing | 816 | 918 |
| hidden-instructions-public-pages | 812 | 897 |
| litellm-release-authority | 816 | 914 |
| llm-proxy-visibility | 810 | 914 |
| materials-structure-ml | 823 | 899 |
| memory-needs-relevance | 814 | 914 |
| mercury-diffusion-serving | 800 | 853 |
| meta-terms-data-governance | 803 | 890 |
| minimax-flash-task-economics | 811 | 890 |
| multiagent-review-tradeoffs | 809 | 906 |
| pew-task-level-adoption | 811 | 902 |
| prompt-judge-evaluation | 803 | 890 |
| recoverable-agent-changes | 815 | 911 |
| scope-executable-policy | 807 | 889 |
| typed-decisions | 820 | 892 |
| voxtral-voice-workflow | 807 | 922 |
