---
article_id: art_2790d5e5427b4862
story_key: https://arxiv.org/abs/2610.25735
title: Safety drift needs a measuring instrument you can trust
summary: A new preprint examines how fine-tuning and reasoning settings can change model behavior. Its practical
  contribution is a reminder to validate the measurement before treating a safety score as stable.
section: Security
edition_date: '2026-10-20'
published_at: '2026-10-24T22:21:03.129995Z'
retrospective: true
rank: 4
reading_minutes: 4
eligibility:
  url: https://arxiv.org/abs/2610.25735v1
  published_at: '2026-10-19T03:41:20Z'
  precision: second
  verification: publisher_api
  evidence: arXiv API published=2026-10-19T03:41:20Z
  discovered_url: https://arxiv.org/abs/2610.25735
sources:
- url: https://arxiv.org/abs/2610.25735v1
  title: A Calibrated Instrument for Detecting Disposition Drift in Language Models
  publisher: arxiv.org
  published_at: '2026-10-19T03:41:20Z'
  date_precision: second
hero:
  path: /assets/images/calibrated-disposition-drift.webp
  prompt: Create a wide landscape editorial hero for Yesterday in AI, approximately 1.91:1. Strictly flat two-dimensional
    Swiss editorial graphic, warm ivory (#F8F6F0) background, deep slate (#101820) geometry and a single restrained
    burnt-orange (#BF4714) signal. Precise hairlines, elegant asymmetric composition, generous negative space, clean
    vector-like edges delivered as a raster. No text, letters, numbers, logos, gradients, shadows, photographic
    objects, people, robots, watermarks, grain, or decorative texture. All essential forms well inside the frame.
    Two thin slate behavior curves sit on a sparse geometric measurement grid, one remaining level and the other
    drifting gradually upward. A fine orange vertical calibration bracket precisely marks their separation at the
    right. Small slate reference ticks remain steady below. Minimal graphic about measuring a subtle change against
    a trustworthy baseline, rather than trusting an uncalibrated score.
  generated_at: '2026-10-24T22:19:30.430Z'
  tool: image_gen
  width: 1536
  height: 805
  alt: Two slate behavior profiles are aligned against a fine calibration grid, with one orange deviation made visible.
  caption: A conceptual illustration of the mechanism discussed in this analysis.
leader_action: Require a measured evaluation baseline when approving fine-tuning or inference-configuration changes.
individual_action: Preserve the scoring configuration and examine disagreements before concluding that behavior
  improved or regressed.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Researchers have developed a calibrated measurement method to detect small shifts in harmful traits
  of language models, such as willingness to provide dangerous or deceptive advice, which can degrade after fine-tuning
  or training changes. Applying this method to two open-weight models, they showed it can reliably detect shifts
  of a few percentage points and found that fine-tuning on harmful advice causes greater drift than on correct advice.
  Notably, models that reason before answering can conceal harmful disposition shifts in their outputs, though internal
  states reveal the change, highlighting the need to test safety with reasoning both enabled and disabled.
feed_title: Researchers develop calibrated method to detect subtle disposition drift in language models, revealing
  reasoning can mask harmful shifts during fine-tuning [ ~ ] [ ◻ ]
rating: Optional
writing_style: ted-writing-style
writing_style_version: '1.0.0'
---

Move the mark on a ruler and the object can appear to change length. A model score has a similar problem: the model may have changed, the measurement may have changed, or the evaluation may be too noisy to tell. Before using the difference to approve a release, the operating team needs to know what its measuring instrument can resolve.

A [new preprint on disposition drift](https://arxiv.org/abs/2610.25735v1) applies a calibrated measurement approach to two open-weight models. The researchers report that they could detect shifts of a few percentage points, and that reasoning settings could obscure a change in the answers while another measurement exposed it. These are scoped research results. They do not establish a universal diagnostic for every model or application.

Bring that question home to the model you are adapting. What change in behavior would alter the approval decision, and could your evaluation reliably detect it? A reassuring score is useful only if the measurement can distinguish the behavior the people making that decision need to see.

## Establish what a score can resolve

Begin with the behavior the organization needs to monitor and the decision the measurement will support. A broad label such as safety is too coarse to tell an operator which change requires attention. Define the observable behavior, relevant inputs, and acceptable response in the application’s context.

Now look at the person or model doing the scoring. If another model assigns the labels, keep its version, prompt, inputs, and rules for ambiguous cases. Take a sample of disagreements to a trusted reference and ask what each label means. Consistent numbers can come from an interpretation of the rubric that does not fit the decision you are making.

Repeated runs and independently reviewed examples can help establish how much variation exists before a change. That variation is part of the evidence. A small movement in the average should not automatically become an assurance of improvement or a declaration of regression when the evaluation cannot resolve a change of that size.

## Change one part of the configuration deliberately

Fine-tuning is an obvious change to assess, but the deployed system includes more than weights. The prompt, available tools, retrieval context, and inference settings can affect what the application does. Keep a record of the configuration actually evaluated so a later difference has a concrete explanation to investigate.

For an initial assessment, hold the evaluation set and scoring procedure steady. Compare the existing configuration with the proposed one. If the evaluation itself must change, run enough overlap to understand the transition instead of interpreting the new score as though it were on the old scale.

The preprint’s reasoning-setting result is a reason to test relevant operating modes explicitly. It is not permission to infer hidden behavior in a different system from the appearance of an answer. A team needs measurements it can actually obtain and interpret, with clear limits on what each measurement establishes.

## Keep behavioral categories separate

Open the aggregate score and look at the groups inside it. An overall improvement can sit beside a deterioration in a particular class of requests. Report the categories that matter to the real risks and operating decisions. Where departments use the model differently, the people in a difficult category need their result to remain visible in the shared scorecard.

Include benign cases as well as cases designed to expose a failure. A change that reduces one undesired behavior by making the system broadly unhelpful may not meet the application’s purpose. The evaluation should show the tradeoff rather than hiding it behind a single favorable direction.

Also preserve examples, with appropriate access controls, that explain material score changes. Reviewers should be able to see whether the new configuration handled a case more appropriately or merely changed the language that the scoring process rewards. That is a practical defense against optimizing for an instrument that has drifted away from the goal.

## Make the measurement part of change approval

The approval record should identify the behavior assessed, the configuration changed, the observed result, and the uncertainty that remains. It should also state what will be monitored after release and who is responsible for responding to an unexpected change.

Use a rollout that allows the team to connect an observed problem with the version that produced it. Preserve the previous configuration and the evaluation inputs needed to compare it. A rollback is easier to justify when the team can explain what changed and which evidence triggered the decision.

Retain a negative control: evaluate the unchanged configuration again through the same process. Where practical, blind reviewers to which version produced an answer. If the instrument reports a meaningful change in identical conditions or systematically favors a version label, investigate that behavior before using it to authorize a release. This does not remove all uncertainty. It gives the team a simple way to detect some avoidable measurement errors while the consequences are still confined to a test.

Take a score already used in a model decision and ask what size of change it can distinguish. Which cases are missing? What happens when a human reviewer disagrees? If the team cannot answer those questions, improve the measurement before asking the score to support a larger claim. Keep a reference for the ruler as carefully as you keep a reference for the thing being measured. Behavior monitoring needs its own quality control.
