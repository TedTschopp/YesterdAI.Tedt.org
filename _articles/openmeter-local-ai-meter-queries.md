---
title: OpenMeter tests local AI on industrial meter data
summary: An OpenMeter preprint finds that planning and retrying queries helped a small local model on industrial
  meter data, while accuracy remained limited.
section: Enterprise Ops
reader_job: When does an agent pipeline help a local model query sensitive meter data, and what still needs
  operator review?
topics:
- infrastructure
- evaluation
- agents
takeaways:
- The full pipeline improved relaxed execution accuracy from 36.3% to 42.4% against the strongest local single-agent
  setup on that measure.
- A query that runs can still answer the wrong question; keep both the data boundary and result checks visible.
leader_action: Start with a read-only pilot on questions operators can independently verify, and set an accuracy
  threshold for each intended use.
individual_action: Compare generated queries and returned values against reviewed examples with wrong units,
  missing intervals and similar meter names.
evidence_type: preprint
rank: 3
sources:
- url: https://arxiv.org/abs/2611.09372v1
  title: Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter Data
  publisher: arXiv / Carlos Martín-Abellán and Mark Kröll
  published_at: '2026-11-09T01:00:00Z'
  kind: preprint
eligibility:
  url: https://arxiv.org/abs/2611.09372v1
  published_at: '2026-11-09T01:00:00Z'
  precision: second
  verification: visible
  evidence: arXiv lists v1 in New submissions for Monday, November 9 in cs.AI. Its official availability schedule
    makes the before-2 p.m. Eastern Friday batch public Sunday at 8 p.m. Eastern (November 9 01:00 UTC). Submission
    history records 2026-11-06T12:11:34Z; that is the deposit, not public availability. The November 9 09:37
    UTC verified GitHub feed snapshot independently bounds availability before cutoff.
  discovered_url: https://arxiv.org/abs/2611.09372
  verified_at: '2026-11-09T13:10:38.500275Z'
  submitted_at: '2026-11-06T12:11:34Z'
  announcement_listing: https://arxiv.org/list/cs.AI/new
  announcement_schedule: https://info.arxiv.org/help/availability.html#announcement-schedule
article_id: art_990f9380e605fd05
edition_date: '2026-11-09'
published_at: '2026-11-09T13:10:38.500275Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://arxiv.org/abs/2611.09372
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'arXiv:2611.09372v1 Announce Type: new Abstract: Energy management officers and grid operators
  increasingly rely on smart meter data for anomaly detection, performance monitoring, and strategic decision-making.
  However, extracting actionable insights from large-scale, heterogeneous telemetry databases requires advanced
  SQL and data engineering expertise, creating a critical bottleneck for non-technical personnel. Furthermore,
  the strict data privacy regulations and security constraints inherent to critical energy infrastructure
  often prohibit the routing of sensitive consumer data through cloud-based Large Language Models (LLMs).
  To address these challenges, we present OpenMeter, a schema-agnostic Multi-Agent System (MAS) designed to
  translate natural language queries into executable code and human-readable insights. This architecture lowers
  the technical barrier for day-to-day utility operations by empowering non-expert personnel to interact with
  complex databases through intuitive natural language dialogue, transforming raw telemetry into a highly
  valuable tool for routine grid workflows and strategic decisions. Multi-scenario ablation studies over this
  environment demonstrate that full multi-agent orchestration shows its largest observed accuracy gains on
  resource-constrained local hardware (+6.1 pp EX-R over the strongest single-agent configuration); at frontier
  scale, individual components retain value but should be enabled selectively, indicating that the cost of
  full orchestration is justified specifically where privacy demands local execution.'
feed_title: Enabling Privacy-Preserving Natural Language Access to Industrial Smart Meter Data [ * ] [ ◼ ]
feed_published_at: '2026-11-09T05:00:00Z'
feed_id: sty_d747d67804130faa
rating: Important
technical_rating: Important
---
A meter query can run without an error and still return the wrong answer. It might read the right meter for the wrong hour. That distinction matters if an operator is about to investigate an alarm.

In the [OpenMeter preprint](https://arxiv.org/abs/2611.09372v1), Carlos Martín-Abellán and Mark Kröll test a system that turns a question into a database query and then explains the result. One component plans the work, another writes and retries the query, and a third interprets the readings. The authors use a sandbox with read-only execution and test on roughly 7.5 million rows from an industrial partner. The local experiments ran on premises; the separate cloud experiments used data with identifying information anonymized before transmission.

On a 9-billion-parameter model running locally, the full pipeline lifted the relaxed execution score from 36.3% to 42.4% compared with the best single-agent setup on that measure. That [measure](https://arxiv.org/html/2611.09372v1#S4) allows extra columns as long as the reference values are present and the row count matches. On the stricter test, which also checks column count and order, the full pipeline reached 32.2%. These are averages from five runs of 49 questions. On the larger cloud model, the plain single-agent baseline had the best relaxed score. The local gain makes those extra steps worth testing on smaller models. The scores still leave plenty for an operator to check.

For a pilot, give the system a small set of questions with results someone has already checked. Include a missing interval or two meters with similar names. Have the operator see the time range, units and rows that produced the answer. The useful result is a reading the operator can check before acting on it.
