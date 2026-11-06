---
title: Gemini Omni 1.2 Flash expands clips and lowers generation prices
summary: Google announces 15-second video and conversational editing in Gemini Omni 1.2 Flash, with a
  lower listed rate and remaining motion limitations.
section: Vendors
reader_job: What changes in the cost and review process for producing short videos with Gemini Omni 1.2
  Flash?
topics:
- infrastructure
- economics-adoption
- evaluation
takeaways:
- Google announces clips up to 15 seconds, multi-turn editing and a listed 720p generation rate of $0.07
  per second.
- Reference consistency remains a vendor claim; compare the full cost of obtaining an approved clip, including
  retries and review.
leader_action: Budget a pilot around approved clips and review effort, using representative product references
  and acceptance criteria.
individual_action: Check reference details and motion after each conversational edit, and record retries
  before comparing production costs.
evidence_type: vendor
rank: 3
sources:
- url: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/
  title: 'Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips'
  publisher: Google
  published_at: '2026-11-05T17:00:00Z'
  kind: vendor
eligibility:
  url: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/
  published_at: '2026-11-05T17:00:00Z'
  precision: second
  verification: jsonld
  evidence: Original NewsArticle JSON-LD datePublished is 2026-11-05T17:00:00+00:00, corroborated by meta
    name=published_time. dateModified is 2026-11-05T17:03:44.791497+00:00; eligibility uses original publication.
    Complete original body and visible Nov 05, 2026 date read.
  discovered_url: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/
  verified_at: '2026-11-06T13:11:26.986982Z'
article_id: art_485654c1f98a7cdc
edition_date: '2026-11-06'
published_at: '2026-11-06T13:11:26.986982Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash
feed_name: Ted Tschopp's AI News
feed_summary: 'Estimated GAI-style rating: Important. Rationale (estimate): Estimated from similar historically
  rated GAI selections. Selected in GAI Insights'' briefing dated 2026-11-06. Briefing source: https://gaiinsights.com/articles.'
feed_title: 'Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips [ * ] (Estimated)'
feed_published_at: '2026-11-06T00:00:00+00:00'
feed_id: d7977b13e92f9e9aa07a08b19302f25c
rating: Important
---
The price of a generated video matters most after someone decides the clip is usable. A cheaper first attempt can still leave a person fixing the product, checking the motion and asking for another version.

Google’s [November 5 Gemini Omni 1.2 Flash announcement](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/) changes several parts of that workflow. The model generates and edits clips up to 15 seconds, compared with 10 seconds for Omni 1.1. Google lists 720p generation at $0.07 per second, a 30% reduction from the earlier version, and says the model is generally available through the Gemini API and Gemini for business.

Conversational editing lets a user request successive changes to a clip. Google also claims stronger adherence to supplied references and better continuity across frames. Those improvements could reduce the number of complete restarts, but the announcement supplies demonstrations rather than an independently measured acceptance rate for enterprise content.

That distinction is useful when planning a trial. Give the model a small set of representative product images and a written acceptance checklist. Inspect whether the product’s shape, visible wording and colors remain correct after each edit. Record how many attempts reach approval and how much review time they require. This tests the part of the promise that affects a production budget.

Google still identifies fast sports action, rapid script changes and complex physics as areas needing improvement. Keep those limits beside the examples when deciding which work to try first.

The immediate opportunity is a more flexible short-video process. Its value depends on whether the person responsible for the final asset can approve it with fewer revisions. Compare that finished result, and the work needed to obtain it, before translating a lower generation rate into promised savings.
