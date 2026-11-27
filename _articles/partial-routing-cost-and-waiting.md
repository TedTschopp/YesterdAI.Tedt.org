---
title: Partial routing changes the cost of agent handoffs
summary: Partial Routing improved software-agent scores in small tests, but delegation added waiting time.
  Token savings and completed-work costs need separate measurements.
section: Enterprise Ops
topics:
- agents
- economics-adoption
- infrastructure
reader_job: When does delegating part of a coding task to a cheaper model justify its coordination and
  waiting costs?
takeaways:
- Guided delegation improved the tested scores, with lower token spending on ViBench and similar spending
  on Terminal-Bench.
- Terminal-Bench median duration rose from 14 to 69 minutes; a lead given only a plan also saved tokens.
leader_action: Set acceptable completion time alongside model spending before funding a delegation pilot.
individual_action: Compare the solo lead, a planned solo lead and a delegated run using the same completion
  tests and elapsed-time accounting.
rank: 1
article_id: art_67c9e709c0576805
story_key: https://arxiv.org/abs/2611.33402
edition_date: '2026-11-27'
published_at: '2026-11-27T13:12:07.383856Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: preprint
sources:
- url: https://arxiv.org/abs/2611.33402
  title: 'Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows'
  publisher: arXiv
  published_at: '2026-11-26T01:00:00Z'
  submitted_at: '2026-11-24T20:23:53Z'
  kind: preprint
- url: https://arxiv.org/html/2611.33402v1
  title: 'Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows — full paper,
    version 1'
  publisher: arXiv
  published_at: '2026-11-26T01:00:00Z'
  kind: preprint
eligibility:
  url: https://arxiv.org/abs/2611.33402
  published_at: '2026-11-26T01:00:00Z'
  submitted_at: '2026-11-24T20:23:53Z'
  precision: second
  verification: visible
  timestamp_url: https://arxiv.org/list/cs.AI/pastweek?show=2000
  evidence: The Thu, 26 Nov 2026 (showing 248 of 248 entries ) primary cs.AI listing includes 2611.33402
    as entry 68, with no cross-list or replacement marker. The official availability schedule at https://info.arxiv.org/help/availability.html
    establishes Wednesday 20:00 America/New_York announcement, equivalent to 2026-11-26T01:00:00Z. This
    is the inclusive start of this edition’s window. The Thursday Thanksgiving holiday does not move the
    preceding Wednesday announcement. Earlier deposit and later feed timestamps are recorded separately
    and are not used as publication evidence.
  verified_at: '2026-11-27T13:12:07.383856Z'
  event: public_announcement
feed_name: TedTschopp News Graph - Top Stories
feed_id: sty_55899a5229224c84
feed_title: Researchers introduce partial routing to delegate subtasks from expensive AI models to cheaper
  ones, improving task performance and reducing costs on ViBench and Terminal-Bench 4.0 [ ~ ] [ ◼ ]
feed_summary: Researchers propose partial routing, a method that enables a leading AI model to delegate
  suitable subtasks to a less costly worker model based on analysis of past task runs. This approach identifies
  recurring subtasks and measures each model's quality and cost, guiding delegation without retraining
  either model. Evaluations on ViBench and Terminal-Bench 4.0 show that partial routing improves mean
  task performance and reduces costs compared to using the lead model alone or task-level routing. With
  a delegation parameter set to 0.75, the method increased the lead's ViBench score from 70.2 to 78.5
  while lowering costs by 19%, and raised the Terminal-Bench pass rate from 54% to 61% at similar cost.
  The study demonstrates that leveraging past execution data can enhance planning and delegation efficiency
  with minimal overhead.
feed_published_at: '2026-11-27T05:00:00Z'
feed_snapshot: docs/runs/2026-11-27-feed-snapshot.json
rating: Optional
technical_rating: Important
---

An agent can spend less on model calls while keeping a person waiting longer. [Partial Routing, a new preprint](https://arxiv.org/abs/2611.33402), studies that trade-off by delegating pieces of a job to a cheaper model.

The method first examines runs where each model worked alone. Model-based annotators identify recurring subtasks, and a judge compares their quality and token costs. Those measurements become instructions telling the lead agent which work to keep, delegate or decide about as it goes. Neither model needs retraining.

On ten held-out ViBench application-building tasks, the strongest tested delegation setting raised the mean score from 70.2 to 78.5 at 19% lower token cost than the lead alone. On 23 Terminal-Bench tasks, it raised the pass rate from 54.3% to 60.9% at approximately the same cost.

The [controls and limitations](https://arxiv.org/html/2611.33402v1) complicate the savings story. Giving the lead a subtask plan without any worker also reduced cost. Delegation itself added waiting: on Terminal-Bench, median task duration was 69 minutes for the strongest guided setting, against 14 minutes for the lead alone. The lead waits for worker reports.

These are small software-workload evaluations, with three runs per ViBench task and two per Terminal-Bench task for the main model pairs. The annotator and judge were checked for consistency, without validation against human labels. A cheaper token bill does not establish lower operating cost elsewhere.

For an internal trial, compare the lead alone, the lead with a plan, and the lead with a worker. Preserve the same completion tests. Record elapsed time, token spending, retries and the work a person must redo. Include the initial profiling cost when estimating whether repeated use pays for it.

Then decide where waiting matters. An overnight repository cleanup and an engineer blocked on a fix can accept different trade-offs. The useful handoff finishes acceptable work within the budget that includes the person’s time.
