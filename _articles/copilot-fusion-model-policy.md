---
article_id: art_af8e72e013cbe8cf
story_key: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion
title: Copilot Fusion puts model routing inside an administrator’s policy
summary: GitHub’s generally available routing system combines model orchestration with administrator controls
  and per-model billing, creating a concrete choice about permitted models and cost.
section: Enterprise Ops
edition_date: '2026-10-29'
published_at: '2026-10-29T12:11:15.279432Z'
rank: 1
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: vendor
reader_job: What must administrators decide when Copilot chooses and combines models for a coding task?
takeaways:
- Fusion can use one model, escalate a draft or run a critique workflow, within enabled model policies.
- Charges follow the models actually used; compare accepted work and undiscounted cost before making routing
  the default.
topics:
- agents
- governance
- economics-adoption
eligibility:
  url: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/
  published_at: '2026-10-28T16:00:00Z'
  precision: second
  verification: jsonld
  evidence: Publisher TechArticle/BlogPosting JSON-LD gives 2026-10-28T09:00:00-07:00; WebPage JSON-LD
    gives the equivalent 16:00:00Z. Modified at 16:02:31Z, also before cutoff.
  discovered_url: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/
  verified_at: '2026-10-29T12:11:15.279432Z'
sources:
- url: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/
  title: Route and orchestrate models with GitHub Copilot Fusion
  publisher: GitHub
  published_at: '2026-10-28T16:00:00Z'
  kind: vendor
  date_precision: second
leader_action: Decide which models Fusion may use and compare the cost of accepted tasks before setting
  an organization-wide default.
individual_action: Keep the selected effort, observable model calls, billed usage and review result with
  each comparison task.
feed_name: Ted Tschopp's AI News
feed_summary: 'Estimated GAI-style rating: Important. Rationale (estimate): Estimated from similar historically
  rated GAI selections. Selected in GAI Insights'' briefing dated 2026-10-29. Briefing source: https://gaiinsights.com/articles.'
feed_title: Route and orchestrate models with GitHub Copilot Fusion [ * ] (Estimated)
feed_published_at: '2026-10-29T00:00:00+00:00'
feed_id: 473647821428b82ce0e46909545f2ced
---
When Copilot chooses the models, an administrator still chooses which models it may use.

GitHub’s [October 28 Copilot Fusion announcement](https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion/) makes automatic model routing and orchestration generally available across all Copilot plans in Visual Studio Code, the Copilot app, Copilot CLI and JetBrains IDEs. Users select Standard, High or Max effort rather than a specific model.

Fusion can send a task to one model, have an efficient model draft before a quality check decides whether to escalate, or have another model critique a draft before revision. That changes the unit being selected: a request can invoke a small workflow whose cost and behavior depend on several calls.

The announcement says Fusion respects enabled enterprise and organization model policies. Administrators can also disable a model specifically for Fusion while leaving it available elsewhere, and can set Fusion’s effort level as the default through managed settings. Those controls let an organization define the permitted pool before asking the router to choose within it.

Billing follows every model used at its standard rate. GitHub is offering paid plans a temporary 30% discount on model costs through Fusion. A launch discount and an efficient workflow affect the bill in different ways. Keep the undiscounted comparison visible when deciding whether the routing system should become the default.

For a pilot, use representative coding tasks with the same acceptance criteria and review process. Record effort level, observable model calls, billed usage, elapsed time and whether the change passed review. If a complete route is unavailable to the administrator, retain that visibility limit with the result rather than assuming which models participated.

A useful trial ends with a change someone can accept and a cost someone can explain. The model picker has become an operating decision; the organization still needs a clear account of what it authorized and what useful work it received.