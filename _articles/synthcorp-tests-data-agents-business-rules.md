---
title: SynthCorp tests data agents against changing business rules
summary: A preprint presents simulated companies with dated policy changes, operational data and reference
  answers traceable to the events that produced them.
section: Enterprise Ops
reader_job: How can a data team test whether an agent finds the correct business rule before writing a query?
topics:
- evaluation
- agents
- governance
takeaways:
- SynthCorp uses simulated business events to create databases, documents and a catalog from the same history.
- The researchers created 256 tasks across seven simulated data estates. Most required evidence beyond SQL
  alone.
leader_action: Include dated policy changes and competing source tables when a data agent’s answers are
  evaluated.
individual_action: For one recurring metric, write a test where the schema is unchanged but a dated memo
  changes which rows count.
evidence_type: preprint
rank: 3
sources:
- url: https://arxiv.org/abs/2611.14765
  title: 'SynthCorp: A Platform for Creating Benchmarks for Data Agents'
  publisher: arXiv / Jiani Zhang et al.
  published_at: '2026-11-13T01:00:00Z'
  kind: preprint
- url: https://arxiv.org/html/2611.14765v1
  title: 'SynthCorp: A Platform for Creating Benchmarks for Data Agents (full text, v1)'
  publisher: arXiv / Jiani Zhang et al.
  published_at: '2026-11-13T01:00:00Z'
  kind: preprint
eligibility:
  url: https://arxiv.org/abs/2611.14765
  published_at: '2026-11-13T01:00:00Z'
  precision: second
  verification: visible
  evidence: arXiv's Friday, November 13 New submissions list contains arXiv:2611.14765 v1. The official
    schedule places that batch at 8 p.m. Eastern on Thursday (November 13 at 01:00 UTC); November 11 was
    an arXiv holiday. The submission history records an earlier deposit at 2026-11-10T21:43:12Z, not first
    public availability. The publisher's batch time, not the discovery feed's 05:00 UTC, establishes eligibility.
  discovered_url: https://arxiv.org/abs/2611.14765
  verified_at: '2026-11-14T13:11:11.430390Z'
  listing_url: https://arxiv.org/list/cs.AI/new?show=2000&skip=0
  schedule_url: https://info.arxiv.org/help/availability.html#announcement-schedule
  submitted_at: '2026-11-10T21:43:12Z'
article_id: art_cd1f1a3b900c4624
edition_date: '2026-11-14'
published_at: '2026-11-14T13:14:15.200836Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://arxiv.org/abs/2611.14765
feed_name: TedTschopp News Graph - Top Stories
feed_summary: SynthCorp is a platform designed to generate customizable data environments and benchmarks
  by simulating business events that produce and modify corporate data over time. It integrates relational
  databases, document stores, and data catalogs, scheduling events on a virtual calendar to build consistent
  data estates and generate analytical tasks with verified solutions. The platform has produced initial
  benchmarks featuring multiple data estates and tasks across various domains, enabling evaluation of model
  performance and data contexts without manual annotation. SynthCorp aims to support the development of
  advanced enterprise data agents by providing complex, targeted benchmarking scenarios that expose reasoning
  challenges in current models.
feed_title: SynthCorp launches platform to create customizable data estates and benchmarks for evaluating
  LLM-driven data agents with verified analytical tasks [ ~ ] [ ◼ ]
feed_published_at: '2026-11-14T05:00:00Z'
feed_id: sty_98305e2d2efe52bd
rating: Optional
technical_rating: Important
---
A sales table can tell you the size of a discount. It may take a policy memo to tell you whether staff purchases count toward revenue. If the policy changed last month, even a well-written query can give the wrong answer for the period you asked about.

[SynthCorp](https://arxiv.org/abs/2611.14765), a research prototype from Jiani Zhang and colleagues, makes cases like that testable. It simulates routine work and disruptions, such as a policy or schema change, on one calendar. Those events produce tables, documents and a catalog together. The system records what each event changed, so the researchers can trace the reference answer for a question back to the simulated events and check the program that computes it.

The paper describes seven generated data estates and 256 tasks. In 205 of them, the query needed evidence from a document or catalog. In the authors’ model comparisons, furnishing one retrieved document helped when one memo contained the relevant rule. On larger or more dispersed collections, agents that could look up several sources before answering generally did better. The results measure performance inside the simulation. An agent that does well there still needs to prove it can find the right rule in your own systems, with the documents and access it will actually have. [Benchmark construction and comparisons](https://arxiv.org/html/2611.14765v1)

A data team can borrow the test idea without recreating the entire company. Pick a familiar metric and ask for the same measure just before and just after a known rule change. Have the data owner supply the two expected answers and the dated source for each. Grade the policy the agent chose as well as the number it returned.
