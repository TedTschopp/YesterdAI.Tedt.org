---
title: A turbotap update makes phone actions and limits more explicit
summary: turbotap 1.6.7 adds clearer waits and readback while requiring caller-supplied label restrictions.
  A tap acknowledgment can leave its effect unconfirmed.
section: Enterprise Ops
topics:
- agents
- evaluation
- security
reader_job: What should an iPhone-automation caller check after updating to turbotap 1.6.7?
takeaways:
- The release reports an unconfirmed screen reaction separately from an acknowledged tap, and adds exact
  accessibility and control-change waits.
- Label filtering now needs caller-supplied patterns; existing app allowlists and stop checks remain separate.
leader_action: Require observed task completion and an explicit migration of label restrictions before
  reusing a phone workflow.
individual_action: Keep tap receipts beside observed state and exercise delayed reactions, unreadable
  fields and app switches.
rank: 2
article_id: art_f3acd91c9b1ccd5f
story_key: https://github.com/Maxteabag/turbotap/releases/tag/v1.6.7
edition_date: '2026-11-28'
published_at: '2026-11-28T13:08:08.433591Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: practitioner
sources:
- url: https://github.com/Maxteabag/turbotap/releases/tag/v1.6.7
  title: turbotap v1.6.7 release notes
  publisher: Maxteabag/turbotap on GitHub
  published_at: '2026-11-27T08:37:00Z'
  kind: practitioner
- url: https://github.com/Maxteabag/turbotap/blob/v1.6.7/README.md
  title: turbotap README at release v1.6.7
  publisher: Maxteabag/turbotap on GitHub
  published_at: '2026-11-27T08:37:00Z'
  kind: practitioner
eligibility:
  url: https://github.com/Maxteabag/turbotap/releases/tag/v1.6.7
  published_at: '2026-11-27T08:37:00Z'
  precision: second
  verification: publisher_api
  evidence: GitHub’s release API reports published_at 2026-11-27T08:37:00Z for v1.6.7, separately from
    created_at 08:36:40Z and later asset upload times. Pull request 41 merged at 08:36:40Z. Read the release
    notes, the merged PR record and the v1.6.7 README, including filter migration and limits. The development
    is this release, not the feed’s later suggestion of a new project launch.
  verified_at: '2026-11-28T13:08:08.433591Z'
  event: original_release
  timestamp_url: https://api.github.com/repos/Maxteabag/turbotap/releases/460338957
feed_name: TedTschopp News Graph - Top Stories
feed_id: sty_fbab730dd5a3905b
feed_title: Turbotap launches open-source CLI enabling AI agents to control iPhones over Wi-Fi with multi-step
  UI automation and integrated OCR [ ~ ] [ ◼ ]
feed_summary: Turbotap is an open-source command-line tool that allows AI agents to remotely control a
  real iPhone over Wi-Fi by executing multi-step UI interactions in a single command. It uses a patched
  WebDriverAgent on the iPhone to batch taps, scrolls, text entry, and screen reading, significantly speeding
  up automation compared to screenshot-per-step methods. The tool supports iOS 17+ devices with Developer
  Mode enabled and runs on macOS or Linux machines on the same network.
feed_published_at: '2026-11-28T11:47:33Z'
feed_snapshot: docs/runs/2026-11-28-feed-snapshot.json
rating: Optional
technical_rating: Important
---

A phone can acknowledge a tap before the screen shows whether it worked. [turbotap 1.6.7](https://github.com/Maxteabag/turbotap/releases/tag/v1.6.7) makes that distinction explicit in its release notes, alongside new waits for exact accessibility elements and observed changes in a control.

The tool lets a terminal or AI agent drive a real iPhone over local Wi-Fi through WebDriverAgent. A sequence of actions runs in one command, returning observations for the next decision. The new release improves field matching and readback, and reports when an acknowledged tap has an unconfirmed screen reaction. That gives the caller evidence that another check is needed.

There is also a migration decision. The [versioned documentation](https://github.com/Maxteabag/turbotap/blob/v1.6.7/README.md) says label filtering now requires patterns supplied by the caller or configuration. A workflow that relied on the earlier built-in filter must supply its own restrictions. A raw coordinate cannot be checked against a label pattern; the documented alternative is an exact labeled target when filtering matters.

The application allowlist and stop-file checks remain separate controls. Neither determines whether an action fulfills the person’s intended task. An agent still has to interpret the observed interface and the authority it has been given.

The release notes report 384 passing tests and a loopback comparison reducing command invocations from seven to one. The comparison used a simulated download wait. It does not establish faster completion of that task on a real phone.

For a device-automation pilot, retain the intended control, the tap acknowledgment and the subsequent observed state. Exercise a delayed reaction, a field that does not report its value and an unexpected application switch. Check the migrated label restrictions before reusing a saved workflow.

Completion should depend on the state the person requested. A successful input receipt is useful evidence along the way, with the resulting screen still to be checked.
