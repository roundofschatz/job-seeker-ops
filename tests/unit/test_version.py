"""One version everywhere: .claude-plugin/plugin.json, the newest release in
CHANGELOG.md, and the package in dist/ when one has been built.

    python tests/unit/test_version.py

A package that lags the repository installs an old copy under a new number, or
a new copy under an old one. The dist test skips when dist/ is empty.
"""
import json
import re
import unittest
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PACKAGES = ("job-seeker-ops.plugin", "job-seeker-ops.zip")


def changelog_version(text):
    match = re.search(r"^## (\d+\.\d+\.\d+)\b", text, re.M)
    return match.group(1) if match else None


def same_text(a, b):
    """Equal bytes, with line endings read as plain newlines."""
    return a.replace(b"\r\n", b"\n") == b.replace(b"\r\n", b"\n")


class Version(unittest.TestCase):
    def test_plugin_json_matches_the_changelog(self):
        plugin = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        log = (REPO / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertEqual(plugin["version"], changelog_version(log))

    def test_the_package_matches_the_repository(self):
        built = [REPO / "dist" / name for name in PACKAGES if (REPO / "dist" / name).is_file()]
        if not built:
            self.skipTest("no package in dist/")
        for path in built:
            with zipfile.ZipFile(path) as archive:
                names = [n for n in archive.namelist() if not n.endswith("/")]
                self.assertTrue(names, path.name)
                for name in names:
                    rel = name.split("/", 1)[1]
                    local = REPO / rel
                    self.assertTrue(local.is_file(), f"{path.name} holds {rel}, which the repository doesn't")
                    self.assertTrue(same_text(archive.read(name), local.read_bytes()),
                                    f"{path.name}: {rel} differs from the repository")
                for must in (".claude-plugin/plugin.json", "CHANGELOG.md", "README.md"):
                    self.assertIn(f"job-seeker-ops/{must}", names, path.name)
                shipped = {n.split("/", 1)[1] for n in names}
                for skill in (REPO / "skills").iterdir():
                    for f in skill.rglob("*"):
                        rel = f.relative_to(REPO).as_posix()
                        if f.is_file() and "__pycache__" not in rel:
                            self.assertIn(rel, shipped, f"{path.name} leaves out {rel}")
                self.assertFalse([n for n in shipped if n.startswith("tests/")], path.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
