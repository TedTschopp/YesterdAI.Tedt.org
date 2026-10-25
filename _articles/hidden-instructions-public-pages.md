---
article_id: art_55c3c0be518a12ff
story_key: https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions
title: Retrieved Pages Need an Evidence Boundary
summary: Redact’s WhatsApp investigation shows why a retrieved page can contain instructions as well as information.
  An enterprise assistant needs a clear rule for which material may influence its behavior.
section: Security
edition_date: '2026-10-20'
published_at: '2026-10-24T22:21:03.133926Z'
retrospective: true
rank: 1
reading_minutes: 3
eligibility:
  url: https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions
  published_at: '2026-10-19T16:00:00Z'
  precision: second
  verification: jsonld
  evidence: Publisher JSON-LD and article:published_time=2026-10-19T16:00:00+00:00; dated substantive response update
  discovered_url: https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions
sources:
- url: https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions
  title: WhatsApp help pages contained hidden AI instructions
  publisher: redact.dev
  published_at: '2026-10-19T16:00:00Z'
  date_precision: second
hero:
  path: /assets/images/hidden-instructions-public-pages.webp
  prompt: Create a wide landscape editorial hero for Yesterday in AI, approximately 1.91:1. Strictly flat two-dimensional
    Swiss editorial graphic, warm ivory (#F8F6F0) background, deep slate (#101820) geometry and a single restrained
    burnt-orange (#BF4714) signal. Precise hairlines, elegant asymmetric composition, generous negative space, clean
    vector-like edges delivered as a raster. No text, letters, numbers, logos, gradients, shadows, photographic
    objects, people, robots, watermarks, grain, or decorative texture. All essential forms well inside the frame.
    An open stack of thin rectangular document sheets sits on the left. A very fine orange path hidden between the
    sheets bypasses a small slate reading aperture in the center and bends the direction of a neat outgoing slate
    arrow on the right. Clearly show the difference between visible document content and a concealed instruction
    changing an assistant's route. Flat geometric visual metaphor for a web page attempting to influence an AI reader.
  generated_at: '2026-10-24T22:00:38.298Z'
  tool: image_gen
  width: 1536
  height: 804
  alt: An orange path hidden among document sheets bypasses a reading gate and redirects the outgoing answer.
  caption: The concealed orange path redirects the answer, illustrating how retrieved material can cross from evidence
    into instructions.
leader_action: Require assistants to distinguish retrieved evidence from instructions authorized by your organization
  and the user.
individual_action: Check what the retrieval tool actually returns, including text that a normal browser view does
  not show.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: WhatsApp's help pages contained hidden instructions for AI chatbots that prevented them from recommending
  data protection authorities or citing privacy laws if users mentioned legal action or lawyers. These instructions
  contradicted WhatsApp's publicly stated privacy policy in Europe, which affirms users' rights to complain to regulators
  under GDPR. The hidden notes also advised the AI not to suggest manual account deletion or alternative phone numbers
  if users lost access to their phone number, directing them instead to wait for automatic deletion after extended
  inactivity.
feed_title: WhatsApp's hidden AI instructions told chatbots not to recommend data protection regulators or cite
  privacy laws when users mentioned lawyers [ * ] [ ◼ ]
rating: Important
writing_style: ted-writing-style
writing_style_version: 1.0.0
format: analysis
takeaways:
- Redact reported hidden directions in WhatsApp help material; its update records WhatsApp’s explanation that chatbot
  notes appeared through a bug and were removed.
- Compare clean and altered retrieval payloads, checking omissions and attempted actions as well as the final answer.
topics:
- security
- agents
- evaluation
evidence_type: reporting
reader_job: Keep retrieved information from acquiring authority over an assistant’s task.
modified_at: '2026-10-25T05:04:24Z'
legacy_anchors:
- review-the-input-the-assistant-receives
- authority-is-a-separate-property
- evaluate-changes-in-the-answer
- make-correction-practical
- actions-heading
editorial_contract: 2
---
A reference book can explain a product. A work order tells you what you have been authorized to do. When an assistant retrieves a page, those two kinds of text can arrive in the same payload.

[Redact’s investigation of WhatsApp help pages](https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions) reports hidden instructions in material delivered to AI readers. Its dated update records WhatsApp’s explanation that notes intended for its support chatbot had appeared because of a bug and had been removed. The dispute concerns the origin and purpose of those notes; the operational issue is broader. Retrieval can bring another party’s behavioral directions into an assistant’s context alongside ordinary reference material.

The distinction matters even when the page is useful and current. Its publisher can be authoritative about the product without acquiring authority over the user's task. The reported dispute does not need to be resolved into a universal claim about malicious intent before an enterprise can test that boundary.

## Review the Input the Assistant Receives

Preserve the exact representation returned by a retrieval tool. A screenshot alone may leave out hidden text, metadata, accessibility content, navigation, or fragments the extractor adds from other locations.

Compare that payload with the visible page. Identify expected differences and passages that could redirect an answer. Keep each passage connected to its source and retrieval time; an unlabeled mixture makes an investigation start with the avoidable problem of finding where the instruction entered.

The relevant question is what the model actually received. A person reviewing the browser may have read a materially different representation.

## Authority Is a Separate Property

Keep approved organizational rules, the user's request, and retrieved reference material in their respective roles. A product page can supply evidence about how the product works. Its request to suppress another source, withhold an escalation path, or take an unrelated action remains content to assess.

Enforce the same distinction in tool access. Reading a page should not grant permission to send a message or change an account. A model instruction is one part of the application; the tool and its authorization checks are another.

This case establishes a reason to inspect that design. Different extraction methods, model instructions, tools, and permissions can produce different results. The investigation does not supply a universal failure rate for retrieval applications.

## Evaluate Changes in the Answer

Create an isolated comparison using the same factual material and user question. One source is clean; the other adds text attempting to direct the assistant's behavior.

Measure source selection, omitted information, escalation, and attempted actions. A plausible final sentence can hide selective omission. Keep the trace needed to distinguish a failed retrieval from an inappropriate instruction being followed.

Define the expected answer and required disclosures before the test. Where practical, have a reviewer compare the results without knowing which source variant produced each one. That helps expose an answer which remains fluent while dropping something the user needs.

## Make Correction Practical
{: #for-practitioners }

Retain the source version, returned payload, assistant configuration, and representative answer. If a later correction changes how the assistant handles the material, those records let the team identify affected work and replay the case.

Keep the exercise away from real customer accounts and actual outbound actions. For a support assistant, inspect the answer, its evidence, and the available escalation route. For an operational agent, also inspect what it attempted to execute and which authority permitted it.

A prompt change can improve the next answer. The people responsible for previous answers need enough of the retrieval record to discover what those answers were based on.

Start with one real payload and one conflicting instruction in an isolated test. Keep the useful facts available and follow what happens to the attempted redirection. The result should explain where the reference book informed the work and where the application preserved the work order.