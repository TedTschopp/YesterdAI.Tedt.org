---
article_id: art_55c3c0be518a12ff
story_key: https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions
title: Retrieved pages need an evidence boundary
summary: Redact’s WhatsApp investigation shows why a retrieved page can contain instructions as well as information.
  An enterprise assistant needs a clear rule for which material may influence its behavior.
section: Security
edition_date: '2026-10-20'
published_at: '2026-10-24T22:21:03.133926Z'
retrospective: true
rank: 1
reading_minutes: 4
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
  caption: A conceptual illustration of the mechanism discussed in this analysis.
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
---

A page that an assistant retrieves is not necessarily written only to inform it. The page may also contain language designed to influence what the assistant says or does. A trusted brand on the page does not resolve that distinction.

[Redact’s investigation of WhatsApp help pages](https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions) reports hidden instructions in material delivered to AI readers. Its dated update records WhatsApp’s explanation that notes intended for its support chatbot had appeared because of a bug and had been removed. The dispute concerns the origin and purpose of those notes; the operational issue is broader. Retrieval can bring another party’s behavioral directions into an assistant’s context alongside ordinary reference material.

Our analysis is that enterprise retrieval needs an explicit evidence boundary. Information from a source can help answer a question without gaining authority to redefine the task.

## Review the input the assistant receives

A screenshot is not a complete record of a retrieval operation. A tool might extract hidden text, metadata, accessibility content, surrounding navigation, or fragments from several pages. The important input for an evaluation is the exact representation returned to the model.

Choose a representative support or policy task and preserve that representation. Compare it with the user-visible page, then identify which differences are expected and which could affect the answer. This is a concrete test of the retrieval pipeline, rather than an assumption that the model saw what a human reviewer saw.

The inspection should include provenance. The assistant needs to retain enough information to connect a passage with its source and retrieval time. If a response mixes text from several locations into an unlabeled block, it becomes harder to determine where an instruction entered and harder to correct an inaccurate answer afterward.

## Authority is a separate property

An organization may authorize a support assistant to apply an internal policy. That does not mean every external page describing the subject can add new restrictions to the assistant’s behavior. The relevant question is who is allowed to issue the instruction, not whether the wording sounds professional or helpful.

Represent that distinction in the system design. Task instructions, user requests, approved organizational rules, and retrieved material should have clear roles. A retrieved page should be treated as evidence about its subject. Requests embedded in it to suppress sources, change reporting, or take unrelated actions need to remain source content rather than operating instructions.

The model’s response is only one place to enforce the distinction. Tool access and application logic should also reflect the actual authorization. An assistant that reads a page should not thereby acquire permission to send a message, change an account, or withhold an independently required escalation route.

## Evaluate changes in the answer

A useful test compares the same user question against a clean source and a deliberately altered version. Keep the factual material the same while introducing text that attempts to change the assistant’s behavior. Then measure what changes: source selection, omitted information, escalation, and proposed actions.

Do not score only whether the final sentence sounds plausible. A response can be fluent and factually unobjectionable in what it includes while selectively leaving out something the user needs. Review omissions as well as false statements, and preserve the trace needed to distinguish a retrieval failure from an instruction-following failure.

These are suggested evaluation methods, not a claim that this particular investigation proves a universal failure rate. The reported case establishes a reason to test the boundary in the actual application. Different tools, extraction methods, model instructions, and permissions may produce different outcomes.

## Make correction practical

When an input is found to contain inappropriate directions, a team should be able to identify affected source versions and rerun representative cases. That requires a record of what was retrieved and which version of the assistant used it. Without those records, changing the prompt may improve the next answer while leaving the earlier impact unknown.

Keep the human review focused on the decision the assistant is supporting. For a customer-support application, that means the answer, the evidence provided, and the available escalation path. For an operational agent, it also means the actions attempted and the authority under which they were attempted.

Keep an approved reference answer for the test, including what the assistant must disclose and when it should ask the user for direction. Have a reviewer assess the clean and altered cases without being told which is which. This makes selective omission easier to notice and gives the team a repeatable example to retain after a fix. The exercise should remain isolated from real customer accounts and actual outbound actions.

The immediate step is to inspect a real retrieved payload and test one conflicting instruction. A source can be valuable, current, and authoritative about its own product while still lacking authority over your assistant. Building that distinction into the workflow is more dependable than asking the model to infer it afresh on every page.
