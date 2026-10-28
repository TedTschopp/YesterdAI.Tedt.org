---
article_id: art_a9a5887ca8150cae
story_key: https://arxiv.org/abs/2610.37276v1
title: Two studies separate faster agent optimization from cheaper evaluation
summary: 'Parallel GEPA proposals and EvalAlloc target different costs of improving agent workflows: elapsed
  time and the number of evaluations needed to choose a candidate.'
section: Enterprise Ops
edition_date: '2026-10-28'
published_at: '2026-10-28T14:53:45.531563Z'
rank: 2
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: preprint
reader_job: Which cost of agent optimization can these studies reduce, and what must remain comparable
  when testing either method?
takeaways:
- GEPA batching reduces elapsed optimization time in two tasks; available parallel workers limit the gain.
- EvalAlloc reserves evaluations for final selection and reports comparable or higher mean scores with
  roughly half the evaluation cells in its tested settings.
topics:
- agents
- evaluation
- economics-adoption
eligibility:
  url: https://arxiv.org/abs/2610.37276v1
  published_at: '2026-10-27T14:06:26Z'
  precision: second
  verification: visible
  evidence: Original arXiv submission history gives v1 Tue, 27 Oct 2026 14:06:26 UTC. The companion GEPA
    paper v1 was submitted at 07:41:40 UTC the same day. Both original versions and full texts were read;
    feed announcement times did not control eligibility.
  discovered_url: https://arxiv.org/abs/2610.37276
  verified_at: '2026-10-28T14:53:45.531563Z'
sources:
- url: https://arxiv.org/abs/2610.37276v1
  title: Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?
  publisher: Sichun Luo and colleagues / arXiv
  published_at: '2026-10-27T14:06:26Z'
  kind: preprint
  date_precision: second
- url: https://arxiv.org/html/2610.37276v1
  title: EvalAlloc — version 1 full text
  publisher: arXiv
  published_at: '2026-10-27T14:06:26Z'
  kind: preprint
  date_precision: second
- url: https://arxiv.org/abs/2610.36774v1
  title: 'Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster and Better'
  publisher: Jialin Zhang and colleagues / arXiv
  published_at: '2026-10-27T07:41:40Z'
  kind: preprint
  date_precision: second
- url: https://arxiv.org/html/2610.36774v1
  title: GEPA parallel proposals — version 1 full text
  publisher: arXiv
  published_at: '2026-10-27T07:41:40Z'
  kind: preprint
  date_precision: second
leader_action: Separate elapsed time, evaluation executions and dollars when budgeting an agent-optimization
  experiment.
individual_action: Keep a held-out test set and record worker limits, candidate versions and final-selection
  evaluations.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Researchers investigate how to allocate evaluation budgets in large language model (LLM)-driven
  agent scaffold evolution, which improves agent workflows through iterative candidate generation and
  evaluation but incurs high execution costs when evaluating every candidate fully. They find that sparse
  feedback can sustain productive evolution, while targeted evaluation enhances final selection, and propose
  EvalAlloc, a framework combining sparse search-time feedback with targeted final confirmation to optimize
  evaluation efficiency. EvalAlloc uses a short fully evaluated warm-up to establish a shared informative
  core and calibrate a response model, then applies paired successive halving after search to reuse observations
  and execute only missing evaluations. Tested across four benchmarks and two evolution frameworks, EvalAlloc
  achieves higher mean performance than full evaluation in most settings while using approximately half
  as many evaluation cells, indicating a more efficient approach to managing evaluation costs in LLM-driven
  agent development.
feed_title: Researchers propose EvalAlloc framework to optimize evaluation budget allocation in LLM-driven
  agent scaffold evolution, achieving higher performance with half the evaluations [ ~ ] [ ◼ ]
feed_published_at: '2026-10-28T04:00:00Z'
feed_id: sty_64f5e88793942d83
discovery_feeds:
- feed_name: TedTschopp News Graph - Top Stories
  feed_id: sty_64f5e88793942d83
  url: https://arxiv.org/abs/2610.37276
  date_published: '2026-10-28T04:00:00Z'
- feed_name: TedTschopp News Graph - Top Stories
  feed_id: sty_1f89ca79287a731f
  url: https://arxiv.org/abs/2610.36774
  date_published: '2026-10-28T04:00:00Z'
---

An agent-improvement run can spend its budget in two ways: waiting for work to finish and paying to find out which change helped. Two October 27 preprints tackle those costs from different directions.

The [GEPA batching study](https://arxiv.org/html/2610.36774v1) changes the queue. GEPA proposes edits to an agent’s prompts or code and evaluates them. The extension proposes several candidates together and runs their evaluations concurrently. Most batched settings finished in half the elapsed time or less across two tasks. The best reported test scores rose from 68.9% to 72.1% on LiveBench-Math and from 49.0% to 60.0% on HoVer, using different batch configurations.

Each setting received the same task-specific budget of evaluation calls. That makes the result more useful than a comparison that simply buys more trials. But extra parallelism has limits: slow calls and a finite worker pool still determine when a batch finishes. These are benchmark results, rather than a promised speedup for an enterprise workflow.

The [EvalAlloc study](https://arxiv.org/html/2610.37276v1) changes where evaluation effort goes. It fully evaluates a short opening set, then uses shared informative tasks and a fixed scoring reference to guide further search. Afterward, it concentrates additional evaluations on choosing among candidates, reusing observations already collected.

Across four benchmarks, two evolution frameworks and three runs per setting, EvalAlloc reports comparable or higher mean test performance with roughly half as many evaluation cells. A cell is one candidate executed on one task. That count does not translate directly into half the bill or half the elapsed time, because executions can have different costs and durations. The study’s test set remains separate from search and selection.

These methods invite two distinct experiments. If workers sit idle while proposals run in sequence, test batching under a fixed budget. If testing every candidate dominates spending, test selective evaluation while preserving a common comparison basis. Neither paper establishes the gain from combining them.

Before a run starts, reserve the final test set and name the stopping rule. Record elapsed time, evaluation count, spend and the chosen candidate’s test result separately. Otherwise, a faster search can conceal a more expensive decision.
