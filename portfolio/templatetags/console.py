"""Template helpers: the icon set and a few lookups."""

from __future__ import annotations

import json
from typing import Any

from django import template
from django.utils.html import format_html
from django.utils.safestring import SafeString, mark_safe

register = template.Library()

# One drawn family: 24-unit grid, 1.75 stroke, round joins. Paths only, so the SVG wrapper
# stays in one place.
ICONS: dict[str, str] = {
    "arrow-up-right": '<path d="M7 17 17 7"/><path d="M8 7h9v9"/>',
    "arrow-left": '<path d="M19 12H5"/><path d="m11 6-6 6 6 6"/>',
    "arrow-right": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    "play": '<path d="M7 5v14l12-7z"/>',
    "pause": '<path d="M8 5v14"/><path d="M16 5v14"/>',
    "lamp": '<path d="M9 18h6"/><path d="M10 21h4"/><path d="M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.4 1 2.5h6c0-1.1.3-1.8 1-2.5A6 6 0 0 0 12 3z"/>',
    "wave": '<path d="M3 12c2.5 0 2.5-6 5-6s2.5 12 5 12 2.5-12 5-12 2.5 6 3 6"/>',
    "linkedin": '<path d="M7 10v7"/><path d="M7 7v.01"/><path d="M11 17v-4a2.5 2.5 0 0 1 5 0v4"/><path d="M11 10v7"/><rect x="3" y="3" width="18" height="18" rx="3"/>',
    "github": '<path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.4 5.4 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 8 9 6 9-6"/>',
    "chevron": '<path d="m9 6 6 6-6 6"/>',
}


@register.simple_tag
def icon(name: str, size: int = 20) -> SafeString:
    return format_html(
        '<svg class="icon" width="{0}" height="{0}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{1}</svg>',
        size,
        mark_safe(ICONS[name]),  # noqa: S308 - paths are constants defined above
    )


@register.filter
def get(mapping: dict[str, Any], key: str) -> Any:
    return mapping.get(key)


_JSON_ESCAPES = {ord("<"): "\\u003C", ord(">"): "\\u003E", ord("&"): "\\u0026"}


@register.filter
def jsonld(data: dict[str, Any]) -> SafeString:
    """A JSON-LD block. `<`, `>` and `&` are escaped so the copy cannot close the script."""
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":")).translate(_JSON_ESCAPES)
    return mark_safe(f'<script type="application/ld+json">{text}</script>')  # noqa: S308 - escaped above
