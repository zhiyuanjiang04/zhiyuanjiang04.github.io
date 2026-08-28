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

1. **Top navigation:** keep a minimal set of academic destinations, with the homepage as the visual entry point. Existing site destinations remain available but should not compete with the profile header.
2. **Profile header:** show name, current academic/research roles, portrait, location/affiliation, and a short row of links. The profile copy remains left aligned inside a centered page container.
3. **Research statement:** one concise paragraph distilled from the existing homepage copy, covering autonomous agents, world models, GUI agents, and compositional generalization.
4. **Selected publications:** show the three existing publications as compact image-and-text rows. Each row includes the existing title, author information, year, and only links already present in the repository.
5. **Research news:** keep only research-relevant milestones already stated in the current homepage, in a compact list below the selected publications.
6. **CV entry:** include a single academic CV link in the profile links. The first local version may point to the existing `/cv/` route; once the resume PDF is finalized it can be changed to `/files/cv.pdf` without changing the homepage structure.

## Content rules

- Treat `_config.yml`, `_pages/about.md`, `_publications/`, and the existing `files/`/`images/` assets as the authoritative content sources.
- Preserve exact paper titles, author formatting, dates, affiliations, and external URLs unless the source repository already contains an updated value.
- Use short descriptive prose only when it is a direct condensation of existing homepage text; do not introduce new achievements or unsupported claims.
- Keep research content before news and keep news before any low-priority navigation or footer content.

## Visual system

- Background: white.
- Main text: dark neutral gray; secondary text: muted gray.
- Links: one restrained academic blue, with hover underline or a subtle opacity change.
- Typography: retain the theme's existing readable sans-serif stack; do not introduce a novelty display font.
- Container: centered, with a comfortable maximum width and generous but controlled whitespace.
- Profile: a narrow portrait/profile column paired with a wider content column on desktop; stack naturally on mobile.
- Publication rows: subtle separators, consistent thumbnail dimensions, readable title sizing, and no heavy cards or gradients.
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
- At desktop width, the profile and content columns align cleanly inside one centered container.
- At mobile width, the profile column stacks above the research content without horizontal overflow.
- The homepage contains no grades, score statistics, course-performance content, or unrelated personal sections.
- The profile identity, affiliations, links, research statement, and publication metadata match the repository source.
- Selected publications are visually more prominent than news and secondary navigation.
- Paragraph text remains left aligned; only the overall content block is centered by the layout.
- Existing publication detail pages and the `/cv/` route still resolve.
- Local preview is checked visually before any future push.
