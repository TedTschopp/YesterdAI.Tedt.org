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
reading_minutes: 2
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
  caption: The preserved orange tile represents evidence that a context window could otherwise discard before the
    agent finishes its task.
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
writing_style_version: 1.0.0
format: brief
takeaways:
- A missing observation may be recoverable from a source, or permanently lost after a context change.
- Test whether a later action still has its supporting evidence after ordinary summarization.
topics:
- agents
- evaluation
evidence_type: preprint
reader_job: Decide which task evidence must survive a context boundary.
modified_at: '2026-10-25T03:42:17.530845Z'
legacy_anchors:
- inventory-the-state-a-task-depends-on
- test-the-moment-information-is-compressed
- preserve-the-record-at-the-appropriate-level
- evaluate-the-system-you-will-operate
- actions-heading
editorial_contract: 2
---
Pass a task to a colleague and you decide what belongs in the handoff. An agent's surrounding software makes the same choice when it summarizes a conversation. The useful question is which evidence the next decision will need after the original observation is gone.

A [preprint on agent harnesses and state](https://arxiv.org/abs/2610.26632v1) distinguishes cases where a missing fact can be looked up again from cases where it cannot. Its experiments show substantial differences under those conditions and examine how summaries and replay affect a small set of benchmark runs. The authors explicitly limit parts of their analysis to narrow configurations and counted runs. The findings support a design question, not a universal ranking of harnesses.

## Preserve the record at the appropriate level

A versioned manual can be retrieved again. A user's conditional approval or the state observed before a change may be harder to reconstruct. Give those facts different treatment. Retain what was observed, where it came from, and the conditions under which it justified an action.

An approval is a useful example. Keeping the word *approved* while dropping the permitted recipient, resource, or condition changes its meaning. A polished summary can therefore preserve the conversation's tone while losing the authority the application actually needs.

Re-observation also has a version problem. Fetching today's value does not necessarily recover the value that justified yesterday's decision.

## Test the moment information is compressed
{: #for-practitioners }

Choose one task with a fact that will become unavailable. Preserve the fact, apply the normal summarization or truncation, then continue without access to the original observation. Inspect the retained record and the next action together.

Compare the same model under the old and proposed preservation policies. Count recovery calls and unresolved decisions alongside completion. A correct answer alone may reflect a guess or an incidental clue.

Keep the model and harness configuration attached to the result. This small test can identify where a handoff loses evidence; it cannot rank every context-management system. The next component needs enough of the work order to make its own decision for a defensible reason.