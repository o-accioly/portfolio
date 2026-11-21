"""The three languages must say the same things: same keys, same placeholders."""

import re
from typing import Any

from django.test import SimpleTestCase

from portfolio.catalog import LAYER_KEYS, PROJECTS, TRACKS, TRANSLATED_SKILLS
from portfolio.content import get_content

LANGUAGES = ("pt-br", "en", "es")
PLACEHOLDER = re.compile(r"\{(\w+)\}")


def shape(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: shape(item) for key, item in value.items()}
    if isinstance(value, list):
        return [shape(item) for item in value]
    return type(value).__name__


def strings(value: Any, path: str = "") -> list[tuple[str, str]]:
    if isinstance(value, dict):
        return [pair for key, item in value.items() for pair in strings(item, f"{path}.{key}")]
    if isinstance(value, list):
        return [pair for index, item in enumerate(value) for pair in strings(item, f"{path}[{index}]")]
    return [(path, value)]


class ContentTests(SimpleTestCase):
    def test_every_language_has_the_same_structure(self) -> None:
        source = shape(get_content("pt-br"))
        for language in LANGUAGES[1:]:
            with self.subTest(language=language):
                self.assertEqual(shape(get_content(language)), source)

    def test_placeholders_survive_translation(self) -> None:
        source = dict(strings(get_content("pt-br")))
        for language in LANGUAGES[1:]:
            for path, text in strings(get_content(language)):
                with self.subTest(language=language, path=path):
                    self.assertEqual(sorted(PLACEHOLDER.findall(text)), sorted(PLACEHOLDER.findall(source[path])))

    def test_no_string_is_empty(self) -> None:
        for language in LANGUAGES:
            for path, text in strings(get_content(language)):
                with self.subTest(language=language, path=path):
                    self.assertTrue(text.strip())

    def test_copy_covers_the_catalog(self) -> None:
        for language in LANGUAGES:
            content = get_content(language)
            with self.subTest(language=language):
                self.assertEqual(set(content["projects"]["items"]), {project.slug for project in PROJECTS})
                self.assertEqual(set(content["journey"]["tracks"]), {track.key for track in TRACKS})
                self.assertEqual(set(content["layers"]), set(LAYER_KEYS))
                self.assertEqual(set(content["skills"]["labels"]), set(TRANSLATED_SKILLS))
                for project in PROJECTS:
                    notes = content["projects"]["items"][project.slug]["layers"]
                    self.assertEqual(set(notes), {layer.key for layer in project.layers}, project.slug)

    def test_unknown_language_falls_back_to_english(self) -> None:
        self.assertIs(get_content("de"), get_content("en"))
        self.assertIs(get_content("pt"), get_content("pt-br"))
