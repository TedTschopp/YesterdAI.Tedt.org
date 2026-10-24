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
reading_minutes: 4
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
  caption: A conceptual illustration of the mechanism discussed in this analysis.
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
---

A reference that opens successfully creates a strong impression of grounded work. It establishes that a resource exists. Whether the resource supports the sentence beside it is another question.

A [preprint on biomedical claim-verification agents](https://arxiv.org/abs/2610.29812v1) studies that distinction using a controlled task and PubMed retrieval. The authors report that closed-book models often supplied identifiers for real papers while those papers rarely supported the claims being checked. Their experiments also separate retrieval limitations from the performance possible when relevant abstracts are supplied. The study is narrow and some comparisons are not statistically resolved at its sample size.

The operating lesson applies to evidence workflows more broadly: citation checks should examine the connection between the claim, the retrieved passage, and the conclusion drawn from it.

## Define what the reference must establish

Before scoring a response, identify the claims that require support and the kind of evidence appropriate to each. A source can establish that a company made an announcement without independently validating the announcement’s performance claim. A policy document can describe a rule without proving that it applied to a particular historical case.

Those distinctions should be part of the evaluation rubric. Ask whether the cited material is relevant, whether it supports the strength of the statement, and whether important conditions or limitations survived the summary. A working URL is a useful preliminary check, but it cannot answer those questions.

Keep the unit of review small enough to inspect. A response containing many references can make it difficult to tell which one is supposed to support which statement. Connecting specific claims to specific passages gives a human reviewer a more manageable task.

## Separate search from interpretation

A retrieval failure and an interpretation failure need different remedies. If the relevant evidence never reaches the model, revising the answer prompt may have limited value. If the evidence is present but the conclusion misstates it, expanding the search may add noise without addressing the error.

Use a controlled evaluation that can distinguish the two. Compare ordinary retrieval with a condition where reviewed relevant material is supplied. Inspect the returned passages, not just the query or the final answer. This makes it possible to locate a bottleneck before choosing a new model or indexing strategy.

The paper’s controlled design is useful precisely because it exposes that separation. Its numerical results should remain attached to its task, tools, and sample. An enterprise needs a corresponding evaluation on the documents and decisions its own application handles.

## Preserve scope and version

Source relevance includes time and context. An accurate citation to the wrong version of a procedure can still mislead a user making a current decision. Retain the document identifier, version or retrieval date where available, and the passage used to support the claim.

When the underlying material changes, define whether the answer should refer to the current rule or reconstruct the rule applicable at an earlier date. Those are different requests. An assistant should not quietly switch between them because a search result happens to favor the newest document.

This is particularly important for a retrospective analysis. The preparation date of an answer does not establish when the evidence became available. The evaluation should make later information visible instead of allowing it to improve an earlier decision invisibly.

## Make insufficient evidence an acceptable result

Some questions will remain unresolved by the retrieved material. The application should have a supported way to say so, ask for clarification, or send the question to an accountable reviewer. A requirement to provide a definite answer to every input can encourage a polished conclusion from inadequate evidence.

Measure that behavior alongside answer accuracy. A system that properly identifies an unsupported claim is doing useful work, provided the user understands what remains unknown and how to proceed. The review should distinguish that result from a retrieval error presented as a confident answer.

Do not assume that adding more references solves the problem. Additional sources can improve coverage, but only if their relationship to the claim is examined. A longer bibliography can otherwise give the same weak inference a more impressive appearance.

Add a control case containing a genuine source that discusses the topic but does not establish the particular claim. This tests whether the review can distinguish relevance from support. A source can pass a link check and still require the answer to be narrowed or withdrawn.

## Audit a small set of real answers

Choose a sample of consequential answers from an existing retrieval application. For each supported statement, ask a reviewer to open the source, locate the evidence, and judge whether the wording preserves its scope. Record link validity, relevance, and support as separate findings.

Use the disagreements to improve the retrieval and response process, then retain the cases for future evaluations. This is a practical quality check for evidence handling, not a medical recommendation or a universal finding about scientific assistants. The dependable habit is simple: follow the link far enough to establish what it actually proves.
