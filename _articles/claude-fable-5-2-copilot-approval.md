---
title: Claude Fable 5.2 gets a policy switch in GitHub Copilot
summary: GitHub leaves Claude Fable 5.2 off by default for Copilot Business and Enterprise, where enabling
  it acknowledges Anthropic’s default safety-monitoring retention.
section: Vendors
reader_job: What must a Copilot administrator check before allowing Claude Fable 5.2 to handle company
  code?
topics:
- governance
- infrastructure
takeaways:
- Copilot Business and Enterprise admins have to enable a dedicated Fable 5.2 policy.
- GitHub describes a time-limited zero data retention exception for eligible customers. Enabling the model
  is a separate step.
leader_action: Decide which repositories can use Fable 5.2 after confirming the retention terms and exception
  for your Copilot account.
individual_action: Check the model picker against your repository’s data policy before sending sensitive
  code to Fable 5.2.
evidence_type: vendor
rank: 1
sources:
- url: https://www.anthropic.com/claude-fable-and-mythos-5-2
  title: Claude Fable 5.2 and Mythos 5.2
  publisher: Anthropic
  published_at: '2026-11-09T00:00:00Z'
  kind: vendor
  date_precision: day
- url: https://github.blog/changelog/2026-11-09-claude-fable-5-5-in-github-copilot/
  title: Claude Fable 5.2 in GitHub Copilot
  publisher: GitHub Changelog
  published_at: '2026-11-09T00:00:00Z'
  kind: vendor
  date_precision: day
- url: https://x.com/claudeai/status/2119867114450268322
  title: Claude Fable 5.2 and Claude Mythos 5.2 launch announcement
  publisher: Anthropic / Claude
  published_at: '2026-11-09T18:57:59.968Z'
  kind: vendor
eligibility:
  url: https://x.com/claudeai/status/2119867114450268322
  published_at: '2026-11-09T18:57:59.968Z'
  precision: second
  verification: meta
  evidence: The public @claudeai launch post ID encodes November 9 at 18:57:59.968 UTC. ArtificialWatch
    and Zeitgraphs independently identify the same publisher post and launch date. The direct X page returned
    403. Anthropic’s complete launch page and GitHub’s Changelog both show November 9 without a clock
    time. The post establishes eligibility for the launch, with no exact time assigned to either article.
  discovered_url: https://www.anthropic.com/claude-fable-and-mythos-5-2
  verified_at: '2026-11-10T13:08:53.559051Z'
article_id: art_a989f1582084d0cf
edition_date: '2026-11-10'
published_at: '2026-11-10T13:08:53.559051Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://www.anthropic.com/claude-fable-and-mythos-5-2
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Anthropic has upgraded its Claude Fable and Claude Mythos models to version 5.2, enhancing
  their abilities in coding, reasoning, and vision tasks. These models have demonstrated success in complex
  technical challenges such as software migrations, device design, physics problem-solving, robotics,
  and formal mathematical proofs. Claude Fable 5.2 includes robust cybersecurity and biology safeguards,
  making it broadly available, while Mythos 5.2 is accessible through specialized programs for life sciences
  and cybersecurity research. The new versions communicate more clearly and generate outputs up to 30%
  faster than their predecessors, with an optional fast mode that increases speed by up to 2.5 times at
  higher pricing. Extensive prerelease safety testing indicates that these models maintain or improve
  alignment and safety measures, including protections against misuse and distillation attacks. Anthropic
  recommends using Claude Opus 5.5 for most coding and knowledge tasks, reserving Fable and Mythos 5.2
  for more ambitious technical work or as advisors and orchestrators in multi-model workflows.
feed_title: Anthropic releases Claude Fable 5.2 and Mythos 5.2 with improved coding, reasoning, and vision
  capabilities, faster output, and enhanced safety features [ * ] [ ⬢ ]
feed_published_at: '2026-11-09T18:01:10Z'
feed_id: sty_b256c40e4b9562ca
rating: Important
technical_rating: Transformational
---
A developer can read about Fable 5.2 and still have no model to select in GitHub Copilot. GitHub is rolling it out gradually, and the policy for Copilot Business and Enterprise starts off. An administrator who enables it acknowledges that Anthropic retains prompts and outputs by default for safety monitoring. [GitHub Changelog](https://github.blog/changelog/2026-11-09-claude-fable-5-5-in-github-copilot/)

Anthropic released Fable 5.2 alongside Mythos 5.2. They share an underlying model. Fable adds safeguards on high-risk cybersecurity and biology requests, while organizations working in those fields can apply for Mythos through verification programs. Anthropic lists standard rates of $8 per million input tokens and $40 per million output tokens for both. Those rates tell a team what a run costs. The service a team uses determines who can run the model and which retention terms apply. [Anthropic’s release](https://www.anthropic.com/claude-fable-and-mythos-5-2)

The exception has its own approval. GitHub says eligible enterprise customers can use Fable 5.2 with zero data retention through the end of the calendar year while Anthropic rolls out Enterprise Frontier Safeguards. Approved Copilot requests route to zero data retention endpoints once an admin enables the model. Anthropic describes the new safeguards as running automated monitoring on prompts and responses stored in customer infrastructure. [GitHub’s eligibility details](https://github.blog/changelog/2026-11-09-claude-fable-5-5-in-github-copilot/) and [Anthropic’s explanation of safety monitoring](https://www.anthropic.com/claude-fable-and-mythos-5-2)

Before sending sensitive code from a long migration, have the Copilot admin confirm which endpoint will receive the prompts. Record who owns that check and when any exception expires. A migration can outlast the approval that let a team start it.
