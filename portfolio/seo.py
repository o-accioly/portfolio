"""Search and answer-engine metadata: JSON-LD graphs and share images.

Every page carries one `@graph` that names the same three entities by `@id` (the person, the
company and the site), so search engines and language models tie "Gabriel Accioly",
"oAccioly" and "oAccioly Faz" to one person and one company across pages and languages.
"""

from __future__ import annotations

from typing import Any

from django.conf import settings
from django.templatetags.static import static

from .catalog import (
    AUTHOR_ALIAS,
    AUTHOR_COUNTRY,
    AUTHOR_LOCALITY,
    AUTHOR_NAME,
    AUTHOR_SCHOOL,
    BRAND_NAME,
    COMPANY_CITY,
    COMPANY_CNPJ,
    COMPANY_LEGAL_NAME,
    GITHUB_URL,
    LINKEDIN_URL,
    SKILLS,
    Project,
)

OG_DIR = settings.BASE_DIR / "static" / "og"
LANGUAGE_TAGS = {"pt-br": "pt-BR", "en": "en", "es": "es"}


def absolute(path: str) -> str:
    return f"{settings.SITE_URL}{path}"


def og_image(key: str, language: str) -> str:
    """Absolute URL of the share image for a page; the home card of the language as fallback."""
    for name in (key, f"home-{language}", "home-en"):
        if (OG_DIR / f"{name}.jpg").exists():
            return absolute(static(f"og/{name}.jpg"))
    return ""


def _ids() -> dict[str, str]:
    root = settings.SITE_URL
    return {"person": f"{root}/#person", "org": f"{root}/#organization", "site": f"{root}/#website"}


def entities(content: dict[str, Any], language: str, about_url: str) -> list[dict[str, Any]]:
    """The person, the company and the site: the same nodes on every page."""
    ids = _ids()
    tag = LANGUAGE_TAGS.get(language, language)
    city, _, state = COMPANY_CITY.partition(", ")
    return [
        {
            "@type": "Person",
            "@id": ids["person"],
            "name": AUTHOR_NAME,
            "givenName": AUTHOR_NAME.split()[0],
            "familyName": AUTHOR_NAME.split()[-1],
            "alternateName": [AUTHOR_ALIAS, f"{AUTHOR_NAME} ({AUTHOR_ALIAS})"],
            "url": absolute(about_url),
            "jobTitle": content["meta"]["job_title"],
            "description": content["meta"]["description"],
            "address": {"@type": "PostalAddress", "addressLocality": AUTHOR_LOCALITY, "addressCountry": AUTHOR_COUNTRY},
            "alumniOf": {"@type": "CollegeOrUniversity", "name": AUTHOR_SCHOOL},
            "worksFor": {"@id": ids["org"]},
            "knowsAbout": [content["skills"]["labels"].get(key, label) for key, (label, _) in SKILLS.items()],
            "sameAs": [LINKEDIN_URL, GITHUB_URL],
        },
        {
            "@type": "Organization",
            "@id": ids["org"],
            "name": BRAND_NAME,
            "legalName": COMPANY_LEGAL_NAME,
            "alternateName": [AUTHOR_ALIAS, COMPANY_LEGAL_NAME.title()],
            "url": absolute("/"),
            "logo": absolute(static("og/logo.png")),
            "taxID": COMPANY_CNPJ,
            "address": {
                "@type": "PostalAddress",
                "addressLocality": city,
                "addressRegion": state,
                "addressCountry": "BR",
            },
            "founder": {"@id": ids["person"]},
        },
        {
            "@type": "WebSite",
            "@id": ids["site"],
            "url": absolute("/"),
            "name": BRAND_NAME,
            "alternateName": [AUTHOR_NAME, AUTHOR_ALIAS],
            "inLanguage": tag,
            "publisher": {"@id": ids["person"]},
            "author": {"@id": ids["person"]},
        },
    ]


def page(
    kind: str,
    url: str,
    name: str,
    description: str,
    language: str,
    image: str = "",
    **extra: Any,
) -> dict[str, Any]:
    ids = _ids()
    node: dict[str, Any] = {
        "@type": kind,
        "@id": f"{absolute(url)}#page",
        "url": absolute(url),
        "name": name,
        "description": description,
        "inLanguage": LANGUAGE_TAGS.get(language, language),
        "isPartOf": {"@id": ids["site"]},
        "about": {"@id": ids["person"]},
    }
    if image:
        node["primaryImageOfPage"] = {"@type": "ImageObject", "url": image}
    node.update(extra)
    return node


def breadcrumbs(url: str, trail: list[tuple[str, str]]) -> dict[str, Any]:
    return {
        "@type": "BreadcrumbList",
        "@id": f"{absolute(url)}#breadcrumb",
        "itemListElement": [
            {"@type": "ListItem", "position": index, "name": name, "item": absolute(href)}
            for index, (name, href) in enumerate(trail, start=1)
        ],
    }


def project_work(project: Project, text: dict[str, Any], url: str, stack: list[str], image: str) -> dict[str, Any]:
    """A product as a creative work by the author, linked to its live address when it has one."""
    ids = _ids()
    work: dict[str, Any] = {
        "@type": "CreativeWork",
        "@id": f"{absolute(url)}#work",
        "name": project.name,
        "headline": text["tagline"],
        "description": f"{text['problem']} {text['built']}",
        "genre": text["kind"],
        "creator": {"@id": ids["person"]},
        "keywords": ", ".join(stack),
        "mainEntityOfPage": absolute(url),
    }
    if project.since:
        work["dateCreated"] = str(project.since)
    if project.url:
        work["url"] = project.url
        work["sameAs"] = [project.url]
    if project.repo:
        work["codeRepository"] = project.repo
    if image:
        work["image"] = image
    return work


def faq(url: str, items: list[dict[str, str]]) -> dict[str, Any]:
    return {
        "@type": "FAQPage",
        "@id": f"{absolute(url)}#faq",
        "mainEntity": [
            {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in items
        ],
    }


def graph(*nodes: dict[str, Any] | list[dict[str, Any]]) -> dict[str, Any]:
    flat: list[dict[str, Any]] = []
    for node in nodes:
        flat.extend(node if isinstance(node, list) else [node])
    return {"@context": "https://schema.org", "@graph": flat}
