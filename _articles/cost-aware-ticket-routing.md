---
article_id: art_acf94d966a173a22
story_key: https://arxiv.org/abs/2610.31657
title: The best ticket-routing decision may be to defer
summary: A cost-aware IT-routing study makes human triage an explicit option. Its results favor evaluating the whole
  decision policy, including the cost of a wrong route and the capacity of the review queue.
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
    burnt-orange (#BF4714) signal. Precise hairlines, elegant asymmetric composition, generous negative space, clean
    vector-like edges delivered as a raster. No text, letters, numbers, logos, gradients, shadows, photographic
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
feed_summary: 'arXiv:2610.31657v1 Announce Type: new Abstract: Wrong automatic routing of an IT support ticket can
  cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment:
  select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out
  test data. On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four
  large language models under zero- and few-shot prompting. Under the illustrative cost model (c_ok, c_triage, c_wrong)
  = (0, 1, 5), TF-IDF with logistic regression and a threshold of 0.60 selected on calibration reduces test cost
  from 0.763 to 0.472, a 38.1% relative reduction (paired ratio-bootstrap 95% CI [35.7%, 40.4%]), while lowering
  wrong routes from 15.3% to 3.5%. Frozen calibration-selected policies also beat both always-route and always-defer
  on held-out test data in 14 of 16 settings in a post-hoc cost-parameter analysis. The strongest prompted configuration
  reaches 0.477 accuracy on a stratified 1,000-ticket test subset, versus 0.879 for fine-tuned DistilBERT on the
  same tickets. Isotonic lowers expected calibration error without reliably improving discrimination: GPT-4o-mini
  few-shot has one confidence value before and after recalibration and correctness AUROC 0.500. We therefore report
  correctness AUROC and tie-aware risk-coverage area alongside ECE. At the analytically derived break-even probability
  0.80, seven prompted configurations defer all tickets; Haiku few-shot routes only 19/1,000. An LLM-only agreement
  control and margin/entropy rejection baselines further separate calibration from discrimination. The findings
  are scoped to this dataset, prompt design, model endpoints, and illustrative costs; the work is an evaluation
  framework, not a new abstention algorithm or universal deployment certification.'
feed_title: Cost-Aware Abstention for LLM-Based IT Ticket Classification
rating: ''
writing_style: ted-writing-style
writing_style_version: '1.0.0'
---

A ticket has to reach somebody who can help. An automated system can choose the destination, or it can recognize that a person needs to decide. Put both paths on the drawing before choosing the classifier. The useful outcome is work arriving where it belongs, including the cases where a human decision is the next step.

A [cost-aware ticket-classification preprint](https://arxiv.org/abs/2610.31657v1) tests frozen routing policies on a public eight-class support-ticket corpus. Under an illustrative cost model, the authors report a 38.1% relative cost reduction for a thresholded logistic-regression configuration, alongside fewer wrong routes. They also find substantial limitations in the prompted LLM configurations tested. The paper explicitly limits its findings to the dataset, endpoints, prompts, and assumed costs; it is not a universal deployment certificate.

Follow the route-or-review decision through the service and make its consequences measurable. Once you can explain those paths, the choice of model has a clearer job to do. It needs to help choose a useful next step under the costs and constraints of the queue that will receive the work.

## Put the alternatives in the cost model

Walk a ticket down each possible path: a correct route, a wrong route, and a deferral. Who handles it, how long does it wait, and who puts it back on course if it reaches the wrong team? Include handling time, delay, reassignment, and recovery effort. Write the measurements and assumptions beside those steps so the person using the cost model can tell them apart.

Use several plausible cost conditions when uncertainty is material. A policy that looks attractive only when wrong routes are assumed to be inexpensive may not fit a queue where those errors create substantial disruption. Report the dependency instead of hiding it inside a single average.

Human triage also has a capacity constraint. A policy that defers many difficult cases may improve a model score while overwhelming the people receiving the work. The operating evaluation should connect the selected threshold with the volume and composition of that queue.

## Keep threshold selection out of the final test

Choose the decision policy using calibration data, then evaluate the frozen choice on held-out records. Repeatedly adjusting a threshold after inspecting test results turns the test set into part of the development process and weakens the claim made from it.

Preserve the split, labels, configuration, and selection procedure with the result. A later reviewer should be able to identify which decisions were made before the final evaluation and which observations came afterward. This is particularly useful when several configurations are being compared.

Do not copy the threshold from a published study into a different workflow merely because the study reports a favorable result. A threshold is a decision under particular score behavior, costs, and inputs. It needs to be selected and tested for the application in which it will operate.

## Check whether confidence separates errors

Ask the confidence score to help make the actual choice. Does it separate predictions that are correct from those that are wrong? A tidy-looking score that stays nearly the same across cases may give you little help deciding which tickets to route automatically. The number needs to earn its place at the branch between routing and review.

Evaluate the relationship between confidence, coverage, and error rate. As the system routes fewer tickets automatically, does the accepted set become meaningfully more reliable? Inspect ties and groups of cases with similar scores rather than relying only on a global calibration summary.

The paper is valuable because it keeps calibration and discrimination separate. Our operational reading is to require evidence that the score supports the intended decision. The existence of a probability field does not establish that it can safely control a review boundary.

## Give simple baselines a fair comparison

For a fixed classification task, include suitable conventional classifiers and the existing human process in the evaluation. A generative model may be useful for other parts of the service workflow while a different method handles the routing decision more effectively.

Keep labels and inputs consistent when comparing approaches. If a candidate receives additional context or uses a different taxonomy, describe that configuration separately. The goal is to identify a useful operating policy, not to produce a flattering comparison between unequal tasks.

Inspect the wrong routes that remain. Some error types may be tolerable with a clear reassignment path, while others need a more conservative treatment. The service owner should decide those boundaries from actual consequences rather than a model’s aggregate accuracy.

Follow a deferred ticket through to resolution. A routing policy has not demonstrated its value if its apparent savings merely move unfinished work into an unmeasured queue.

## Pilot the handoff as well as the classifier

Start with one queue whose categories and downstream owners are clear. Run the proposed policy alongside the current process, record the route it would have chosen, and review disagreements before enabling consequential changes. Include busy periods and cases outside the normal taxonomy.

Specify what information a deferred ticket carries to the human reviewer. A useful handoff can preserve the evidence and uncertainty that caused deferral, helping the reviewer reach a decision without reconstructing the entire interaction.

Return to the ticket and the person waiting for help. Did the service send the work down a useful path at an acceptable operating cost? Sometimes the answer will be an automatic route. Sometimes the evidence will support asking a person to decide. Give the evaluation room to recognize both, and follow the work far enough to establish that somebody can finish it.
