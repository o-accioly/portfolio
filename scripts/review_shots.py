"""Screenshot the running site for design review (development only).

Usage: .venv/bin/python scripts/review_shots.py [base_url]
Writes PNGs to .impeccable/review/ (ignored by git).
"""

from __future__ import annotations

import sys
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

OUT = Path(__file__).resolve().parent.parent / ".impeccable" / "review"
BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8791"

VIEWPORTS = (
    ("desktop", 1440, 900, "light"),
    ("desktop-dark", 1440, 900, "dark"),
    ("mobile", 390, 844, "light"),
)


def full_page(page: Page, path: Path) -> None:
    """Scroll through first, so lazy images and reveals are in before the capture."""
    height = page.evaluate("document.documentElement.scrollHeight")
    for offset in range(0, height, 600):
        page.evaluate("y => window.scrollTo(0, y)", offset)
        page.wait_for_timeout(120)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(400)
    page.screenshot(path=path, full_page=True)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome")
        for name, width, height, scheme in VIEWPORTS:
            context = browser.new_context(
                viewport={"width": width, "height": height},
                color_scheme=scheme,
                reduced_motion="reduce",
                locale="pt-BR",
            )
            page = context.new_page()
            page.goto(f"{BASE}/pt-br/", wait_until="networkidle")
            page.wait_for_timeout(600)
            page.screenshot(path=OUT / f"{name}-first.png")
            overflow = page.evaluate("document.body.scrollWidth - window.innerWidth")
            tape = page.evaluate("Math.round(document.querySelector('.tape-strip').getBoundingClientRect().bottom)")
            print(f"{name}: home overflow {overflow}px, tape bottom at {tape}px of {height}px")
            for device in ("ultrawide", "desktop", "tablet", "phone"):
                page.locator(f"[data-set-device={device}]").dispatch_event("click")  # outlines overlap
                page.wait_for_timeout(700)
                page.screenshot(path=OUT / f"{name}-first-{device}.png")
            page.locator("[data-set-device=laptop]").dispatch_event("click")
            page.click("[data-patch-tab='3']")
            page.wait_for_timeout(700)
            full_page(page, OUT / f"{name}.png")
            page.goto(f"{BASE}/pt-br/stack/", wait_until="networkidle")
            page.click("[data-solo=desbravador]")
            page.wait_for_timeout(700)
            full_page(page, OUT / f"{name}-stack.png")
            for path in ("about", "projects"):
                page.goto(f"{BASE}/pt-br/{path}/", wait_until="networkidle")
                page.wait_for_timeout(600)
                full_page(page, OUT / f"{name}-{path}.png")
            for slug in ("diapasao", "desbravador"):
                page.goto(f"{BASE}/pt-br/projects/{slug}/", wait_until="networkidle")
                page.wait_for_timeout(600)
                full_page(page, OUT / f"{name}-project-{slug}.png")
            overflow = page.evaluate("document.documentElement.scrollWidth - window.innerWidth")
            print(f"{name}: horizontal overflow {overflow}px")
            context.close()
        browser.close()


if __name__ == "__main__":
    main()
