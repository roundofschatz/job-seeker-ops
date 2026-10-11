"""tools/release_notes.py: the title and notes the release workflow publishes.

    python tests/unit/test_release_notes.py
"""
import importlib.util
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("release_notes", REPO / "tools" / "release_notes.py")
rn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rn)

LOG = """# Changelog

Intro line.

## 0.2.0 · The second thing

Second body.

## 0.1.1 · A fix

Fix body.

## 0.1.0 · First release

First body.
"""


class ReleaseNotes(unittest.TestCase):
    def test_one_new_entry_gives_its_body_and_a_lowercase_title(self):
        title, notes = rn.build("0.2.0", "v0.1.1", LOG)
        self.assertEqual(title, "job-seeker-ops 0.2.0: the second thing")
        self.assertTrue(notes.startswith("Second body."))
        self.assertNotIn("Fix body.", notes)
        self.assertIn("/plugin install job-seeker-ops@roundofschatz", notes)

    def test_entries_with_no_release_of_their_own_come_along(self):
        title, notes = rn.build("0.2.0", "v0.1.0", LOG)
        self.assertIn("also covers 0.1.1", notes)
        self.assertIn("## 0.2.0 · The second thing", notes)
        self.assertIn("## 0.1.1 · A fix", notes)
        self.assertNotIn("First body.", notes)

    def test_an_unknown_or_missing_last_release_gives_only_the_newest_entry(self):
        for last in ("", "v9.9.9"):
            with self.subTest(last=last):
                _, notes = rn.build("0.2.0", last, LOG)
                self.assertTrue(notes.startswith("Second body."))
                self.assertNotIn("Fix body.", notes)

    def test_a_version_the_changelog_doesnt_lead_with_stops_the_release(self):
        with self.assertRaises(ValueError):
            rn.build("0.3.0", "v0.2.0", LOG)

    def test_the_real_changelog_leads_with_the_plugin_version(self):
        import json
        version = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
        title, _ = rn.build(version, "", (REPO / "CHANGELOG.md").read_text(encoding="utf-8"))
        self.assertTrue(title.startswith(f"job-seeker-ops {version}"))


if __name__ == "__main__":
    unittest.main()
