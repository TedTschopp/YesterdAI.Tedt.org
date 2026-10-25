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
reading_minutes: 4
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
  caption: A conceptual illustration of the mechanism discussed in this analysis.
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
writing_style_version: '1.0.0'
---

Follow the policy sounds like a short instruction. Try carrying it through a decision that depends on several conditions, evidence from different places, and an exception that applies only after a particular sequence of actions. The sentence has become a small program. Someone has to be able to inspect how that program reaches its answer.

The [SCOPE preprint](https://arxiv.org/abs/2610.31062v1) explores compiling such policies into programs composed of smaller neural predicates, deterministic extractors, and explicit logic. The authors optimize the program with counterexamples and report favorable accuracy and stability on their evaluated policy tasks. Those findings are research evidence for the approach, not a proof that an automatically compiled enterprise policy is correct in every situation.

Open the verdict and look for the parts that produced it. Can the policy owner recognize the conditions, can an operator find the evidence, and can a reviewer test how those parts were combined? Those questions give an inspectable policy program a job beyond producing a plausible final explanation.

## Make the policy interpretation reviewable

Start with the authoritative policy and identify the decisions the application must make from it. Record the conditions, relevant exceptions, required evidence, and allowed outcomes. The person responsible for the policy should be able to recognize that interpretation before it becomes an executable gate.

A generated program is an implementation proposal. It may omit a qualification, broaden an exception, or resolve an ambiguity in a way the policy owner did not intend. Keeping the mapping between the source rule and its checks visible gives the review something more concrete than a plausible overall explanation.

Distinguish a genuine policy ambiguity from an implementation error. If reviewers disagree about the intended result, route that question to the policy owner and retain the resolution. Repeatedly adjusting the model until it gives a convenient answer would conceal the underlying governance decision.

## Separate extraction from judgment

Some conditions can be checked from a well-defined field or an exact comparison. Others require interpreting language or context. A composite system should make that distinction clear because the components have different failure modes and different evidence requirements.

For example, an application might need to establish that a required identifier is present and that an action fits an approved purpose. The first question may have a straightforward data contract; the second may require a reviewed semantic judgment. This is a hypothetical design example, not a description of a particular SCOPE deployment.

Give the operator a path from the final verdict back through its intermediate results. Which condition was responsible, what evidence did it receive, and what remained uncertain? Those details make a pass or fail easier to investigate. They also give a correction somewhere specific to go, instead of requiring the team to adjust an opaque overall answer.

## Test combinations and boundaries

Checking each condition independently is necessary but may not reveal a mistake in how the conditions are combined. Include examples where one condition changes while the others remain fixed, along with cases exercising exceptions and missing information.

Use reviewed expected outcomes and preserve the reasoning behind them. Counterexamples are useful when they expose a mismatch with the policy, not merely when they make a score improve. A collection of difficult cases becomes a durable asset if the organization knows why each case belongs in it.

Keep a held-out evaluation separate from the examples used to generate or repair the program. Otherwise the team may learn that the implementation fits its development cases without learning how it behaves on new inputs. Report important categories and unresolved disagreements alongside the overall result.

## Preserve uncertainty through composition

A semantic predicate may be uncertain even when the code combining predicates is deterministic. The overall system needs a defined response when the evidence is incomplete, a component fails, or a judgment does not meet the application’s confidence requirement.

Ask what happens when a required check produces no usable result. Deferral, a request for more evidence, or an accountable human review may be appropriate, depending on the workflow. Have the policy owner and application owner agree on that behavior, then test it. The missing result should remain visible in the record rather than quietly turning into permission to proceed.

Also examine whether intermediate confidence values are meaningful for the decision. A number attached to a predicate is not automatically a calibrated probability. The evaluation should show how it is used and whether it helps distinguish acceptable from unacceptable cases.

Represent an unavailable check explicitly in the decision record. Record which input or component was missing and which fallback applied. This lets an operator distinguish a policy rejection from an incomplete evaluation, and it makes the next required action visible without reconstructing the entire program.

## Maintain the program with the policy

A policy revision should identify which checks, examples, and operating decisions need to change. Version the policy interpretation and executable artifacts together closely enough that an incident can be traced to the rules actually in effect.

Choose a bounded compound rule with a known owner and clear expected outcomes. Compare the current implementation with parts you can inspect, including the time needed to investigate an error and revise the rule. Then ask the owner to follow a verdict back to the policy. A useful implementation lets that person recognize the rule, understand the decision, and keep the uncertainty in view when the policy changes.
