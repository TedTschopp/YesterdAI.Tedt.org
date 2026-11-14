---
title: Meta’s Muse Ember charges a higher rate for long prompts
summary: Meta launched Muse Ember for repeated agent tasks, with input and output rates that triple when
  a prompt exceeds 200,000 tokens.
section: Vendors
reader_job: How should a team estimate the cost of routing routine tasks and long documents to Muse Ember?
topics:
- infrastructure
- economics-adoption
- agents
takeaways:
- Meta lists $0.10 per million uncached input tokens and $0.50 per million output tokens for prompts up
  to 200,000 tokens.
- Both rates triple above 200,000 input tokens, so a workload’s long requests can change its average cost.
leader_action: Model cost per accepted result using the actual mix of short prompts, long prompts and
  escalations.
individual_action: Run a sample of routine extractions and long-document requests, then compare token
  use and review effort by prompt size.
evidence_type: vendor
rank: 3
sources:
- url: https://research.meta.ai/blog/muse-ember
  title: 'Introducing Our Smallest, Most Efficient Model: Muse Ember'
  publisher: Meta AI Research
  published_at: '2026-11-09T00:00:00Z'
  kind: vendor
  date_precision: day
- url: https://x.com/AIatMeta/status/2119853591703998787
  title: Muse Ember launch announcement
  publisher: AI at Meta
  published_at: '2026-11-09T18:04:15.894Z'
  kind: vendor
eligibility:
  url: https://x.com/AIatMeta/status/2119853591703998787
  published_at: '2026-11-09T18:04:15.894Z'
  precision: second
  verification: meta
  evidence: The public @AIatMeta launch post ID encodes November 9 at 18:04:15.894 UTC. Advance Intelligence
    shows the publisher post at 1:04 p.m. Eastern and ArtificialWatch corroborates 18:04:15 UTC. The direct
    X page returned 403. Meta’s complete research announcement shows November 9 without a clock time.
    The post establishes eligibility for the launch.
  discovered_url: https://research.meta.ai/blog/muse-ember
  verified_at: '2026-11-10T13:08:53.559051Z'
article_id: art_86708699833d3a97
edition_date: '2026-11-10'
published_at: '2026-11-10T13:08:53.559051Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://research.meta.ai/blog/muse-ember
feed_name: Ted Tschopp's AI News
feed_summary: 'Estimated GAI-style rating: Optional. Rationale (estimate): Estimated from similar historically
  rated GAI selections. Selected in GAI Insights'' briefing dated 2026-11-10. Briefing source: https://gaiinsights.com/articles.'
feed_title: 'Introducing Our Smallest, Most Efficient Model: Muse Ember [ ~ ] (Estimated)'
feed_published_at: '2026-11-10T00:00:00+00:00'
feed_id: 4577dd898ad846d9cefc6fa352e4faa4
rating: Optional
technical_rating: ''
additional_feed_input:
  feed_name: TedTschopp News Graph - Top Stories
  feed_id: sty_748109105e142b3e
  feed_title: Meta launches Muse Ember, its smallest and most efficient AI model for complex reasoning
    and agent tasks, offering higher intelligence per cost than Claude Haiku 5.5 and GPT-6 Luna [ * ]
    [ ◼ ]
  feed_published_at: '2026-11-09T17:58:46Z'
  feed_summary: Meta introduced Muse Ember, a compact and efficient AI model designed for complex reasoning
    tasks such as tool calls, coding subtasks, routing, extraction, and long document parsing. It delivers
    superior intelligence per dollar compared to Claude Haiku 5.5 and GPT-6 Luna, matching or exceeding
    their performance at significantly lower costs. Muse Ember is available via the Meta Model API with
    pricing set at $0.10 per million input tokens and $0.50 per million output tokens. The model supports
    a 1 million token context window and up to 512,000 output tokens, enabling it to process entire codebases
    or document sets in a single call. Early testing by partners highlighted its speed, accuracy, and
    efficiency in tasks like contract review, candidate screening, and coding, with latency significantly
    lower than comparable models. Muse Ember also natively understands multiple modalities including text,
    images, audio, and video, allowing it to handle diverse real-world inputs without separate models.
    Designed for high-throughput agentic workloads, Muse Ember excels at repetitive, structured tasks
    agents perform throughout the day. It is positioned as a cost-effective foundation for enterprise
    AI agents handling workflows end to end, and it can be paired with Meta's larger Muse Wonder model
    for more complex problem-solving.
  rating: Important
  technical_rating: Important
---
An agent looking for one clause can send the likely pages or a stack of contracts. With Muse Ember, crossing 200,000 input tokens changes the price of the request. Meta released the small model in Muse Code and on its Model API for repeated work such as tool calls, code fixes and document extraction. It supports a context window of about one million tokens. [Meta’s launch announcement](https://research.meta.ai/blog/muse-ember)

For prompts up to 200,000 tokens, Meta lists $0.10 per million uncached input tokens and $0.50 per million output tokens. Above that line, the rates are $0.30 and $1.50. A 190,000-token uncached prompt therefore costs about two cents in input, while a 210,000-token prompt costs about six cents before the model writes a word. If your agent sends the same long document on every turn, check what the provider counts as cached input as well. [Meta’s pricing footnote](https://research.meta.ai/blog/muse-ember)

Meta’s launch table reproduces Artificial Analysis results that put Ember at about $0.14 per Intelligence Index task at maximum reasoning effort, compared with about $2.39 for Meta’s Muse Spark 1.3 at its maximum setting. Those are costs for a particular benchmark and token mix. An agent doing contract intake can add its own costs in retries, escalations and review, especially if the first extraction misses a field. [Meta’s benchmark comparison](https://research.meta.ai/blog/muse-ember)

Try both sizes on the same work. Give Ember the likely pages for one run and the full document for another, then have a reviewer check the extracted fields and their source passages. If the shorter request misses an exception buried in an appendix, count the time a reviewer spends finding it by hand.
