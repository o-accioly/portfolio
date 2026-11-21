from django.test import SimpleTestCase
from django.urls import reverse
from django.utils import translation
from django.utils.html import escape

from portfolio.catalog import PROJECTS
from portfolio.content import get_content

LANGUAGES = ("pt-br", "en", "es")


class LanguageDetectionTests(SimpleTestCase):
    def test_root_redirects_to_the_browser_language(self) -> None:
        cases = {
            "pt-BR,pt;q=0.9,en;q=0.8": "/pt-br/",
            "pt-PT": "/pt-br/",
            "es-AR,es;q=0.9": "/es/",
            "en-GB": "/en/",
            "de-DE,de;q=0.9": "/en/",  # none of the three: English
            "": "/en/",
        }
        for header, expected in cases.items():
            with self.subTest(header=header):
                response = self.client.get("/", headers={"accept-language": header})
                self.assertRedirects(response, expected, fetch_redirect_response=False)

    def test_url_prefix_wins_over_the_browser(self) -> None:
        response = self.client.get("/es/", headers={"accept-language": "pt-BR"})
        self.assertContains(response, get_content("es")["hero"]["title"])
        self.assertContains(response, 'lang="es"')


class PageTests(SimpleTestCase):
    def test_home_renders_in_every_language(self) -> None:
        for language in LANGUAGES:
            with self.subTest(language=language), translation.override(language):
                response = self.client.get(reverse("portfolio:home"))
                self.assertEqual(response.status_code, 200)
                content = get_content(language)
                self.assertContains(response, escape(content["hero"]["title"]))
                for project in PROJECTS:
                    self.assertContains(response, reverse("portfolio:project", args=[project.slug]))

    def test_home_links_the_three_languages(self) -> None:
        response = self.client.get("/en/")
        for language in LANGUAGES:
            self.assertContains(response, f'hreflang="{language}"')
        self.assertContains(response, 'hreflang="x-default"')

    def test_every_project_renders_in_every_language(self) -> None:
        for language in LANGUAGES:
            for project in PROJECTS:
                with self.subTest(language=language, project=project.slug), translation.override(language):
                    response = self.client.get(reverse("portfolio:project", args=[project.slug]))
                    self.assertEqual(response.status_code, 200)
                    text = get_content(language)["projects"]["items"][project.slug]
                    self.assertContains(response, escape(text["tagline"]))
                    if project.url or project.repo:
                        self.assertContains(response, project.url or project.repo)

    def test_unknown_project_is_a_404(self) -> None:
        self.assertEqual(self.client.get("/en/projects/nope/").status_code, 404)

    def test_css_numbers_are_not_localised(self) -> None:
        """A decimal comma in an inline style would silently break the layout."""
        response = self.client.get("/pt-br/")
        html = response.content.decode()
        self.assertNotRegex(html, r"--(left|width|pan|nw|nh|year): -?\d+,\d")

    def test_sitemap_and_robots(self) -> None:
        sitemap = self.client.get("/sitemap.xml")
        self.assertEqual(sitemap.status_code, 200)
        self.assertContains(sitemap, "/pt-br/projects/diapasao/")
        self.assertEqual(self.client.get("/robots.txt").status_code, 200)
