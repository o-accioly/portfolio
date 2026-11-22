"""Screenshots on disk, described by `static/shots/manifest.json`.

`scripts/capture.py` writes the manifest (image sizes per project, device and page), so the
site never opens an image at request time. A shot scrolls inside its device by a share of its
own height; that share depends only on the two aspect ratios, so it is computed here once.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import cache

from django.conf import settings
from django.templatetags.static import static

from .catalog import DEVICE_BY_KEY, DEVICES, Device

MANIFEST_PATH = settings.BASE_DIR / "static" / "shots" / "manifest.json"
COVER = "home"
SECONDS_PER_SCREEN = 3.6
MIN_SECONDS = 6.0


@dataclass(frozen=True)
class Shot:
    device: str
    page: str
    full: str  # scrolled page
    width: int
    height: int
    pan: float  # how far the scrolled page travels, in % of its own height (negative)
    duration: float  # seconds for one pass
    top: str = ""  # first viewport; only the cover has one

    @property
    def pan_css(self) -> str:
        """`pan` as a CSS value (templates would localise the float's decimal mark)."""
        return f"{self.pan}%"

    @property
    def duration_css(self) -> str:
        return f"{self.duration}s"

    @property
    def ratio_css(self) -> str:
        """The capture's viewport as a CSS aspect ratio."""
        device = DEVICE_BY_KEY[self.device]
        return f"{device.width} / {device.height}"

    def as_json(self) -> dict[str, str | float]:
        return {"src": self.full, "pan": self.pan, "dur": self.duration}


@cache
def _manifest() -> dict:
    if not MANIFEST_PATH.exists():
        return {}
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def _shot(slug: str, device: Device, page: str, sizes: dict[str, list[int]]) -> Shot:
    full_width, full_height = sizes["full"]
    screens = (full_height / full_width) * device.ratio
    travel = max(0.0, 1 - 1 / screens) if screens else 0.0
    return Shot(
        device=device.key,
        page=page,
        full=static(f"shots/{slug}/{device.key}-{page}-full.webp"),
        width=full_width,
        height=full_height,
        pan=round(-travel * 100, 3),
        duration=round(max(MIN_SECONDS, (screens - 1) * SECONDS_PER_SCREEN), 1),
        top=static(f"shots/{slug}/{device.key}-{page}.webp") if "top" in sizes else "",
    )


def shots_for(slug: str) -> dict[str, list[Shot]]:
    """Per device, the pages the monitor shows in order: the cover, then the inner pages.

    A device appears only when its cover was captured.
    """
    pages = _manifest().get(slug, {}).get("pages", {})
    names = [COVER] + [name for name in pages if name != COVER]
    result: dict[str, list[Shot]] = {}
    for device in DEVICES:
        if device.key not in pages.get(COVER, {}):
            continue
        result[device.key] = [
            _shot(slug, device, name, pages[name][device.key]) for name in names if device.key in pages.get(name, {})
        ]
    return result


def inside_shots(slug: str) -> list[dict[str, str | int]]:
    """Hand-picked screens from behind a login (`inside-*.webp`), when the author added any.

    A screen may come with a recording (`.webm` / `.mp4` of the same name) that plays in place.
    """
    shots = []
    for item in _manifest().get(slug, {}).get("inside", []):
        video = item.get("video", {})
        shots.append(
            {
                "name": item.get("name", ""),
                "src": static(f"shots/{slug}/{item['file']}"),
                "width": item["size"][0],
                "height": item["size"][1],
                "device": item["device"] if item.get("device") in DEVICE_BY_KEY else "laptop",
                "webm": static(f"shots/{slug}/{video['webm']}") if "webm" in video else "",
                "mp4": static(f"shots/{slug}/{video['mp4']}") if "mp4" in video else "",
            }
        )
    return shots
