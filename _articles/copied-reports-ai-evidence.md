---
title: Copied reports can look like independent evidence to AI judges
summary: A preprint finds that identical reprints can raise model judges’ confidence in false claims and tests
  how grouping copies changes those decisions.
section: Enterprise Ops
reader_job: How should an evidence pipeline handle syndicated reports before asking a model to corroborate
  a claim?
topics:
- evaluation
- governance
takeaways:
- Several identical reprints raised false-claim acceptance in two tested models, even though every copy carried
  the same underlying evidence.
- Grouping known reprints helped in a simulation; paraphrases and coordinated sources still require scrutiny.
leader_action: Require the evidence pipeline to expose where each consequential claim originated before treating
  it as independently confirmed.
individual_action: Test with a known syndication chain, a paraphrase and an independently sourced account
  of the same event.
evidence_type: preprint
rank: 2
sources:
- url: https://arxiv.org/abs/2611.09203v1
  title: 'Copies Are Not Confirmations: How News Duplication Fools LLM Judges and Continual Learners'
  publisher: arXiv / Abdelkader Metales, Miriam Grabenheinrich and Aicha Metales
  published_at: '2026-11-09T01:00:00Z'
  kind: preprint
eligibility:
  url: https://arxiv.org/abs/2611.09203v1
  published_at: '2026-11-09T01:00:00Z'
  precision: second
  verification: visible
  evidence: arXiv lists v1 in New submissions for Monday, November 9 in cs.LG. Its official availability schedule
    makes the before-2 p.m. Eastern Friday batch public Sunday at 8 p.m. Eastern (November 9 01:00 UTC). Submission
    history records 2026-11-06T09:22:29Z; that is the deposit, not public availability. The November 9 09:37
    UTC verified GitHub feed snapshot independently bounds availability before cutoff.
  discovered_url: https://arxiv.org/abs/2611.09203
  verified_at: '2026-11-09T13:10:38.500275Z'
  submitted_at: '2026-11-06T09:22:29Z'
  announcement_listing: https://arxiv.org/list/cs.LG/new
  announcement_schedule: https://info.arxiv.org/help/availability.html#announcement-schedule
article_id: art_631a29fba65f0551
edition_date: '2026-11-09'
published_at: '2026-11-09T13:10:38.500275Z'
format: brief
reading_minutes: 2
writing_style: ted-writing-style
writing_style_version: 1.0.0
editorial_contract: 2
story_key: https://arxiv.org/abs/2611.09203
feed_name: TedTschopp News Graph - Top Stories
feed_summary: 'arXiv:2611.09203v1 Announce Type: new Abstract: Many news reports of a claim are copies of
  one source: wire stories, content shared within a media group, syndicated features and press releases. We
  ask whether LLM judges and continual learners treat such copies as independent confirmations. In 200,000
  English CC-News articles, a MinHash detector links 18.9% to a near-copy from another outlet (precision 0.97
  once boilerplate is removed); it links 92% of edited reprints to their originals but none of the LLM rewrites
  by phi4, Llama 3.2 or Gemini 2.5 Flash. Shown three identical reprints of a claim about an unknown person
  instead of one report, Llama 3.2 3B and phi4 14B raised the share of lies they accepted from 0.06 to 0.71
  and from 0.21 to 0.90 and ignored a note that the reports came from one source; Gemini 2.5 Flash already
  believed a single report, and Gemini 2.5 Pro followed provenance notes and tables. In a simulated continual-learning
  stream, showing the judge one report per detected chain cut the copied lies it accepted by 0.10-0.24 across
  four judges, at a mean cost of no more than 4.2 percentage points of accepted truths. Against reworded copies,
  a test of how many of a report''s named entities are absent from an earlier look-alike separates LLM rewrites
  from 100 labelled independent reports of the same event with AUC 0.98-0.99 and wrongly flags one; entity
  overlap alone does as well, TF-IDF and a current embedding model come close, and the test catches few natural
  same-source derivatives. With the miss patterns of generated rewrite networks, it cut the reworded-copy
  lies accepted from 0.67 to 0.20 (0.40 when the rewriter invents details). Counting reports or chains alone
  is not a reliable defence, the effect of provenance information depends on the judge, and colluding sources
  remain the open problem. Code and labels: https://github.com/Metalesaek/copies-experiment'
feed_title: 'Copies Are Not Confirmations: How News Duplication Fools LLM Judges and Continual Learners [
  ~ ] [ ◻ ]'
feed_published_at: '2026-11-09T05:00:00Z'
feed_id: sty_77746720f8168285
rating: Optional
technical_rating: Informational
---
Open three tabs and you might see three copies of the same dispatch. The headlines and mastheads change. The reporting behind them doesn’t.

Abdelkader Metales, Miriam Grabenheinrich and Aicha Metales [tested what happens when a model judges those copies](https://arxiv.org/abs/2611.09203v1). In a controlled experiment with claims about invented people, Llama 3.2 3B accepted 6% of false claims when shown one report and 71% when shown three identical copies under different outlet names. For phi4 14B the figures were 21% and 90%. A note about the shared source did little for those two models. Gemini 2.5 Pro responded much more strongly to the note, but in that test it could also reject true claims about invented people.

The authors then [simulated a system](https://arxiv.org/html/2611.09203v1#S5) that uses judges to decide which claims a learner takes in. Showing one report per detected copy chain lowered the share of copied lies accepted by 10 to 24 percentage points across four judges. The largest average drop in acceptance of true claims was 4.2 points. The text comparison missed the generated rewrites. In the simulation, grouping duplicates also left coordinated claims from separate sources untouched.

This matters when an analyst asks an AI system to confirm an incident or a supplier change. The useful question is what each source saw for itself. Keep the wire credit, filing or interview attached to each claim, and let a reviewer inspect why two accounts were grouped. If all three links lead back to the same interview, the analyst still has one source.
