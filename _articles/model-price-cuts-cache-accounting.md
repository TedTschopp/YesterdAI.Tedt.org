---
article_id: art_240888442444abd5
story_key: https://minimaxir.com/2026/10/cheap-llms
title: Model price cuts make cache accounting matter
summary: Max Woolf’s new pricing analysis highlights cache reads; workload accounting determines whether lower
  token rates reduce the cost of accepted work.
section: Vendors
edition_date: '2026-10-26'
published_at: '2026-10-26T12:08:51.029733Z'
rank: 1
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: practitioner
reader_job: How should a team compare model costs when ordinary input, cached context and completed-task quality
  differ?
takeaways:
- Max Woolf’s October 25 post analyzes earlier price changes; it does not announce a new cut.
- Measure billed usage categories and accepted results before treating a lower token rate as a workflow saving.
topics:
- economics-adoption
- infrastructure
eligibility:
  url: https://minimaxir.com/2026/10/cheap-llms/
  published_at: '2026-10-25T21:00:00Z'
  precision: second
  verification: jsonld
  evidence: Publisher BlogPosting JSON-LD and article:published_time agree on 2026-10-25T14:00:00-07:00; the
    original commentary is eligible, while its older announcement dates remain explicit.
  discovered_url: https://minimaxir.com/2026/10/cheap-llms/
  verified_at: '2026-10-26T12:08:51.029733Z'
sources:
- url: https://minimaxir.com/2026/10/cheap-llms/
  title: OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why?
  publisher: Max Woolf
  published_at: '2026-10-25T21:00:00Z'
  kind: practitioner
  date_precision: second
- url: https://www.anthropic.com/claude-opus-5-5
  title: Claude Opus 5.5
  publisher: Anthropic
  published_at: '2026-09-22T00:00:00Z'
  kind: vendor
  date_precision: day
  date_basis: Publisher visible original day September 22, 2026; older context for the specified token rates
    and vendor comparison, not eligibility.
leader_action: Compare representative accepted tasks using separate ordinary-input, cache-read, cache-write
  and output charges.
individual_action: Inspect one agent run’s billed usage categories and retain retries and correction work
  in the task-cost comparison.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: OpenAI and Anthropic have significantly reduced the prices of their large language models (LLMs)
  since June 2026, with cuts reaching up to 80%. These reductions include OpenAI's GPT-5.6 Luna and Sol models
  and Anthropic's Claude series, reflecting a rapid decrease in cost without apparent compromises in output
  quality. The price cuts appear to be a response to competitive dynamics between the two companies, aiming
  to make LLM usage more affordable for various applications, including agentic coding. The timeline of announcements
  shows a pattern of tit-for-tat price adjustments, with both companies lowering input, output, and cache
  read token costs. Notably, cache read costs, which dominate token expenditure in agent-based coding, have
  been reduced by up to 75%, significantly lowering overall usage costs. Despite the price drops, model performance
  has generally remained stable or improved, with newer versions like Anthropic's Claude Opus 5.5 and OpenAI's
  GPT-6.1 Sol offering competitive benchmarks. These price reductions have contributed to a broader trend
  of decreasing cost-per-token in the LLM market, even as aggregate spending rises due to increased adoption
  and improved model capabilities. The moves highlight the evolving economics of AI services and the strategic
  pricing responses by leading AI providers to maintain market share and encourage wider usage.
feed_title: OpenAI and Anthropic cut large language model prices by up to 80% over several months amid competitive
  pressure [ * ] [ ◼ ]
feed_published_at: '2026-10-25T21:11:31Z'
feed_id: sty_f0c2d6bcb7c78c05
rating: Important
technical_rating: Important
---

The cheaper line on a model's rate card may be the one your budget spreadsheet barely tracks.

In an [October 25 analysis](https://minimaxir.com/2026/10/cheap-llms/), practitioner Max Woolf reviews several months of OpenAI and Anthropic pricing and argues that cache-read charges deserve more attention in agent workloads. His post is new commentary on earlier announcements, rather than an October 25 price cut. He also argues that competing inference providers constrain prices. That is an economic interpretation, not evidence that any particular rate will last.

A cache read lets a request reuse previously processed prompt context at a separate rate. The difference is visible in [Anthropic's September 22 Opus 5.5 announcement](https://www.anthropic.com/claude-opus-5-5): standard input costs $4 per million tokens, output $20, and cache reads $0.20. Anthropic reports a 40% reduction in typical workload cost against Opus 5. That is the vendor's comparison, with its own workload assumptions.

Consider a deliberately simple example using those rates. One million ordinary input tokens, ten million cache-read tokens and 100,000 output tokens cost $4, $2 and $2 respectively: $8 before cache writes or other charges. The largest token count contributes only a quarter of that subtotal. Counting every token at the ordinary input rate would describe a different bill.

What should a team carry into its next model comparison? Record ordinary input, cache reads, cache writes and output separately. Then connect the total to an accepted result, including retries and human correction. A cheaper cache rate cannot compensate for a workflow that repeatedly loses reusable context or produces work someone must redo.

Woolf's broader forecast may prove right or wrong. The operational question is already testable: replay representative tasks, inspect the billed usage categories, and compare the cost of results that meet the same acceptance standard.
