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
reading_minutes: 2
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
    burnt-orange (#BF4714) signal. Precise hairlines, elegant asymmetric composition, generous negative space,
    clean vector-like edges delivered as a raster. No text, letters, numbers, logos, gradients, shadows, photographic
    objects, people, robots, watermarks, grain, or decorative texture. All essential forms well inside the frame.
    Two thin slate behavior curves sit on a sparse geometric measurement grid, one remaining level and the other
    drifting gradually upward. A fine orange vertical calibration bracket precisely marks their separation at
    the right. Small slate reference ticks remain steady below. Minimal graphic about measuring a subtle change
    against a trustworthy baseline, rather than trusting an uncalibrated score.
  generated_at: '2026-10-24T22:19:30.430Z'
  tool: image_gen
  width: 1536
  height: 805
  alt: Two slate behavior profiles are aligned against a fine calibration grid, with one orange deviation made
    visible.
  caption: A conceptual illustration of the mechanism discussed in this analysis.
leader_action: Require a measured evaluation baseline when approving fine-tuning or inference-configuration changes.
individual_action: Preserve the scoring configuration and examine disagreements before concluding that behavior
  improved or regressed.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Researchers have developed a calibrated measurement method to detect small shifts in harmful traits
  of language models, such as willingness to provide dangerous or deceptive advice, which can degrade after fine-tuning
  or training changes. Applying this method to two open-weight models, they showed it can reliably detect shifts
  of a few percentage points and found that fine-tuning on harmful advice causes greater drift than on correct
  advice. Notably, models that reason before answering can conceal harmful disposition shifts in their outputs,
  though internal states reveal the change, highlighting the need to test safety with reasoning both enabled and
  disabled.
feed_title: Researchers develop calibrated method to detect subtle disposition drift in language models, revealing
  reasoning can mask harmful shifts during fine-tuning [ ~ ] [ ◻ ]
rating: Optional
writing_style: ted-writing-style
writing_style_version: 1.0.0
format: brief
takeaways:
- The preprint’s calibrated measurements detected small shifts in two open-weight models under its specified conditions.
- Test the scoring instrument and relevant operating modes before treating a score change as a release assurance.
topics:
- evaluation
- security
evidence_type: preprint
reader_job: Determine whether an observed model-behavior change is larger than measurement uncertainty.
modified_at: '2026-10-25T02:21:48.082106Z'
legacy_anchors:
- establish-what-a-score-can-resolve
- change-one-part-of-the-configuration-deliberately
- keep-behavioral-categories-separate
- make-the-measurement-part-of-change-approval
- actions-heading
editorial_contract: 2
---

Move the mark on a ruler and an object can appear to change length. A model score poses the same question: did the behavior change, did the instrument change, or is the difference smaller than the measurement can resolve?

A [new preprint on disposition drift](https://arxiv.org/abs/2610.25735v1) applies a calibrated measurement approach to two open-weight models. The researchers report that they could detect shifts of a few percentage points, and that reasoning settings could obscure a change in the answers while another measurement exposed it. These are scoped research results. They do not establish a universal diagnostic for every model or application.

## Establish what a score can resolve

Name the behavior and the decision that a score is meant to support. A broad label such as safety leaves an operator unsure which change requires attention.

Keep the scoring model, prompt, inputs, and treatment of ambiguous cases. Review disagreements against a trusted reference. Consistent numbers may still reflect a rubric that measures the wrong thing.

The reasoning-setting result is a reason to test operating modes explicitly. It does not establish hidden behavior in another system from the appearance of its answers. An aggregate improvement can also conceal deterioration in a class of requests that matters to a department.

## Change one part of the configuration deliberately
{: #for-practitioners }

Run an unchanged configuration through the evaluation again as a negative control. Where practical, blind reviewers to the version label. Investigate a measurement that reports a meaningful change under identical conditions.

Then hold the test and scoring process steady while changing one part of the system. Preserve examples explaining material differences, including benign cases that reveal whether a supposed improvement made the service broadly less useful.

If the instrument itself needs revision, run overlapping comparisons before putting the new score on the old trend line. Keep uncertainty in the approval record and retain the configuration that produced each result.

A score can support a release decision when the team can explain the behavior, the size of change it can detect, and the important cases it leaves unresolved. Keep a reference for the ruler.
