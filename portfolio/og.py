"""Share-card sources (development only).

`scripts/og_images.py` opens `/og/<key>/` at 1200 × 630 and saves a JPEG to `static/og/`.
Keys: `home-<language>` for the general pages, a project slug for each project, and `logo`.
Project cards carry only names, hosts and screens, so one image serves every language.
"""

from __future__ import annotations

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import translation

from .catalog import AUTHOR_NAME, BRAND_NAME, PROJECT_BY_SLUG, PROJECTS
from .content import get_content
from .views import _project_view

CARD_LANGUAGES = ("pt-br", "en", "es")


def card(request: HttpRequest, key: str) -> HttpResponse:
    if key == "logo":
        return render(request, "og_card.html", {"kind": "logo"})
    if key.startswith("home-"):
        language = key.removeprefix("home-")
        if language not in CARD_LANGUAGES:
            raise Http404(key)
        with translation.override(language):
            content = get_content(language)
            projects = [_project_view(project, content) for project in PROJECTS]
            return render(
                request,
                "og_card.html",
                {
                    "kind": "home",
                    "t": content,
                    "projects": [project for project in projects if project["phone"]][:4],
                    "author": AUTHOR_NAME,
                    "brand": BRAND_NAME,
                },
            )
    project = PROJECT_BY_SLUG.get(key)
    if project is None:
        raise Http404(key)
    with translation.override("en"):
        view = _project_view(project, get_content("en"))
        return render(
            request,
            "og_card.html",
            {"kind": "project", "project": view, "author": AUTHOR_NAME, "brand": BRAND_NAME},
        )
