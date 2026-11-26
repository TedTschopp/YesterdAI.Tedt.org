---
title: An image comparison can succeed without comparing images
summary: ASTERISM finds that many multi-image tests can be solved from one image. Its audit and training
  experiments separate a correct answer from evidence of comparison.
section: Enterprise Ops
topics:
- evaluation
- agents
reader_job: How can a team check whether an image-comparison assistant actually needs evidence from every
  relevant image?
takeaways:
- One image or the question alone settled 24.2% of the audited benchmark items; the finding describes
  those tests.
- Removing visual evidence while preserving the layout helps expose shortcuts that an ordinary accuracy
  score hides.
leader_action: Require comparison tasks whose answers depend on several images before accepting a multi-image
  capability claim.
individual_action: Keep the image layout fixed while hiding individual images, then check whether the
  answer follows the available evidence.
rank: 1
article_id: art_07faf2fc1a583cf3
story_key: https://arxiv.org/abs/2611.32316
edition_date: '2026-11-26'
published_at: '2026-11-26T13:10:34.864628Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
evidence_type: preprint
sources:
- url: https://arxiv.org/abs/2611.32316
  title: 'ASTERISM: Do Multimodal LLMs Actually Look at All the Images?'
  publisher: arXiv
  published_at: '2026-11-25T01:00:00Z'
  submitted_at: '2026-11-24T10:12:44Z'
  kind: preprint
- url: https://arxiv.org/html/2611.32316v2
  title: 'ASTERISM: Do Multimodal LLMs Actually Look at All the Images? — full paper, version 2'
  publisher: arXiv
  published_at: '2026-11-26T01:00:00Z'
  kind: preprint
eligibility:
  url: https://arxiv.org/abs/2611.32316
  published_at: '2026-11-25T01:00:00Z'
  submitted_at: '2026-11-24T10:12:44Z'
  precision: second
  verification: visible
  timestamp_url: https://arxiv.org/list/cs.CV/pastweek?show=2000
  evidence: The Wed, 25 Nov 2026 (showing 302 of 302 entries ) primary-category listing contains 2611.32316
    as entry 420, without a cross-list or replacement marker. The official schedule at https://info.arxiv.org/help/availability.html
    establishes public announcement at 2026-11-25T01:00:00Z. Deposit timestamps are recorded separately,
    and the discovery feed timestamp is not used as publication evidence. Version two was deposited at
    2026-11-25T17:26:17Z; its Wednesday-before-14:00-Eastern submission slot yields public announcement
    at 2026-11-26T01:00:00Z. The story is eligible from its original announcement; no update is needed
    to move an old story into the window.
  verified_at: '2026-11-26T13:10:34.864628Z'
  event: public_announcement
feed_name: TedTschopp News Graph - Top Stories
feed_id: sty_c892400c7fdc41ed
feed_title: Researchers build ASTERISM, a large multi-image benchmark revealing multimodal LLMs often
  rely on single-image shortcuts, and propose cross-image credit assignment to improve training [ ~ ]
  [ ◻ ]
feed_summary: Researchers audited 33,000 items from 19 public multi-image benchmarks and found that 24.2%
  can be answered using only one image or the question alone, leading multimodal large language models
  (MLLMs) to take a single-image shortcut even when multiple images are needed. They created ASTERISM,
  the largest audited multi-image benchmark with 18,700 items requiring multiple images, along with training
  and hard subsets. The strongest proprietary MLLM scored 68% on the hardest subset. The study found that
  reinforcement learning with verifiable rewards (RLVR), commonly used in MLLM post-training, inadvertently
  rewards this shortcut because correct answers from one image receive the same reward as those combining
  multiple images. To address this, the researchers proposed cross-image credit assignment (CICA), an
  extension of RLVR that shifts credit toward tokens requiring multiple images. Applying CICA to three
  open-source MLLMs improved ASTERISM scores by 2.6 to 6.0 points, more than doubling gains from other
  reinforcement learning objectives trained on the same data.
feed_published_at: '2026-11-26T05:00:00Z'
feed_snapshot: docs/runs/2026-11-26-feed-snapshot.json
rating: Optional
technical_rating: Informational
---

Suppose an assistant compares two inspection photographs. Getting the right answer proves little about comparison if one photograph gives it away. [ASTERISM, a new preprint](https://arxiv.org/abs/2611.32316), tests that gap between a correct answer and the evidence needed to reach it.

Researchers audited 32,688 items from 19 public benchmarks. One image or the question alone settled 24.2% of them. They assembled ASTERISM from about 18,700 items requiring multiple images, including corrected and rewritten questions.

The diagnostic experiment keeps image positions and sizes fixed while turning hidden images gray. On tests where several images are needed, wrong answers from three studied models frequently repeated an answer the same model gave from one image, above the authors' chance comparison. That is evidence of a shortcut in these experiments, rather than proof that every apparently correct comparison used one.

The researchers also changed how training assigns credit. Their cross-image credit assignment method emphasizes response tokens that several images help explain. Across three open models, it raised the benchmark score by 2.6–6.0 points over the starting models, exceeding gains from the tested alternatives trained on the same data. [Audit, experiments and training method](https://arxiv.org/html/2611.32316v2)

The audit uses model judgments with human checks; those checks do not cover every original item. The training result is bounded by three model configurations and this constructed evaluation.

For an inspection pilot, build examples where each photograph contributes something necessary. Include a changed label, a missing component or a difference visible only across views. Then hide each image in turn without changing the surrounding prompt. Review whether the answer changes for the right reason.

Keep that evidence beside the score. The person relying on an inspection result needs to know that the assistant compared the views, especially when a plausible answer could come from just one.
