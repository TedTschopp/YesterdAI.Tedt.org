---
article_id: art_3e32bae570ff21ee
story_key: https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model
title: Gemini 4 Carbon starts with restricted access for cyber defenders
summary: Google’s new model pairs claimed cybersecurity gains with a phased defender rollout; announced
  pricing and unguarded benchmark scores do not establish broad availability or local performance.
section: Vendors
edition_date: '2026-10-29'
published_at: '2026-10-29T12:11:15.279432Z'
rank: 2
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: vendor
reader_job: What does Carbon’s announcement make available now, and what evidence would justify an enterprise
  pilot?
takeaways:
- Google starts with selected cyber defenders and trusted partners; broader developer and business access
  is still forthcoming.
- The launch post reports external cyber scores without guardrails, so a pilot must test the configuration
  actually offered.
topics:
- infrastructure
- security
- evaluation
eligibility:
  url: https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/
  published_at: '2026-10-28T17:00:00Z'
  precision: second
  verification: jsonld
  evidence: Original publisher published_time meta and NewsArticle JSON-LD give 2026-10-28T17:00:00+00:00;
    Google’s companion announcement agrees. dateModified is 2026-10-28T18:02:36.657805+00:00, inside the
    reporting window.
  discovered_url: https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/
  verified_at: '2026-10-29T12:11:15.279432Z'
sources:
- url: https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/
  title: 'Gemini 4 Carbon: our next frontier model'
  publisher: Google DeepMind
  published_at: '2026-10-28T17:00:00Z'
  kind: vendor
  date_precision: second
- url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
  title: 'Gemini 4 Carbon: our next frontier model'
  publisher: Google
  published_at: '2026-10-28T17:00:00Z'
  kind: vendor
  date_precision: second
leader_action: Confirm access and the offered safeguards before budgeting a Carbon evaluation against
  the organization’s own security workflow.
individual_action: Preserve the available model configuration, task permissions, patch checks and observed
  failures with the pilot result.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Google DeepMind announced Gemini 4 Carbon, its most powerful AI model to date, featuring
  state-of-the-art cybersecurity performance and enhanced abilities for complex, long-duration engineering
  tasks. The model leads benchmarks in vulnerability detection, exploitation, and patching, and shows
  significant improvements in generating secure code and reducing errors in live coding environments.
  Building on the recently released Gemini 4 Argon, Carbon is designed for sustained agentic workflows
  and excels in multi-step engineering challenges. Google is rolling out Carbon gradually through a controlled
  program with cybersecurity partners and plans to make it available to developers and businesses after
  further testing and refinement of safety measures. Gemini 4 Carbon maintains a multi-layered safety
  and security framework, improving alignment and resilience against misuse. It is priced at $2 per million
  input tokens and $10 per million output tokens, matching Argon's introductory pricing, with discounts
  for cached inputs.
feed_title: Google DeepMind launches Gemini 4 Carbon, a frontier AI model with advanced cybersecurity
  and long-horizon engineering capabilities [ * ] [ ◼ ]
feed_published_at: '2026-10-28T17:00:58Z'
feed_id: sty_4d1a214f8b70e9d3
---

Gemini 4 Carbon’s first users will be selected cyber defenders. An enterprise planning a general rollout still has an access gate ahead.

In its [October 28 announcement](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/), Google describes a phased release through its Fairwind Program, beginning with a subset of defenders and expanding to trusted partners. Broader access through developer, business and consumer products remains forthcoming. The announcement establishes a new candidate to evaluate, with access still depending on that rollout.

Google reports 88.2% on SEC-bench Pro for finding vulnerabilities, 54.8% on ExploitGym for exploitation and 71.0% on CWE-bench for patching. The post explicitly says these external cybersecurity benchmarks were evaluated without guardrails. Those are vendor-reported results under stated test conditions. They do not establish the performance of the safeguarded service a customer will eventually receive.

The [companion Google post](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/) announces introductory pricing of $2 per million input tokens and $10 per million output tokens, with cached input priced 95% below the input rate. These are launch terms for the model, rather than evidence that a general enterprise account can already purchase access.

The company also describes internal engineering runs lasting days. Long execution makes the recovery path part of the evaluation: what happens when a tool fails, a permission expires or a proposed patch breaks another behavior? A benchmark score cannot answer those workflow questions on its own.

If your organization obtains access, start with a bounded repair task and the configuration actually offered. Preserve the allowed tools, source revision, generated change, independent patch checks and any intervention needed to finish. Measure accepted repairs and total effort, including failed attempts and human review. Those are proposed evaluation steps, not tests performed by this publication.

The next useful result is a repair that survives review in the environment where the team will run it. Keep that result attached to its access conditions and safeguards.
