---
article_id: art_35e334c198740f74
story_key: https://openai.com/index/introducing-gpt-6-1-terra
title: GPT-6.1 Terra lowers the price of computer-use trials
summary: OpenAI’s new Terra release combines lower API rates with vendor-reported visual and computer-use gains;
  a task-level comparison still needs fixed tools and acceptance criteria.
section: Vendors
edition_date: '2026-10-27'
published_at: '2026-10-27T12:10:07.452207Z'
rank: 4
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: vendor
reader_job: What changed with GPT-6.1 Terra, and how can a team test whether its computer-use capability fits
  a particular workflow?
takeaways:
- OpenAI lists standard rates of $1 per million input tokens, $0.05 for cached input and $5 for output.
- The launch benchmarks are vendor evaluations; the system card cautions that research and API settings can
  differ from production ChatGPT.
topics:
- infrastructure
- evaluation
- agents
eligibility:
  url: https://openai.com/index/introducing-gpt-6-1-terra/
  published_at: '2026-10-26T00:00:00Z'
  precision: day
  verification: publisher_api
  evidence: 'OpenAI’s own News RSS item for the exact release URL gives pubDate Mon, 26 Oct 2026 00:00:00 GMT.
    Treat midnight conservatively as a whole publisher UTC day, not an exact launch instant: the entire October
    26 UTC day lies inside the window. The linked original system card visibly says Published October 26, 2026.
    The two discovery-feed timestamps do not establish eligibility.'
  discovered_url: https://openai.com/index/introducing-gpt-6-1-terra/
  verified_at: '2026-10-27T12:10:07.452207Z'
sources:
- url: https://openai.com/index/introducing-gpt-6-1-terra/
  title: Introducing GPT-6.1 Terra
  publisher: OpenAI
  published_at: '2026-10-26T00:00:00Z'
  kind: vendor
  date_precision: day
  date_basis: Original publisher RSS pubDate explicitly uses GMT; evaluated as the full UTC publication day,
    with the linked system card’s visible October 26 date as corroboration.
- url: https://deploymentsafety.openai.com/gpt-6-1-terra
  title: 'Addendum to GPT-6 Astra System Card: GPT-6.1 Terra'
  publisher: OpenAI Deployment Safety Hub
  published_at: '2026-10-26T00:00:00Z'
  kind: vendor
  date_precision: day
  date_basis: Visible original Published October 26, 2026; paired release RSS provides an explicit GMT publication
    day, rather than an observed exact hour.
leader_action: Authorize a bounded comparison on a real workflow before changing its model or expanding the
  agent’s permissions.
individual_action: Keep tools, permissions, reasoning effort and task acceptance fixed while comparing successful
  outcomes and correction effort.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: OpenAI has introduced GPT-6.1 Terra, an AI model designed to deliver fast and capable computer
  use at scale with enhanced visual reasoning, precise computer tasks, and clearer writing. It offers significant
  improvements over GPT-5.6 Terra, including a 50% reduction in API pricing and better performance on professional
  benchmarks such as Agents' Last Exam and MMMU-Pro. GPT-6.1 Terra demonstrates substantial gains in reducing
  hallucinations and factual errors, with error rates dropping from 53.6% to 16.7% at low reasoning effort.
  It also more than doubles coding task success rates compared to its predecessor. The model maintains strong
  safety and alignment features, meeting OpenAI's cybersecurity standards and resisting malicious prompt injections.
  Available now to ChatGPT Work, Codex users, and via API, GPT-6.1 Terra aims to make high-volume automation
  tasks more practical and cost-effective while advancing AI capabilities in visual understanding, coding,
  and factual reliability.
feed_title: OpenAI launches GPT-6.1 Terra, a faster, more efficient AI model with improved visual reasoning,
  coding, and factual accuracy at half the cost of GPT-5.6 Terra [ * ] [ ◼ ]
feed_published_at: '2026-10-26T18:01:17Z'
feed_id: sty_c07f6dd02f750834
rating: Important
technical_rating: Important
---

A cheaper model becomes useful when it can finish the task on the screen. OpenAI’s new Terra release makes that a more practical comparison for teams automating ordinary application work.

In its [October 26 announcement](https://openai.com/index/introducing-gpt-6-1-terra/), OpenAI positions GPT-6.1 Terra around visual understanding and computer use. Standard API rates are $1 per million input tokens, $0.05 for cached input and $5 for output. The company says those rates are 50% below GPT-5.6 Terra and GPT-6.1 Sol. It lists availability in the API as `gpt-6.1-terra` and in ChatGPT Work and Codex for Plus, Pro, Enterprise and Edu users.

OpenAI reports gains on computer-use and coding evaluations. On Agents’ Last Exam, it says Terra at medium reasoning effort scores 15 percentage points above GPT-5.6 Terra at about one-third the cost. These are the vendor’s measurements under its evaluation conditions, rather than evidence of a saving on your particular process.

The accompanying [system card](https://deploymentsafety.openai.com/gpt-6-1-terra) makes an important qualification: evaluations used research or API environments, whose prompts, tools and reasoning settings can differ from production ChatGPT. It also says some comparison values for earlier models reflect later versions. A model name alone therefore does not identify everything being compared.

Consider a hypothetical invoice-entry trial. Give each candidate the same documents, application permissions and completion rule. Count a result only when the correct fields are entered and the required confirmation is preserved. Keep the human corrections, retries and elapsed time beside the token bill. This proposed comparison would test the complete workflow, including the points where screen interpretation becomes an action.

A lower rate gives a team room to run that experiment. The deployment decision still rests on whether the agent completes the permitted work and leaves enough evidence for someone to check it.
