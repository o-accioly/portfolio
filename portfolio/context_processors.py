from __future__ import annotations

from typing import Any

from django.conf import settings
from django.http import HttpRequest
from django.urls import translate_url
from django.utils.translation import get_language

from .catalog import (
    AUTHOR_NAME,
    BRAND_NAME,
    COMPANY_CITY,
    COMPANY_CNPJ,
    COMPANY_LEGAL_NAME,
    GITHUB_URL,
    LINKEDIN_URL,
)

LANGUAGE_SHORT = {"pt-br": "PT", "en": "EN", "es": "ES"}


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
            "current": code == current,
        }
        for code, name in settings.LANGUAGES
    ]
    return {
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
