---
title: Google’s Gemini Decisions API scores choices in one pass
summary: Gemini Decision 1 scores up to 1,000 predefined questions against a shared input and returns
  probabilities for routing, grading and review.
section: Vendors
reader_job: When can a dedicated scoring endpoint replace a generated answer for a repetitive decision?
topics:
- infrastructure
- evaluation
takeaways:
- Gemini Decision 1 can score yes-or-no, multiple-choice and rubric questions against a shared multimodal
  input.
- Google bills the shared input once per request, with additional input tokens for each question’s instructions
  and criteria.
leader_action: Price a bounded pilot by the cost of correctly routed items, including the work sent to
  people.
individual_action: Measure false accepts and review volume on labeled examples before setting confidence
  thresholds.
evidence_type: vendor
sources:
- url: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
  title: 'Gemini Decisions API: Fast, calibrated multimodal decisions'
  publisher: Google DeepMind / Min Choi and Felix Yu
  published_at: '2026-11-11T18:00:00Z'
  kind: vendor
rank: 3
eligibility:
  url: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
  published_at: '2026-11-11T18:00:00Z'
  precision: second
  verification: meta
  evidence: The original Google blog visibly dates the release November 11, 2026. Google Blog’s recorded
    publication time is 18:00 UTC, matching AGI Pulse’s contemporaneous timestamp report, the AI Barometer
    archive and the pinned ranked feed. The first-party XML was unavailable to the web reader. The time
    is supported by the captured publisher timestamp and is not inferred from a feed placeholder.
  discovered_url: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
  verified_at: '2026-11-12T13:17:22.588594Z'
article_id: art_02bfed5e7aa817ea
edition_date: '2026-11-12'
published_at: '2026-11-12T13:17:22.588594Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'Google has introduced the Gemini Decisions API, powered by the Gemini Decision 1 model,
  enabling fast, probabilistic evaluation of up to 1,000 yes/no, multiple-choice, and rubric-scoring questions
  in a single pass across various data types including text, images, audio, video, and PDFs. The API provides
  confidence scores for each decision, supporting use cases like content grading, policy checks, and model
  routing with low latency and cost efficiency. The Gemini Decision 1 model processes multimodal inputs
  natively and returns probabilities without token-by-token decoding, achieving 150-250 ms end-to-end
  latency and costing $0.10 per million input tokens with no output token charges. It supports combined
  modalities in one request and offers three decision types: binary (yes/no), multiple choice, and ordered
  rubric scoring, each with confidence metrics to enable fallback or human review. Google teams are already
  using the API for dynamic model routing and other control plane functions.'
feed_title: Google launches Gemini Decisions API for fast, calibrated multimodal decision-making across
  text, images, audio, video, and PDFs [ * ] [ ◼ ]
feed_published_at: '2026-11-11T18:00:00Z'
feed_id: sty_38f100496edac62f
rating: Important
technical_rating: Important
---
An invoice routing service has a narrow job. Send a bill to accounts payable, to a reviewer or back to the intake team. Google’s new Gemini Decisions API takes the questions and options you supply and returns scores. Gemini Decision 1 can answer up to 1,000 independent questions about a shared input in one pass through the model. [Google’s announcement](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

A team could send an invoice PDF and a short note about its vendor in one request. One question could check whether a purchase order appears. Another could rate how legible the scan is. The service supports yes-or-no checks, multiple choice and ordered rubrics, with probability information that the application can use to send uncertain cases to a reviewer. Its inputs can combine text, images, audio, video and PDFs. [Google’s examples and response types](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

Google lists a price of 10 cents per million input tokens and zero output-token charges. The shared input is billed once, with each added question contributing its own instructions and criteria. Google reports end-to-end times of 150 to 250 milliseconds in tests with contexts up to 16,000 tokens. It says latency stayed nearly flat from one to 100 questions. A workload with more questions needs its own performance test. [Google’s benchmark and pricing](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

Take a week of invoices that staff have already routed. Compare the model’s probabilities with what the staff actually found, including blurry scans and unusual vendors. The useful threshold is the one that catches expensive errors while leaving the review queue small enough for someone to work through.
