---
title: Databricks gives Genie a shared set of business definitions
summary: Genie Ontology is generally available. It combines context learned from existing work with definitions
  that data owners approve in Unity Catalog.
section: Enterprise Ops
reader_job: How can several agents use the same approved metric while preserving its owner and permissions?
topics:
- governance
- agents
- evaluation
takeaways:
- Genie can use certified metrics and named business definitions alongside context learned from dashboards
  and queries.
- Genie Ontology is generally available. Databricks says the new always-on Genie is headed to preview.
leader_action: Assign an owner for the definitions that appear in executive reporting before sharing them
  across agents.
individual_action: Ask two authorized users the same business question and inspect which source and definition
  each answer cites.
evidence_type: vendor
sources:
- url: https://www.databricks.com/blog/announcing-ga-genie-ontology
  title: Announcing GA of Genie Ontology
  publisher: Databricks / Ken Wong, Paul Roome and Richard Tomlinson
  published_at: '2026-11-11T00:00:00-08:00'
  kind: vendor
  date_precision: day
- url: https://www.databricks.com/company/newsroom/press-releases/databricks-launches-new-always-genie-autonomous-ai-complex
  title: 'Databricks Launches New Always-on Genie: Autonomous AI for Complex Enterprise Work'
  publisher: Databricks
  published_at: '2026-11-11T00:00:00-08:00'
  kind: vendor
  date_precision: day
rank: 2
eligibility:
  url: https://www.databricks.com/company/newsroom/press-releases/databricks-launches-new-always-genie-autonomous-ai-complex
  published_at: '2026-11-11T00:00:00-08:00'
  precision: day
  verification: visible
  evidence: Databricks’ primary release is dated November 11, 2026, with a San Francisco dateline. That
    entire Pacific Standard Time day (November 11 08:00 UTC to November 12 08:00 UTC) is within the edition
    window. The same-day technical announcement confirms general availability for Genie Ontology. Original
    TechCrunch interview reporting is visibly dated 7:00 a.m. PST on November 11.
  discovered_url: https://techcrunch.com/2026/11/11/databricks-new-ai-agent-tells-ceo-ali-ghodsi-the-unvarnished-truth/
  verified_at: '2026-11-12T13:17:22.588594Z'
article_id: art_272019dad641131e
edition_date: '2026-11-12'
published_at: '2026-11-12T13:17:22.588594Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://www.databricks.com/company/newsroom/press-releases/databricks-launches-new-always-genie-autonomous-ai-complex
feed_name: TedTschopp News Graph - Top Stories
feed_summary: With Databricks at 12,000 employees, AI Ghodsi is the first to admit that he can't know
  everyone and that they are unlikely to confess the things that go wrong to him. But he doesn't need
  them to. He uses Databricks' newly revised Genie agent for that.
feed_title: Databricks' new AI agent tells CEO Ali Ghodsi the unvarnished truth [ * ] [ ◼ ]
feed_published_at: '2026-11-11T15:00:00Z'
feed_id: sty_2323201bb5550097
rating: Important
technical_rating: Important
---
Ask two departments how many customers are active and you can get two correct answers. One team might count recent purchases. Another might count accounts with a current contract. Databricks has made Genie Ontology generally available to give agents a way to find the definition that applies to the question. [Databricks’ release](https://www.databricks.com/blog/announcing-ga-genie-ontology)

Genie learns reusable pieces of context from dashboards, SQL queries and notebooks. Databricks calls these snippets and says they inherit access permissions from the original asset. Data owners can also publish approved definitions in Unity Catalog Pages and certify key performance indicators in Metric Views. Databricks says Genie prefers the authoritative Page for a defined term and cites it. Domains let different teams maintain definitions for their own work. [Databricks’ technical announcement](https://www.databricks.com/blog/announcing-ga-genie-ontology)

In a benchmark it built with Turing, Databricks says Genie passed 91% of runs in a simulated workspace for a fictional utility. The comparison tested a workspace where Genie already had learned business rules, alongside agents that had to find them during each run. The new always-on Genie, which Databricks says will run longer jobs and notify people when decisions are needed, is slated for preview. [Benchmark and release details](https://www.databricks.com/blog/announcing-ga-genie-ontology) and [product availability](https://www.databricks.com/company/newsroom/press-releases/databricks-launches-new-always-genie-autonomous-ai-complex)

Pick a metric that already causes disagreement. Give each approved definition an owner and ask the same question from the accounts of two people who should use it. When a quarterly report changes, both people should be able to follow the answer back to the rule that changed.
