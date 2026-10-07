"""Tests for skills/submission-review/scripts/build_packet.py.

    python3 tests/unit/test_build_packet.py

Standard library only. The last test runs the real plainspeak-writer checker
when a copy sits next to this repository, and skips otherwise.
"""
import contextlib
import importlib.util
import io
import os
import re
import sys
import tempfile
import textwrap
import unittest
import zipfile
from unittest import mock
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "skills" / "submission-review" / "scripts" / "build_packet.py"
spec = importlib.util.spec_from_file_location("build_packet", SCRIPT)
bp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bp)

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def make_docx(path, paragraphs, header=None):
    def part(paras):
        body = "".join(
            f'<w:p><w:r><w:t xml:space="preserve">{p}</w:t></w:r></w:p>' for p in paras)
        return (f'<?xml version="1.0" encoding="UTF-8"?>'
                f'<w:document xmlns:w="{W_NS}"><w:body>{body}</w:body></w:document>')
    with zipfile.ZipFile(path, "w") as z:
        z.writestr("[Content_Types].xml", "<Types/>")
        z.writestr("word/document.xml", part(paragraphs))
        if header:
            z.writestr("word/header1.xml", part(header))


def make_voice(root, version="1.4.0", checker=None, full_check=False):
    folder = Path(root) / "plainspeak-writer"
    (folder / "references").mkdir(parents=True)
    (folder / "scripts").mkdir()
    (folder / "SKILL.md").write_text("---\nname: plainspeak-writer\n---\n# x\n", encoding="utf-8")
    (folder / "references" / "tells.md").write_text("# Tells\n", encoding="utf-8")
    if full_check:
        # From 1.5 on, the full check has its own file instead of a section of tells.md.
        (folder / "references" / "full-check.md").write_text("# The full check\n", encoding="utf-8")
    (folder / "CHANGELOG.md").write_text(f"# Changelog\n\n## {version} · test\n", encoding="utf-8")
    script = checker or textwrap.dedent('''\
        import sys
        args = sys.argv[1:]
        surface = args[args.index("--surface") + 1]
        text = open(args[-1], encoding="utf-8").read()
        print("fake checker surface:", surface)
        if "HARDWORD" in text:
            print("HARD FAIL (1): fake")
            sys.exit(1)
        print("RESULT: PASS")
        sys.exit(0)
        ''')
    (folder / "scripts" / "check_voice.py").write_text(script, encoding="utf-8")
    return folder


def run(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = bp.main(argv)
        except SystemExit as exc:
            code = exc.code
    return code, out.getvalue(), err.getvalue()


def packet_from(stdout):
    match = re.search(r"^Packet: (.+)$", stdout, re.MULTILINE)
    return Path(match.group(1).strip()) if match else None


class BuildPacketTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.out = self.dir / "packets"
        self.piece = self.dir / "my letter v3.txt"
        # Written as bytes, so the file holds \r\n on every system. In text mode,
        # Windows turns each \n into \r\n, and the file would hold \r\r\n.
        self.piece.write_bytes(b"Dear team,\r\nI ran the clinic.\r\n")

    def tearDown(self):
        self.tmp.cleanup()

    def base(self, *extra):
        return ["--type", "letter", "--piece", str(self.piece), "--out", str(self.out),
                "--no-voice", *extra]

    def test_text_piece_copied_with_line_endings_fixed(self):
        code, out, _ = run(self.base())
        self.assertEqual(code, 0)
        folder = packet_from(out)
        # Read as bytes, because a text-mode read turns \r\n into \n and would
        # hide a line ending the script left unfixed.
        self.assertEqual((folder / "piece.txt").read_bytes(),
                         b"Dear team,\nI ran the clinic.\n")

    def test_message_line_is_exact(self):
        code, out, _ = run(self.base())
        folder = packet_from(out)
        self.assertIn(f"Review the packet in {folder}. Read manifest.md first.", out.splitlines())

    def test_docx_text_and_header_note(self):
        docx = self.dir / "letter.docx"
        make_docx(docx, ["First line — with a dash", "Second\tline"], header=["Jane Doe"])
        code, out, _ = run(["--type", "letter", "--piece", str(docx), "--out", str(self.out),
                            "--no-voice"])
        self.assertEqual(code, 0)
        folder = packet_from(out)
        text = (folder / "piece.txt").read_text(encoding="utf-8")
        self.assertEqual(text, "First line — with a dash\nSecond\tline\n")
        self.assertIn("header or footer", (folder / "manifest.md").read_text(encoding="utf-8"))

    def test_pdf_refused(self):
        pdf = self.dir / "letter.pdf"
        pdf.write_bytes(b"%PDF-1.4")
        code, _, err = run(["--type", "letter", "--piece", str(pdf), "--out", str(self.out)])
        self.assertEqual(code, 2)
        self.assertIn("PDF", err)

    def test_missing_piece_refused(self):
        code, _, err = run(["--type", "letter", "--piece", str(self.dir / "nope.txt"),
                            "--out", str(self.out), "--no-voice"])
        self.assertEqual(code, 2)
        self.assertIn("Can't find", err)

    def test_empty_piece_refused(self):
        empty = self.dir / "empty.txt"
        empty.write_text("\n\n", encoding="utf-8")
        code, _, _ = run(["--type", "letter", "--piece", str(empty), "--out", str(self.out),
                          "--no-voice"])
        self.assertEqual(code, 2)

    def test_no_field_for_notes(self):
        for flag in ("--notes", "--note", "--context", "--summary"):
            code, _, _ = run(self.base(flag, "this letter leads with the clinic"))
            self.assertEqual(code, 2, flag)

    def test_original_file_names_left_out(self):
        companion = self.dir / "resume-leads-with-clinic-wins.txt"
        companion.write_text("Resume text\n", encoding="utf-8")
        code, out, _ = run(self.base("--companion", str(companion)))
        folder = packet_from(out)
        names = sorted(p.name for p in folder.iterdir())
        self.assertEqual(names, ["companion-1.txt", "manifest.md", "piece.txt"])
        manifest = (folder / "manifest.md").read_text(encoding="utf-8")
        self.assertNotIn("leads-with", manifest)
        self.assertNotIn("my letter v3", manifest)

    def test_strategy_name_warns(self):
        notes = self.dir / "positioning-notes.md"
        notes.write_text("Lead with the clinic numbers.\n", encoding="utf-8")
        code, out, _ = run(self.base("--companion", str(notes)))
        self.assertEqual(code, 0)
        self.assertIn("Warning:", out)

    def test_no_voice_marks_voice_unchecked(self):
        code, out, _ = run(self.base())
        folder = packet_from(out)
        manifest = (folder / "manifest.md").read_text(encoding="utf-8")
        self.assertIn("Voice rules: not found. Voice is unchecked.", manifest)
        self.assertFalse((folder / "checker.txt").exists())

    def test_voice_dir_runs_checker_with_mapped_surface(self):
        voice = make_voice(self.dir / "skills")
        expected = {"letter": "letter", "resume": "resume", "outreach": "letter", "blurb": "blurb",
                    "linkedin": "linkedin", "answer": "general", "other": "general"}
        for kind, surface in expected.items():
            code, out, _ = run(["--type", kind, "--piece", str(self.piece), "--out", str(self.out),
                                "--voice-dir", str(voice)])
            self.assertEqual(code, 0, kind)
            folder = packet_from(out)
            checker = (folder / "checker.txt").read_text(encoding="utf-8")
            self.assertIn(f"fake checker surface: {surface}", checker, kind)
            self.assertIn("exit code 0", checker, kind)
            manifest = (folder / "manifest.md").read_text(encoding="utf-8")
            self.assertIn("plainspeak-writer 1.4.0", manifest, kind)
            self.assertIn(str(voice / "references" / "tells.md"), manifest, kind)

    def test_checker_exit_code_recorded(self):
        voice = make_voice(self.dir / "skills")
        self.piece.write_text("This has HARDWORD in it.\n", encoding="utf-8")
        code, out, _ = run(["--type", "letter", "--piece", str(self.piece), "--out", str(self.out),
                            "--voice-dir", str(voice)])
        folder = packet_from(out)
        self.assertIn("exit code 1", (folder / "checker.txt").read_text(encoding="utf-8"))

    def test_full_check_named_when_it_has_its_own_file(self):
        voice = make_voice(self.dir / "skills", version="1.5", full_check=True)
        code, out, _ = run(["--type", "letter", "--piece", str(self.piece), "--out", str(self.out),
                            "--voice-dir", str(voice)])
        self.assertEqual(code, 0)
        manifest = (packet_from(out) / "manifest.md").read_text(encoding="utf-8")
        self.assertIn(f"Rules file: {voice / 'references' / 'tells.md'}", manifest)
        self.assertIn(f"- Full check: {voice / 'references' / 'full-check.md'}", manifest)

    def test_no_full_check_line_when_the_rules_file_holds_it(self):
        voice = make_voice(self.dir / "skills")
        code, out, _ = run(["--type", "letter", "--piece", str(self.piece), "--out", str(self.out),
                            "--voice-dir", str(voice)])
        manifest = (packet_from(out) / "manifest.md").read_text(encoding="utf-8")
        self.assertNotIn("Full check:", manifest)

    def test_a_checker_that_stops_points_at_the_full_check(self):
        broken = "import sys\nprint('boom', file=sys.stderr)\nsys.exit(3)\n"
        expected = {False: "Run the full check in the rules file by hand.",
                    True: "Run the full check by hand, from the file the Full check line names."}
        for split, line in expected.items():
            voice = make_voice(self.dir / f"split-{split}", checker=broken, full_check=split)
            code, out, _ = run(["--type", "letter", "--piece", str(self.piece), "--out", str(self.out),
                                "--voice-dir", str(voice)])
            self.assertEqual(code, 0, split)
            folder = packet_from(out)
            self.assertIn(line, (folder / "manifest.md").read_text(encoding="utf-8"), split)
            self.assertFalse((folder / "checker.txt").exists(), split)

    def test_unknown_surface_falls_back_to_general(self):
        script = textwrap.dedent('''\
            import sys
            args = sys.argv[1:]
            surface = args[args.index("--surface") + 1]
            if surface != "general":
                print("error: argument --surface: invalid choice", file=sys.stderr)
                sys.exit(2)
            print("fake checker surface:", surface)
            sys.exit(0)
            ''')
        voice = make_voice(self.dir / "skills", checker=script)
        code, out, _ = run(["--type", "letter", "--piece", str(self.piece), "--out", str(self.out),
                            "--voice-dir", str(voice)])
        folder = packet_from(out)
        manifest = (folder / "manifest.md").read_text(encoding="utf-8")
        self.assertIn("surface letter wasn't accepted", manifest)

    def test_discovery_finds_each_layout_and_picks_newest(self):
        home = self.dir / "home" / ".claude"
        standalone = make_voice(home / "skills", version="1.3.1")
        synced = make_voice(home / "skills" / "synced" / "bucket", version="1.3")
        in_plugin = make_voice(home / "plugins" / "cache" / "market" / "a-plugin" / "1.0.0" / "skills",
                               version="1.4.0")
        found = bp.find_voice_dirs([home / "skills", home / "plugins"])
        self.assertEqual(sorted(map(str, found)), sorted(map(str, [standalone, synced, in_plugin])))
        self.assertEqual(bp.choose_voice_dir(found), in_plugin)

    def test_discovery_finds_a_skill_uploaded_to_the_desktop_app(self):
        # The Claude desktop app keeps a skill uploaded under Customize here.
        sessions = self.dir / "AppData" / "Roaming" / "Claude" / "local-agent-mode-sessions"
        uploaded = make_voice(sessions / "skills-plugin" / "org-id" / "user-id" / "skills", version="1.5")
        self.assertEqual(bp.find_voice_dirs([sessions]), [uploaded])

    def test_default_roots_include_the_desktop_apps_folder(self):
        home = self.dir / "home"
        env = {"APPDATA": str(self.dir / "AppData" / "Roaming"),
               "HOME": str(home), "USERPROFILE": str(home)}
        with mock.patch.dict(os.environ, env):
            os.environ.pop("CLAUDE_CONFIG_DIR", None)
            roots = bp.default_roots()
        self.assertIn(self.dir / "AppData" / "Roaming" / "Claude" / "local-agent-mode-sessions", roots)
        self.assertIn(home / "Library" / "Application Support" / "Claude" / "local-agent-mode-sessions", roots)
        self.assertIn(home / ".config" / "Claude" / "local-agent-mode-sessions", roots)

    def test_packet_finds_a_skill_uploaded_to_the_desktop_app_on_its_own(self):
        appdata = self.dir / "AppData" / "Roaming"
        sessions = appdata / "Claude" / "local-agent-mode-sessions"
        make_voice(sessions / "skills-plugin" / "org-id" / "user-id" / "skills", version="1.5",
                   full_check=True)
        home = self.dir / "home"
        home.mkdir()
        env = {"APPDATA": str(appdata), "HOME": str(home), "USERPROFILE": str(home)}
        with mock.patch.dict(os.environ, env):
            os.environ.pop("CLAUDE_CONFIG_DIR", None)
            code, out, _ = run(["--type", "letter", "--piece", str(self.piece), "--out", str(self.out)])
        self.assertEqual(code, 0)
        manifest = (packet_from(out) / "manifest.md").read_text(encoding="utf-8")
        self.assertIn("Voice rules: plainspeak-writer 1.5. Rules file: ", manifest)
        self.assertIn("local-agent-mode-sessions", manifest)
        self.assertIn("- Full check: ", manifest)

    def test_discovery_skips_a_folder_with_another_skill_name(self):
        impostor = make_voice(self.dir / "roots")
        (impostor / "SKILL.md").write_text("---\nname: something-else\n---\n", encoding="utf-8")
        self.assertEqual(bp.find_voice_dirs([self.dir / "roots"]), [])

    def test_limit_over_and_under(self):
        code, out, _ = run(self.base("--channel", "textbox", "--limit", "10"))
        manifest = (packet_from(out) / "manifest.md").read_text(encoding="utf-8")
        self.assertRegex(manifest, r"which is \d+ over the limit")
        code, out, _ = run(self.base("--channel", "textbox", "--limit", "5000"))
        manifest = (packet_from(out) / "manifest.md").read_text(encoding="utf-8")
        self.assertIn("which fits", manifest)

    def test_readers_validated(self):
        code, _, err = run(self.base("--readers", "recruiter,friend"))
        self.assertEqual(code, 2)
        code, out, _ = run(self.base("--readers", "grader"))
        manifest = (packet_from(out) / "manifest.md").read_text(encoding="utf-8")
        self.assertIn("Readers: AI grader (chosen by the person).", manifest)

    def test_no_target_says_general_reader(self):
        code, out, _ = run(self.base())
        manifest = (packet_from(out) / "manifest.md").read_text(encoding="utf-8")
        self.assertIn("Target: none given.", manifest)

    def test_real_checker_when_available(self):
        real = REPO.parent / "plainspeak-writer"
        if not bp.is_voice_dir(real):
            self.skipTest("plainspeak-writer isn't next to this repository")
        self.piece.write_text("Dear team,\nI ran the clinic — every shift.\n", encoding="utf-8")
        code, out, _ = run(["--type", "letter", "--piece", str(self.piece), "--out", str(self.out),
                            "--voice-dir", str(real)])
        self.assertEqual(code, 0)
        checker = (packet_from(out) / "checker.txt").read_text(encoding="utf-8")
        self.assertIn("R01", checker)
        self.assertIn("exit code 1", checker)


if __name__ == "__main__":
    unittest.main(verbosity=2)
