---
title: Claude joins Google Meet calls to draft work live
summary: Anthropic’s Team and Enterprise beta adds a visible meeting participant that can create shared drafts
  while retaining a transcript and notes.
section: Enterprise Ops
reader_job: What can Claude do during a meeting, and who can see its work during and after the call?
topics:
- agents
- governance
takeaways:
- Claude can create documents and whiteboards during a Google Meet call and save the artifacts with the transcript
  and notes.
- Enterprise administrators enable the beta. The default excludes calls with external invitees, and an admin
  can allow those calls.
leader_action: Set rules for eligible meeting types, external guests and transcript access before enabling
  the beta for a team.
individual_action: Check who is on the call before asking Claude to retrieve information or share a draft.
evidence_type: vendor
sources:
- url: https://claude.com/resources/articles/claude-meetings
  title: Introducing Claude Meetings
  publisher: Anthropic
  published_at: '2026-11-12T00:00:00-08:00'
  date_precision: day
  kind: vendor
- url: https://x.com/claudeai/status/2120973994191094179
  title: Claude Meetings launch announcement
  publisher: Anthropic / Claude
  published_at: '2026-11-12T20:16:20Z'
  kind: vendor
rank: 4
eligibility:
  url: https://claude.com/resources/articles/claude-meetings
  published_at: '2026-11-12T00:00:00-08:00'
  precision: day
  verification: visible
  evidence: Anthropic’s original product announcement displays November 12, 2026, corroborated by Claude release
    notes. Claude’s official launch post is reproduced with a November 12 3:16 p.m. Eastern timestamp by Advance
    Intelligence; decoding the linked post ID yields 20:16:20.663 UTC (12:16 p.m. Pacific). Anthropic is based
    in San Francisco. The whole November 12 Pacific day is within the window. Direct X returned 403; product
    details are verified in the original Anthropic announcement.
  discovered_url: https://the-decoder.com/claude-meetings-lets-anthropics-ai-join-your-video-calls/
  verified_at: '2026-11-13T13:26:11.778218Z'
article_id: art_779abe288b1c01da
edition_date: '2026-11-13'
published_at: '2026-11-13T13:26:11.778218Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://claude.com/resources/articles/claude-meetings
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Anthropic is adding Claude directly to video calls. Claude Meetings joins Google Meet sessions
  and creates documents, whiteboards, and meeting notes in real time. The feature launches in beta for Team
  and Enterprise plans, with more platforms coming later. The article Claude Meetings lets Anthropic's AI join
  your video calls appeared first on The Decoder.
feed_title: Claude Meetings lets Anthropic's AI join your video calls [ * ] [ ◼ ]
feed_published_at: '2026-11-12T20:26:50Z'
feed_id: sty_fdf6e135f15a2420
rating: Important
technical_rating: Important
---
A team can ask Claude to start a document while everyone is still talking in Google Meet. In a beta announced Nov. 12, Anthropic says Claude joins as a visible participant, posts a notice and can build a document or whiteboard that teammates refine during the call. It saves the transcript, notes, action items and drafts on a meeting page that invited colleagues in the organization can open afterward. [Anthropic’s announcement](https://claude.com/resources/articles/claude-meetings)

The assistant can use a person’s connected tools after asking for permission. Anthropic says the first approval carries forward and that Claude currently confirms the speaker each time a request is made aloud. When Claude posts an answer in the Google Meet chat, everyone on that call can see it. Someone can give Claude permission to look up a number that the full group would otherwise have no way to see. [Anthropic’s privacy details](https://claude.com/resources/articles/claude-meetings)

The beta starts with Google Meet on Team and Enterprise. Team accounts have the feature on by default, and Enterprise administrators enable it for all or part of their organization. Claude stays out of meetings with external invitees by default. If an administrator allows external calls, guests’ contributions become part of the transcript. Organizations with certain configurations, including zero data retention and customer-managed encryption keys, are excluded from the beta. [Anthropic’s rollout terms](https://claude.com/resources/articles/claude-meetings)

Start with a recurring internal meeting where the team already keeps minutes. Ask for one shared draft. After the call, check who can open it and whether the person who usually writes the minutes has less to do.
