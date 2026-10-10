"""Tests for the copies of plainspeak-writer and resume-ops that come with this plugin.

    python tests/unit/test_bundled.py

Each copy in skills/ has to match its record in bundled.json file for file.
When the skill's own repository sits next to this one, the record has to match
the commit it names, so nobody can edit a copy here and record the edit. The
bundled resume-ops reads the example positioning file, so the two plugins'
skills still agree on its format.

Standard library and git only.
"""
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SYNC = REPO / "tools" / "sync_bundled.py"
spec = importlib.util.spec_from_file_location("sync_bundled", SYNC)
sb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sb)

WRITER = REPO / "tests" / "writers" / "b-okafor"
POSITIONING = "positioning-switchgrass-freight-supply-chain-planning-analyst.md"


def record():
    return json.loads((REPO / "bundled.json").read_text(encoding="utf-8"))["skills"]


def own_repository(name, commit):
    """The skill's own clone next to this repository, when it holds the commit."""
    repo = REPO.parent / name
    if not (repo / ".git").exists():
        return None
    proc = subprocess.run(["git", "--no-optional-locks", "-C", str(repo), "cat-file", "-e", f"{commit}^{{commit}}"],
                          capture_output=True)
    return repo if proc.returncode == 0 else None


class Copies(unittest.TestCase):
    def test_the_record_lists_both_skills(self):
        self.assertEqual(sorted(record()), ["plainspeak-writer", "resume-ops"])

    def test_each_copy_matches_its_record(self):
        for name, entry in record().items():
            with self.subTest(name):
                self.assertEqual(sb.problems(name, entry), [])

    def test_each_record_states_the_copys_own_version_and_name(self):
        for name, entry in record().items():
            with self.subTest(name):
                folder = REPO / "skills" / name
                files = {rel: (folder / rel).read_bytes() for rel in ("CHANGELOG.md", "SKILL.md")}
                self.assertEqual(sb.version_of(name, files), entry["version"])
                head = files["SKILL.md"].decode("utf-8")[:2000]
                self.assertRegex(head, rf"(?m)^name:\s*{re.escape(name)}\s*$")

    def test_tests_stay_in_the_skills_own_repositories(self):
        for name, entry in record().items():
            with self.subTest(name):
                self.assertIn("tests/", entry["left_out"])
                self.assertFalse([rel for rel in entry["files"] if rel.startswith("tests/")])

    def test_each_record_matches_its_commit(self):
        checked = 0
        for name, entry in record().items():
            repo = own_repository(name, entry["commit"])
            if repo is None:
                continue
            with self.subTest(name):
                source = "" if entry["source"] == "." else entry["source"]
                paths = sb.files_at(repo, entry["commit"], source, entry["left_out"])
                self.assertEqual(sorted(paths), sorted(entry["files"]))
                for rel, name_in_repo in paths.items():
                    data = sb.git(repo, "cat-file", "blob", f"{entry['commit']}:{name_in_repo}")
                    self.assertEqual(sb.digest(data), entry["files"][rel], rel)
                checked += 1
        if not checked:
            self.skipTest("neither skill's repository sits next to this one")

    def test_a_folder_the_record_doesnt_list_is_never_replaced(self):
        with tempfile.TemporaryDirectory() as tmp:
            fake = Path(tmp)
            (fake / "skills" / "resume-ops").mkdir(parents=True)
            (fake / "skills" / "resume-ops" / "SKILL.md").write_text("mine\n", encoding="utf-8")
            old_repo, old_manifest = sb.REPO, sb.MANIFEST
            sb.REPO, sb.MANIFEST = fake, fake / "bundled.json"
            try:
                with self.assertRaises(sb.SyncError) as caught:
                    sb.sync("resume-ops", REPO, "HEAD")
            finally:
                sb.REPO, sb.MANIFEST = old_repo, old_manifest
            self.assertIn("isn't a copy this script made", str(caught.exception))
            self.assertEqual((fake / "skills" / "resume-ops" / "SKILL.md").read_text(encoding="utf-8"), "mine\n")

    def test_an_edited_copy_is_caught(self):
        entry = record()["plainspeak-writer"]
        with tempfile.TemporaryDirectory() as tmp:
            fake = Path(tmp)
            shutil.copytree(REPO / "skills" / "plainspeak-writer", fake / "skills" / "plainspeak-writer")
            copy = fake / "skills" / "plainspeak-writer"
            (copy / "references" / "tells.md").write_bytes(b"# Tells\n")
            (copy / "references" / "voice.md").unlink()
            (copy / "notes.md").write_bytes(b"added here\n")
            old_repo = sb.REPO
            sb.REPO = fake
            try:
                found = sb.problems("plainspeak-writer", entry)
            finally:
                sb.REPO = old_repo
        self.assertEqual(len(found), 3, found)
        self.assertTrue(any("tells.md differs" in p for p in found), found)
        self.assertTrue(any("voice.md is in the record and missing" in p for p in found), found)
        self.assertTrue(any("notes.md is in the copy and not in the record" in p for p in found), found)


class Marketplace(unittest.TestCase):
    """The marketplace for the three tools lists the releases this plugin copies,
    so a person who installs one tool on its own gets the version in the bundle."""

    def test_it_lists_the_three_tools_by_the_copies_tags(self):
        market = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(market["name"], "roundofschatz")
        entries = {p["name"]: p for p in market["plugins"]}
        self.assertEqual(sorted(entries), ["job-seeker-ops", "plainspeak-writer", "resume-ops"])
        self.assertIn(entries["job-seeker-ops"]["source"], ("./", "."))
        for name, entry in record().items():
            with self.subTest(name):
                source = entries[name]["source"]
                # HTTPS, since a github source clones over SSH and fails without a key.
                self.assertEqual(source["source"], "url")
                self.assertEqual(source["url"], entry["repository"] + ".git")
                self.assertEqual(source["ref"], entry["ref"])
        # plainspeak-writer has no plugin manifest, so its entry states the version.
        self.assertEqual(entries["plainspeak-writer"]["version"], record()["plainspeak-writer"]["version"])

    def test_a_tool_without_a_manifest_is_declared_by_its_entry(self):
        # claude.ai's marketplace sync skips a plugin with no .claude-plugin/plugin.json
        # unless its entry sets "strict": false and names its skills. Claude Code accepts either.
        market = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        entries = {p["name"]: p for p in market["plugins"]}
        checked = 0
        for name, spec in sb.SKILLS.items():
            if spec["source"] or (REPO / "skills" / name / ".claude-plugin" / "plugin.json").exists():
                continue
            with self.subTest(name):
                self.assertTrue((REPO / "skills" / name / "SKILL.md").exists())
                self.assertIs(entries[name].get("strict"), False)
                self.assertEqual(entries[name].get("skills"), ["./"])
            checked += 1
        self.assertEqual(checked, 1)

    def test_the_readme_names_each_copys_version(self):
        text = (REPO / "README.md").read_text(encoding="utf-8")
        section = text.split("## plainspeak-writer and resume-ops", 1)[1].split("\n## ", 1)[0]
        for name, entry in record().items():
            with self.subTest(name):
                self.assertRegex(section, rf"\[{re.escape(name)}\]\([^)]*\) {re.escape(entry['version'])}(?!\.?\d)")


class ResumeOpsReadsPositioning(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        text = (REPO / "skills" / "candidate-positioning" / "references" / "format.md").read_text(encoding="utf-8")
        body = text.split("## A full example", 1)[1]
        example = re.search(r"```markdown\n(.*?)\n```\s*$", body, re.S).group(1) + "\n"
        (self.dir / POSITIONING).write_bytes(example.encode("utf-8"))
        for name in ("posting.txt", "resume.txt"):
            shutil.copy(WRITER / name, self.dir / name)

    def tearDown(self):
        self.tmp.cleanup()

    def run_check(self, *flags):
        script = REPO / "skills" / "resume-ops" / "scripts" / "positioning_check.py"
        proc = subprocess.run([sys.executable, str(script), str(self.dir / POSITIONING), *map(str, flags)],
                              capture_output=True, text=True, encoding="utf-8")
        return proc.returncode, proc.stdout + proc.stderr

    def test_the_example_file_is_read_for_the_build(self):
        code, out = self.run_check("--posting", self.dir / "posting.txt")
        self.assertEqual(code, 0, out)
        self.assertIn("RESULT: use it", out)
        self.assertIn("posting.txt is the copy the file was built from", out)

    def test_the_resume_is_checked_against_the_keep_off_list(self):
        code, out = self.run_check("--resume", self.dir / "resume.txt")
        self.assertEqual(code, 0, out)
        resume = self.dir / "resume.txt"
        resume.write_bytes(resume.read_bytes() + b"\nNew to freight, and learning fast.\n")
        code, out = self.run_check("--resume", resume)
        self.assertEqual(code, 1, out)
        self.assertIn("new to freight", out.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
