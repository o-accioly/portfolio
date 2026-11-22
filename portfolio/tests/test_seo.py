"""Search and answer engines: every page names the person, the company and itself."""

import json
import re

from django.conf import settings
from django.test import SimpleTestCase
from django.urls import reverse
from django.utils import translation
from django.utils.html import escape

from portfolio.catalog import AUTHOR_ALIAS, AUTHOR_NAME, BRAND_NAME, GITHUB_URL, LINKEDIN_URL, PROJECTS
from portfolio.content import get_content

LANGUAGES = ("pt-br", "en", "es")
PAGES = ("portfolio:home", "portfolio:about", "portfolio:projects", "portfolio:stack")
LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def graph(html: str) -> list[dict]:
    blocks = LD.findall(html)
    assert len(blocks) == 1, f"expected one JSON-LD block, found {len(blocks)}"
    return json.loads(blocks[0])["@graph"]


def node(nodes: list[dict], kind: str) -> dict:
    return next(item for item in nodes if item["@type"] == kind)


class PageTests(SimpleTestCase):
    def test_every_page_renders_in_every_language(self) -> None:
        for language in LANGUAGES:
            for name in PAGES:
                with self.subTest(language=language, page=name), translation.override(language):
                    response = self.client.get(reverse(name))
                    self.assertEqual(response.status_code, 200)
                    self.assertContains(response, f'lang="{language}"')

    def test_each_page_has_its_own_title_and_one_h1(self) -> None:
        titles = set()
        for language in LANGUAGES:
            with translation.override(language):
                urls = [reverse(name) for name in PAGES] + [reverse("portfolio:project", args=["diapasao"])]
            for url in urls:
                with self.subTest(url=url):
                    html = self.client.get(url).content.decode()
                    title = re.search(r"<title>(.*?)</title>", html, re.S).group(1)
                    self.assertIn(AUTHOR_NAME, title)
                    titles.add(title)
                    self.assertEqual(len(re.findall(r"<h1[\s>]", html)), 1)
        self.assertEqual(len(titles), 3 * (len(PAGES) + 1))

    def test_home_heading_names_the_author(self) -> None:
        html = self.client.get("/pt-br/").content.decode()
        h1 = re.search(r"<h1.*?</h1>", html, re.S).group(0)
        self.assertIn(AUTHOR_NAME, h1)


class MetadataTests(SimpleTestCase):
    def test_person_and_company_are_described_on_every_page(self) -> None:
        for url in ("/en/", "/pt-br/about/", "/es/projects/", "/en/stack/", "/pt-br/projects/zipzap/"):
            with self.subTest(url=url):
                nodes = graph(self.client.get(url).content.decode())
                person = node(nodes, "Person")
                self.assertEqual(person["name"], AUTHOR_NAME)
                self.assertIn(AUTHOR_ALIAS, person["alternateName"])
                self.assertEqual(set(person["sameAs"]), {LINKEDIN_URL, GITHUB_URL})
                self.assertEqual(node(nodes, "Organization")["name"], BRAND_NAME)
                self.assertEqual(node(nodes, "WebSite")["publisher"]["@id"], person["@id"])

    def test_project_page_describes_the_work_and_its_path(self) -> None:
        nodes = graph(self.client.get("/en/projects/diapasao/").content.decode())
        work = node(nodes, "CreativeWork")
        self.assertEqual(work["name"], "Diapasão")
        self.assertEqual(work["url"], "https://diapasao.com/")
        crumbs = node(nodes, "BreadcrumbList")["itemListElement"]
        self.assertEqual([item["position"] for item in crumbs], [1, 2, 3])
        self.assertTrue(crumbs[-1]["item"].endswith("/en/projects/diapasao/"))

    def test_about_page_is_a_profile_with_questions(self) -> None:
        nodes = graph(self.client.get("/pt-br/about/").content.decode())
        self.assertEqual(node(nodes, "ProfilePage")["mainEntity"]["@id"], node(nodes, "Person")["@id"])
        faq = node(nodes, "FAQPage")["mainEntity"]
        self.assertEqual(len(faq), len(get_content("pt-br")["about"]["faq"]))

    def test_json_ld_cannot_close_its_script(self) -> None:
        html = self.client.get("/pt-br/about/").content.decode()
        self.assertNotIn("</", LD.search(html).group(1))

    def test_canonical_hreflang_and_x_default(self) -> None:
        html = self.client.get("/es/projects/sabo/").content.decode()
        self.assertIn(f'<link rel="canonical" href="{settings.SITE_URL}/es/projects/sabo/">', html)
        for language in LANGUAGES:
            self.assertIn(f'hreflang="{language}" href="{settings.SITE_URL}/{language}/projects/sabo/"', html)
        self.assertIn(f'hreflang="x-default" href="{settings.SITE_URL}/projects/sabo/"', html)
        # The x-default address sends the visitor to their language.
        response = self.client.get("/projects/sabo/", headers={"accept-language": "es"})
        self.assertRedirects(response, "/es/projects/sabo/", fetch_redirect_response=False)

    def test_open_graph_has_a_locale_per_language(self) -> None:
        html = self.client.get("/pt-br/").content.decode()
        self.assertIn('<meta property="og:locale" content="pt_BR">', html)
        self.assertIn('<meta property="og:locale:alternate" content="en_US">', html)
        self.assertIn('name="twitter:card" content="summary_large_image"', html)


class MachineFileTests(SimpleTestCase):
    def test_robots_welcomes_search_and_ai_crawlers(self) -> None:
        body = self.client.get("/robots.txt").content.decode()
        for bot in ("GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended"):
            self.assertIn(f"User-agent: {bot}\nAllow: /", body)
        self.assertNotIn("Disallow", body)
        self.assertIn(f"Sitemap: {settings.SITE_URL}/sitemap.xml", body)

    def test_sitemap_lists_every_page_in_every_language(self) -> None:
        body = self.client.get("/sitemap.xml").content.decode()
        for language in LANGUAGES:
            for path in ("", "about/", "projects/", "stack/", "projects/diapasao/"):
                self.assertIn(f"<loc>{settings.SITE_URL}/{language}/{path}</loc>", body)
        self.assertIn("<lastmod>", body)

    def test_llms_txt_names_the_author_and_every_project(self) -> None:
        for url in ("/llms.txt", "/llms-full.txt"):
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response["Content-Type"], "text/plain; charset=utf-8")
                body = response.content.decode()
                self.assertTrue(body.startswith(f"# {AUTHOR_NAME} ({AUTHOR_ALIAS})"))
                for project in PROJECTS:
                    self.assertIn(f"[{project.name}]({settings.SITE_URL}/en/projects/{project.slug}/)", body)
                self.assertNotIn("&amp;", body)
        full = self.client.get("/llms-full.txt").content.decode()
        self.assertIn(get_content("en")["projects"]["items"]["zipzap"]["problem"], full)

    def test_project_pages_show_every_captured_screen(self) -> None:
        html = self.client.get("/pt-br/projects/kayaeducation/").content.decode()
        for caption in get_content("pt-br")["projects"]["pages"]["kayaeducation"].values():
            self.assertIn(escape(caption), html)
