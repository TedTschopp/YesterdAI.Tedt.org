---
article_id: art_4714611be4537b33
story_key: https://arxiv.org/abs/2610.31148
title: Evaluation scores need their prompts and judges attached
summary: Two new studies show how wording, tool interfaces, judge choice, and language affect model comparisons.
  An enterprise scorecard needs to preserve those conditions and expose important reversals.
section: Enterprise Ops
edition_date: '2026-10-23'
published_at: '2026-10-24T22:46:52.148862Z'
retrospective: true
rank: 2
reading_minutes: 3
eligibility:
  url: https://arxiv.org/abs/2610.31148v1
  published_at: '2026-10-22T12:07:01Z'
  precision: second
  verification: publisher_api
  evidence: arXiv API published=2026-10-22T12:07:01Z
  discovered_url: https://arxiv.org/abs/2610.31148
sources:
- url: https://arxiv.org/abs/2610.31148v1
  title: Prompt Sensitivity in Tool-Augmented Model Comparisons
  publisher: arxiv.org
  published_at: '2026-10-22T12:07:01Z'
  date_precision: second
- url: https://arxiv.org/abs/2610.31172v1
  title: 'Prompting Strategy Effects Depend on the Judge: A Multilingual Study of LLM-as-a-Judge Robustness'
  publisher: arXiv
  published_at: '2026-10-22T12:27:05Z'
  date_precision: second
hero:
  path: /assets/images/prompt-judge-evaluation.webp
  prompt: Create a wide landscape editorial hero for Yesterday in AI, approximately 1.91:1. Strictly flat two-dimensional
    Swiss editorial graphic, warm ivory (#F8F6F0) background, deep slate (#101820) geometry and a single restrained
    burnt-orange (#BF4714) signal. Precise hairlines, elegant asymmetric composition, generous negative space,
    clean vector-like edges delivered as a raster. No text, letters, numbers, logos, gradients, shadows, photographic
    objects, people, robots, watermarks, grain, or decorative texture. All essential forms well inside the frame.
    Three identical slate evidence tiles sit above three slightly different open geometric framing brackets. Their
    thin output lines lead to noticeably different arrangements of small result blocks. One orange alignment rule
    runs beneath all three to make the comparison visible. A restrained graphic about prompt wording, judge configuration,
    and the stability of AI evaluation.
  generated_at: '2026-10-24T22:30:59.709Z'
  tool: image_gen
  width: 1536
  height: 804
  alt: Identical evidence tiles pass through different framing brackets and produce different results along one
    shared comparison line.
  caption: A conceptual illustration of the mechanism discussed in this analysis.
leader_action: Require comparison stability and important subgroup results alongside the headline evaluation score.
individual_action: Rerun a meaningful comparison across reasonable prompt wordings and preserve the judge configuration.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Researchers studied how equipping language models with external tools affects the stability of model
  comparisons on question-answering benchmarks with varied question wordings. They developed a protocol separating
  reasoning, tool use, and answer reporting steps, applying it to six open models across five domains and five
  question formulations. The study found that while tools improve accuracy when programs answer questions, they
  also increase sensitivity to prompt wording in many pairwise model comparisons, influenced by how often models
  call tools and the interface design. The sensitivity varied depending on the tool-calling interface and instructions;
  for example, a native tool interface and a second tool description eliminated detected sensitivity in molecular
  tasks, whereas sensitivity persisted when tools returned intermediate results. These results indicate that deterministic
  answer reports do not guarantee stable model comparisons, leading the researchers to recommend reporting both
  tool call frequency and comparison stability across multiple prompt wordings alongside accuracy metrics.
feed_title: Researchers find tool-augmented language models increase accuracy but also widen prompt sensitivity
  in model comparisons across multiple domains and wordings [ ~ ] [ ◻ ]
rating: Optional
writing_style: ted-writing-style
writing_style_version: 1.0.0
format: analysis
takeaways:
- The tool study examines six open models, five domains, and five wordings; accuracy gains can coexist with less
  stable pairwise comparisons.
- The multilingual judge study finds prompt effects dependent on judge, task, and language, including reversals.
topics:
- evaluation
- agents
evidence_type: preprint
reader_job: Determine how much weight a model ranking deserves under plausible changes to its evaluation conditions.
modified_at: '2026-10-25T02:26:50.298474Z'
legacy_anchors:
- preserve-the-comparison-contract
- test-reasonable-alternative-wordings
- inspect-how-tools-enter-the-result
- validate-the-judge-in-the-intended-setting
- report-what-the-evidence-supports
- actions-heading
editorial_contract: 2
---

A scorecard puts the model names in order. Keep the conditions of that contest on the page too: the wording, tool interface, judge, and language can affect what the order means.

One [new study of tool-augmented comparisons](https://arxiv.org/abs/2610.31148v1) examines six open models across five domains and five wordings. It finds settings where tools improve accuracy while making pairwise comparisons more sensitive to wording. A [second study of multilingual LLM judges](https://arxiv.org/abs/2610.31172v1) reports that prompting effects depend on the judge, task, and language, with some effects reversing across configurations.

Neither paper establishes that evaluation is futile. The useful question is whether a decision survives reasonable variations in presenting and judging the same work. A model identifier alone cannot explain the whole comparison.

## Preserve the comparison contract

Retain the task, dataset, model revision, tool permissions, prompt, judge configuration, language, and scoring rule. Write the acceptance criterion before using the results to choose a system.

A change to one of those conditions may be a legitimate improvement, but it needs an identifiable place in the record. Otherwise a new score can be mistaken for evidence of a better model when the test or interface changed around it.

Separate a capability result from a selection decision. Several models may meet the application’s threshold even when their order is unstable. Conversely, a narrow numerical lead may matter little if it reverses under plausible wordings and does not alter which service the organization can operate successfully.

## Test reasonable alternative wordings

Keep the underlying task and factual constraints constant while trying equivalent instructions. Inspect cases where a meaningful pairwise comparison changes.

A different wording can clarify a real ambiguity. Have reviewers decide whether the variants still ask the same question before interpreting variation as a model weakness. If the task itself changed, it belongs in a separate comparison.

Report important reversals and the conditions producing them. Averaging every variant into one ranking can hide the uncertainty most relevant to the buying or release decision.

## Inspect how tools enter the result

A model with tools receives another way to obtain information or act on the task. Preserve the interface, allowed operations, returned payload, and actual trace. The presence of a tool label does not establish which capability was exercised.

The tool-comparison study finds differences across interfaces and instructions. It does not support a universal claim that tools increase or decrease comparison stability. Its finding that accuracy can improve while wording sensitivity also increases is a reason to keep both observations in the result.

For a local test, distinguish whether the tool was available, whether it was called, and whether the relevant evidence reached the model. Those details help the team locate a change before selecting a remedy.

## Validate the judge in the intended setting
{: #for-practitioners }

Take a reviewed sample from the intended task and language. Compare the judge's assessments with an appropriate reference, including ambiguous answers and important error categories.

Preserve the judge prompt and model version with the candidate outputs. A judge is part of the measurement process and can respond differently across tasks and languages. The multilingual study reports reversals, so a favorable setting should not quietly become an assurance for another one.

Keep disagreements for later comparisons. A fluent rationale or a successful scoring response does not independently establish that the rubric was applied as intended.

## Report what the evidence supports

Choose a comparison that drives a real decision and show its stability alongside its headline score. Keep unresolved differences and the scope of the two studies visible.

Use the result to state which options meet the task's acceptance criteria, what the remaining uncertainty could change, and which comparison would resolve it. The person approving the work should be able to follow the score back to the conditions that produced it. A ranking earns its place when that account can support the decision being made.
