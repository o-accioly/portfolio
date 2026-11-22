from __future__ import annotations

from typing import Any

from django.conf import settings
from django.http import HttpRequest
from django.urls import reverse, translate_url
from django.utils.translation import get_language

from .catalog import (
    AUTHOR_ALIAS,
    AUTHOR_NAME,
    BRAND_NAME,
    COMPANY_CITY,
    COMPANY_CNPJ,
    COMPANY_LEGAL_NAME,
    GITHUB_URL,
    LINKEDIN_URL,
    PROJECTS,
)

LANGUAGE_SHORT = {"pt-br": "PT", "en": "EN", "es": "ES"}
OG_LOCALE = {"pt-br": "pt_BR", "en": "en_US", "es": "es_ES"}


def site(request: HttpRequest) -> dict[str, Any]:
    """Author links, the public origin and this page's address in each language."""
    current = get_language() or settings.LANGUAGE_CODE
    path = request.get_full_path()
    languages = [
        {
            "code": code,
            "short": LANGUAGE_SHORT.get(code, code.upper()),
            "name": name,
            "url": translate_url(path, code),
            "locale": OG_LOCALE.get(code, code),
            "current": code == current,
        }
        for code, name in settings.LANGUAGES
    ]
    # x-default: the same page without a language prefix, which LocaleMiddleware sends to the
    # visitor's language.
    prefix = f"/{current}/"
    x_default = "/" + request.path[len(prefix) :] if request.path.startswith(prefix) else "/"
    match = getattr(request, "resolver_match", None)
    return {
        "x_default_url": x_default,
        "footer_projects": [
            {"name": project.name, "href": reverse("portfolio:project", args=[project.slug])} for project in PROJECTS
        ],
        "url_name": match.url_name if match else "",
        "author_alias": AUTHOR_ALIAS,
        "author": AUTHOR_NAME,
        "brand": BRAND_NAME,
        # "oAccioly Faz" split for the wordmark: the name letter by letter, then the verb.
        "brand_letters": list(BRAND_NAME.split()[0]),
        "brand_verb": BRAND_NAME.split()[1].lower(),
        "company": {"name": COMPANY_LEGAL_NAME, "cnpj": COMPANY_CNPJ, "city": COMPANY_CITY},
        "linkedin_url": LINKEDIN_URL,
        "github_url": GITHUB_URL,
        "contact_email": settings.CONTACT_EMAIL,
        "repo_url": settings.REPO_URL,
        "site_url": settings.SITE_URL,
        "languages": languages,
    }
