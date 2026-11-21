from django.test import SimpleTestCase

from portfolio.catalog import BUSES, DEVICES, LAYER_KEYS, PROJECTS, SKILLS


class CatalogTests(SimpleTestCase):
    def test_projects_only_reference_known_skills_and_layers(self) -> None:
        for project in PROJECTS:
            with self.subTest(project=project.slug):
                self.assertFalse(set(project.skills) - set(SKILLS))
                self.assertEqual(len(project.skills), len(set(project.skills)))
                self.assertFalse({layer.key for layer in project.layers} - set(LAYER_KEYS))

    def test_slugs_and_codes_are_unique(self) -> None:
        self.assertEqual(len({project.slug for project in PROJECTS}), len(PROJECTS))
        self.assertEqual(len({project.code for project in PROJECTS}), len(PROJECTS))

    def test_every_skill_is_used_and_sits_on_a_bus(self) -> None:
        used = {skill for project in PROJECTS for skill in project.skills}
        self.assertEqual(used, set(SKILLS))
        self.assertEqual({bus for _, bus in SKILLS.values()}, set(BUSES))

    def test_links_are_absolute(self) -> None:
        """A project may have no public address (private work), but never a relative one."""
        for project in PROJECTS:
            for link in (project.url, project.repo):
                with self.subTest(project=project.slug, link=link):
                    self.assertTrue(link == "" or link.startswith("https://"))

    def test_five_devices(self) -> None:
        self.assertEqual([device.key for device in DEVICES], ["ultrawide", "desktop", "laptop", "tablet", "phone"])
