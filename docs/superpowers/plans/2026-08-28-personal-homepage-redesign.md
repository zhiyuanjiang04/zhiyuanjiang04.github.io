# Personal Academic Homepage Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the current academic-pages homepage with a restrained, research-first personal homepage that combines the selected B direction, a white Nerfies-like visual language, and the supplied project links, while leaving inner pages unchanged.

**Architecture:** Use a homepage-only Jekyll layout and include so the existing `default`, sidebar, publication, CV, and archive layouts remain untouched. The homepage will contain a compact profile column and a research column with a statement, three research-news items, and four image-led work rows; all new styles will be scoped under `.homepage-main`.

**Tech Stack:** Jekyll/Liquid, existing Academic Pages Sass pipeline, existing repository images, Python standard-library contract tests, Bundler/GitHub Pages for local build and preview.

---

### Task 1: Add a failing homepage contract test

**Files:**
- Create: `tests/test_homepage_contract.py`

- [ ] **Step 1: Write the failing contract test**

  Add Python `unittest` checks that read the repository source and assert the frozen homepage contract: the page uses the homepage include/layout marker; the three navigation labels remain `Publications`, `Projects`, and `CV`; the homepage contains the three existing paper URLs, the three user-supplied project URLs, and the exact recent-work title/description; the homepage contains the three required news dates/items; and the homepage does not contain GPA, TOEFL, ranking, education, Berkeley-exchange, or ongoing-project content.

- [ ] **Step 2: Run the test to verify it fails before implementation**

  Run `python3 -m unittest discover -s tests -v`.

  Expected: FAIL because the current about page still contains the old sidebar-oriented content, education statistics, Berkeley exchange news, no recent-work row, and no ZoomClick project URL.

- [ ] **Step 3: Commit the red test**

  Run `git add tests/test_homepage_contract.py && git commit -m "test: define personal homepage content contract"`.

### Task 2: Create the isolated homepage structure

**Files:**
- Modify: `_pages/about.md`
- Create: `_includes/homepage.html`
- Create: `_layouts/homepage.html`

- [ ] **Step 1: Replace the about page with the homepage entry point**

  Set `_pages/about.md` to use `layout: homepage`, `permalink: /`, `title: ""`, `author_profile: false`, and the existing redirect paths. Include `homepage.html` as the sole page content so the old inline styles, education table, ongoing-project list, and Berkeley exchange item cannot leak into the new homepage.

- [ ] **Step 2: Add the homepage layout wrapper**

  Create `_layouts/homepage.html` on top of `default`, retaining the site masthead/footer/scripts while rendering a dedicated `<div id="main" class="homepage-main">` and an article/page-content wrapper without the global sidebar.

- [ ] **Step 3: Add source-backed homepage markup**

  Create `_includes/homepage.html` with:

  - a profile block using the configured portrait, name, XJTU/Princeton roles, location/affiliation, and exactly `Email`, `GitHub`, and `CV` links;
  - a short research statement condensed only from the current about page;
  - exactly the three ordered research-news entries from the approved spec;
  - four compact work rows, with the supplied recent work plus `Wow, wo, val!`, ZoomClick, and WoW. Use existing local teaser assets for the three papers; because no recent-work teaser is present in the repository, use a restrained text-only `Agent Skills` thumbnail block for that row rather than a misleading paper image or a new unsupported visual asset;
  - exact paper/project/code URLs from the design spec, keeping `Paper` and `Project` as separate actions;
  - a restrained `View all publications` link after the work rows.

  Keep paragraph copy left aligned; center only the outer layout through CSS. Use `relative_url` for local assets and internal routes.

- [ ] **Step 4: Run the contract test and verify the content assertions pass**

  Run `python3 -m unittest discover -s tests -v`.

  Expected: all content assertions pass. The contract intentionally checks source files rather than browser styling, so no styling assertion should remain for Task 3. Do not modify unrelated inner pages.

- [ ] **Step 5: Commit the homepage structure**

  Run `git add _pages/about.md _includes/homepage.html _layouts/homepage.html && git commit -m "feat: add research-first homepage structure"`.

### Task 3: Implement the scoped visual system

**Files:**
- Modify: `assets/css/main.scss`
- Create: `_sass/layout/_homepage.scss`

- [ ] **Step 1: Add the homepage Sass import**

  Import `layout/homepage` after the existing page/layout imports so the homepage rules are available without changing the site-wide theme variables.

- [ ] **Step 2: Implement desktop layout rules**

  Scope all selectors under `.homepage-main`. Explicitly reset the inherited theme selectors on `.homepage-main`, `.homepage-page`, and `.homepage-page .page__content` so the global `#main` container padding, `.page` Susy span/prefix/suffix widths, and default page-content heading borders cannot distort the homepage geometry. Use a white background, dark neutral text, one academic-blue link color, and no gradients or heavy cards. Set the centered outer container to `width: min(1080px, 100%)`, `box-sizing: border-box`, and 24px horizontal padding. Use a `240px minmax(0, 1fr)` profile/research grid with a 56px gap at widths `>= 768px`; keep headings concise and bold, and keep body paragraphs left aligned.

- [ ] **Step 3: Implement research-row and responsive rules**

  Render work rows with subtle separators and `156px` desktop thumbnails, including a compact text-only thumbnail for the recent work, readable titles, compact metadata/action links, and no horizontal overflow. At widths `<= 767px`, switch the page to one column, make the profile full width, and use an `88px minmax(0, 1fr)` thumbnail/text grid. Preserve normal title wrapping and use `max-width: 100%` for all images.

- [ ] **Step 4: Run the contract test and static checks**

  Run `python3 -m unittest discover -s tests -v` and `git diff --check`.

  Expected: all contract tests pass and Git reports no whitespace errors.

- [ ] **Step 5: Commit the scoped visual system**

  Run `git add assets/css/main.scss _sass/layout/_homepage.scss && git commit -m "style: add restrained research homepage layout"`.

### Task 4: Build and visually verify the homepage locally

**Files:**
- Modify only if required by build output: the files from Tasks 2–3.

- [ ] **Step 1: Install or validate the existing Jekyll dependencies**

  Run `bundle config set --local path vendor/bundle` and `bundle install` if `bundle check` reports missing dependencies. Do not add a new runtime dependency to the site.

- [ ] **Step 2: Build the site**

  Run `bundle exec jekyll build --trace`.

  Expected: the site builds successfully and `_site/index.html` contains the homepage profile, links, work rows, and news without the omitted education/side-content strings.

- [ ] **Step 3: Start a local preview server**

  Run `bundle exec jekyll serve --host 127.0.0.1 --port 4000 --no-watch` from the worktree and keep the process alive for browser review. Do not push any branch.

- [ ] **Step 4: Inspect the rendered page at desktop and mobile widths**

  Open `http://127.0.0.1:4000/` in the in-app browser, capture a desktop screenshot, then set a narrow mobile viewport and capture a second screenshot. Check the profile/research columns, white canvas, row thumbnail sizes, link visibility, title wrapping, and absence of horizontal scrolling. If a layout issue appears, patch only the homepage files, rebuild, and re-check.

- [ ] **Step 5: Final verification**

  Run `python3 -m unittest discover -s tests -v`, `git diff --check`, and `bundle exec jekyll build --trace` once more. Report the local preview URL and worktree path; leave all changes local and unpushed.
