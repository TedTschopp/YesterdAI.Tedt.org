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
reading_minutes: 4
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
    burnt-orange (#BF4714) signal. Precise hairlines, elegant asymmetric composition, generous negative space, clean
    vector-like edges delivered as a raster. No text, letters, numbers, logos, gradients, shadows, photographic
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
  reasoning, tool use, and answer reporting steps, applying it to six open models across five domains and five question
  formulations. The study found that while tools improve accuracy when programs answer questions, they also increase
  sensitivity to prompt wording in many pairwise model comparisons, influenced by how often models call tools and
  the interface design. The sensitivity varied depending on the tool-calling interface and instructions; for example,
  a native tool interface and a second tool description eliminated detected sensitivity in molecular tasks, whereas
  sensitivity persisted when tools returned intermediate results. These results indicate that deterministic answer
  reports do not guarantee stable model comparisons, leading the researchers to recommend reporting both tool call
  frequency and comparison stability across multiple prompt wordings alongside accuracy metrics.
feed_title: Researchers find tool-augmented language models increase accuracy but also widen prompt sensitivity
  in model comparisons across multiple domains and wordings [ ~ ] [ ◻ ]
rating: Optional
writing_style: ted-writing-style
writing_style_version: '1.0.0'
---

A scorecard can put the model names in order while leaving the conditions of the contest off the page. Change the wording, interface, or judge and that order may become less stable. To use the comparison for a real decision, keep the conditions attached to the scores. They are part of what was measured.

One [new study of tool-augmented comparisons](https://arxiv.org/abs/2610.31148v1) examines six open models across five domains and five wordings. It finds settings where tools improve accuracy while making pairwise comparisons more sensitive to wording. A [second study of multilingual LLM judges](https://arxiv.org/abs/2610.31172v1) reports that prompting effects depend on the judge, task, and language, with some effects reversing across configurations.

Neither paper establishes that evaluation is futile. They give you a practical question to put beside a result: would the decision survive reasonable variations in how the same work is presented and judged? Keep the configuration with the score so you can test that question instead of asking a model name to explain the whole result.

## Preserve the comparison contract

Record the task set, input representation, tool interface, prompt, model identifier, scoring rules, and judge configuration. Where a provider does not offer an immutable version, record the evaluation date and the resulting limitation. A model name alone is not enough to reconstruct what happened.

Keep changes to that contract visible. If one candidate requires a different prompt or tool description, evaluate and label the resulting configuration rather than presenting the result as a property of the model in isolation. The difference may be entirely reasonable, but it belongs in the record.

When the score moves later, return to that record. Did the model change, did the prompt improve, did the judge interpret the answer differently, or was an integration repaired? Each possibility can teach the team something useful. Keeping the changes distinguishable gives the movement an explanation the next person can investigate.

## Test reasonable alternative wordings

Choose a small set of wordings that preserve the task and the available evidence. Avoid quietly changing the requirements while calling the result a prompt-sensitivity test. Have a reviewer confirm that the variants still ask the same substantive question.

Measure whether the model ordering changes as well as how much individual scores move. If the procurement or deployment decision depends on a narrow ranking that reverses easily, the uncertainty deserves a place in the decision record.

Do not automatically search for the wording that makes the preferred candidate win. The purpose is to understand the stability of the comparison under the ways people may actually express the task. Preserve unfavorable variants and investigate them alongside the favorable ones.

## Inspect how tools enter the result

Tools can change the information available to a model and the decisions required to obtain it. A successful tool-supported answer therefore reflects more than reasoning over a fixed passage. Record whether the model called a tool, what it received, and what it did with the result.

The tool-comparison paper makes this separation particularly useful. Its findings vary across interfaces and instructions rather than supporting one universal claim that tools increase or decrease stability. An enterprise evaluation should retain those distinctions instead of flattening them into a slogan.

Use matched cases where possible. Compare a result supplied directly with the same result obtained through a tool, while keeping the substantive evidence constant. Differences can identify an interface or decision-to-call effect that a single accuracy number would conceal.

## Validate the judge in the intended setting

Take the judge into the setting where its decisions will be used. A prompt that works acceptably on a task or language may behave differently elsewhere. Ask people qualified to assess the work to review a sample, then examine the disagreements in the languages and categories the application actually serves. That gives the judging process a local reference.

Keep subgroup results available when they affect an operating decision. A favorable aggregate can conceal a reversal or a weak category. Where sample sizes are small, label the uncertainty rather than treating every observed difference as a settled ranking.

Also distinguish changes in the system being evaluated from changes in the judge. If both move together, run an overlap comparison that helps identify which change explains the result. Otherwise an apparent quality improvement may partly reflect a different scoring instrument.

Set aside a small decision set that is not used to select prompts or tune the judge. Run the chosen configuration there after development ends, preserving inconvenient cases. If the ranking changes, investigate whether the difference comes from the sample, the wording, or the evaluator. This separate check can reveal a configuration that fits the development exercise better than the work it is meant to represent.

## Report what the evidence supports

A useful scorecard can include the central result, its important variation, and the conditions under which the team would revisit the choice. It does not need to compress every question into one winner. Some applications may justify a bounded pilot or different configurations for different kinds of work.

Choose a comparison that currently drives a real decision. Keep its configuration, try a few equivalent wordings, and review meaningful disagreements with the judge. Then put the scorecard back in front of the decision maker, with the conditions and variation visible. You can explain how much weight the ranking deserves and which questions still need work before a choice is made.
