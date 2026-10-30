---
article_id: art_c3a6927a59480677
story_key: https://arxiv.org/abs/2610.40516
title: MSafeTemp tests safety beyond English and simple translation
summary: A new preprint expands multilingual safety testing with localized prompts and paired benign requests,
  while limited human validation and automated judging qualify its results.
section: Security
edition_date: '2026-10-30'
published_at: '2026-10-30T12:05:35.170940Z'
rank: 3
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: preprint
reader_job: How should a multilingual service check whether safety behavior survives translation and local
  context?
takeaways:
- The HarmBench-based evaluation spans 60 languages; the separate training track spans 44.
- Translation and localization expose different failures, while uncertain benign labels and automated judging
  limit the conclusions.
topics:
- security
- evaluation
- governance
eligibility:
  url: https://arxiv.org/abs/2610.40516
  published_at: '2026-10-29T17:26:02Z'
  precision: second
  verification: visible
  evidence: Original arXiv submission history gives v1 Thu, 29 Oct 2026 17:26:02 UTC. Citation metadata and
    the visible submitted-on date agree. The version-pinned full text was read for methods, model-specific
    results and limitations.
  discovered_url: https://arxiv.org/abs/2610.40516
  verified_at: '2026-10-30T12:05:35.170940Z'
sources:
- url: https://arxiv.org/abs/2610.40516
  title: 'How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates, v1'
  publisher: arXiv · Max Neuwinger, Hanna Yukhymenko and Imanol Schlag
  published_at: '2026-10-29T17:26:02Z'
  kind: preprint
  date_precision: second
- url: https://arxiv.org/html/2610.40516v1
  title: 'How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates, v1 — full text'
  publisher: arXiv · Max Neuwinger, Hanna Yukhymenko and Imanol Schlag
  published_at: '2026-10-29T17:26:02Z'
  kind: preprint
  date_precision: second
leader_action: Require results for the service’s actual languages, including harmful compliance and unnecessary
  refusal, before extending a safety approval.
individual_action: Test translated and locally grounded variants with matched legitimate requests and fluent
  reviewers, retaining model and judge versions.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: Researchers have developed MSafeTemp, a large-scale multilingual dataset spanning 60 languages,
  designed to enhance safety alignment in large language models beyond English. The dataset is created using
  a scalable template-based augmentation pipeline that extracts safe templates from harmful prompts, translates
  them, and fills slots with culturally authentic entities to produce refusal and benign corpora. The study
  shows that English-only safety evaluations can miss vulnerabilities that appear in other languages or culturally
  localized variants, and that augmenting training data with templates improves safety performance across languages.
  MSafeTemp and its pipeline aim to support research and development of safer AI models for underrepresented
  cultures.
feed_title: Researchers release MSafeTemp, a 60-language template-based corpus to improve multilingual safety
  alignment for large language models [ ~ ] [ ◼ ]
feed_published_at: '2026-10-30T04:00:00Z'
feed_id: sty_a648bfde965a338b
---
A safety test in English leaves a question unanswered: what happens when the same request arrives in another language, with local names and context?

The October 29 [MSafeTemp preprint](https://arxiv.org/abs/2610.40516) studies that gap. Max Neuwinger, Hanna Yukhymenko and Imanol Schlag build templates from existing prompts, translate them and fill their slots with generic or culturally relevant entities. The separate HarmBench evaluation track spans 60 languages; the WildGuard-based training track spans 44. Those counts describe different parts of the corpus.

The [version-pinned experiments](https://arxiv.org/html/2610.40516v1) show why a single multilingual average can conceal important behavior. Several tested models comply with harmful translated requests more often than with the English originals. Llama-3.3-70B-Instruct fails most often on the English originals in these comparisons. Localized variants reach failures that translation misses, but they do not consistently produce a higher overall attack-success rate. The finding concerns coverage of different failures, rather than one universally stronger attack.

The study also pairs harmful prompts with intended benign alternatives to measure unnecessary refusal. That control has a limit: human raters endorsed only 65% of the sampled benign labels. Some softened requests still looked harmful, so the resulting refusal measure may overstate refusal of legitimate work. Human validation covered 11 languages, while most evaluation relied on automated model judges. Fixed, single-turn templates also leave longer conversations outside the tested setting.

For a service team, this suggests a practical review. Start with the languages people actually use. Compare original, translated and locally grounded requests, and include legitimate requests that resemble the risky ones. Ask fluent reviewers to check intent and labels before treating a refusal as a defect. Keep the exact model, prompt and judge versions with each result.

The decision is whether the service both refuses dangerous work and completes legitimate work in each supported language. A strong English result answers only part of that question.
