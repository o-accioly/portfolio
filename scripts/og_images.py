"""Render the share cards (Open Graph / Twitter) and the square logo (development only).

Usage, with the development server running (DJANGO_DEBUG=1 serves `/og/<key>/`):
    .venv/bin/python scripts/og_images.py [base_url]

Writes `static/og/<key>.jpg` (1200 × 630) for the general pages in each language and for every
project, plus `static/og/logo.png` (512 × 512, from `static/favicon.svg`). The cards are built from
the same templates, tokens and screenshots as the site, so they need no separate source file.
"""

from __future__ import annotations

import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from portfolio.catalog import PROJECTS  # noqa: E402

OUT = ROOT / "static" / "og"
BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8791"
LANGUAGES = ("pt-br", "en", "es")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    keys = [f"home-{language}" for language in LANGUAGES] + [project.slug for project in PROJECTS]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome")
        page = browser.new_page(viewport={"width": 1200, "height": 630}, reduced_motion="reduce")
        for key in keys:
            page.goto(f"{BASE}/og/{key}/", wait_until="networkidle")
            page.evaluate("document.fonts.ready")
            target = OUT / f"{key}.jpg"
            page.screenshot(path=target, type="jpeg", quality=84, clip={"x": 0, "y": 0, "width": 1200, "height": 630})
            print(f"{target.relative_to(ROOT)}  {target.stat().st_size // 1024} KB")
        page.set_viewport_size({"width": 512, "height": 512})
        page.goto(f"{BASE}/og/logo/", wait_until="networkidle")
        target = OUT / "logo.png"
        page.screenshot(path=target, clip={"x": 0, "y": 0, "width": 512, "height": 512})
        print(f"{target.relative_to(ROOT)}  {target.stat().st_size // 1024} KB")
        browser.close()


if __name__ == "__main__":
    main()
