---
title: Fireworks AI breach exposes Notion AI chat transcripts
summary: Notion says the Fireworks AI incident affected fewer than 1% of its workspaces and included transcripts
  used by its Insights feature.
section: Security
reader_job: Which Notion AI data was involved, and what should an affected workspace check?
topics:
- security
- governance
takeaways:
- The affected dataset included Notion AI chat transcripts used by Insights. Notion says the incident affected
  fewer than 1% of workspaces.
- Notion disabled Insights and directed notified customers to review the data inside their workspace and rotate
  credentials pasted into affected chats.
leader_action: Have the workspace owner and security team review the vendor’s notice together and assign ownership
  for any exposed credentials.
individual_action: If your workspace was notified, use Notion’s in-workspace instructions to check which conversations
  were involved.
evidence_type: vendor
sources:
- url: https://www.notion.com/security/advisories/security-incident-involving-a-third-party-ai-vendor
  title: Fireworks AI incident
  publisher: Notion
  published_at: '2026-11-12T00:00:00-08:00'
  date_precision: day
  kind: vendor
- url: https://techcrunch.com/2026/11/12/cyberattack-on-fireworks-ai-allowed-hackers-to-access-notion-customers-chat-transcripts/
  title: Cyberattack on Fireworks AI allowed hackers to access Notion customers’ chat transcripts
  publisher: TechCrunch / Zack Whittaker
  published_at: '2026-11-12T15:02:00Z'
  date_precision: minute
  kind: reporting
rank: 2
eligibility:
  url: https://techcrunch.com/2026/11/12/cyberattack-on-fireworks-ai-allowed-hackers-to-access-notion-customers-chat-transcripts/
  published_at: '2026-11-12T15:02:00Z'
  precision: minute
  verification: visible
  evidence: Zack Whittaker’s original reporting is visibly dated November 12, 2026 at 7:02 a.m. PST (15:02
    UTC). It quotes Notion’s disclosure and confirms the Insights transcript scope. Notion’s separate Security
    Advisories version is visibly dated November 12. Its November 13 update is excluded because its exact publication
    time is unverified.
  discovered_url: https://www.notion.com/en-gb/security/advisories/security-incident-involving-a-third-party-ai-vendor
  verified_at: '2026-11-13T13:26:11.778218Z'
article_id: art_a3523f73e3129004
edition_date: '2026-11-13'
published_at: '2026-11-13T13:26:11.778218Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://techcrunch.com/2026/11/12/cyberattack-on-fireworks-ai-allowed-hackers-to-access-notion-customers-chat-transcripts
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Notion disclosed that chat transcripts from its AI feature were exposed due to a security breach
  at third-party vendor Fireworks AI. The company revoked exposed Notion API keys found in affected user messages
  and reported the issue to the vendors that issued those keys. Notion has notified impacted customers and
  is continuing to investigate the incident.
feed_title: Notion says AI chat transcripts were exposed in Fireworks AI breach, revoked affected API keys
  and notified impacted customers in November 2026 [ * ] [ ◼ ]
feed_published_at: '2026-11-13T02:49:47Z'
feed_id: sty_a34ae9041ba30cdd
rating: Important
technical_rating: Important
---
A chat transcript can lose its author label and still contain a password. Notion said data exposed in a breach at Fireworks AI included Notion AI transcripts used for Insights, a feature that helped customers understand how they used AI. Notion says fewer than 1% of its workspaces were affected. [Notion’s advisory](https://www.notion.com/security/advisories/security-incident-involving-a-third-party-ai-vendor)

Fireworks handled the classification work behind Insights and also served open-weight models for Notion. Notion said it disconnected from Fireworks on Nov. 3. Fireworks confirmed the affected dataset on Nov. 8 and Notion began contacting affected customers on Nov. 9. The advisory says the transcripts lacked labels identifying the author or workspace for the vast majority of affected workspaces. It also says the transcripts excluded results returned by connected tools. A person could still have typed identifying details or credentials into a message. [Notion’s timeline](https://www.notion.com/security/advisories/security-incident-involving-a-third-party-ai-vendor) · [TechCrunch’s reporting](https://techcrunch.com/2026/11/12/cyberattack-on-fireworks-ai-allowed-hackers-to-access-notion-customers-chat-transcripts/)

Notion disabled Insights during the investigation. It says it revoked exposed Notion API keys it found in affected user messages on Nov. 11. Customers it notified can follow the email instructions to retrieve the affected data securely inside the workspace. Notion advises those customers to rotate sensitive credentials they pasted into Notion AI during the affected period. [Notion’s response and instructions](https://www.notion.com/security/advisories/security-incident-involving-a-third-party-ai-vendor)

In an affected workspace, the person who can review the transcript and the person who can replace a credential may be on different teams. Have the workspace owner tell each service owner which credential appeared in a transcript and where the service uses it.
