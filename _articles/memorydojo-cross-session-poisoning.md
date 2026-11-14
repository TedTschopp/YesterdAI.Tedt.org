---
title: MemoryDojo traces how a poisoned tool result reaches later tasks
summary: The MemoryDojo preprint follows malicious tool output into stored memory and later actions across
  five agent memory systems.
section: Security
reader_job: Where can an instruction from an untrusted tool result survive, and how should a team test its
  effect on a later session?
topics:
- security
- agents
- evaluation
takeaways:
- In simulated tasks, all five tested integrations sometimes brought back and acted on malicious content from
  an earlier session.
- Inspect what gets saved, what gets recalled and which actions it can influence.
leader_action: Include cross-session poisoning and memory recovery in the release criteria for agents that
  can take sensitive actions.
individual_action: Trace a single untrusted tool result through stored notes, later retrieval and the audit
  log for the resulting action.
evidence_type: preprint
rank: 1
sources:
- url: https://arxiv.org/abs/2611.09721v1
  title: 'MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory'
  publisher: arXiv / David H. Yang and colleagues
  published_at: '2026-11-09T01:00:00Z'
  kind: preprint
eligibility:
  url: https://arxiv.org/abs/2611.09721v1
  published_at: '2026-11-09T01:00:00Z'
  precision: second
  verification: visible
  evidence: arXiv lists v1 in New submissions for Monday, November 9 in cs.CR. Its official availability schedule
    makes the before-2 p.m. Eastern Friday batch public Sunday at 8 p.m. Eastern (November 9 01:00 UTC). Submission
    history records 2026-11-06T17:00:09Z; that is the deposit, not public availability. The November 9 09:37
    UTC verified GitHub feed snapshot independently bounds availability before cutoff.
  discovered_url: https://arxiv.org/abs/2611.09721
  verified_at: '2026-11-09T13:10:38.500275Z'
  submitted_at: '2026-11-06T17:00:09Z'
  announcement_listing: https://arxiv.org/list/cs.CR/new
  announcement_schedule: https://info.arxiv.org/help/availability.html#announcement-schedule
article_id: art_fb361bac5ee689fe
edition_date: '2026-11-09'
published_at: '2026-11-09T13:10:38.500275Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://arxiv.org/abs/2611.09721
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'arXiv:2611.09721v1 Announce Type: cross Abstract: LLM agents benefit from using memory systems
  to improve performance on long-horizon, multi-session tasks. However, memory introduces a critical attack
  surface. Malicious instructions encountered in one session may be stored and propagated through memory before
  being retrieved and acted upon in later sessions. Because memory systems differ in how they process and
  retrieve information, the downstream effects of poisoning can vary significantly across systems. To quantify
  the effects of poisoning across different memory architectures, we introduce MemoryDojo, a benchmark for
  tracing the lifecycle of poisoned information through agent memory and measuring its influence on subsequent
  agent behavior. MemoryDojo is easily extensible, consists of 155 multi-session long-horizon trajectories
  covering four domains, and supports five different memory systems. Through our evaluation, we find that
  all memory systems are susceptible to memory poisoning, with substantial variation in downstream effects.
  We further propose a memory-aware poison optimization process that increases the poisoning efficacy, highlighting
  differences between memory architectures. We hope that MemoryDojo will support research on understanding
  and mitigating agentic memory risks.'
feed_title: 'MemoryDojo: Benchmarking Poisoning Through LLM Agent Memory [ ~ ] [ ◼ ]'
feed_published_at: '2026-11-09T05:00:00Z'
feed_id: sty_f3a4eeaa2dc3a9b4
rating: Optional
technical_rating: Important
---
An agent can close a compromised page and carry its instructions into tomorrow’s work. The part to watch is what it writes down.

In the [MemoryDojo preprint](https://arxiv.org/abs/2611.09721v1), David H. Yang and colleagues put one malicious instruction into a simulated tool response, then followed what agents stored, brought back and acted on in later sessions. The benchmark spans 155 task sequences in four domains, including banking and workplace tools, and compares five memory integrations. All five showed some effect on later tasks. Four showed effects across domains in the cross-domain test, less often than within the original domain.

Storage and action are two different steps. In one experiment with GPT-5.6-Luna, [instructions tailored to the Letta integration](https://arxiv.org/html/2611.09721v1#S6) raised the share of later tasks in which the attack objective was reached from 15.3% to 46.3% in same-domain sequences. Retrieval rose much less. Those numbers describe the study’s simulated tasks and attack setup. They are not estimates of attack success for deployed Letta systems.

Consider a support agent that reads a customer’s message and saves a note for the next shift. The note may accurately describe what the customer said. If it comes back stripped of its source, the next agent may read the customer’s request as a rule the business already approved. A release test can plant one instruction, start a fresh session and check whether the agent’s tools still require authorization. Follow any notes derived from the original tool response as well.

That test also gives an incident responder something concrete to look for. Deleting the first note won’t clear the instruction from any later notes that inherited it.
