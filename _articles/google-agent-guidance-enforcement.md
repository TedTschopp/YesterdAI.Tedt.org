---
article_id: art_d26f3b9150349619
story_key: https://www.infoq.com/news/2026/10/data-agent-kit-ga
title: Google’s agent controls separate guidance from enforcement
summary: InfoQ’s new reporting distinguishes written agent procedures from Google Cloud permissions. A useful
  pilot verifies which tool calls the service actually refuses.
section: Enterprise Ops
edition_date: '2026-10-25'
published_at: '2026-10-25T12:06:11.472068Z'
rank: 1
format: analysis
reading_minutes: 3
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: reporting
reader_job: Which Google agent controls are instructions, which are enforced, and how can an operator verify
  the boundary?
takeaways:
- Google’s data-loss-prevention skill describes a consent procedure; IAM separately evaluates covered tool
  calls.
- A read-only deny policy still exposes write tools in the tool list and has documented scope limits.
- Verify the service response and the application’s explanation using the identity intended for the task.
topics:
- agents
- security
- governance
eligibility:
  url: https://www.infoq.com/news/2026/10/data-agent-kit-ga/
  published_at: '2026-10-24T08:34:00Z'
  precision: second
  verification: jsonld
  evidence: Publisher NewsArticle JSON-LD datePublished=2026-10-24T08:34:00Z; original reporting, not feed
    discovery time. Older primary context is dated separately.
  discovered_url: https://www.infoq.com/news/2026/10/data-agent-kit-ga/
  verified_at: '2026-10-25T12:06:11.472068Z'
sources:
- url: https://www.infoq.com/news/2026/10/data-agent-kit-ga/
  title: Google’s Data Agent Kit hits GA, splitting agent guardrails between skills and IAM
  publisher: InfoQ
  published_at: '2026-10-24T08:34:00Z'
  kind: reporting
  date_precision: second
- url: https://cloud.google.com/blog/topics/developers-practitioners/data-agent-kit-is-now-ga-bring-google-data-cloud-to-any-coding-agent/
  title: 'Data Agent Kit is now GA: Bring Google Data Cloud to any coding agent'
  publisher: Google Cloud
  published_at: '2026-09-30T13:11:29-07:00'
  kind: vendor
  date_precision: second
- url: https://github.com/GoogleCloudPlatform/data-agent-kit-plugin/blob/9a49a83f0e1088e8a64cd6d7db686dab20ccb7a3/skills/accidental-data-loss-prevention/SKILL.md
  title: Accidental data loss prevention skill, pinned to the October 13 source commit
  publisher: Google Cloud / GitHub
  published_at: '2026-10-13T22:21:26Z'
  kind: vendor
  date_precision: second
  source_commit: 9a49a83f0e1088e8a64cd6d7db686dab20ccb7a3
  date_basis: Pinned repository snapshot commit time, not a claim that the skill first appeared then.
- url: https://docs.cloud.google.com/mcp/prevent-read-write-tool-use
  title: Prevent read-write MCP tool use
  publisher: Google Cloud
  published_at: '2026-10-22T00:00:00Z'
  kind: vendor
  date_precision: day
  date_basis: Visible last-updated day is October 22 UTC; midnight normalizes the contextual date and is not
    eligibility evidence.
leader_action: Require evidence of a permitted read and a refused write under the intended agent identity before
  approving broader access.
individual_action: Trace the actual MCP service, caller identity and refusal response, then identify routes
  outside that policy.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'Google has made Data Agent Kit generally available, a free set of MCP tools and 37 open-source
  skills that connect coding agents to more than fifteen Google Data Cloud services. Two kinds of guardrail
  ship with it, and practitioners need to tell them apart: one is a skill asking the agent to stop, the other
  an IAM deny policy that refuses the call. By Steef-Jan Wiggers'
feed_title: Google's Data Agent Kit Hits GA, Splitting Agent Guardrails Between Skills and IAM [ * ] [ ◼ ]
feed_published_at: '2026-10-24T08:34:00Z'
feed_id: sty_77d7d2bfade49080
rating: Important
technical_rating: Important
hero:
  path: /assets/images/google-agent-guidance-enforcement.webp
  prompt: 'Create a wide landscape editorial hero for Yesterday in AI, approximately 1.91:1 and at least 1536
    pixels wide. International Typographic Style translated into a crisp conceptual graphic: warm ivory paper
    (#F8F6F0), deep slate (#101820), restrained burnt-orange (#BF4714) signal, fine hairlines, precise geometry,
    ample negative space, flat matte finish. One clear visual relationship tied to this article. No text, letters,
    logos, gradients, photographic people, robots, watermarks, or decorative texture. Keep all essential forms
    comfortably inside the frame. Article-specific subject: Google''s Data Agent Kit separates written guidance
    for an AI agent from an enforced permission check before a data tool can write. Compose a quiet horizontal
    workflow: on the left, a small stack of three slate-outline instruction sheets; in the center, a single
    small slate request block traveling along a fine horizontal rule; on the right, an outlined database cylinder
    behind a strong vertical slate boundary. The request route meets one closed burnt-orange rectangular gate
    at that boundary, visibly stopping the request before it reaches the database. The instruction sheets sit
    above and beside the route, connected to the request by a fine dotted line, making their advisory relationship
    clear without giving them control of the gate. The enforced boundary and orange gate dominate. No arrows,
    padlock icons, interface mockups, pseudo-writing, charts, extra colors, shadows, or 3D perspective. Strictly
    flat precise 2D forms, plenty of warm-paper negative space, clear at thumbnail size.'
  generated_at: '2026-10-25T12:03:29.072555Z'
  tool: image_gen
  width: 1734
  height: 907
  alt: Three outlined instruction sheets connect by a dotted line to a request block stopped at an orange gate,
    with a database beyond a slate boundary.
  caption: Instruction sheets feed a request that meets an orange gate before the database, showing how guidance
    and enforced permission act at different points.
---

A prompt can tell an agent to stop. A permission check can refuse its request. That difference becomes concrete when the agent can reach a database containing somebody else's work.

[InfoQ's October 24 report](https://www.infoq.com/news/2026/10/data-agent-kit-ga/) examines these two controls in Google's Data Agent Kit: skills that guide behavior and identity rules that govern tool calls. The underlying product is older. [Google announced general availability on September 30](https://cloud.google.com/blog/topics/developers-practitioners/data-agent-kit-is-now-ga-bring-google-data-cloud-to-any-coding-agent/). The useful finding in the new reporting is where each control operates, and what an operator can actually verify.

## Put the control where the action happens

Think of a warehouse instruction sheet and the key to its loading dock. The sheet explains how a careful operator should work. The key determines whether the door can open. Both matter, and they answer different questions.

Google's [published data-loss-prevention skill](https://github.com/GoogleCloudPlatform/data-agent-kit-plugin/blob/9a49a83f0e1088e8a64cd6d7db686dab20ccb7a3/skills/accidental-data-loss-prevention/SKILL.md), pinned here to the October 13 source commit, directs an agent to halt before irreversible deletion, explain the impact and obtain affirmative consent. It identifies operations such as dropping tables, broad SQL deletions and destroying encryption keys. This is a procedure carried in instructions. Its success depends on the agent applying that procedure to the action in front of it.

Google's [Identity and Access Management documentation](https://docs.cloud.google.com/mcp/prevent-read-write-tool-use) describes a separate decision when a Model Context Protocol tool is called. MCP is the interface through which the assistant asks another service to perform an operation. An IAM deny policy can reject calls to tools that are not marked read-only, at the organization, folder or project level.

The documented condition reads `api.getAttribute('mcp.googleapis.com/tool.isReadOnly', false) == false`. The fallback value is false, so a missing read-only attribute also meets that condition. This makes the tool's classification part of the authorization boundary. A reassuring explanation from the agent cannot substitute for that check.

Google says a denied write returns an HTTP client error, while the write tool can remain in the tool list. Visibility alone therefore says little about what the caller may do. The application has to explain a refusal without claiming completion.

## Follow the edges of the permission

The policy covers Google Cloud MCP servers. Its attributes apply only to the MCP tool-call permission; project-level checking also excludes resourceless APIs. Policies using service or tool-name attributes require the Google Cloud CLI.

Those details make a difference to an architecture review. A drawing with one box labeled read-only can hide several routes to the same data. The team has to account for each route: the covered MCP server, another vendor's server, a shell command or a separate application credential. A policy on one route establishes a property of that route. Extending the conclusion to the whole assistant requires more evidence.

Authorization also leaves a different operational question open. After a write is permitted, a timeout can obscure whether it completed. Retrying safely requires information about that operation's result and repeat behavior. A permission decision alone cannot supply it. Treat that as a separate application design problem rather than expecting the consent prompt to resolve it.

## Test the refusal {#for-practitioners}

A useful pilot can stay small. Use disposable data and the identity intended for investigation. Record one permitted read and one attempted write through the same covered MCP service. Keep the actual service response alongside the assistant's explanation. That checks the permission boundary and the application's handling of it.

Then inspect the routes outside that test. Identify which credentials can reach them and whether their operations receive an equivalent check. When a later task requires a write, define its approval, result confirmation and recovery path before granting that capability.

These are proposed checks, not tests performed by this publication. Neither the vendor documentation nor InfoQ's report demonstrates enforcement in your configuration. The useful handoff to an operator is a short record showing which identity could read, which request was refused and where the next permission decision belongs.
