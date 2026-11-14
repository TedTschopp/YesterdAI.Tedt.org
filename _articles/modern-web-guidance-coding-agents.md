---
title: Modern Web Guidance gives coding agents cross-browser advice
summary: Version 1.0 adds reviewed web platform guidance, browser support data and public evaluations,
  with Firefox and Edge joining the project.
section: Enterprise Ops
reader_job: How should a web team check platform recommendations from its coding agent?
topics:
- agents
- evaluation
takeaways:
- Version 1.0 ships 203 use-case guides and adds Firefox and Edge participation alongside Chrome and MDN.
- Compatibility data can inform a recommendation. Teams can verify the proposed behavior against the browsers
  and assistive technology they support.
leader_action: Set the browser support policy before asking agents to modernize a shared component.
individual_action: Test one generated component with a keyboard and the oldest browser version the project
  supports.
evidence_type: practitioner
rank: 5
sources:
- url: https://developer.chrome.com/blog/modern-web-guidance-v1
  title: 'Modern Web Guidance 1.0: The web platform expertise your coding agent is missing'
  publisher: Chrome for Developers
  published_at: '2026-11-10T00:00:00Z'
  kind: practitioner
  date_precision: day
- url: https://github.com/GoogleChrome/modern-web-guidance/releases/tag/v1.0.0
  title: Modern Web Guidance v1.0.0
  publisher: GoogleChrome / Modern Web Guidance
  published_at: '2026-11-10T03:24:59Z'
  kind: practitioner
eligibility:
  url: https://github.com/GoogleChrome/modern-web-guidance/releases/tag/v1.0.0
  published_at: '2026-11-10T03:24:59Z'
  precision: second
  verification: publisher_api
  evidence: The official GoogleChrome repository’s GitHub release API for tag v1.0.0 gives published_at
    2026-11-10T03:24:59Z. Chrome for Developers separately dates its stable-release announcement November
    10.
  discovered_url: https://github.com/GoogleChrome/modern-web-guidance
  verified_at: '2026-11-11T15:34:57.860831Z'
article_id: art_a4978faa7e166cdb
edition_date: '2026-11-11'
published_at: '2026-11-11T15:34:57.860831Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://github.com/GoogleChrome/modern-web-guidance
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Modern Web Guidance is a collaborative project by Google Chrome, Microsoft Edge, Mozilla
  Firefox, and MDN teams that provides curated skills and guidelines to help coding agents avoid outdated
  JavaScript patterns and use modern web platform features. It offers a CLI tool that integrates expert
  knowledge on browser APIs, performance, accessibility, and native UI components to improve code quality
  and efficiency. The guidance covers recent web platform advancements including CSS layout, animations,
  accessibility improvements, and built-in AI capabilities like on-device language detection and translation.
  It aims to bridge the gap between large language models' training on legacy code and the current best
  practices by embedding targeted, token-efficient instructions directly into coding agents' workflows.
feed_title: Google, Microsoft, Mozilla, and MDN teams launch Modern Web Guidance to help coding agents
  adopt current web platform APIs and best practices [ ~ ] [ ◻ ]
feed_published_at: '2026-11-10T18:01:15Z'
feed_id: sty_6a88f4254febf0f5
rating: Optional
technical_rating: Informational
---
Ask a coding agent to build a dialog and it can produce something that opens when you click a button. The next questions are what happens to keyboard focus, how you close it without a mouse, and whether the browser your organization supports handles the same behavior. Modern Web Guidance 1.0 gives the agent maintained references for those decisions. Chrome announced the stable version with Firefox and Edge joining its stewardship alongside MDN and the web development community. [Chrome’s announcement](https://developer.chrome.com/blog/modern-web-guidance-v1) and [the v1.0.0 release](https://github.com/GoogleChrome/modern-web-guidance/releases/tag/v1.0.0)

The release includes 203 guides covering 250 web platform features. The guides are organized around things developers build, such as tab bars and sortable tables, and carry browser compatibility data. Chrome says specialists reviewed the user-facing guidance with assistive technology. The project publishes its agent evaluation results so a developer can see which guides improved performance in its tests. [Chrome’s announcement](https://developer.chrome.com/blog/modern-web-guidance-v1)

A team adopting it can start with one component that gets reused across the site. Give the agent the project’s supported browser versions and ask it to explain the API it chose. Then put the change through the same keyboard and assistive-technology checks a person’s patch would receive. In a dialog, closing with Escape and returning focus to the opening button are concrete behaviors a reviewer can see. Write down which ones passed before sending the new component to every team that uses it.
