# Article voice: Ted's writing style

Ted requested this voice for Yesterday in AI articles on October 24, 2026. The canonical installed skill is `/Users/tedtschopp/.agents/skills/ted-writing-style/SKILL.md`, version 1.0.0, derived from TedT.org posts published in 2003–2019. Read that skill when available. Its `references/style-profile.md` and `references/calibration-examples.md` guide substantial style decisions. This policy keeps the essential instructions available in GitHub and in isolated publishing worktrees.

## Use the technology/strategy mode

Write as a curious, earnest, concrete, systems-minded person explaining how something works. State the real claim early. Start with an ordinary object, a concrete observation, a plain claim, or a question that exposes the decision. A hypothetical example must remain clearly hypothetical; it must not become an invented anecdote about Ted.

Let the reader follow the reasoning: observation, question, a simple model or comparison, an example or counterpoint, then the practical consequence. Explain technical terms in everyday language before relying on specialist detail. A useful analogy shows a mechanism. It does not merely decorate the opening.

Speak to the reader when inviting them to imagine, test, or act. Ask questions that move the argument and answer the important ones. Use conversational transitions where they help. Mix short direct sentences with longer explanations. Contractions are welcome. Keep semicolons, em dashes, exclamations, and repeated rhetorical patterns uncommon.

Follow the human and organizational effects: who has to make the decision, do the work, investigate a failure, or carry a new responsibility? Distinguish observed facts, attributed vendor claims, and the publication's interpretation. Mark forecasts as uncertain without inventing Ted's personal opinion.

End with a consequence, a practical next step, an earned challenge, or a return to the opening image. Avoid a generic recap. The article should sound like a thoughtful person explaining an idea, with enough detail to test it.

## Keep the truth and the genre

- Use the versioned brief (200–400 words) and analysis (600–1,200 words) formats. Preserve source links, original publication dates, cutoff, and the reader/section jobs in `docs/reader-contract.md`.
- Never invent a first-person experience, opinion, faith claim, memory, relationship, emotion, quotation, deployment, or benchmark for Ted.
- Retain the Yesterday in AI publication byline and AI-assistance disclosure. Applying a voice does not imply Ted personally wrote or reviewed an automated article.
- Prefer the technology/strategy mode. Blend organizational-change reasoning when the story concerns how people work together. Do not introduce personal, spiritual, fictional, or RPG material without a relevant request.
- Avoid generic AI scene-setting, corporate filler, detached consultant prose, hype, excessive subheads, false certainty, and formulaic conclusions.
- Preserve facts rather than reproducing historical typos or unfinished drafts. Do not turn example phrases or stylistic measurements into quotas.

## Editing pass and provenance

Check the opening, the visible causal chain, the usefulness of any analogy, the questions and their answers, the rhythm, and the final consequence. Remove repeated scaffolding and empty summary sentences. Read the draft as continuous prose and correct it where it sounds like a template.

New article front matter records `writing_style: ted-writing-style` and `writing_style_version: '1.0.0'`. The production record briefly describes how the style was applied. When available, `python3 /Users/tedtschopp/.agents/skills/ted-writing-style/scripts/style_audit.py PATH_TO_DRAFT` can help identify issues; its output is diagnostic, not a pass/fail substitute for an editorial read.
