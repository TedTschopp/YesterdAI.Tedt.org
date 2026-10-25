---
article_id: art_b7505ce4183649e7
story_key: https://arxiv.org/abs/2610.26632
title: An agent harness can discard the fact that matters
summary: New research separates the cost of losing context from the cost of losing evidence that cannot be recovered.
  Enterprise agents need a deliberate policy for preserving task state across long runs.
section: Enterprise Ops
edition_date: '2026-10-20'
published_at: '2026-10-24T22:21:03.125486Z'
retrospective: true
rank: 5
reading_minutes: 4
eligibility:
  url: https://arxiv.org/abs/2610.26632v1
  published_at: '2026-10-19T15:59:13Z'
  precision: second
  verification: publisher_api
  evidence: arXiv API published=2026-10-19T15:59:13Z
  discovered_url: https://arxiv.org/abs/2610.26632
sources:
- url: https://arxiv.org/abs/2610.26632v1
  title: When the harness decides success — state that cannot be re-observed
  publisher: arxiv.org
  published_at: '2026-10-19T15:59:13Z'
  date_precision: second
hero:
  path: /assets/images/agent-harness-state.webp
  prompt: Create a wide landscape editorial hero for Yesterday in AI, approximately 1.91:1. Strictly flat two-dimensional
    Swiss editorial graphic, warm ivory (#F8F6F0) background, deep slate (#101820) geometry and a single restrained
    burnt-orange (#BF4714) signal. Precise hairlines, elegant asymmetric composition, generous negative space, clean
    vector-like edges delivered as a raster. No text, letters, numbers, logos, gradients, shadows, photographic
    objects, people, robots, watermarks, grain, or decorative texture. All essential forms well inside the frame.
    A long horizontal row of small slate evidence tiles passes through a narrow open rectangular context window.
    Some gray tiles fade out before the window, while one important orange tile is deliberately carried along a
    thin lower preservation path and rejoins the task after the window. Elegant flat diagram of retaining non-recoverable
    evidence across context compression.
  generated_at: '2026-10-24T22:19:44.248Z'
  tool: image_gen
  width: 1536
  height: 804
  alt: A continuous slate task path crosses a narrowed context window, with one orange evidence tile preserved below
    the narrowing.
  caption: A conceptual illustration of the mechanism discussed in this analysis.
leader_action: Identify which task facts become unavailable later and require the harness to preserve them explicitly.
individual_action: Test a long-running task after context compression, checking whether its essential evidence remains
  recoverable.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'arXiv:2610.26632v1 Announce Type: new Abstract: Agent harnesses decide what a language model sees
  across turns: they drop old turns, summarize them, or replay the model''s own earlier reasoning. We ask when these
  choices change whether an agent succeeds, not only what it costs, and report three findings. First, in a pre-registered
  synthetic probe, truncating the context window costs a low-cost reasoning model nothing in success when a needed
  fact can be looked up again (it looks the fact up instead), but drops its success to chance when the fact cannot
  be re-observed: the two penalties differ by 92.5 percentage points (90% CI [89.5, 95.5]). A pre-registered replication
  on one model from a second provider showed the same contrast. Once the fact was lost, that model chose no answer
  rather than guessing. Second, on ARC-AGI-3, where the benchmark''s Standard harness trails its Provider Adapter
  harness by a wide margin, we decompose that gap one component at a time, for one model on four games. Summarizing
  old turns instead of dropping them, while keeping the Standard harness''s invitation to take notes, recovers 86%
  of a 63-point gap without replaying the model''s reasoning. The same harness without the invitation recovers 43%,
  and adding the provider''s native replay of the model''s reasoning recovers the remaining 57%. These are point
  estimates from one counted run per configuration and game, and the replay share depends on a single run. Third,
  in the benchmark''s published runs and in ours, the Adapter''s advantage in the probability of clearing a level
  it has reached is larger at deep levels than at early ones. This largely restates where runs stopped and does
  not separate a growing advantage from a constant one.'
feed_title: 'When the harness decides success: state that cannot be re-observed [ ~ ] [ ◻ ]'
rating: Optional
writing_style: ted-writing-style
writing_style_version: '1.0.0'
---

Pass a task to a colleague and you have to decide what to put in the handoff. A long-running agent faces a similar problem when its surrounding software keeps some turns, summarizes others, and decides which observations can be retrieved again. The model may still be ready to work. The evidence it needs may already have been left out of the handoff.

A [preprint on agent harnesses and state](https://arxiv.org/abs/2610.26632v1) distinguishes cases where a missing fact can be looked up again from cases where it cannot. Its experiments show substantial differences under those conditions and examine how summaries and replay affect a small set of benchmark runs. The authors explicitly limit parts of their analysis to narrow configurations and counted runs. The findings support a design question, not a universal ranking of harnesses.

Look ahead to the next decision in the work. What information will it require, and which part of that information could be gone by then? Asking that question gives a context-management policy a concrete job: carry the evidence that the next step cannot safely reconstruct for itself.

## Inventory the state a task depends on

Some information is stable and retrievable, such as a versioned reference document. Other information may be temporary: a user’s confirmation, a transient tool response, a decision made during a review, or the state observed before a change. Treating all of it as interchangeable conversation history makes preservation decisions harder to reason about.

Choose a representative task and identify the facts required for its later decisions. Record where each fact comes from, whether it can be obtained again, and whether a later retrieval would return the same version. This gives the harness designer a more useful requirement than a general instruction to keep important context.

Read an approval as carefully as any other task fact. What action did the user approve, within what scope, and under which conditions? Those details belong together in the retained record. A summary that carries the word approved into the next step while dropping its condition hands over a different decision from the one the user actually made.

## Test the moment information is compressed

An evaluation should exercise the points where the harness changes the record. Run the task until it has acquired an essential observation, apply the ordinary truncation or summarization behavior, and then test whether the next decision can still be made from the retained evidence.

Include a case where the lost information cannot be re-observed. A benchmark that lets the agent retrieve every fact again may show the cost of extra calls while missing a more consequential failure. Conversely, a failure caused by unavailable evidence should not automatically be attributed to a weak model.

Inspect the retained state directly. A correct final answer in a small test does not establish that the right evidence survived; the agent may have guessed or used an incidental clue. The review should connect the later action to the preserved observation that justifies it.

## Preserve the record at the appropriate level

Write the handoff around the decisions the application has to make. A case identifier, an accepted constraint, a source version, or an unresolved question may need an explicit place, with a link back to the evidence. A compact record can do useful work here. Judge it by whether the next step can find and use those facts, rather than by how polished its summary sounds.

Do not assume that a more elaborate summary is always better. Additional prose can obscure the distinction between an observed fact, a proposed step, and an action that actually completed. The state representation should make those categories easy for the next component and a human reviewer to distinguish.

Where the system preserves raw traces, decide how an agent should locate and use them. Keeping a record somewhere does not establish that the agent will retrieve the relevant portion at the right time. Evaluate that handoff as part of the workflow rather than counting retained bytes as a success measure.

## Evaluate the system you will operate

Model comparisons should record the harness configuration alongside the model identifier. A change in context management can alter the task that the model effectively receives. If the evaluation changes both at once, an apparent model improvement may be a harness improvement, or the reverse.

Use the same task set to compare the existing policy with a proposed state-preservation change. Measure successful outcomes, recovery calls, unresolved decisions, and the evidence available at completion. Keep narrow or variable results labeled as such rather than promoting a small pilot into a broad capability claim.

Re-observation deserves its own validity check. A record retrieved later may have changed since the original decision, even when the identifier is the same. Preserve a source version or an observation time where that distinction matters, and define when the agent must obtain fresh confirmation. Recovering a current value and recovering the value that justified an earlier action are separate needs. A state policy should specify which one the next step requires.

Choose a fact the agent must carry across a context boundary. Give it a durable place in the record, then test the next step with the original observation unavailable. Can the system still make the decision for the right reason? Keep that case as a check on the handoff. When it fails, you can investigate what was lost and where, with a more useful starting point than saying the model forgot.
