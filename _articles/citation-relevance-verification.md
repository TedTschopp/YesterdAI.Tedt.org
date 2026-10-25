---
article_id: art_1353be402f8662ba
story_key: https://arxiv.org/abs/2610.29812
title: A real citation can still support the wrong claim
summary: A biomedical claim-verification study finds that valid publication identifiers can hide irrelevant evidence.
  Enterprise retrieval systems should test the relationship between a claim and its source, beyond link existence.
section: Security
edition_date: '2026-10-22'
published_at: '2026-10-24T22:46:52.117360Z'
retrospective: true
rank: 4
reading_minutes: 2
eligibility:
  url: https://arxiv.org/abs/2610.29812v1
  published_at: '2026-10-21T14:35:56Z'
  precision: second
  verification: publisher_api
  evidence: arXiv API published=2026-10-21T14:35:56Z
  discovered_url: https://arxiv.org/abs/2610.29812
sources:
- url: https://arxiv.org/abs/2610.29812v1
  title: Real PMIDs, Wrong Papers — harness design for biomedical claim-verification agents
  publisher: arxiv.org
  published_at: '2026-10-21T14:35:56Z'
  date_precision: second
hero:
  path: /assets/images/citation-relevance-verification.webp
  prompt: Create a wide landscape editorial hero for Yesterday in AI, approximately 1.91:1. Strictly flat two-dimensional
    Swiss editorial graphic, warm ivory (#F8F6F0) background, deep slate (#101820) geometry and a single restrained
    burnt-orange (#BF4714) signal. Precise hairlines, elegant asymmetric composition, generous negative space, clean
    vector-like edges delivered as a raster. No text, letters, numbers, logos, gradients, shadows, photographic
    objects, people, robots, watermarks, grain, or decorative texture. All essential forms well inside the frame.
    Three open slate document rectangles each contain a distinctive small geometric evidence shape. A thin slate
    reference line connects a claim tile to a document with a mismatched shape, while an orange correction line
    connects it to the matching shape in another document. Minimal graphic showing that a valid reference link is
    different from relevant supporting evidence.
  generated_at: '2026-10-24T22:30:24.847Z'
  tool: image_gen
  width: 1536
  height: 804
  alt: A valid document marker connects to the wrong evidence tile, while an orange link identifies the claim’s
    actual source relationship.
  caption: The mismatched document link shows why a real citation still needs to be checked against the claim it
    is meant to support.
leader_action: Require evidence of claim-to-source relevance in retrieval evaluations, alongside checks that citations
  resolve.
individual_action: Open the cited material and verify the specific claim and context before treating the link as
  support.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'arXiv:2610.29812v1 Announce Type: cross Abstract: Literature-searching language agents are becoming
  a standard component of scientific assistants for the life sciences, yet there is little controlled evidence on
  which parts of their harness matter. We run a controlled ablation on biomedical claim verification (SciFact) with
  the live PubMed API as the only tool. Holding the backbone and output format fixed, we compare four harnesses:
  closed-book answering, single-shot retrieval using the claim as the query, a ReAct-style agent that writes its
  own PubMed queries, and an oracle given the gold abstracts, each with two efficient frontier backbones. Naive
  single-shot retrieval finds the gold paper for only 6% of claims and turns overconfident errors into abstentions
  without improving accuracy. Letting the model formulate its own queries triples gold recall and yields the best
  verdicts (62% accuracy vs. 49-59% for the other realistic harnesses), although these differences are not significant
  at our sample size and agents use fewer than half of their search budget. With gold abstracts, the same models
  reach 79-86% accuracy, a significant 17-24 point gap showing that retrieval, not reasoning, is the main bottleneck.
  Finally, a citation audit shows that closed-book models cite PubMed IDs that almost always exist (327/335) but
  are almost never relevant: a cross-family LLM judge rates only 3 of 327 existing citations as relevant to the
  claim, versus 67% for citations produced by the search agent. Existence checks are therefore insufficient safeguards
  for scientific agents. We release code, prompts, and all cached tool calls at https://github.com/saqlain2204/real-pmids-wrong-papers.'
feed_title: 'Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification Agents [ ~ ] [ ◼ ]'
rating: Optional
writing_style: ted-writing-style
writing_style_version: 1.0.0
format: brief
takeaways:
- A valid publication identifier can point to a real paper that does not support the answer’s claim.
- Check link validity, relevance, and claim support separately; distinguish retrieval failures from interpretation
  failures.
topics:
- evaluation
- security
evidence_type: preprint
reader_job: Verify the relationship between a specific answer and the evidence cited for it.
modified_at: '2026-10-25T03:42:17.530845Z'
legacy_anchors:
- define-what-the-reference-must-establish
- separate-search-from-interpretation
- preserve-scope-and-version
- make-insufficient-evidence-an-acceptable-result
- audit-a-small-set-of-real-answers
- actions-heading
editorial_contract: 2
---
Open the reference beside a confident sentence. The link may work and the paper may be real. Where is the passage that supports this particular claim?

A [preprint on biomedical claim-verification agents](https://arxiv.org/abs/2610.29812v1) studies that distinction using a controlled task and PubMed retrieval. The authors report that closed-book models often supplied identifiers for real papers while those papers rarely supported the claims being checked. Their experiments also separate retrieval limitations from the performance possible when relevant abstracts are supplied. The study is narrow and some comparisons are not statistically resolved at its sample size.

## Define what the reference must establish

A company announcement can establish that a claim was made without independently validating its benchmark. A real paper can discuss the topic while failing to support the conclusion attributed to it.

Keep the unit of review small: a claim, its cited passage, and the strength of the conclusion. Record link validity, relevance, and support separately. A longer bibliography does not repair a missing connection.

Version matters as well. The current procedure may answer today's question while being unsuitable for a question about an earlier decision. Retain the document version or retrieval date and the passage actually used.

## Separate search from interpretation
{: #for-practitioners }

Compare ordinary retrieval with a controlled condition that supplies reviewed relevant material. Inspect what reaches the model. Missing evidence and a misread passage need different remedies.

Include a genuine, on-topic source that does not establish the particular claim. That control tests whether the system confuses relevance with support. Give an unresolved claim a legitimate outcome: insufficient evidence, clarification, or an accountable review.

Keep the study's results attached to its task, tools, and sample. Some comparisons were not statistically resolved; an enterprise needs evidence from its own documents before treating the findings as a local performance estimate.

This is an evidence-handling quality check, not a medical recommendation or a universal result about scientific assistants. The useful next step is to open a few consequential answers and locate the evidence each sentence is asking its reference to carry.