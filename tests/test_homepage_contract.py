import unittest
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABOUT = (ROOT / "_pages" / "about.md").read_text(encoding="utf-8")
NAVIGATION = (ROOT / "_data" / "navigation.yml").read_text(encoding="utf-8")
HOMEPAGE_INCLUDE = ROOT / "_includes" / "homepage.html"
HOMEPAGE_LAYOUT = ROOT / "_layouts" / "homepage.html"


class HomepageContractTest(unittest.TestCase):
    def test_homepage_uses_dedicated_layout_and_include(self):
        self.assertIn("layout: homepage", ABOUT)
        self.assertIn('{% include homepage.html %}', ABOUT)
        self.assertTrue(HOMEPAGE_INCLUDE.exists())
        self.assertTrue(HOMEPAGE_LAYOUT.exists())

    def test_navigation_keeps_research_destinations(self):
        self.assertIn('title: "Publications"', NAVIGATION)
        self.assertIn('title: "Projects"', NAVIGATION)
        self.assertIn('title: "CV"', NAVIGATION)

    def test_homepage_contains_source_backed_research_links_and_work(self):
        homepage = ABOUT + HOMEPAGE_INCLUDE.read_text(encoding="utf-8")
        for value in (
            "https://arxiv.org/abs/2509.22642",
            "https://arxiv.org/abs/2512.05941",
            "https://arxiv.org/abs/2601.04137",
            "https://wow-world-model.github.io",
            "https://princeton-ai2-lab.github.io/ZoomClick",
            "https://github.com/Princeton-AI2-Lab/ZoomClick",
            "https://zhiyuanjiang04.github.io/demystify-agent-skills",
            "Demystifying Agent Skills: Why They Work - Until They Don't",
            "Research code and artifacts for the paper",
        ):
            self.assertIn(value, homepage)

    def test_homepage_contains_only_approved_news(self):
        homepage = ABOUT + HOMEPAGE_INCLUDE.read_text(encoding="utf-8")
        plain_homepage = re.sub(r"<[^>]+>", "", homepage)
        plain_homepage = re.sub(r"\s+", " ", plain_homepage).lower()
        required_news = (
            "Dec 2025",
            "ZoomClick released",
            "Sep 2025",
            "WoW released",
            "started research internship at Princeton AI2 Lab",
        )
        for value in required_news:
            self.assertIn(value.lower(), plain_homepage)
        self.assertNotIn("began exchange semester at uc berkeley", plain_homepage)

    def test_homepage_omits_non_research_profile_sections_and_stats(self):
        homepage = ABOUT + HOMEPAGE_INCLUDE.read_text(encoding="utf-8")
        for value in ("GPA", "TOEFL", "Top 5%", "## Education", "Ongoing Projects"):
            self.assertNotIn(value, homepage)


if __name__ == "__main__":
    unittest.main()
