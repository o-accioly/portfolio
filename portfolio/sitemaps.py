from __future__ import annotations

from datetime import date
from types import SimpleNamespace
from typing import Any

from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .catalog import PROJECTS, SITE_UPDATED

Item = tuple[str, tuple[str, ...]]


class PortfolioSitemap(Sitemap):
    """Every page, once per language, with hreflang alternates."""

    i18n = True
    alternates = True
    x_default = True
    changefreq = "monthly"

    def items(self) -> list[Item]:
        pages: list[Item] = [
            ("portfolio:home", ()),
            ("portfolio:about", ()),
            ("portfolio:projects", ()),
            ("portfolio:stack", ()),
        ]
        pages.extend(("portfolio:project", (project.slug,)) for project in PROJECTS)
        return pages

    def location(self, item: Item) -> str:
        name, args = item
        return reverse(name, args=args)

    def lastmod(self, item: Item) -> date:
        return SITE_UPDATED

    def priority(self, item: Item) -> float:
        return {"portfolio:home": 1.0, "portfolio:about": 0.9, "portfolio:projects": 0.9}.get(item[0], 0.7)

    def get_urls(self, page: int = 1, site: Any = None, protocol: str | None = None) -> list[dict[str, Any]]:
        # No `django.contrib.sites` here: the public origin comes from SITE_URL.
        scheme, _, domain = settings.SITE_URL.partition("://")
        return super().get_urls(page=page, site=SimpleNamespace(domain=domain, name=domain), protocol=scheme)
