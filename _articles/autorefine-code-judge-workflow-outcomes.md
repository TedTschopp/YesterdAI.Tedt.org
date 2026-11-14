---
title: AutoRefine tests what code judges can learn from merges
summary: Meta researchers improved an AI judge’s agreement with recent merge and abandonment outcomes
  in a small test, while the older judge still did better on earlier work.
section: Enterprise Ops
reader_job: When can merge and abandonment decisions help calibrate an AI code judge, and when do they
  hide important context?
topics:
- evaluation
- agents
takeaways:
- The study uses a second model to set aside training examples when the outcome lacks support in what
  the judge can see.
- On 17 recent held-out changes, chance-adjusted agreement rose from 0.16 to 0.51. On 16 older changes,
  the previous judge did better.
leader_action: Measure both missed useful changes and passed weak changes before making a recalibrated
  judge a release gate.
individual_action: Record why a change was abandoned, and compare that reason with the information the
  judge actually receives.
evidence_type: preprint
rank: 2
sources:
- url: https://arxiv.org/abs/2611.09291v1
  title: 'AutoRefine: Auto-Calibrating Code Judges from Workflow Outcomes'
  publisher: arXiv / Shervin Shahidi, James Poon and colleagues
  published_at: '2026-11-09T01:00:00Z'
  kind: preprint
eligibility:
  url: https://arxiv.org/abs/2611.09291v1
  published_at: '2026-11-09T01:00:00Z'
  precision: second
  verification: visible
  evidence: arXiv’s cs.AI recent listings place v1 under Monday, November 9, entry 523. The version history
    records a Friday deposit at 10:43:03 UTC, before 2 p.m. Eastern. The publisher’s official announcement
    schedule releases that batch Sunday at 8 p.m. Eastern, November 9 at 01:00 UTC, the inclusive window
    boundary.
  submitted_at: '2026-11-06T10:43:03Z'
  announcement_listing: https://arxiv.org/list/cs.AI/recent?show=50&skip=480
  announcement_schedule: https://info.arxiv.org/help/availability.html#announcement-schedule
  discovered_url: https://arxiv.org/abs/2611.09291
  verified_at: '2026-11-10T13:08:53.559051Z'
article_id: art_ea813f828db1bd3b
edition_date: '2026-11-10'
published_at: '2026-11-10T13:08:53.559051Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://arxiv.org/abs/2611.09291
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'arXiv:2611.09291v1 Announce Type: new Abstract: LLM judges increasingly serve as quality
  gates for code changes that have no test oracle, but a judge prompt must be calibrated for its task
  and recalibrated as the system it judges evolves, while hand labels for the calibration are resource
  intensive and go stale. Development workflows emit outcome labels for free (tests pass or fail, changes
  land or are abandoned), but these labels are noisy. We present AutoRefine, a loop that rewrites a deployable
  judge''s prompt to reproduce outcome labels, with an informed teacher that sees the judge''s input plus
  the outcome, explains each label it keeps, and abstains when the outcome cannot be explained from what
  the judge sees. On a held-out dataset with an execution oracle, calibration raised chance-corrected
  agreement (Scott''s $\pi$) from 0.36 to 0.60. On a deployed agent''s outcome labels, with 25\% flipped
  at random to introduce noise, the teacher set aside flipped \textsc{fail} labels at more than twice
  the rate of genuine ones, cutting overall label noise from 25\% to 20\%. Recalibrating that agent''s
  judge using AutoRefine raised its agreement with merge/abandon outcomes on 17 independently held-out
  diffs from the current workflow ($\pi$ 0.16 to 0.51); on 16 diffs from older workflows, the previous
  judge stayed ahead, illustrating the need for recalibration as the agent evolves. By abstaining, the
  teacher not only removes noisy labels but also flags changes whose outcome the judge''s input cannot
  explain, telling a team when a judge needs better inputs rather than a better prompt.'
feed_title: 'AutoRefine: Auto-Calibrating Code Judges from Workflow Outcomes [ ~ ] [ ◼ ]'
feed_published_at: '2026-11-10T05:00:00Z'
feed_id: sty_8856a019bc44754f
rating: Optional
technical_rating: Important
---
An engineer can abandon a good patch because the project changed. An AI judge that sees only the patch may treat that outcome as evidence of bad code. What would it take to learn from the team’s decisions without learning the wrong lesson?

In the AutoRefine preprint, Meta researchers give a second model the patch information the judge will see, plus the recorded outcome. That second model explains the outcome when it can ground a reason in the judge’s inputs. It can set an example aside when the evidence is missing. The researchers then revise the judge’s instructions using disagreements on the retained training examples, and select the revision on separate data. A hidden test or a decision to drop a feature can leave a training label the judge has little chance of explaining. [AutoRefine preprint](https://arxiv.org/abs/2611.09291v1)

On 17 changes from the current version of an internal performance-optimization agent, chance-adjusted agreement with merge and abandonment rose from 0.16 to 0.51 after recalibration. The new judge passed all eight changes that eventually landed, up from six. It marked five of the nine abandoned changes as failures, up from four. The older judge did better on a separate set of 16 changes from earlier workflows. The score measures agreement with one team’s workflow outcomes, with considerable uncertainty across those 17 changes. [The study’s results and limits](https://arxiv.org/html/2611.09291v1)

When a patch stalls, give reviewers a way to distinguish a technical rejection from a scope change or a pipeline failure. Keep those notes with the evaluation set and check what evidence would have been available when the judge scored the change. If the judge could learn the reason only after the decision, set that example aside when tuning.
