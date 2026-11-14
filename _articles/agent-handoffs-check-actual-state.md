---
title: A clean AI handoff can hide unfinished work
summary: Experiments found that a success message made agents less likely to finish a simulated task when
  the underlying database write had not happened.
section: Enterprise Ops
reader_job: What should a receiving agent verify before trusting a predecessor’s report that a change is
  complete?
topics:
- agents
- evaluation
- governance
takeaways:
- On AppWorld, a success receipt helped when the database change existed and hurt when it was absent.
- The researchers tested specific edits and saved states. They did not evaluate a production handoff system.
leader_action: Require handoff records to distinguish attempted actions from effects confirmed in the target
  system.
individual_action: Check the current record before marking a handed-off operation complete or attempting
  it again.
evidence_type: preprint
rank: 4
sources:
- url: https://arxiv.org/abs/2611.14654
  title: Cleaning an Agent’s History Hurts When the World Still Holds the Error
  publisher: arXiv / Egor Pakhomov et al.
  published_at: '2026-11-13T01:00:00Z'
  kind: preprint
- url: https://arxiv.org/html/2611.14654v1
  title: Cleaning an Agent’s History Hurts When the World Still Holds the Error (full text, v1)
  publisher: arXiv / Egor Pakhomov et al.
  published_at: '2026-11-13T01:00:00Z'
  kind: preprint
eligibility:
  url: https://arxiv.org/abs/2611.14654
  published_at: '2026-11-13T01:00:00Z'
  precision: second
  verification: visible
  evidence: arXiv's Friday, November 13 New submissions list contains arXiv:2611.14654 v1. The official
    schedule places that batch at 8 p.m. Eastern on Thursday (November 13 at 01:00 UTC); November 11 was
    an arXiv holiday. The submission history records an earlier deposit at 2026-11-10T19:06:36Z, not first
    public availability. The publisher's batch time, not the discovery feed's 05:00 UTC, establishes eligibility.
  discovered_url: https://arxiv.org/abs/2611.14654
  verified_at: '2026-11-14T13:11:11.430390Z'
  listing_url: https://arxiv.org/list/cs.AI/new?show=2000&skip=0
  schedule_url: https://info.arxiv.org/help/availability.html#announcement-schedule
  submitted_at: '2026-11-10T19:06:36Z'
article_id: art_c44ac57feedcf64a
edition_date: '2026-11-14'
published_at: '2026-11-14T13:14:15.200836Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://arxiv.org/abs/2611.14654
feed_name: TedTschopp News Graph - Top Stories
feed_summary: A study investigates how modifying the recorded history of mistakes made by tool-using language-model
  agents affects their task success when the actual environment still holds those errors. The research shows
  that simply correcting the history without updating the world state can worsen outcomes, as demonstrated
  by experiments where truthful notes improved recovery but presenting completed actions without corresponding
  world changes decreased performance. The experiments involved freezing an agent mid-task and altering
  either its history or the world state, revealing that the effectiveness of history edits depends on their
  consistency with the real-world state. For example, reporting success for an action that failed in the
  world lowered task success, while accurate reporting aligned with the world improved it. These findings
  highlight the importance of synchronizing history corrections with the actual state to avoid degrading
  agent performance.
feed_title: Researchers find that editing an AI agent's error history can reduce performance if the real-world
  state still contains those errors [ ~ ] [ ◻ ]
feed_published_at: '2026-11-14T05:00:00Z'
feed_id: sty_d69cecc04f6a89a8
rating: Optional
technical_rating: Informational
---
Suppose an agent hands you a note saying a new account record was saved. You have two things you can check: what the note says and whether the record exists. An agent taking over the work faces that same choice.

[Researchers at Salesforce AI Research](https://arxiv.org/abs/2611.14654) paused agent runs and let a receiving model continue from a saved point. In one AppWorld experiment, they independently changed two things: whether a database operation’s receipt reported success and whether the database contained its effect. When the effect was absent, a success receipt lowered completion of the whole task from about 45% to 28%, pooled across two receiving models. When the effect was present, the success receipt helped: completion rose from about 38% to 49%. [AppWorld experiment](https://arxiv.org/html/2611.14654v1)

A separate test kept the environment fixed and changed how the history described a wrong value. A note acknowledging the error and supplying the right value improved recovery over a neutral note. Rewriting the history as if the action had already succeeded performed worse than leaving it alone. These were controlled edits on two benchmarks. The authors didn’t test a complete handoff or history summarization policy in production.

What should a handoff call done? Give the next worker separate entries for what was tried and what the system confirmed. Leave an unresolved status visible when there’s no independent confirmation. After a database write, read the target record before continuing or retrying. The answer belongs in the handoff, where the next worker can find it.
