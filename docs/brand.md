# Yesterday in AI Brand

The publication is **Yesterday in AI**. The outlined **YesterdAI** logo is the mark, with accessible name “Yesterday in AI.” It is an endorsed publication of Ted Tschopp’s Public Workbench, not the AI skills catalog at AI.Tedt.org.

Article prose follows the `ted-writing-style` skill and [the project voice policy](ted-writing-style.md). Use the technology/strategy mode for enterprise AI reporting, with concrete openings, visible reasoning, useful comparisons, conversational clarity, and practical human consequences. Preserve factual attribution and the publication byline; do not invent Ted's personal testimony. The design rules below govern presentation and hero artwork.

## Interface

The checked-in `assets/css/tokens.css` and `assets/css/brand.css` originate in Ted’s `design-yesterday-in-ai` skill, aligned with preview.tedt.org on October 23, 2026. Use those role tokens rather than inventing new colors or fonts.

- Paper ground: #F8F6F0; raised paper: #FFFDFA; slate ink: #101820; body: #1F2126. Dark theme reverses paper/slate roles with raised #17222C.
- One orange accent: #BF4714 on paper, #E86027 on slate. No orange-filled cards, bands, or sections. Section tags use colored dots and labels.
- Cal Sans 400 for headings, Inter for body text at 18px / 1.65, Fira Code for dates, numbers, counts, domains, and code. Headings are not bold; 600 marks labels.
- Hairline dividers, a two-pixel strong rule over labeled sections, generous whitespace, no card shadows, restrained six-pixel radii. Stories are open editorial rows.
- Use [AP-style title case](title-capitalization.md) for all h1–h6, article/edition/page titles, topic names, and other title or header text, including labels used as headers. This project policy overrides sentence-case headline guidance in the design and writing skills. Preserve names such as OpenAI, LiteLLM, arXiv, and MiniMax. Review authored text; do not use CSS capitalization or blanket lowercasing. Headlines use no more than 12 words. No all-caps labels, emoji, gradients, glass, stock imagery, or redrawn logos.
- A slate navbar in both themes; visible focus, 44px targets, underlined links, and reduced-motion support.

## Hero Art Direction

Generate a **distinct conceptual editorial graphic** for each full article. Use a wide landscape composition, warm paper ground, slate forms, fine rules, deliberate negative space, and one restrained orange signal. Express the article’s specific mechanism: a bounded connection, separated credentials, a review gate, a ranked decision, a verifiable trail, or another concrete relationship grounded in the reporting. Avoid generic robot heads, glowing brains, science-fiction circuitry, or fabricated company marks.

Keep headlines and logos outside generated pixels, in real HTML/SVG. Use minimal crisp geometric forms rather than hand-drawn illustration or photographic claims. The image should remain clear in both themes and at thumbnail size. Write alt text describing the actual composition. A caption explains what the visible relationship means for this story, preferably in one sentence and never more than two. Avoid generic illustration or generation credits in captions; the publication’s footer and About page provide the AI disclosure.

Shared prompt foundation:

> Create a wide landscape editorial hero for Yesterday in AI. International Typographic Style translated into a crisp conceptual graphic: warm ivory paper (#F8F6F0), deep slate (#101820), restrained burnt-orange (#BF4714) signal, fine hairlines, precise geometry, ample negative space, flat matte finish. One clear visual relationship tied to this article. No text, letters, logos, gradients, photographic people, robots, watermarks, or decorative texture. Keep all essential forms comfortably inside the frame.

Append the article-specific subject and composition. Save the exact combined prompt with the resulting asset’s metadata.

## Reader Components (Version 2)

The approved reader contract in docs/reader-contract.md controls levels of detail and supersedes older example-page content arrangements. The visual tokens and logos retain their identity.

- **Briefing:** compact date/theme header, linked TL;DR, explicit lead, up to five headline-first rows. Leadership implication once per preview.
- **Newspaper:** fixed topical order, headline-first rows with sources and role implications, contextual contents rail only above 1,100px.
- **Research article:** decision takeaways, proportionate native-ratio illustration, concise contents links for longer analyses, body, Sources, topic links, and related coverage.
- **Finder:** compact text results with edition date, section, format, and reading time. No duplicated role-action blocks or decorative thumbnail grid.
- **History:** month rules, edition title/date, and representative linked headlines.
- **Small screens:** one reading column; native-ratio images stack instead of leaving a narrow strip of text.

Use the same geometry, palette, and negative space for future heroes, choosing a specific mechanism rather than a repeated generic symbol. Comparisons can use paired fields; data/authority boundaries can use gates; decisions can use routes; evidence can use linked records. These are composition choices, not extra colors or fabricated statistical charts. Preserve existing article images.

## Pinned Fonts

The same Cal Sans, Inter, Fira Code, and Titillium Web faces are served from assets/fonts/ rather than depending on a changing remote stylesheet. The manifest records source URLs and SHA-256 hashes; OFL licenses accompany the Latin and extended-Latin subsets. Keep the names, weights, and metrics fixed during editorial runs.
