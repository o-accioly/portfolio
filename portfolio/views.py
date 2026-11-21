"""The two pages of the site: the console (home) and one project."""

from __future__ import annotations

from datetime import date
from typing import Any

from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import get_language

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
from .shots import inside_shots, shots_for


def _skill_label(skill: str, content: dict[str, Any]) -> str:
    if skill in TRANSLATED_SKILLS:
        return content["skills"]["labels"][skill]
    return SKILLS[skill][0]


def _project_view(project: Project, content: dict[str, Any]) -> dict[str, Any]:
    shots = shots_for(project.slug)
    return {
        "slug": project.slug,
        "code": project.code,
        "name": project.name,
        "since": content["projects"]["since"].format(year=project.since) if project.since else "",
        "url": project.url,
        "repo": project.repo,
        "host": project.host,
        "href": reverse("portfolio:project", args=[project.slug]),
        "text": content["projects"]["items"][project.slug],
        "meters": _meters(project, content),
        "demo_screens": project.demo_screens,
        "screen": content["projects"]["items"][project.slug]["screen"],
        "shots": shots,
        # Covers: the first page of the site at two sizes, for thumbnails and the first paint.
        "phone": shots["phone"][0] if "phone" in shots else None,
        "laptop": shots[DEFAULT_DEVICE][0] if DEFAULT_DEVICE in shots else None,
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
                    "uses": " ".join(cell["slug"] for cell in cells if cell["on"]),
                    "summary": content["skills"]["used_in"].format(count=count, total=total),
                    "names": ", ".join(cell["name"] for cell in cells if cell["on"]),
                }
            )
        groups.append({"bus": bus, "label": content["skills"]["buses"][bus], "rows": rows})
    return groups


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


def home(request: HttpRequest) -> HttpResponse:
    content = get_content(get_language())
    projects = [_project_view(project, content) for project in PROJECTS]
    first = projects[0]
    context = {
        "t": content,
        "projects": projects,
        "current": first,
        "current_shot": first["laptop"],
        "current_device": DEFAULT_DEVICE,
        "devices": _device_options(content),
        "stage_data": _stage_data(projects, content),
        "matrix": _matrix(content),
        "timeline": _timeline(content, date.today()),
        "open_label": content["hero"]["open"].format(name=first["name"]),
    }
    return render(request, "portfolio/home.html", context)


def project_detail(request: HttpRequest, slug: str) -> HttpResponse:
    project = PROJECT_BY_SLUG.get(slug)
    if project is None:
        raise Http404(slug)
    content = get_content(get_language())
    projects = [_project_view(item, content) for item in PROJECTS]
    index = PROJECTS.index(project)
    current = projects[index]
    layers = [
        {
            "key": layer.key,
            "label": content["layers"][layer.key],
            "parts": [content["parts"].get(part, part) for part in layer.parts],
            "note": current["text"]["layers"].get(layer.key, ""),
        }
        for layer in project.layers
    ]
    context = {
        "t": content,
        "project": current,
        "current": current,
        "current_shot": current["laptop"],
        "current_device": DEFAULT_DEVICE,
        "devices": _device_options(content),
        "stage_data": _stage_data([current], content),
        "layers": layers,
        "stack": [_skill_label(skill, content) for skill in project.skills],
        "inside": [
            {**shot, "caption": current["text"]["inside"].get(shot["name"], "")} for shot in inside_shots(project.slug)
        ],
        "previous": projects[index - 1],
        "next": projects[(index + 1) % len(projects)],
        "page_title": f"{project.name} · {content['projects']['items'][project.slug]['kind']}",
        "page_description": content["projects"]["items"][project.slug]["tagline"],
    }
    return render(request, "portfolio/project_detail.html", context)


def not_found(request: HttpRequest, exception: Exception | None = None) -> HttpResponse:
    return render(request, "404.html", {"t": get_content(get_language())}, status=404)
