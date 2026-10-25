---
article_id: art_acf94d966a173a22
story_key: https://arxiv.org/abs/2610.31657
title: The best ticket-routing decision may be to defer
summary: A cost-aware IT-routing study makes human triage an explicit option. Its results favor evaluating the
  whole decision policy, including the cost of a wrong route and the capacity of the review queue.
section: Enterprise Ops
edition_date: '2026-10-23'
published_at: '2026-10-24T22:46:52.125806Z'
retrospective: true
rank: 1
reading_minutes: 4
eligibility:
  url: https://arxiv.org/abs/2610.31657v1
  published_at: '2026-10-22T17:58:52Z'
  precision: second
  verification: publisher_api
  evidence: arXiv API published=2026-10-22T17:58:52Z
  discovered_url: https://arxiv.org/abs/2610.31657
sources:
- url: https://arxiv.org/abs/2610.31657v1
  title: Cost-Aware Abstention for LLM-Based IT Ticket Classification
  publisher: arxiv.org
  published_at: '2026-10-22T17:58:52Z'
  date_precision: second
hero:
  path: /assets/images/cost-aware-ticket-routing.webp
  prompt: Create a wide landscape editorial hero for Yesterday in AI, approximately 1.91:1. Strictly flat two-dimensional
    Swiss editorial graphic, warm ivory (#F8F6F0) background, deep slate (#101820) geometry and a single restrained
    burnt-orange (#BF4714) signal. Precise hairlines, elegant asymmetric composition, generous negative space,
    clean vector-like edges delivered as a raster. No text, letters, numbers, logos, gradients, shadows, photographic
    objects, people, robots, watermarks, grain, or decorative texture. All essential forms well inside the frame.
    A stream of small slate ticket rectangles approaches a precise fork. Most follow a solid slate automatic-routing
    lane; a few cross a narrow orange threshold gate into a clearly organized second review lane. One stray pale
    ticket is stopped before the wrong endpoint. Elegant graphic about selective automation and a useful option
    to defer uncertain IT tickets.
  generated_at: '2026-10-24T22:30:41.806Z'
  tool: image_gen
  width: 1536
  height: 804
  alt: An orange threshold diverts uncertain tickets into an organized review lane while routine tickets continue
    automatically.
  caption: A conceptual illustration of the mechanism discussed in this analysis.
leader_action: Compare automatic routing, human triage, and selective deferral using costs and workload conditions
  your service desk can defend.
individual_action: Keep a held-out test set and select any routing threshold on separate calibration data.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'arXiv:2610.31657v1 Announce Type: new Abstract: Wrong automatic routing of an IT support ticket
  can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness
  assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy
  once on held-out test data. On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers
  with four large language models under zero- and few-shot prompting. Under the illustrative cost model (c_ok,
  c_triage, c_wrong) = (0, 1, 5), TF-IDF with logistic regression and a threshold of 0.60 selected on calibration
  reduces test cost from 0.763 to 0.472, a 38.1% relative reduction (paired ratio-bootstrap 95% CI [35.7%, 40.4%]),
  while lowering wrong routes from 15.3% to 3.5%. Frozen calibration-selected policies also beat both always-route
  and always-defer on held-out test data in 14 of 16 settings in a post-hoc cost-parameter analysis. The strongest
  prompted configuration reaches 0.477 accuracy on a stratified 1,000-ticket test subset, versus 0.879 for fine-tuned
  DistilBERT on the same tickets. Isotonic lowers expected calibration error without reliably improving discrimination:
  GPT-4o-mini few-shot has one confidence value before and after recalibration and correctness AUROC 0.500. We
  therefore report correctness AUROC and tie-aware risk-coverage area alongside ECE. At the analytically derived
  break-even probability 0.80, seven prompted configurations defer all tickets; Haiku few-shot routes only 19/1,000.
  An LLM-only agreement control and margin/entropy rejection baselines further separate calibration from discrimination.
  The findings are scoped to this dataset, prompt design, model endpoints, and illustrative costs; the work is
  an evaluation framework, not a new abstention algorithm or universal deployment certification.'
feed_title: Cost-Aware Abstention for LLM-Based IT Ticket Classification
rating: ''
writing_style: ted-writing-style
writing_style_version: 1.0.0
format: analysis
takeaways:
- The study reports a 38.1% relative cost reduction for a thresholded logistic-regression setup under an illustrative
  cost model.
- Compare routing and deferral together, including wrong-route costs and the capacity of the human review queue.
topics:
- evaluation
- economics-adoption
- agents
evidence_type: preprint
reader_job: Choose a routing policy using completed work and support costs rather than classifier accuracy alone.
modified_at: '2026-10-25T02:23:35.242233Z'
legacy_anchors:
- put-the-alternatives-in-the-cost-model
- keep-threshold-selection-out-of-the-final-test
- check-whether-confidence-separates-errors
- give-simple-baselines-a-fair-comparison
- pilot-the-handoff-as-well-as-the-classifier
- actions-heading
editorial_contract: 2
---

A ticket has to reach somebody who can help. The routing system can choose a destination, or it can send the decision to a person. Put both paths on the drawing before choosing the classifier.

A [cost-aware ticket-classification preprint](https://arxiv.org/abs/2610.31657v1) tests frozen routing policies on a public eight-class support-ticket corpus. Under an illustrative cost model, the authors report a 38.1% relative cost reduction for a thresholded logistic-regression configuration, alongside fewer wrong routes. They also find substantial limitations in the prompted LLM configurations tested. The paper explicitly limits its findings to the dataset, endpoints, prompts, and assumed costs; it is not a universal deployment certificate.

The useful unit of comparison is the whole route-or-review decision. A probability field matters when it helps choose between those paths under the queue's actual costs. A lower model price or a higher overall score can leave the service with more expensive unfinished work.

## Put the alternatives in the cost model

Walk through a correct route, a wrong route, and a deferral. Record handling time, delay, reassignment, and recovery effort. Keep measured quantities beside assumptions so the service owner can see which part of a favorable result depends on a guess.

Use several plausible cost conditions where the uncertainty could change the choice. A policy attractive only when wrong routes are cheap may fit poorly in a queue where an error sends urgent work through another round of triage.

Human review also has a capacity. A policy can improve its accepted predictions by sending difficult cases to people, while increasing the workload those people cannot finish. Follow deferred tickets to resolution. An unmeasured review queue is an easy place to hide a supposed saving.

The paper keeps calibration and discrimination separate. In practical terms, ask whether the score distinguishes correct predictions from wrong ones. A nearly constant confidence value may offer little help at the branch between routing and review, even if it looks orderly in a dashboard.

## Keep threshold selection out of the final test

Choose a policy on calibration data, then evaluate the frozen choice on held-out records. Preserve the split, labels, configuration, and selection procedure. Repeated threshold adjustments after seeing the final results make those records part of development.

A published threshold is a decision under particular scores, costs, and inputs. Select and test the threshold again for the intended application rather than copying it because a paper reports a favorable result.

As automatic coverage falls, does the accepted set become more reliable? Inspect tied scores and consequential error categories alongside the aggregate. The remaining wrong routes may have different recovery costs, and the service owner needs to decide which ones require a more conservative handoff.

## Give simple baselines a fair comparison

Use the same inputs, taxonomy, and reviewed outcomes to compare the current process, suitable conventional classifiers, and a proposed generative approach. If one candidate receives more context, describe that as a different configuration.

The study's limitations in the tested prompted LLM setups remain attached to its endpoints, prompts, and task. They do not establish that generative models have no useful role elsewhere in a support workflow. The decision here is which method supports routing under the measured conditions.

## Pilot the handoff as well as the classifier
{: #for-practitioners }

Choose a queue with clear categories and downstream owners. First record what the proposed policy would have done alongside the current process. Review disagreements before enabling consequential routing changes.

Include busy periods and inputs outside the normal taxonomy. For a deferred ticket, preserve the evidence and uncertainty that caused the handoff so a reviewer can decide without reconstructing the interaction.

Measure the route through to useful resolution, including the cost of errors and deferrals. Keep acceptance criteria constant while comparing policies. The choice can legitimately be a simpler classifier, a more conservative threshold, or more human review.

The person waiting for help experiences the whole path. Ask whether the work reached somebody able to finish it, and whether the service can support the cost of getting it there. That is the result the routing decision has to improve.
