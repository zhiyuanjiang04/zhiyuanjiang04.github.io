# Personal Academic Homepage Redesign Design

## Goal

Create a local preview version of Zhiyuan Jiang's personal academic homepage using the selected **B / Al-folio-like** direction: a compact personal profile area, a restrained white research-first layout, and publication cards that receive more visual priority than general biography.

The homepage should feel like a researcher's landing page rather than a general student profile. Grades, course performance, and unrelated personal content are explicitly out of scope. A CV entry is reserved as an academic link and can later be pointed to the final resume PDF.

## Selected direction

The user selected **B: personal information and publications balanced** from the visual comparison.

The design combines:

- **Al-folio structure:** compact profile identity, small navigation, selected publications, and optional news.
- **Nerfies visual language:** white canvas, centered page container, dark neutral text, restrained borders, and research images used as the main visual anchors.
- **Jon Barron hierarchy:** concise introduction, no decorative hero section, and research outputs shown early and clearly.

## Scope

### In scope

- Redesign the homepage at `/_pages/about.md`.
- Add homepage-specific styles without changing the global theme more than necessary.
- Keep the current English content and links as the source of truth.
- Present the existing research identity, research interests, selected publications, and compact research news.
- Preserve the current publication detail pages and other site sections.
- Keep a visible `CV`/`Resume` entry as a link target that can later be changed to the final PDF.
- Make the layout responsive for desktop and mobile widths.

### Out of scope

- No grades, rankings, course results, or academic performance statistics on the homepage.
- No hobbies, lifestyle content, generic “achievements,” or decorative personal-brand sections.
- No changes to publication metadata or claims that are not already present in the repository.
- No rewrite of the Publications, CV, Talks, Teaching, or Portfolio inner pages in this first iteration.
- No push to GitHub; the result is for local review only.

## Information architecture

1. **Top navigation:** keep exactly the current three destinations: `Publications`, `Projects`, and `CV`. Do not add a blog, portfolio, teaching, or general achievements item in this iteration.
2. **Profile header:** show name, current academic/research roles, portrait, location/affiliation, and exactly three compact links: `Email`, `GitHub`, and `CV`. The profile copy remains left aligned inside a centered page container. The `CV` link initially targets the existing `/cv/` route and can later be changed to the final resume PDF.
3. **Research statement:** one concise paragraph distilled from the existing homepage copy, covering autonomous agents, world models, GUI agents, and compositional generalization.
4. **Selected publications:** show the three existing publications as compact image-and-text rows. Keep the existing three-paper set: `ZoomClick`, `WoW`, and `Wow, wo, val!`. Each row includes the existing title, author information, year, and only verified links. Use the following project links: `WoW` → `https://wow-world-model.github.io`, `ZoomClick` → `https://princeton-ai2-lab.github.io/ZoomClick`; retain the existing paper link for `Wow, wo, val!` unless a new project link is supplied.
5. **Recent work:** add a fourth research row for `Demystifying Agent Skills: Why They Work - Until They Don't`, linked to `https://zhiyuanjiang04.github.io/demystify-agent-skills`. Use the title/authors and description already present in the repository's project page or README; do not invent a venue or publication status.
6. **Research news:** keep only these three research-relevant items, in reverse chronological order: `Dec 2025` — ZoomClick released; `Sep 2025` — WoW released; `Sep 2025` — started research internship at Princeton AI2 Lab. Omit the Berkeley exchange item from the homepage.

## Content rules

- Treat `_config.yml` as authoritative for identity, current roles, and profile links; `_publications/*.md` as authoritative for existing paper titles, author formatting, dates, abstracts, and paper URLs; `_pages/about.md` as authoritative for research-prose wording; and the existing `files/`/`images/` assets as the authoritative local visual assets.
- When a project URL is explicitly supplied by the user, it overrides an older or missing project URL in the source repository. The three user-supplied project URLs above are therefore authoritative for the homepage links.
- Preserve exact paper titles, author formatting, dates, affiliations, and external URLs unless one of the above sources or the user's explicit links provides an updated value.
- Use short descriptive prose only when it is a direct condensation of existing homepage text; do not introduce new achievements or unsupported claims.
- Keep research content before news and keep news before any low-priority navigation or footer content.

## Visual system

- Background: white.
- Main text: dark neutral gray; secondary text: muted gray.
- Links: one restrained academic blue, with hover underline or a subtle opacity change.
- Typography: retain the theme's existing readable sans-serif stack; do not introduce a novelty display font.
- Container: centered, with a comfortable maximum width of approximately 1,080–1,160px on a 1,280px desktop viewport and generous but controlled whitespace.
- Profile: a narrow portrait/profile column of approximately 220–260px paired with a wider content column of approximately 680–760px on desktop; stack naturally below 768px.
- Publication rows: subtle separators, consistent thumbnails of approximately 150–180px wide, readable title sizing, and no heavy cards or gradients.
- Headings: concise, bold, left aligned within the centered content block.
- Interaction: simple hover emphasis on links and publication rows only; no auto-playing or attention-seeking animation.

## Technical approach

Keep the existing Jekyll/Academic Pages foundation. Add a small homepage-specific partial or class namespace so the new presentation is isolated from the existing archive/publication layouts. Prefer repository-local CSS and existing assets over new dependencies. Avoid modifying the generated/minified JavaScript unless a real interaction requirement appears.

Expected implementation files:

- Modify: `_pages/about.md` for homepage content and semantic structure.
- Modify or create: a scoped stylesheet under `assets/css/` imported by `assets/css/main.scss`.
- Modify only if needed: `_config.yml` for a CV link or minimal navigation cleanup.
- Do not modify: publication collection content or inner-page templates unless the homepage integration exposes a concrete regression.

## Acceptance criteria

- Homepage renders on the existing Jekyll stack without introducing a new runtime dependency.
- At a 1,280px desktop viewport, the profile and content columns align cleanly inside one centered container with no unexpected large empty column.
- At a viewport below 768px, the profile column stacks above the research content without horizontal overflow.
- The homepage contains no grades, score statistics, course-performance content, or unrelated personal sections.
- The profile identity, affiliations, visible link set, research statement, three existing publications, and one recent-work row match the repository source plus the user's three supplied project URLs.
- Selected publications are visually more prominent than news and secondary navigation.
- Paragraph text remains left aligned; only the overall content block is centered by the layout.
- Existing publication detail pages and the `/cv/` route still resolve.
- Local preview is checked visually before any future push.
