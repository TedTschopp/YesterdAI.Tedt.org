---
title: Google separates agent state from compute in Agent Substrate
summary: Google’s Agent Substrate separates saved agent sessions from pooled compute; its CNCF announcement
  and fast-resume claims create a practical restore test.
section: Enterprise Ops
reader_job: How does Agent Substrate preserve an idle agent’s work, and what should a platform team test
  before adopting it?
topics:
- agents
- infrastructure
takeaways:
- Agent Substrate keeps session state in Actors and supplies execution through warm worker pools, according
  to Google.
- Google announces CNCF Sandbox donation and sub-500-millisecond resumes; production suitability needs
  workload-specific verification.
leader_action: Compare saved idle compute with storage, restoration and operational costs using a representative
  agent workload.
individual_action: Pause a session with uncommitted work, restore it on another worker, and verify both
  state and access boundaries.
evidence_type: vendor
rank: 2
sources:
- url: https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html
  title: 'Sandboxing Untrusted AI Agents at Scale: Google Donates Agent Substrate and gVisor to the CNCF'
  publisher: Google Open Source Blog
  published_at: '2026-11-05T17:00:00Z'
  kind: vendor
eligibility:
  url: https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html
  published_at: '2026-11-05T17:00:00Z'
  precision: second
  verification: publisher_api
  evidence: Google Open Source Blog official RSS matches this exact original URL and gives pubDate Thu,
    05 Nov 2026 17:00:00 +0000. The complete original displays Thursday, November 5, 2026. Publisher claims,
    including CNCF Sandbox status and performance, remain attributed.
  discovered_url: https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html
  verified_at: '2026-11-06T13:11:26.986982Z'
article_id: art_b8acd5d605b0c189
edition_date: '2026-11-06'
published_at: '2026-11-06T13:11:26.986982Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Google has contributed its Agent Substrate and gVisor projects to the Cloud Native Computing
  Foundation (CNCF) to foster community collaboration and development within the cloud native ecosystem.
  Agent Substrate is designed to efficiently manage AI agents by separating stateful actors from compute
  workers, addressing challenges like idle resource waste and control plane overload that traditional
  Kubernetes cannot handle. Agent Substrate enables AI agents to maintain state while minimizing resource
  use during idle periods and supports rapid wake-up times under 500 milliseconds. Google announced this
  donation at KubeCon North America 2026, marking these projects as Sandbox-level CNCF initiatives aimed
  at advancing secure, scalable AI agent infrastructure.
feed_title: Google donates Agent Substrate and gVisor to CNCF to support scalable, secure AI agent orchestration
  [ * ] [ ⬢ ]
feed_published_at: '2026-11-06T10:19:21Z'
feed_id: sty_0d25a569660cb3e0
rating: Important
technical_rating: Transformational
---
An agent waiting for a model still has a working directory, unfinished edits and a process to resume. Turning off its compute is easy. Keeping its place is the harder part.

Google’s [November 5 Agent Substrate announcement](https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html) describes a runtime that separates those jobs. An Actor represents a session’s filesystem, environment, memory and network rules. A pool of warm Workers supplies the compute when the session needs to run. After a turn, the runtime can save the Actor’s state and release its worker slot.

Google says the project has reached version 1.0 and announces the donation of Agent Substrate and gVisor to the Cloud Native Computing Foundation in Sandbox status. These are Google’s statements about the project’s release and governance, rather than an independent assessment of production readiness.

The mechanism matters for agents that spend long periods waiting between short bursts of work. Instead of keeping a dedicated Kubernetes Pod occupied for each session, a platform can move saved sessions through shared execution capacity. Google reports restoration in under 500 milliseconds and describes gVisor’s user-space interception of system calls as part of the isolation boundary. The announcement supplies no independent measurement of that restoration time.

For a platform team, the useful experiment is a recovery test with recognizable work inside it. Pause an agent after an uncommitted file edit, restore it on another worker, and inspect the file, running process and network access. Then repeat with a worker failure. A fast wakeup is useful only if the resumed session preserves the right state and the intended permissions.

Measure storage and restoration overhead beside the compute saved during idle time. The decision belongs to the complete session lifecycle, including the moment someone has to recover work that stopped midway.
