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
4. **Selected publications:** show the three existing publications as compact image-and-text rows. Keep the existing three-paper set: `ZoomClick`, `WoW`, and `Wow, wo, val!`. Existing paper links remain visible as `Paper`; user-supplied project links are added as separate `Project` links rather than replacing paper links. Use this exact link matrix:
   - `WoW`: `Paper` → `https://arxiv.org/abs/2509.22642`; `Project` → `https://wow-world-model.github.io`.
   - `ZoomClick`: `Paper` → `https://arxiv.org/abs/2512.05941`; `Project` → `https://princeton-ai2-lab.github.io/ZoomClick`; `Code` → `https://github.com/Princeton-AI2-Lab/ZoomClick`.
   - `Wow, wo, val!`: `Paper` → `https://arxiv.org/abs/2601.04137`; no project link unless one is supplied later.
5. **Recent work:** add a fourth research row for `Demystifying Agent Skills: Why They Work - Until They Don't`, linked as `Project` to `https://zhiyuanjiang04.github.io/demystify-agent-skills`. Use the exact title and any short description from the current `README.md` of `https://github.com/zhiyuanjiang04/demystify-agent-skills`; until that content is imported locally, do not add extra author, venue, or publication-status claims.
6. **Research news:** include exactly these three research-relevant items, in this exact order: `Dec 2025` — ZoomClick released; `Sep 2025` — WoW released; `Sep 2025` — started research internship at Princeton AI2 Lab. Omit the Berkeley exchange item from the homepage.

## Content rules

- Treat `_config.yml` as authoritative for identity, current roles, and profile links; `_publications/*.md` as authoritative for existing paper titles, author formatting, dates, abstracts, and paper URLs; `_pages/about.md` as authoritative for research-prose wording; and the existing `files/`/`images/` assets as the authoritative local visual assets.
- When a project URL is explicitly supplied by the user, it is authoritative for the `Project` link and supplements, rather than replaces, an existing `Paper` link. The three user-supplied project URLs above are therefore authoritative for the homepage project links.
- For the recent-work row, use this frozen content from the user-supplied project and its current repository README: title `Demystifying Agent Skills: Why They Work - Until They Don't`; description `Research code and artifacts for the paper Demystifying Agent Skills: Why They Work - Until They Don't.`; `Project` link → `https://zhiyuanjiang04.github.io/demystify-agent-skills`. Do not add authors, venue, date, or publication-status claims in this iteration.
- Preserve exact paper titles, author formatting, dates, affiliations, and external URLs unless one of the above sources or the user's explicit links provides an updated value.
- Use short descriptive prose only when it is a direct condensation of existing homepage text; do not introduce new achievements or unsupported claims.
- Keep research content before news and keep news before any low-priority navigation or footer content.

## Visual system

- Background: white.
- Main text: dark neutral gray; secondary text: muted gray.
- Links: one restrained academic blue, with hover underline or a subtle opacity change.
- Typography: retain the theme's existing readable sans-serif stack; do not introduce a novelty display font.
- Container: centered at exactly `width: min(1080px, 100%)`, with `box-sizing: border-box` and 24px left/right padding included inside the 1,080px outer box on a 1,280px desktop viewport.
- Profile: a fixed `240px` profile column paired with a flexible content column, using `grid-template-columns: 240px minmax(0, 1fr)` and a `56px` column gap on desktop widths `>= 768px`. At widths `<= 767px`, switch to one column and make the profile width 100%.
- Publication rows: subtle separators, consistent `156px` thumbnails on desktop, readable title sizing, and no heavy cards or gradients.
- Mobile publication rows: at widths `<= 767px` use `grid-template-columns: 88px minmax(0, 1fr)`, keep thumbnails at `88px` maximum width, and allow titles to wrap normally without horizontal overflow.
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
- At a 1,280px desktop viewport, the layout uses a 1,080px border-box container, a 240px profile column, a 56px gap, and a flexible content column with no unexpected large empty column.
- At widths `<= 767px`, the profile becomes full width, stacks above the research content, and publication rows use an 88px thumbnail column without horizontal overflow.
- The homepage contains no grades, score statistics, course-performance content, or unrelated personal sections.
- The profile identity, affiliations, visible link set, research statement, three existing publications, and one recent-work row match the repository source plus the user's three supplied project URLs.
- The homepage contains all three required research-news items in the specified order.
- Selected publications are visually more prominent than news and secondary navigation.
- Paragraph text remains left aligned; only the overall content block is centered by the layout.
- Existing publication detail pages and the `/cv/` route still resolve.
- Local preview is checked visually before any future push.
