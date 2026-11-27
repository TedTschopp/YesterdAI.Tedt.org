---
title: A skill-loading gate can score its own good luck
summary: A SkillsBench reanalysis finds apparent skill-loading gains even after labels are shuffled. Its
  retrospective held-out checks show why a few runs cannot settle a removal decision.
section: Enterprise Ops
topics:
- agents
- evaluation
reader_job: What evidence should support retiring an agent skill or choosing when to load it?
takeaways:
- Reusing a noisy no-skill score to choose and grade a loading decision can create apparent gains.
- The studied gates showed no statistically significant improvement in retrospective held-out checks;
  this does not rule out effective gates.
leader_action: Require evaluation work separate from the runs used to choose a skill-loading policy.
individual_action: Retain loaded instructions and repeated trial outcomes, and score each removal rule
  on work withheld from that decision.
rank: 2
article_id: art_f5160be78c9a6a70
story_key: https://arxiv.org/abs/2611.33943
edition_date: '2026-11-27'
published_at: '2026-11-27T13:12:07.383856Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: preprint
sources:
- url: https://arxiv.org/abs/2611.33943
  title: What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of
    SkillsBench
  publisher: arXiv
  published_at: '2026-11-26T01:00:00Z'
  submitted_at: '2026-11-25T08:02:04Z'
  kind: preprint
- url: https://arxiv.org/html/2611.33943v1
  title: What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of
    SkillsBench — full paper, version 1
  publisher: arXiv
  published_at: '2026-11-26T01:00:00Z'
  kind: preprint
eligibility:
  url: https://arxiv.org/abs/2611.33943
  published_at: '2026-11-26T01:00:00Z'
  submitted_at: '2026-11-25T08:02:04Z'
  precision: second
  verification: visible
  timestamp_url: https://arxiv.org/list/cs.AI/pastweek?show=2000
  evidence: The Thu, 26 Nov 2026 (showing 248 of 248 entries ) primary cs.AI listing includes 2611.33943
    as entry 32, with no cross-list or replacement marker. The official availability schedule at https://info.arxiv.org/help/availability.html
    establishes Wednesday 20:00 America/New_York announcement, equivalent to 2026-11-26T01:00:00Z. This
    is the inclusive start of this edition’s window. The Thursday Thanksgiving holiday does not move the
    preceding Wednesday announcement. Earlier deposit and later feed timestamps are recorded separately
    and are not used as publication evidence.
  verified_at: '2026-11-27T13:12:07.383856Z'
  event: public_announcement
feed_name: TedTschopp News Graph - Top Stories
feed_id: sty_9cb551a56123c891
feed_title: Source-code audit and reanalysis of SkillsBench finds average skill lift of 18.7 percentage
  points with no statistically significant task-level reductions [ ~ ] [ ◻ ]
feed_summary: Researchers conducted a source-code-level audit and noise-aware reanalysis of SkillsBench,
  a benchmark measuring agent skill improvements, analyzing 7,554 public trials across 1,421 configuration-task
  pairs. They identified grader dependence issues, placeholder skill directories, and additional built-in
  skills affecting results, with an overall average skill lift of 18.7 percentage points but no statistically
  significant reductions in task performance after correcting for multiple tests. The audit revealed that
  observed negative differences in some tasks were likely due to run-sampling noise, as most cells lacked
  sufficient runs to detect decreases reliably. A gating strategy based on skill-free scores showed apparent
  improvements in logs but did not yield statistically significant gains on held-out data. The researchers
  have published their audit ledger and analysis scripts for transparency and further study.
feed_published_at: '2026-11-27T05:00:00Z'
feed_snapshot: docs/runs/2026-11-27-feed-snapshot.json
rating: Optional
technical_rating: Informational
---

A skill-loading rule can appear effective because it remembers which test runs got lucky. A [new SkillsBench reanalysis](https://arxiv.org/abs/2611.33943) examines that trap before using a few disappointing scores to retire an agent skill.

Haozhe Zhang and Zhen Long analyzed 7,554 public trials, forming 1,421 paired comparisons of a model-and-harness configuration on a task. Each side had at most three runs. After pooling results and correcting for multiple testing, no task showed a statistically significant reduction from skills. That does not establish that every skill is harmless. Sparse trials make harm difficult to detect.

The researchers also tested gates that choose whether to load skills from the recorded results. In ordinary log replay, several gates gained roughly two to three percentage points over always loading. But shuffling the skill and no-skill labels, removing any real skill effect, still produced apparent gains.

Why? The same noisy no-skill score helped choose the action and supplied its evaluation score. A lucky run could therefore become both the reason to skip a skill and the evidence that skipping worked. The [retrospective checks](https://arxiv.org/html/2611.33943v1) withheld trial pairs from each decision. None of the gates then showed a statistically significant improvement.

The frozen exports differ from the benchmark’s final sample. Policy settings had also been chosen during earlier exploration of the data, so the held-out reanalysis is a robustness check, rather than a prospective trial on untouched work.

For a skill library, retain the actual loaded instructions and repeated outcomes beside each proposed removal. Choose the rule using one set of runs, then score its decisions on additional work withheld from that choice. Keep all variants of a task together when testing transfer to new tasks.

A failed run deserves investigation. Removing a skill needs evidence that the next attempt will improve, especially when the apparent improvement comes from reusing yesterday’s score.
