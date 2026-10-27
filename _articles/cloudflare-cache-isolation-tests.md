---
article_id: art_89893d5f73c77515
story_key: https://blog.cloudflare.com/kv-cache-exposure-remediation
title: Cloudflare’s cache disclosure exposes a gap in isolation tests
summary: Cloudflare’s new account of a repaired Workers AI exposure shows why successful responses cannot establish
  that one customer’s data stayed separate from another’s.
section: Security
edition_date: '2026-10-27'
published_at: '2026-10-27T12:10:07.452207Z'
rank: 1
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: vendor
reader_job: What does Cloudflare’s disclosure establish about affected requests, and what should an operator
  test beyond successful responses?
takeaways:
- The October 26 disclosure concerns an August–September exposure that Cloudflare says it repaired on September
  9.
- Isolation tests need to examine returned content and rejected-request handling, alongside status codes and
  capacity.
topics:
- security
- infrastructure
eligibility:
  url: https://blog.cloudflare.com/kv-cache-exposure-remediation/
  published_at: '2026-10-26T22:01:23.889Z'
  precision: second
  verification: jsonld
  evidence: Cloudflare BlogPosting JSON-LD and article:published_time agree on 2026-10-26T22:01:23.889Z. Modification
    is 2026-10-27T08:31:47.243Z, also before cutoff; original disclosure controls eligibility. The incident
    and repair remain explicitly August 27–September 9.
  discovered_url: https://blog.cloudflare.com/kv-cache-exposure-remediation/
  verified_at: '2026-10-27T12:10:07.452207Z'
sources:
- url: https://blog.cloudflare.com/kv-cache-exposure-remediation/
  title: Cross-request KV cache exposure in the GLM-5.3 Workers AI model, and our remediation with SGLang
  publisher: Cloudflare
  published_at: '2026-10-26T22:01:23.889Z'
  kind: vendor
  date_precision: second
- url: https://www.lmsys.org/blog/2026-10-26-cf-security
  title: 'SGLang security update: improving request isolation'
  publisher: SGLang / LMSYS Org
  published_at: '2026-10-26T00:00:00Z'
  kind: practitioner
  date_precision: day
  date_basis: Publisher’s visible original date and publication meta give October 26, 2026 without a timezone.
    Midnight UTC is a storage placeholder, not an observed publication instant. Secondary coordinated account
    only; Cloudflare’s exact original time establishes eligibility.
leader_action: Ask the serving team for evidence that separate customers’ requests remain isolated when capacity
  limits and failure paths are exercised.
individual_action: Compare the running cache capacity with the configured context window and test rejected
  requests with distinct synthetic markers.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Cloudflare addressed a tenant isolation issue in its GLM-5.3 Workers AI model that caused some
  responses to include data from other customers' requests between August 27 and September 9, 2026. The problem
  affected 155 responses involving prompts longer than 681,280 tokens and was discovered by security researcher
  Gadi Evron. Cloudflare took the model offline on September 8, deployed a fix, and restored service the next
  day, confirming no other models were impacted. The issue stemmed from a misconfiguration in the open-source
  inference engine SGLang and a bug in handling over-length requests, which caused stale cache data from previous
  requests to be included in responses. Cloudflare increased the KV cache pool size to accommodate the full
  context window and patched the engine to safely reject invalid requests before processing. These fixes were
  coordinated with SGLang maintainers and validated against reproduction tests to prevent recurrence.
feed_title: Cloudflare fixes cross-request KV cache data leak in GLM-5.3 Workers AI model affecting 155 responses
  with long prompts [ * ] [ ◼ ]
feed_published_at: '2026-10-26T22:41:48Z'
feed_id: sty_ea402a9c7effffb3
rating: Important
technical_rating: Important
---

A successful response can still contain the wrong customer’s data.

In its [October 26 disclosure](https://blog.cloudflare.com/kv-cache-exposure-remediation/), Cloudflare describes a tenant-isolation failure in its GLM-5.3 Workers AI deployment. The company says 155 responses were affected between August 27 and September 9, all involving prompts longer than 681,280 tokens. It reports no evidence of deliberate exploitation and says no other Workers AI model was affected. This is a newly published account of an incident repaired in September.

The failure crossed a handoff between two sets of machines. One processes the prompt and builds a key-value cache, the model’s working record of that context. Another uses that cache to generate the answer. Cloudflare configured a 1,048,576-token context window, but the first set’s cache pool held only 681,280 tokens. Its long-context checks had accepted successful status codes without checking output coherence.

The [SGLang maintainers’ coordinated account](https://www.lmsys.org/blog/2026-10-26-cf-security) explains the second failure. A request marked for rejection could continue into the handoff. The answering machine could then read cache pages that the new request had never populated. A capacity problem became a data-boundary problem because rejection did not stop the work.

Cloudflare says it increased the pool and patched the rejection path before restoring the model on September 9. The maintainers also describe related fixes for cache pages reused while earlier transfers remain in flight. Their report distinguishes the incident’s admission failure from those broader lifetime problems.

For an operator, the useful test is concrete. Send distinct synthetic markers through separate test accounts, including requests near capacity limits, interrupted transfers and rejected work. Check that errors terminate cleanly and that markers never appear in the other account’s output. These are proposed verification steps, not tests performed by this publication.

Keep the deployment topology and engine version beside the result. A single-machine test cannot establish the behavior of a service that splits prompt processing from answer generation. The boundary must hold when a request fails, because that is when the next customer can inherit its unfinished state.
