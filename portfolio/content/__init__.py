"""Copy for the three languages.

Each language is a module with one `CONTENT` dict of the same shape. Portuguese is the
source; a test compares the key trees so a missing translation fails the suite instead of
shipping a blank label. Language detection and URL prefixes still come from Django's i18n.
"""

from __future__ import annotations

from functools import cache
from importlib import import_module
from typing import Any

MODULES = {"pt-br": "pt_br", "pt": "pt_br", "en": "en", "es": "es"}
FALLBACK = "en"


@cache
def get_content(language: str | None) -> dict[str, Any]:
    code = (language or FALLBACK).lower()
    module = MODULES.get(code) or MODULES.get(code.split("-")[0]) or MODULES[FALLBACK]
    return import_module(f"portfolio.content.{module}").CONTENT
