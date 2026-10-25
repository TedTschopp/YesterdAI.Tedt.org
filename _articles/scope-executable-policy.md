---
article_id: art_26bdab7224d77ff2
story_key: https://arxiv.org/abs/2610.31062
title: Compound policies need inspectable decisions
summary: SCOPE explores compiling natural-language policies into smaller predicates and explicit logic. The enterprise
  opportunity is a policy decision whose components can be tested, explained, and maintained separately.
section: Security
edition_date: '2026-10-23'
published_at: '2026-10-24T22:46:52.157329Z'
retrospective: true
rank: 3
reading_minutes: 2
eligibility:
  url: https://arxiv.org/abs/2610.31062v1
  published_at: '2026-10-22T10:41:13Z'
  precision: second
  verification: publisher_api
  evidence: arXiv API published=2026-10-22T10:41:13Z
  discovered_url: https://arxiv.org/abs/2610.31062
sources:
- url: https://arxiv.org/abs/2610.31062v1
  title: SCOPE — compiling natural-language policies into neurosymbolic predicate programs
  publisher: arxiv.org
  published_at: '2026-10-22T10:41:13Z'
  date_precision: second
hero:
  path: /assets/images/scope-executable-policy.webp
  prompt: Create a wide landscape editorial hero for Yesterday in AI, approximately 1.91:1. Strictly flat two-dimensional
    Swiss editorial graphic, warm ivory (#F8F6F0) background, deep slate (#101820) geometry and a single restrained
    burnt-orange (#BF4714) signal. Precise hairlines, elegant asymmetric composition, generous negative space, clean
    vector-like edges delivered as a raster. No text, letters, numbers, logos, gradients, shadows, photographic
    objects, people, robots, watermarks, grain, or decorative texture. All essential forms well inside the frame.
    A tidy slate policy document at left is decomposed into three small separate geometric condition nodes in the
    center. Fine lines connect the conditions to one explicit orange combination gate, then to a single slate decision
    square at right. Each condition remains separately visible. Elegant minimal graphic about compiling a compound
    policy into inspectable tests and deterministic composition.
  generated_at: '2026-10-24T22:37:29.510Z'
  tool: image_gen
  width: 1536
  height: 804
  alt: A policy document separates into three visible condition nodes that meet at an orange composition gate.
  caption: The condition nodes meet at a composition gate, making the steps behind a combined policy decision visible.
leader_action: Require a reviewed mapping from the policy to its executable checks, with examples that challenge
  each condition.
individual_action: Inspect which predicate or extractor produced a verdict before treating the overall result as
  explained.
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'arXiv:2610.31062v1 Announce Type: new Abstract: Policy enforcement for LLM agents has shifted from
  single-turn content moderation to compound, application-specific policies evaluated over multi-turn transcripts
  and tool-call trajectories. Fine-tuned guardrail models are efficient but degrade on compound policies, and while
  LLM-as-a-judge approaches achieve higher accuracy, they incur high inference cost and tend to produce unstable
  predictions. Neurosymbolic methods offer a natural alternative, decomposing the policy into narrow neural decisions
  composed under explicit logic. However, existing symbolic layers lack the required expressiveness and are optimized
  against fixed data rather than the policy itself. To address this, we introduce SCOPE, which compiles a policy
  into an executable program of neural predicates executed by small models, deterministic extractors, and code that
  composes their outputs. The program is optimized jointly with its training data, using adversarial generation
  of counterexamples that target where the program deviates from the policy. We evaluate SCOPE on a benchmark of
  real-world policy tasks against prompt optimization, task decomposition, and workflow generation methods, achieving
  the highest average accuracy across tasks and models. Programs optimized with the weakest executor transfer to
  other models without further optimization. This allows them to be deployed in production on inexpensive models,
  where they reach accuracy comparable to frontier reasoning models. Unlike these monolithic models, SCOPE produces
  substantially more stable predictions, and each verdict is interpretable through the predicate outputs that produced
  it. Additionally, we validate the key components of our method through an ablation study. SCOPE thus enables reliable,
  interpretable, and efficient policy enforcement at production scale.'
feed_title: 'SCOPE: Compiling Natural-Language Policies into Neurosymbolic Predicate Programs [ ~ ] [ ◼ ]'
rating: Optional
writing_style: ted-writing-style
writing_style_version: 1.0.0
format: brief
takeaways:
- SCOPE studies policy programs built from neural predicates, deterministic extractors, and explicit logic, refined
  with counterexamples.
- Make the policy-to-program mapping inspectable and test combinations, sequences, missing evidence, and exceptions.
topics:
- governance
- evaluation
- security
evidence_type: preprint
reader_job: Make a compound policy decision traceable to its component evidence and logic.
modified_at: '2026-10-25T03:42:17.530845Z'
legacy_anchors:
- make-the-policy-interpretation-reviewable
- separate-extraction-from-judgment
- test-combinations-and-boundaries
- preserve-uncertainty-through-composition
- maintain-the-program-with-the-policy
- actions-heading
editorial_contract: 2
---
“Follow the policy” becomes a more demanding instruction when the answer depends on several conditions and an exception tied to their sequence. Someone needs to inspect how those parts combine.

The [SCOPE preprint](https://arxiv.org/abs/2610.31062v1) explores compiling such policies into programs composed of smaller neural predicates, deterministic extractors, and explicit logic. The authors optimize the program with counterexamples and report favorable accuracy and stability on their evaluated policy tasks. Those findings are research evidence for the approach, not a proof that an automatically compiled enterprise policy is correct in every situation.

## Make the policy interpretation reviewable

Keep a mapping from each policy condition to its input evidence, extraction step, judgment, and logical connection. A final verdict needs a route back to the rule it claims to implement.

Separate straightforward extraction from semantic judgment. In a hypothetical workflow, finding a required identifier and deciding whether an action fits an approved purpose are different questions. That example describes a design distinction rather than a SCOPE deployment.

An uncertain intermediate result must retain its meaning when combined with other conditions. Turning missing evidence into a definite-looking Boolean can conceal the question that needed review.

## Test combinations and boundaries
{: #for-practitioners }

Choose a bounded compound rule with an accountable owner and reviewed expected outcomes. Include conditions that pass separately but fail in combination, missing inputs, relevant sequences, and cases near an exception.

When a verdict is wrong, identify the predicate, extractor, or logical connection responsible. Compare the effort required to diagnose and revise the rule alongside accuracy.

Version the policy and program together. A later wording change needs a reviewed path to its corresponding checks and a retained set of examples for comparison.

The reported accuracy and stability remain findings for the evaluated tasks. Automatic compilation does not establish that an enterprise policy is correct in every situation.

Ask the owner to follow one verdict back through its evidence. A useful program leaves that person able to recognize the rule and see where its interpretation still needs judgment.