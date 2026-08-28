import unittest
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABOUT = (ROOT / "_pages" / "about.md").read_text(encoding="utf-8")
NAVIGATION = (ROOT / "_data" / "navigation.yml").read_text(encoding="utf-8")
HOMEPAGE_INCLUDE = ROOT / "_includes" / "homepage.html"
PUBLICATIONS_INCLUDE = ROOT / "_includes" / "selected-publications.html"
HOMEPAGE_LAYOUT = ROOT / "_layouts" / "homepage.html"
PUBLICATIONS_PAGE = ROOT / "_pages" / "publications.html"
PROJECTS_PAGE = ROOT / "_pages" / "projects.md"
HOMEPAGE_STYLES = ROOT / "_sass" / "layout" / "_homepage.scss"


class HomepageContractTest(unittest.TestCase):
    def test_homepage_uses_dedicated_layout_and_include(self):
        self.assertIn("layout: homepage", ABOUT)
        self.assertIn('{% include homepage.html %}', ABOUT)
        self.assertTrue(HOMEPAGE_INCLUDE.exists())
        self.assertTrue(HOMEPAGE_LAYOUT.exists())

    def test_navigation_keeps_research_destinations(self):
        self.assertIn('title: "Publications"', NAVIGATION)
        self.assertNotIn('title: "Projects"', NAVIGATION)
        self.assertNotIn('title: "CV"', NAVIGATION)

    def test_projects_page_is_removed(self):
        self.assertFalse(PROJECTS_PAGE.exists())

    def test_publications_page_uses_the_homepage_publication_list(self):
        publications_page = PUBLICATIONS_PAGE.read_text(encoding="utf-8")
        publications = publications_page + PUBLICATIONS_INCLUDE.read_text(encoding="utf-8")
        self.assertIn("{% include selected-publications.html show_more=false heading=false directory=true %}", publications_page)
        self.assertNotIn("Selected Publications", publications_page)
        self.assertIn("Embodied AI", publications)
        self.assertIn("AI Agents", publications)
        self.assertIn("GUI Agents", publications)
        self.assertTrue(PUBLICATIONS_INCLUDE.exists())

    def test_publication_directory_panels_are_transparent_and_three_column(self):
        styles = HOMEPAGE_STYLES.read_text(encoding="utf-8")
        self.assertNotIn("grid-template-columns: 1fr;", styles)
        for value in (
            "background: rgba(220, 236, 255, 0.58);",
            "background: rgba(251, 232, 199, 0.58);",
            "background: rgba(223, 242, 229, 0.58);",
        ):
            self.assertIn(value, styles)

    def test_publications_use_short_author_metadata_and_first_author_order(self):
        publications = PUBLICATIONS_INCLUDE.read_text(encoding="utf-8")
        self.assertIn(
            '<p class="homepage-work-row__meta"><strong>Zhiyuan Jiang</strong>, '
            "Fangrui Huang, Hanwen Xing, ..., Yijiang Li · arXiv 2026</p>",
            publications,
        )
        self.assertNotIn("Research code and artifacts for the paper", publications)
        self.assertLess(
            publications.index("Zoom in, Click out"),
            publications.index("Wow, wo, val!"),
        )

    def test_homepage_contains_source_backed_research_links_and_work(self):
        homepage = ABOUT + HOMEPAGE_INCLUDE.read_text(encoding="utf-8") + PUBLICATIONS_INCLUDE.read_text(encoding="utf-8")
        for value in (
            "Selected Publications",
            "experimental_pipeline_combined.png",
            "https://arxiv.org/abs/2509.22642",
            "https://arxiv.org/abs/2512.05941",
            "https://arxiv.org/abs/2601.04137",
            "https://arxiv.org/abs/2608.14036",
            "https://arxiv.org/pdf/2608.14036",
            "https://arxiv.org/pdf/2601.04137",
            "https://arxiv.org/pdf/2512.05941",
            "https://arxiv.org/pdf/2509.22642",
            "https://github.com/wow-world-model/wow-world-model",
            "https://wow-world-model.github.io",
            "https://princeton-ai2-lab.github.io/ZoomClick",
            "https://github.com/Princeton-AI2-Lab/ZoomClick",
            "https://github.com/zhiyuanjiang04/demystify-agent-skills",
            "https://zhiyuanjiang04.github.io/demystify-agent-skills",
            "Demystifying Agent Skills: Why They Work - Until They Don't",
        ):
            self.assertIn(value, homepage)
        self.assertNotIn("Selected research", homepage)

    def test_homepage_profile_links_include_google_scholar(self):
        homepage = HOMEPAGE_INCLUDE.read_text(encoding="utf-8")
        self.assertIn(
            '<a href="https://scholar.google.com/citations?user=GPOFX7QAAAAJ&hl=en">Google Scholar</a>',
            homepage,
        )

    def test_cv_page_and_homepage_cv_link_are_removed(self):
        homepage = HOMEPAGE_INCLUDE.read_text(encoding="utf-8")
        self.assertFalse((ROOT / "_pages" / "cv.md").exists())
        self.assertNotIn("/cv/", homepage)

    def test_homepage_profile_uses_requested_role_labels(self):
        homepage = HOMEPAGE_INCLUDE.read_text(encoding="utf-8")
        for value in (
            'CS Undergrad at <a href="http://en.xjtu.edu.cn/">Xi\'an Jiaotong University</a>',
            'Research Intern at <a href="https://jiataogu.me/team/">UPenn GMLR</a>',
            'Prev Intern at <a href="https://ai.princeton.edu/">Princeton AI2 Lab</a>',
        ):
            self.assertIn(value, homepage)
        self.assertNotIn("Computer Science undergraduate", homepage)
        self.assertNotIn("Xi'an, China", homepage)

    def test_homepage_contains_only_approved_news(self):
        homepage = ABOUT + HOMEPAGE_INCLUDE.read_text(encoding="utf-8")
        plain_homepage = re.sub(r"<[^>]+>", "", homepage)
        plain_homepage = re.sub(r"\s+", " ", plain_homepage).lower()
        required_news = (
            "Aug 2026",
            "Demystifying Agent Skills released",
            "Jun 2026",
            "started research internship at UPenn GMLR",
            "Dec 2025",
            "ZoomClick released",
            "Sep 2025",
            "WoW released",
            "started research internship at Princeton AI2 Lab",
        )
        for value in required_news:
            self.assertIn(value.lower(), plain_homepage)

    def test_homepage_omits_non_research_profile_sections_and_stats(self):
        homepage = ABOUT + HOMEPAGE_INCLUDE.read_text(encoding="utf-8")
        for value in ("GPA", "TOEFL", "Top 5%", "## Education", "Ongoing Projects"):
            self.assertNotIn(value, homepage)


if __name__ == "__main__":
    unittest.main()
