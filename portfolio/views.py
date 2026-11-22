"""The pages of the site: the console (home), the projects, one project, about and the stack.

Plus the plain-text files machines read first: `robots.txt`, `llms.txt` and `llms-full.txt`.
"""

from __future__ import annotations

from datetime import date
from typing import Any

from django.conf import settings
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import translation
from django.utils.translation import get_language

from . import seo
from .catalog import (
    BUSES,
    DEFAULT_DEVICE,
    DEVICES,
    PROJECT_BY_SLUG,
    PROJECTS,
    SKILLS,
    TIMELINE_START,
    TRACKS,
    TRANSLATED_SKILLS,
    Project,
)
from .content import get_content
from .shots import Shot, inside_shots, shots_for

# Tools used to write the code, not features of the product: they never make a product count
# as "AI in production".
BUILD_TOOLS = frozenset({"claude_code", "codex"})

# Devices tried, in order, for the large half of a screen pair.
LARGE_DEVICES = ("laptop", "desktop", "ultrawide", "tablet")


def _language() -> str:
    return get_language() or settings.LANGUAGE_CODE


def _skill_label(skill: str, content: dict[str, Any]) -> str:
    if skill in TRANSLATED_SKILLS:
        return content["skills"]["labels"][skill]
    return SKILLS[skill][0]


def _project_view(project: Project, content: dict[str, Any]) -> dict[str, Any]:
    shots = shots_for(project.slug)
    text = content["projects"]["items"][project.slug]
    large = next((shots[key][0] for key in LARGE_DEVICES if key in shots), None)
    return {
        "slug": project.slug,
        "code": project.code,
        "name": project.name,
        "since": content["projects"]["since"].format(year=project.since) if project.since else "",
        "year": project.since,
        "url": project.url,
        "repo": project.repo,
        "host": project.host,
        "href": reverse("portfolio:project", args=[project.slug]),
        "text": text,
        "highlights": content["projects"]["highlights"][project.slug],
        "stack": [_skill_label(skill, content) for skill in project.skills],
        "meters": _meters(project, content),
        "demo_screens": project.demo_screens,
        "screen": text["screen"],
        "shots": shots,
        "screen_count": len({shot.page for pages in shots.values() for shot in pages}),
        # Covers: the first page of the site at two sizes, for thumbnails and the first paint.
        "phone": shots["phone"][0] if "phone" in shots else None,
        "laptop": shots[DEFAULT_DEVICE][0] if DEFAULT_DEVICE in shots else None,
        "large": large,
    }


METER_CELLS = 5


def _meters(project: Project, content: dict[str, Any]) -> list[dict[str, Any]]:
    """One LED ladder per bus: how many of the project's technologies sit on it (capped)."""
    meters = []
    for bus in BUSES:
        count = sum(1 for skill in project.skills if SKILLS[skill][1] == bus)
        lit = min(count, METER_CELLS)
        meters.append(
            {
                "bus": bus,
                "label": content["skills"]["buses"][bus],
                "count": count,
                # Top cell first, the way a ladder is drawn.
                "cells": [index < lit for index in reversed(range(METER_CELLS))],
            }
        )
    return meters


def _stage_data(projects: list[dict[str, Any]], content: dict[str, Any]) -> dict[str, Any]:
    """What the monitor script needs: every shot of every project, and the device sizes."""
    return {
        "devices": {device.key: {"w": device.width, "h": device.height} for device in DEVICES},
        "order": [device.key for device in DEVICES],
        "projects": {
            project["slug"]: {
                "name": project["name"],
                "href": project["href"],
                "kind": project["text"]["kind"],
                "host": project["host"] if project["url"] else content["hero"]["no_page"],
                "open": content["hero"]["open"].format(name=project["name"]),
                "screen": project["screen"],
                "shots": {
                    key: {"top": pages[0].top, "pages": [page.as_json() for page in pages]}
                    for key, pages in project["shots"].items()
                },
            }
            for project in projects
        },
    }


def _matrix(content: dict[str, Any]) -> list[dict[str, Any]]:
    total = len(PROJECTS)
    groups = []
    for bus in BUSES:
        rows = []
        for skill, (_, skill_bus) in SKILLS.items():
            if skill_bus != bus:
                continue
            cells = [
                {"slug": project.slug, "name": project.name, "on": skill in project.skills} for project in PROJECTS
            ]
            count = sum(cell["on"] for cell in cells)
            rows.append(
                {
                    "id": skill,
                    "label": _skill_label(skill, content),
                    "cells": cells,
                    "count": count,
                    "uses": " ".join(cell["slug"] for cell in cells if cell["on"]),
                    "summary": content["skills"]["used_in"].format(count=count, total=total),
                    "names": ", ".join(cell["name"] for cell in cells if cell["on"]),
                }
            )
        groups.append({"bus": bus, "label": content["skills"]["buses"][bus], "rows": rows})
    return groups


def _services(content: dict[str, Any], projects: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """One row per bus: what the author does there and the products where it already runs."""
    by_slug = {project["slug"]: project for project in projects}
    rows = []
    for bus in BUSES:
        weight = {
            project.slug: sum(1 for skill in project.skills if SKILLS[skill][1] == bus and skill not in BUILD_TOOLS)
            for project in PROJECTS
        }
        ranked = sorted((slug for slug, count in weight.items() if count), key=lambda slug: -weight[slug])
        rows.append(
            {
                "bus": bus,
                "label": content["skills"]["buses"][bus],
                "title": content["services"]["items"][bus]["title"],
                "body": content["services"]["items"][bus]["body"],
                "why": content["stack"]["why"][bus],
                "skills": [_skill_label(skill, content) for skill, (_, b) in SKILLS.items() if b == bus],
                "projects": [by_slug[slug] for slug in ranked[:4]],
            }
        )
    return rows


def _timeline(content: dict[str, Any], today: date) -> dict[str, Any]:
    span = (today - TIMELINE_START).days
    lanes = []
    for track in TRACKS:
        end = track.end or today
        lanes.append(
            {
                "key": track.key,
                "name": track.name,
                "role": content["journey"]["tracks"][track.key],
                "bus": track.bus,
                # CSS values are built here: a template would localise the decimal mark.
                "left": f"{(track.start - TIMELINE_START).days / span * 100:.3f}%",
                "width": f"{(end - track.start).days / span * 100:.3f}%",
                "from": track.start.year,
                "to": track.end.year if track.end else content["journey"]["now"],
                "running": track.end is None,
            }
        )
    years = [
        {"year": year, "left": f"{(date(year, 1, 1) - TIMELINE_START).days / span * 100:.3f}%"}
        for year in range(TIMELINE_START.year, today.year + 1)
    ]
    return {"lanes": lanes, "years": years, "year_step": f"{365.25 / span * 100:.3f}%"}


def _device_options(content: dict[str, Any]) -> list[dict[str, Any]]:
    widest = max(device.width for device in DEVICES)
    tallest = max(device.height for device in DEVICES)
    return [
        {
            "key": device.key,
            "label": content["devices"][device.key],
            "width": device.width,
            "height": device.height,
            # Share of the nest diagram, which is drawn at true relative scale.
            "nest_w": f"{device.width / widest * 100:.2f}%",
            "nest_h": f"{device.height / tallest * 100:.2f}%",
        }
        for device in DEVICES
    ]


def _screen_pairs(project: Project, content: dict[str, Any]) -> list[dict[str, Any]]:
    """Every captured page of a product, each as a large screen and, when captured, a phone."""
    shots = shots_for(project.slug)
    captions = content["projects"]["pages"].get(project.slug, {})
    pages: dict[str, dict[str, Shot]] = {}
    for device, device_shots in shots.items():
        for shot in device_shots:
            pages.setdefault(shot.page, {})[device] = shot
    pairs = []
    for name, by_device in pages.items():
        large_key = next((key for key in LARGE_DEVICES if key in by_device), None)
        pairs.append(
            {
                "name": name,
                "caption": captions.get(name, name.replace("-", " ").capitalize()),
                "large": by_device.get(large_key) if large_key else None,
                "large_device": large_key,
                "phone": by_device.get("phone"),
            }
        )
    return pairs


def _common(request: HttpRequest, content: dict[str, Any]) -> dict[str, Any]:
    language = _language()
    return {
        "t": content,
        "about_url": reverse("portfolio:about"),
        "entities": seo.entities(content, language, reverse("portfolio:about")),
        "og_locale": content["meta"]["og_locale"],
    }


def _render(request: HttpRequest, template: str, context: dict[str, Any], nodes: list[dict[str, Any]]) -> HttpResponse:
    context["ld"] = seo.graph(context.pop("entities"), nodes)
    return render(request, template, context)


# ---- pages ------------------------------------------------------------------------------


def home(request: HttpRequest) -> HttpResponse:
    content = get_content(get_language())
    language = _language()
    projects = [_project_view(project, content) for project in PROJECTS]
    first = projects[0]
    image = seo.og_image(f"home-{language}", language)
    context = {
        **_common(request, content),
        "projects": projects,
        "current": first,
        "current_shot": first["laptop"],
        "current_device": DEFAULT_DEVICE,
        "devices": _device_options(content),
        "stage_data": _stage_data(projects, content),
        "services": _services(content, projects),
        "open_label": content["hero"]["open"].format(name=first["name"]),
        "og_image": image,
    }
    url = request.path
    node = seo.page("WebPage", url, content["meta"]["title"], content["meta"]["description"], language, image)
    node["mainEntity"] = {
        "@type": "ItemList",
        "itemListElement": [
            {"@type": "ListItem", "position": index, "url": seo.absolute(project["href"]), "name": project["name"]}
            for index, project in enumerate(projects, start=1)
        ],
    }
    return _render(request, "portfolio/home.html", context, [node])


def projects_index(request: HttpRequest) -> HttpResponse:
    content = get_content(get_language())
    language = _language()
    projects = [_project_view(project, content) for project in PROJECTS]
    image = seo.og_image(f"home-{language}", language)
    title, description = content["meta"]["projects_title"], content["meta"]["projects_description"]
    context = {
        **_common(request, content),
        "projects": projects,
        "page_title": title,
        "page_description": description,
        "page_lead": content["projects"]["page_lead"].format(count=len(projects)),
        "og_image": image,
    }
    url = request.path
    nodes = [
        seo.page(
            "CollectionPage",
            url,
            title,
            description,
            language,
            image,
            mainEntity={
                "@type": "ItemList",
                "numberOfItems": len(projects),
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": index,
                        "url": seo.absolute(project["href"]),
                        "name": f"{project['name']}: {project['text']['kind']}",
                    }
                    for index, project in enumerate(projects, start=1)
                ],
            },
            breadcrumb={"@id": f"{seo.absolute(url)}#breadcrumb"},
        ),
        seo.breadcrumbs(url, [(content["nav"]["home"], reverse("portfolio:home")), (content["nav"]["projects"], url)]),
    ]
    return _render(request, "portfolio/projects.html", context, nodes)


def project_detail(request: HttpRequest, slug: str) -> HttpResponse:
    project = PROJECT_BY_SLUG.get(slug)
    if project is None:
        raise Http404(slug)
    content = get_content(get_language())
    language = _language()
    projects = [_project_view(item, content) for item in PROJECTS]
    index = PROJECTS.index(project)
    current = projects[index]
    text = current["text"]
    layers = [
        {
            "key": layer.key,
            "label": content["layers"][layer.key],
            "parts": [content["parts"].get(part, part) for part in layer.parts],
            "note": text["layers"].get(layer.key, ""),
        }
        for layer in project.layers
    ]
    title = content["meta"]["project_title"].format(name=project.name, kind=text["kind"])
    image = seo.og_image(project.slug, language)
    context = {
        **_common(request, content),
        "project": current,
        "current": current,
        "current_shot": current["laptop"],
        "current_device": DEFAULT_DEVICE,
        "devices": _device_options(content),
        "stage_data": _stage_data([current], content),
        "layers": layers,
        "stack": current["stack"],
        "pairs": _screen_pairs(project, content),
        "inside": [{**shot, "caption": text["inside"].get(shot["name"], "")} for shot in inside_shots(project.slug)],
        "previous": projects[index - 1],
        "next": projects[(index + 1) % len(projects)],
        "page_title": title,
        "page_description": text["tagline"],
        "og_image": image,
        "og_type": "article",
    }
    url = request.path
    nodes = [
        seo.page(
            "WebPage",
            url,
            title,
            text["tagline"],
            language,
            image,
            mainEntity={"@id": f"{seo.absolute(url)}#work"},
            breadcrumb={"@id": f"{seo.absolute(url)}#breadcrumb"},
        ),
        seo.project_work(project, text, url, current["stack"], image),
        seo.breadcrumbs(
            url,
            [
                (content["nav"]["home"], reverse("portfolio:home")),
                (content["nav"]["projects"], reverse("portfolio:projects")),
                (project.name, url),
            ],
        ),
    ]
    return _render(request, "portfolio/project_detail.html", context, nodes)


def about(request: HttpRequest) -> HttpResponse:
    content = get_content(get_language())
    language = _language()
    image = seo.og_image(f"home-{language}", language)
    title, description = content["meta"]["about_title"], content["meta"]["about_description"]
    context = {
        **_common(request, content),
        "timeline": _timeline(content, date.today()),
        "page_title": title,
        "page_description": description,
        "og_image": image,
        "og_type": "profile",
    }
    url = request.path
    nodes = [
        seo.page(
            "ProfilePage",
            url,
            title,
            description,
            language,
            image,
            mainEntity={"@id": f"{settings.SITE_URL}/#person"},
            breadcrumb={"@id": f"{seo.absolute(url)}#breadcrumb"},
        ),
        seo.faq(url, content["about"]["faq"]),
        seo.breadcrumbs(url, [(content["nav"]["home"], reverse("portfolio:home")), (content["nav"]["about"], url)]),
    ]
    return _render(request, "portfolio/about.html", context, nodes)


def stack(request: HttpRequest) -> HttpResponse:
    content = get_content(get_language())
    language = _language()
    projects = [_project_view(project, content) for project in PROJECTS]
    image = seo.og_image(f"home-{language}", language)
    title, description = content["meta"]["stack_title"], content["meta"]["stack_description"]
    context = {
        **_common(request, content),
        "projects": projects,
        "matrix": _matrix(content),
        "services": _services(content, projects),
        "skill_count": len(SKILLS),
        "page_title": title,
        "page_description": description,
        "og_image": image,
    }
    url = request.path
    nodes = [
        seo.page(
            "WebPage",
            url,
            title,
            description,
            language,
            image,
            breadcrumb={"@id": f"{seo.absolute(url)}#breadcrumb"},
        ),
        seo.breadcrumbs(url, [(content["nav"]["home"], reverse("portfolio:home")), (content["nav"]["stack"], url)]),
    ]
    return _render(request, "portfolio/stack.html", context, nodes)


def not_found(request: HttpRequest, exception: Exception | None = None) -> HttpResponse:
    return render(request, "404.html", {"t": get_content(get_language())}, status=404)


# ---- machine-readable files ------------------------------------------------------------

AI_CRAWLERS = (
    "GPTBot",
    "OAI-SearchBot",
    "ChatGPT-User",
    "ClaudeBot",
    "Claude-User",
    "Claude-SearchBot",
    "anthropic-ai",
    "PerplexityBot",
    "Perplexity-User",
    "Google-Extended",
    "Applebot-Extended",
    "Amazonbot",
    "meta-externalagent",
    "DuckAssistBot",
    "MistralAI-User",
    "cohere-ai",
    "CCBot",
)


def robots(request: HttpRequest) -> HttpResponse:
    body = render_to_string("robots.txt", {"site_url": settings.SITE_URL, "ai_crawlers": AI_CRAWLERS})
    return HttpResponse(body, content_type="text/plain; charset=utf-8")


def _llms_context(full: bool) -> dict[str, Any]:
    """English copy for answer engines, with links to every language."""
    with translation.override("en"):
        content = get_content("en")
        projects = [_project_view(project, content) for project in PROJECTS]
        urls = {
            "home": reverse("portfolio:home"),
            "about": reverse("portfolio:about"),
            "projects": reverse("portfolio:projects"),
            "stack": reverse("portfolio:stack"),
        }
        services = _services(content, projects)
    by_language = []
    for code, name in settings.LANGUAGES:
        with translation.override(code):
            by_language.append(
                {
                    "name": name,
                    "home": reverse("portfolio:home"),
                    "about": reverse("portfolio:about"),
                    "projects": reverse("portfolio:projects"),
                }
            )
    return {
        "t": content,
        "projects": projects,
        "services": services,
        "urls": urls,
        "by_language": by_language,
        "site_url": settings.SITE_URL,
        "full": full,
        "timeline": _timeline(content, date.today()),
    }


def llms_txt(request: HttpRequest) -> HttpResponse:
    body = render_to_string("llms.txt", _llms_context(full=False))
    return HttpResponse(body, content_type="text/plain; charset=utf-8")


def llms_full_txt(request: HttpRequest) -> HttpResponse:
    body = render_to_string("llms.txt", _llms_context(full=True))
    return HttpResponse(body, content_type="text/plain; charset=utf-8")
