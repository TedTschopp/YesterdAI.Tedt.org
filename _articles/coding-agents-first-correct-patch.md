---
title: Coding agents often keep working after finding a fix
summary: A preprint follows intermediate patches and finds that coding agents can spend much of a run checking
  their work after a patch passes the benchmark.
section: Enterprise Ops
reader_job: What should a team measure before shortening a coding agent’s run?
topics:
- agents
- evaluation
- economics-adoption
takeaways:
- Across studied settings, 38% to 82% of runs that reached a correct patch did so on the first source edit.
- The first patch to pass the benchmark was visible in hindsight; production teams still need independent
  checks.
leader_action: Measure time to an accepted patch and regressions as well as total agent spend.
individual_action: Save and compare the first independently checked patch with the patch the agent submits.
evidence_type: preprint
rank: 2
sources:
- url: https://arxiv.org/abs/2611.14960
  title: 'Termination Lag: Coding Agents Solve Early but Stop Late'
  publisher: arXiv / Musa Cim, Burak Topcu and Mahmut Taylan Kandemir
  published_at: '2026-11-13T01:00:00Z'
  kind: preprint
- url: https://arxiv.org/html/2611.14960v1
  title: 'Termination Lag: Coding Agents Solve Early but Stop Late (full text, v1)'
  publisher: arXiv / Musa Cim, Burak Topcu and Mahmut Taylan Kandemir
  published_at: '2026-11-13T01:00:00Z'
  kind: preprint
eligibility:
  url: https://arxiv.org/abs/2611.14960
  published_at: '2026-11-13T01:00:00Z'
  precision: second
  verification: visible
  evidence: arXiv's Friday, November 13 New submissions list contains arXiv:2611.14960 v1. The official
    schedule places that batch at 8 p.m. Eastern on Thursday (November 13 at 01:00 UTC); November 11 was
    an arXiv holiday. The submission history records an earlier deposit at 2026-11-11T03:11:00Z, not first
    public availability. The publisher's batch time, not the discovery feed's 05:00 UTC, establishes eligibility.
  discovered_url: https://arxiv.org/abs/2611.14960
  verified_at: '2026-11-14T13:11:11.430390Z'
  listing_url: https://arxiv.org/list/cs.AI/new?show=2000&skip=0
  schedule_url: https://info.arxiv.org/help/availability.html#announcement-schedule
  submitted_at: '2026-11-11T03:11:00Z'
article_id: art_9e5328de36564d89
edition_date: '2026-11-14'
published_at: '2026-11-14T13:14:15.200836Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://arxiv.org/abs/2611.14960
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'arXiv:2611.14960v1 Announce Type: new Abstract: Coding agents can solve a task well before
  they stop working on it. We characterize \emph{termination lag}--the number of steps between an agent''s
  first correct patch and the end of its run--across five models, two agent frameworks, and three SWE-bench
  datasets by recording and testing every distinct repository patch generated during execution. Our analysis
  reveals that 38--82% of successful runs achieve a correct solution on their initial source-code edit.
  However, agents continue to expend substantial effort after correct patches, with post-solution steps
  accounting for a median of 35--37% for Qwen3-Coder and 54--60% for Laguna-XS.2 in successful runs on SWE-bench
  Verified and Multilingual. Agents spend most of these additional steps verifying their work and exploring
  the repository. In a small fraction of cases (1--8%), this continued activity leads agents to undo their
  earlier correct patch, leaving the final solution incorrect.'
feed_title: 'Termination Lag: Coding Agents Solve Early but Stop Late [ ~ ] [ ◻ ]'
feed_published_at: '2026-11-14T05:00:00Z'
feed_id: sty_7c1bf978e8671ecb
rating: Optional
technical_rating: Informational
---
A coding agent can fix a bug and keep going. How much of that extra work is useful? [Musa Cim, Burak Topcu and Mahmut Taylan Kandemir](https://arxiv.org/abs/2611.14960) recorded each distinct patch generated during benchmark runs. They tested the intermediate patches to see when each run first met the benchmark and what happened before the agent stopped.

The preprint covers five models, two agent frameworks and three SWE-bench datasets. Among runs that reached a correct patch, the first source edit already passed in 38% to 82% of cases, depending on the setting. In the authors’ main settings, the median share of steps spent after the first correct patch ranged from 35% to 60%. Most of those steps went to checking work and reading the repository. The authors also found that 1% to 8% of runs that reached a correct patch ended without one. [Patch timing and regressions](https://arxiv.org/html/2611.14960v1)

That finding doesn’t give a live agent a clock for knowing when to quit. The researchers could apply the benchmark tests to patches after the fact. On your repository, the first green check might miss an edge case, a compatibility promise or work that belongs in another file.

Try keeping the first diff that passes your existing acceptance checks. Keep the final diff too. At review, compare what the later changes buy: another verified requirement, a clearer fix or just more code to read. If an agent keeps rewriting work a reviewer would already accept, you have a reason to change when it hands the patch over.
