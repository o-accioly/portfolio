"""Capture public pages of each project at five device sizes.

Usage:
    .venv/bin/python scripts/capture.py                 # every project
    .venv/bin/python scripts/capture.py diapasao duetto # only these slugs
    .venv/bin/python scripts/capture.py --force duetto  # replace what is already on disk
    .venv/bin/python scripts/capture.py --manifest      # only rebuild manifest.json

Output: static/shots/<slug>/<device>-<page>.webp (first viewport) and
        static/shots/<slug>/<device>-<page>-full.webp (scrolled page, capped).

Only public URLs are listed here. Screens behind a login are dropped by hand into
the same folder, following the same names (see README > Screenshots).
"""

from __future__ import annotations

import io
import json
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import Page, sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static" / "shots"

# name -> (viewport width, viewport height, device scale factor, mobile?)
DEVICES: dict[str, tuple[int, int, float, bool]] = {
    "ultrawide": (2560, 1080, 1, False),
    "desktop": (1920, 1080, 1, False),
    "laptop": (1440, 900, 1, False),
    "tablet": (820, 1180, 1.5, True),
    "phone": (390, 844, 2, True),
}

# slug -> {page name: url}. "home" is the project's cover; the other pages are what the
# monitor navigates to after it (in this order), so they only need the scrolled capture.
SITES: dict[str, dict[str, str]] = {
    "diapasao": {
        "home": "https://diapasao.com/",
        "crm": "https://diapasao.com/crm/",
        "loja": "https://diapasao.com/loja-virtual/",
        "assistente": "https://diapasao.com/assistente-de-ia/",
    },
    "kayadoc": {
        "home": "https://kayadoc.com.br/",
        "funcionalidades": "https://kayadoc.com.br/funcionalidades/",
        "planos": "https://kayadoc.com.br/planos/",
    },
    "kayamind": {
        "home": "https://kayamind.com/",
        "relatorios": "https://kayamind.com/relatorios/",
    },
    "kayaeducation": {
        "home": "https://kayaeducation.com.br/",
    },
    # The cover comes from a local demonstration (README > Prints); the public page is the login screen.
    # The phone keeps that login as its cover: the logged-in layout breaks at 390 px.
    "kaya-dashboard": {
        "entrar": "https://dashboard.kayamind.com/usuario/entrar/",
    },
    "duetto": {
        "home": "https://duettomusical.com.br/",
        "categoria": "https://duettomusical.com.br/categoria/mesa-de-som/",
    },
    "optimum": {
        "home": "https://optimumcapital.com.br/",
        "quem-somos": "https://optimumcapital.com.br/quem-somos/",
        "calculadora": "https://optimumcapital.com.br/calculadora/",
    },
}

# Page order of the projects captured by hand from a demonstration environment; it wins over SITES.
DEMO_ORDER: dict[str, list[str]] = {
    "kaya-dashboard": ["home", "console", "paineis", "eventos", "entrar"],
    "sabo": ["home", "consultas", "custo"],
    "standup": ["home", "operacional", "daily", "ata"],
}

COVER = "home"
FULL_PAGE_MAX_SCREENS = 5  # the cover
INNER_PAGE_MAX_SCREENS = 3  # pages the monitor navigates to
REJECT_LABELS = (
    "Recusar",
    "Rejeitar",
    "Apenas necessários",
    "Somente necessários",
    "Apenas essenciais",
    "Reject all",
    "Decline",
)


def _dismiss_consent(page: Page) -> None:
    """Pick the privacy-preserving answer on a consent banner, when one shows."""
    for label in REJECT_LABELS:
        button = page.get_by_role("button", name=label, exact=False)
        try:
            if button.count() and button.first.is_visible():
                # A scripted click: the banner may sit outside the visible area on a page that
                # is wider than its viewport.
                button.first.evaluate("element => element.click()")
                page.wait_for_timeout(400)
                return
        except Exception:  # noqa: BLE001, S112 - a banner that will not close is not fatal
            continue


# Newsletter and promo pop-ups cover the page they sit on; a capture should show the page.
HIDE_OVERLAYS = """
.elementor-popup-modal, .dialog-widget.dialog-lightbox-widget, .pum-overlay, .modal-backdrop,
[class*="mf-modal"], [class*="mf-bar"], [class*="mf-notification"],
[class*="newsletter-popup"], [id*="popup-modal"] { display: none !important; }
"""


# A page wider than a phone or tablet makes the browser zoom out and shift what it shows.
# The capture keeps the device's own width, the way the page is meant to be seen.
CLAMP_WIDTH = "html, body { overflow-x: hidden !important; max-width: 100vw !important; }"


def _clamp_width(page: Page, width: int) -> None:
    wider = page.evaluate("document.documentElement.scrollWidth") > width + 2
    if wider:
        print(f"  page is wider than {width}px; capturing at the device width")
        page.add_style_tag(content=CLAMP_WIDTH)
        page.wait_for_timeout(300)


def _settle(page: Page, height: int) -> None:
    """Scroll through the page once so lazy images and reveals are in place."""
    total = page.evaluate("document.documentElement.scrollHeight")
    limit = min(total, height * FULL_PAGE_MAX_SCREENS)
    position = 0
    while position < limit:
        page.mouse.wheel(0, height)
        position += height
        page.wait_for_timeout(250)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(600)


def _save(png: bytes, target: Path, max_width: int) -> None:
    image = Image.open(io.BytesIO(png)).convert("RGB")
    if image.width > max_width:
        ratio = max_width / image.width
        image = image.resize((max_width, round(image.height * ratio)), Image.Resampling.LANCZOS)
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target, "WEBP", quality=82, method=6)
    print(f"  {target.relative_to(ROOT)}  {image.width}x{image.height}  {target.stat().st_size // 1024} KB")


def capture(slugs: list[str], force: bool = False) -> None:
    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch()
        except Exception:  # noqa: BLE001 - Playwright's own Chromium is not installed
            browser = playwright.chromium.launch(channel="chrome")
        for slug in slugs:
            pages = SITES[slug]
            for device, (width, height, scale, mobile) in DEVICES.items():
                context = browser.new_context(
                    viewport={"width": width, "height": height},
                    device_scale_factor=scale,
                    is_mobile=mobile,
                    has_touch=mobile,
                    locale="pt-BR",
                    reduced_motion="reduce",
                )
                page = context.new_page()
                for name, url in pages.items():
                    base = OUT / slug / f"{device}-{name}"
                    full_target = base.with_name(base.name + "-full.webp")
                    if full_target.exists() and not force:
                        continue  # already captured; pass --force to replace
                    print(f"{slug} / {device} / {name}")
                    try:
                        page.goto(url, wait_until="networkidle", timeout=45000)
                    except Exception as error:  # noqa: BLE001
                        print(f"  load did not go idle ({type(error).__name__}); capturing what rendered")
                    _dismiss_consent(page)
                    page.add_style_tag(content=HIDE_OVERLAYS)
                    _clamp_width(page, width)
                    _settle(page, height)
                    _dismiss_consent(page)  # some banners only show after the first scroll
                    if name == COVER:
                        _save(
                            page.screenshot(type="png"),
                            base.with_suffix(".webp"),
                            max_width=int(width * min(scale, 1.5)),
                        )
                    total = page.evaluate("document.documentElement.scrollHeight")
                    screens = FULL_PAGE_MAX_SCREENS if name == COVER else INNER_PAGE_MAX_SCREENS
                    clip_height = min(total, height * screens)
                    full = page.screenshot(
                        type="png",
                        full_page=True,
                        clip={"x": 0, "y": 0, "width": width, "height": clip_height},
                    )
                    _save(full, full_target, max_width=min(width, 1600))
                context.close()
        browser.close()


def write_manifest() -> None:
    """Describe what is on disk, so the site never opens an image at request time.

    `<device>-<page>.webp` and `<device>-<page>-full.webp` are captured pages;
    `inside-<device>-<name>.webp` are screens the author dropped in by hand, optionally with
    a recording beside them (`inside-<device>-<name>.webm` / `.mp4`).
    """
    manifest: dict[str, dict] = {}
    for folder in sorted(path for path in OUT.iterdir() if path.is_dir()):
        pages: dict[str, dict[str, dict[str, list[int]]]] = {}
        inside: list[dict] = []
        for file in sorted(folder.glob("*.webp")):
            with Image.open(file) as image:
                size = [image.width, image.height]
            stem = file.stem
            if stem.startswith("inside-"):
                _, device, *rest = stem.split("-")
                entry = {"file": file.name, "size": size, "device": device, "name": "-".join(rest)}
                # A screen recording with the same name plays in place of the still.
                videos = {ext: f"{stem}.{ext}" for ext in ("webm", "mp4") if file.with_suffix(f".{ext}").exists()}
                if videos:
                    entry["video"] = videos
                inside.append(entry)
                continue
            kind = "full" if stem.endswith("-full") else "top"
            device, _, page = stem.removesuffix("-full").partition("-")
            if device in DEVICES and page:
                pages.setdefault(page, {}).setdefault(device, {})[kind] = size
        # Every page needs its scrolled capture; the cover also needs its first viewport.
        for name, page in pages.items():
            needed = {"top", "full"} if name == COVER else {"full"}
            for device in [key for key, sizes in page.items() if not needed <= set(sizes)]:
                del page[device]
        # Keep the order of DEMO_ORDER (or SITES), so the monitor navigates the pages as listed there.
        order = DEMO_ORDER.get(folder.name) or list(SITES.get(folder.name, {}))
        pages = dict(sorted(pages.items(), key=lambda item: order.index(item[0]) if item[0] in order else len(order)))
        manifest[folder.name] = {"pages": pages, "inside": inside}
    target = OUT / "manifest.json"
    target.write_text(json.dumps(manifest, indent=1) + "\n", encoding="utf-8")
    print(f"manifest: {target.relative_to(ROOT)} ({len(manifest)} projects)")


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if arguments == ["--manifest"]:
        write_manifest()
        sys.exit(0)
    force = "--force" in arguments
    wanted = [argument for argument in arguments if argument != "--force"] or list(SITES)
    unknown = [slug for slug in wanted if slug not in SITES]
    if unknown:
        sys.exit(f"Unknown project(s): {', '.join(unknown)}. Known: {', '.join(SITES)}")
    capture(wanted, force=force)
    write_manifest()
