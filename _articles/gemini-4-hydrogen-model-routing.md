---
title: Google releases Gemini 4 Hydrogen for everyday coding
summary: Hydrogen adds four levels of reasoning effort and a flat API rate across its million-token context
  window.
section: Vendors
reader_job: How can a coding team compare Hydrogen with its current model on speed, output quality and cost?
topics:
- infrastructure
- evaluation
takeaways:
- Google lists $1.50 per million input tokens and $7.50 per million output tokens across Hydrogen’s full context
  window.
- Google Antigravity’s Orchestrator can switch between models such as Hydrogen and Carbon within a session.
leader_action: Evaluate Hydrogen on a sample of accepted changes and compare time, review effort and total
  cost.
individual_action: Run the same routine change and difficult defect at two reasoning settings with the same
  tests.
evidence_type: vendor
sources:
- url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
  title: Introducing Gemini 4 Hydrogen
  publisher: Google DeepMind / Koray Kavukcuoglu
  published_at: '2026-11-12T18:00:00Z'
  kind: vendor
- url: https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-hydrogen/
  title: 'Gemini 4 Hydrogen: Everyday coding and agentic workflows for developers'
  publisher: Google
  published_at: '2026-11-12T18:00:00Z'
  kind: vendor
rank: 3
eligibility:
  url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/
  published_at: '2026-11-12T18:00:00Z'
  precision: second
  verification: meta
  evidence: Google’s original blog and developer post display November 12. The two Google Blog publication
    timestamps are captured as 18:00 UTC in AI Buzz’s source-date archive, distinct from its 18:15 UTC first-seen
    time. Google’s developer-blog record in the hosted ranked feed agrees, and Google DeepMind’s official launch
    post identifier independently places the announcement at 18:02:36 UTC.
  discovered_url: https://deepmind.google/blog/introducing-gemini-4-hydrogen/
  verified_at: '2026-11-13T13:26:11.778218Z'
article_id: art_d7c21c501eb23f12
edition_date: '2026-11-13'
published_at: '2026-11-13T13:26:11.778218Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Google DeepMind introduced Gemini 4 Hydrogen, a new AI model designed for rapid execution in
  diverse coding and agentic workflows, complementing its more complex Gemini 4 Carbon and Argon models. Hydrogen
  is available across multiple Google platforms including AI Studio, the Gemini API, and Google Search, offering
  improved speed and efficiency for everyday tasks. Hydrogen outperforms previous models in speed and accuracy,
  completing tasks 2.5 times faster than its predecessor and significantly reducing errors. It supports large
  context windows with a flat pricing model and excels in multi-model workflows through Google Antigravity's
  Orchestrator, which dynamically switches between models to optimize performance and cost. The model also
  demonstrates strong capabilities in multimodal knowledge work, web development, and enterprise coding tasks,
  making it a versatile tool for developers and businesses.
feed_title: Google DeepMind launches Gemini 4 Hydrogen, a fast, efficient AI model for coding and agentic workflows,
  integrated across Google AI Studio and Google Search [ * ] [ ◼ ]
feed_published_at: '2026-11-12T18:00:50Z'
feed_id: sty_6417b4f858f3a464
rating: Important
technical_rating: Important
---
A coding assistant that writes a missing unit test has a different job from one tracing a timeout across three services. Google released Gemini 4 Hydrogen on Nov. 12 for everyday coding and tasks that use tools. Developers can try it in Google AI Studio or call it through the Gemini API. The model offers four levels of reasoning effort, with high as the default. [Google’s launch](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/) · [Developer announcement](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-hydrogen/)

Google lists API prices of $1.50 per million input tokens and $7.50 per million output tokens across the full million-token context window. Changing the reasoning level can still change how long a request takes and how much it costs. A call that spends longer working through a defect can use more tokens even when the price per token stays the same. [Google’s pricing and reasoning settings](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)

In Google Antigravity, a feature called Orchestrator can switch between models such as Hydrogen and Carbon during one session. Google reports that on Terminal-Bench 4.0 Orchestrator came close to Carbon’s task success rate while using 24% less quota and finishing 19% faster on average. Those are results from Google’s test of its routing feature. [Google’s benchmark](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)

Replay a routine change and a defect that sent someone through several files. Run them at two reasoning settings with the same tests and acceptance criteria. Count the retries and the reviewer’s corrections alongside the API bill. That shows which work benefits from spending longer on a request.
