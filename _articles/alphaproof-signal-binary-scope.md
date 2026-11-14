---
title: What DeepMind proved about Signal’s compiled code
summary: AlphaProof Code produced machine-checked proofs for an Arm Linux build of Signal’s one-to-one
  session code under defined assumptions.
section: Security
reader_job: What would a proof about a compiled security library let an engineering team promise?
topics:
- security
- evaluation
- agents
takeaways:
- DeepMind’s proofs apply to selected properties of Signal’s one-to-one protocol in a specific Arm Linux
  test executable.
- Researchers approved the specifications, agents wrote the proofs, and Lean checked them against those
  specifications.
leader_action: Ask for the exact build, security property and assumptions when a verification result enters
  a release decision.
individual_action: Pick a small security-critical module and write the property and environment a proof
  would have to cover.
evidence_type: research
rank: 1
sources:
- url: https://deepmind.google/blog/introducing-alphaproof-code/
  title: 'Introducing AlphaProof Code: a breakthrough in verifying complex software at depth'
  publisher: Google DeepMind / Pushmeet Kohli and Swarat Chaudhuri
  published_at: '2026-11-10T00:00:00Z'
  kind: research
  date_precision: day
- url: https://google-deepmind.github.io/code-verification/
  title: 'AlphaProof Code: Verifying Signal’s Security at the Machine-Code Level'
  publisher: Google DeepMind and Google / Swarat Chaudhuri et al.
  published_at: '2026-11-10T00:00:00Z'
  kind: research
  date_precision: day
- url: https://x.com/pushmeet/status/2120127611137634376
  title: AlphaProof Code announcement
  publisher: Google DeepMind / Pushmeet Kohli
  published_at: '2026-11-10T12:13:07.218Z'
  kind: research
eligibility:
  url: https://x.com/pushmeet/status/2120127611137634376
  published_at: '2026-11-10T12:13:07.218Z'
  precision: second
  verification: meta
  evidence: Co-author Pushmeet Kohli’s public launch post ID encodes 12:13:07.218 UTC on November 10.
    CellCog identifies the same post and 12:13 UTC. The direct X reader returned 403. DeepMind’s original
    and technical report show November 10, and timestamped coverage in The Register and Axios establishes
    the public launch by 12:00 UTC. The post time belongs to the post alone.
  discovered_url: https://deepmind.google/blog/introducing-alphaproof-code/
  verified_at: '2026-11-11T15:34:57.860831Z'
article_id: art_0e9fb0eb84f13acf
edition_date: '2026-11-11'
published_at: '2026-11-11T15:34:57.860831Z'
format: analysis
reading_minutes: 3
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://deepmind.google/blog/introducing-alphaproof-code/
feed_name: TedTschopp News Graph - Top Stories
feed_summary: DeepMind introduced AlphaProof Code, an AI system that produced three million lines of formal
  proofs in the Lean language to verify the security of Signal's core encryption software. This represents
  a significant advancement in automated verification of complex software systems. The AI agents systematically
  generated detailed proofs to ensure the correctness and security properties of Signal's encryption,
  demonstrating the potential for AI to assist in rigorous software verification tasks that are traditionally
  labor-intensive and error-prone.
feed_title: DeepMind launches AlphaProof Code AI agents that generated three million lines of Lean proofs
  to verify Signal's core encryption [ * ] [ ◼ ]
feed_published_at: '2026-11-10T12:02:28Z'
feed_id: sty_3bdc7f8d34024408
rating: Important
technical_rating: Important
hero:
  path: /assets/images/alphaproof-signal-binary-scope.webp
  width: 1536
  height: 1024
  tool: image_gen
  generated_at: '2026-11-11T15:29:42Z'
  alt: Fine vertical lines connect an upper row of slate bars to lower blocks, where an orange rectangle
    encloses the middle group.
  caption: The orange frame encloses only the blocks linked to the upper specification, illustrating the
    scope of the proof over the compiled code.
  prompt: 'Create a wide landscape editorial hero for Yesterday in AI, approximately 3:2 or wider. International
    Typographic Style translated into a crisp conceptual graphic: warm ivory paper (#F8F6F0), deep slate
    (#101820), restrained burnt-orange (#BF4714) signal, fine hairlines, precise geometry, ample negative
    space, flat matte finish. One visual relationship tied to formal verification of compiled Signal cryptographic
    code. Show two aligned, clearly separate horizontal layers on the paper. The upper layer is a short
    slate rule with a small set of precisely cut notches, standing for a human-approved formal specification.
    The lower layer is a dense, orderly field of slate rectangular modules, standing for the compiled
    binary. An ultra-thin slate alignment grid leads from the upper notches down to matching positions
    in the lower layer. A single narrow burnt-orange rectangular frame encloses only the modules covered
    by the proof, leaving visibly similar slate modules outside the frame on both sides. Let the orange
    frame convey proof scope, without a checkmark. Center the composition with generous margins. Use strong
    contrast and clean graphic geometry that survives thumbnail size. No text, digits, letters, logos,
    gradients, texture, photographic elements, people, padlocks, robots, watermarks, pseudo-code, decorative
    circuitry, or plotted data. Keep all essential forms comfortably inside the frame.'
---
A phone executes the instructions its software was compiled into. Google DeepMind’s AlphaProof Code project made those instructions the subject of a mathematical proof. Researchers took the unmodified library that handles one-to-one sessions for the Signal protocol, compiled it into an Arm Linux test executable, and proved that the executable met specified security properties under a model of how it runs. The team announced the work on Nov. 10. [DeepMind’s announcement](https://deepmind.google/blog/introducing-alphaproof-code/) and [the technical report](https://google-deepmind.github.io/code-verification/)

## Which promise did they check?

One promise is forward secrecy. If a key is compromised later, past messages protected by secrets that have since been discarded stay protected under the model. Another is recovery after compromise. The protocol can restore protection once the parties update their keys with fresh secrets that the attacker lacks. For someone sending messages, those are two different questions. What remains private after a compromise, and when is it safe to talk again? The paper spells out the conditions under which the library provides each property. [The report’s introduction and verification sections](https://google-deepmind.github.io/code-verification/)

Those properties had been studied at the protocol level, where the object of study is a design. Here the team used the standard Rust compiler to build a test program around the protocol library, then proved properties about that specific executable. Reasoning directly about its instructions removes the need to trust the compiler’s translation. The paper identifies the library versions, the test program that wraps them, and the model of Arm Linux instructions used to reason about its behavior. [The report’s setup and binary-level guarantees](https://google-deepmind.github.io/code-verification/)

## Where human judgment sits

Researchers worked with models to turn descriptions of Signal’s security goals into mathematical statements. Human experts approved those statements before teams of agents set out to prove them. Lean, a proof checker, then checked each proof against the approved statement. DeepMind reports about 6.5 million lines of checked proof code. The report identifies about 26,000 lines of trusted definitions and machine semantics, along with other assumptions such as the behavior of low-level cryptographic routines and the correctness of Lean’s checker. [The AlphaProof Code technical report](https://google-deepmind.github.io/code-verification/)

The division matters because a proof can be right about a claim that a user would find too narrow. The paper studies one-to-one sessions. The authors describe group messaging and server-side protocols as possible extensions. They also distinguish a classical security proof from a separate symbolic result for the secrecy of the initial handshake against a future quantum attacker. Their results leave the ratchet’s post-quantum recovery properties for further work. Those distinctions belong next to any assurance claim that a team carries into a release. [The report’s discussion](https://google-deepmind.github.io/code-verification/)

## For practitioners
{: #for-practitioners }

Start with a promise you can name. A team responsible for a firmware updater might want to prove that it will accept only an image with a valid signature for that device. Ask which bytes the signature covers, how the updater selects a trusted key, and which code decides that the image belongs to the device. The answers make the promise specific enough to review and identify pieces that a proof would have to assume or cover.

Give the specification and the build identity to two people who have different jobs. A security reviewer can read the specification and ask which situations it covers. A release engineer can say which target and library versions the resulting binary uses. If a dependency changes, they have a record to help decide whether the evidence still applies and which checks to repeat. A team experimenting with proof-writing agents can measure the time those two people spend reviewing the claims and assumptions, along with the time it takes to get a passing proof.

Keep the specification, build identifier and checked proof together. If a customer asks what the shipped code guarantees, the team can point to the executable and the property it proved in the same record.
