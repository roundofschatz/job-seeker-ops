"""Tests for skills/cover-letter/scripts/check_letter.py and build_letter.py.

    python tests/unit/test_check_letter.py

Standard library only. The example letter in the skill's references/letter.md
is checked against writer B's files in tests/writers/b-okafor and the example
positioning file in candidate-positioning's references/format.md, so a change
to any of them shows up here. The tests that run the real plainspeak-writer
checker skip when no copy sits next to this repository.
"""
import contextlib
import importlib.util
import io
import re
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILL = REPO / "skills" / "cover-letter"
WRITER = REPO / "tests" / "writers" / "b-okafor"
POSITIONING = "positioning-switchgrass-freight-supply-chain-planning-analyst.md"
SOURCES = ("posting.txt", "resume.txt", "career-record.md", "positioning-notes.md")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cl = load("check_letter", SKILL / "scripts" / "check_letter.py")
bl = load("build_letter", SKILL / "scripts" / "build_letter.py")


def fenced(path, heading, lang):
    text = path.read_text(encoding="utf-8")
    body = text.split(heading, 1)[1]
    return re.search(r"```" + lang + r"\n(.*?)\n```", body, re.S).group(1) + "\n"


def example_positioning():
    return fenced(REPO / "skills" / "candidate-positioning" / "references" / "format.md",
                  "## A full example", "markdown")


def example_letter():
    return fenced(SKILL / "references" / "letter.md", "## A full example", "text")


def run(module, argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        try:
            code = module.main([str(a) for a in argv])
        except SystemExit as exc:
            code = exc.code
    return code, out.getvalue(), err.getvalue()


# A stand-in for plainspeak-writer's checker that blocks the word BADWORD.
FAKE_CHECKER = '''import sys
args = sys.argv[1:]
lines = open(args[-1], encoding="utf-8").read().split("\\n")
hits = [i for i, line in enumerate(lines, 1) if "BADWORD" in line]
print("check_voice 9.9   surface: letter")
if hits:
    print("HARD FAIL (%d):" % len(hits))
    for i in hits:
        print('  L%d: [X01 test word] "BADWORD": a test hit' % i)
    sys.exit(1)
print("RESULT: PASS")
'''


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        for name in SOURCES:
            shutil.copy(WRITER / name, self.dir / name)
        self.pos = self.dir / POSITIONING
        self.pos.write_text(example_positioning(), encoding="utf-8")
        self.letter = self.dir / "letter.txt"
        self.write(example_letter())

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, text, path=None):
        (path or self.letter).write_bytes(text.encode("utf-8"))

    def edit(self, old, new, path=None):
        path = path or self.letter
        text = path.read_text(encoding="utf-8")
        self.assertEqual(text.count(old), 1, old)
        self.write(text.replace(old, new), path)

    def check(self, *flags, letter=True):
        args = ([self.letter] if letter else []) + ["--positioning", self.pos, *flags]
        return run(cl, args)

    def voice(self):
        folder = self.dir / "skills" / "plainspeak-writer"
        (folder / "references").mkdir(parents=True)
        (folder / "scripts").mkdir()
        (folder / "SKILL.md").write_text("---\nname: plainspeak-writer\n---\n# x\n", encoding="utf-8")
        (folder / "references" / "tells.md").write_text("# Tells\n", encoding="utf-8")
        (folder / "CHANGELOG.md").write_text("# Changelog\n\n## 9.9 · test\n", encoding="utf-8")
        (folder / "scripts" / "check_voice.py").write_text(FAKE_CHECKER, encoding="utf-8")
        return folder

    def assertFails(self, out, words):
        fails = out.split("WARN (")[0].split("INFO (")[0]
        self.assertIn("FAIL", fails, out)
        self.assertIn(words, fails, out)


class ExampleTests(Base):
    def test_the_example_letter_passes(self):
        code, out, _ = self.check()
        self.assertEqual(code, 0, out)
        self.assertIn("Body: 350 words in 4 paragraph(s)", out)
        self.assertIn("Paragraph 3 follows resume line 14 closely", out)
        self.assertIn("52 (paragraph 2) comes from P1's deeper record", out)

    def test_before_drafting(self):
        code, out, _ = self.check(letter=False)
        self.assertEqual(code, 0, out)
        self.assertIn("resume.txt is the resume the case was built from, unchanged", out)
        self.assertIn("DMITRI OKAFOR / Kansas City, MO", out)

    def test_parts(self):
        letter = cl.Letter(self.letter)
        self.assertEqual(letter.header[0], "Dmitri Okafor")
        self.assertEqual(letter.date, "October 7, 2026")
        self.assertEqual(letter.salutation, "Dear Switchgrass Freight hiring team,")
        self.assertEqual((letter.sign_off, letter.name), ("Best", "Dmitri Okafor"))
        self.assertEqual(len(letter.paragraphs), 4)


class GateTests(Base):
    def test_a_resume_that_disagrees_with_a_proof_is_caught_before_drafting(self):
        final = self.dir / "resume-final.txt"
        shutil.copy(self.dir / "resume.txt", final)
        self.edit("from 31% to 19%", "from 31% to 21%", final)
        code, out, _ = run(cl, ["--positioning", self.pos, "--resume", final])
        self.assertEqual(code, 1, out)
        self.assertFails(out, "P1's result gives 19%")
        self.assertIn("resume-final.txt isn't the resume the case was built from", out)

    def test_a_changed_stamped_resume_is_caught(self):
        with open(self.dir / "resume.txt", "ab") as f:
            f.write(b"Spanish (conversational)\n")
        code, out, _ = self.check(letter=False)
        self.assertFails(out, "resume.txt has changed since the case was confirmed")


class FactTests(Base):
    def test_a_number_in_no_file_fails(self):
        self.edit("over 52 weeks the error came down to 19%", "over 52 weeks the error came down to 15%")
        code, out, _ = self.check()
        self.assertFails(out, "15% (paragraph 2) isn't in the three files")

    def test_a_figure_the_file_and_the_resume_disagree_on_fails(self):
        final = self.dir / "resume-final.txt"
        shutil.copy(self.dir / "resume.txt", final)
        self.edit("from 2.8% to 0.9%", "from 2.8% to 1.1%", final)
        code, out, _ = self.check("--resume", final)
        self.assertFails(out, "0.9% (paragraph 3) is in P3")

    def test_a_wrong_company_fails(self):
        self.edit("Dear Switchgrass Freight hiring team,", "Dear Quillmoor Freight hiring team,")
        self.edit("I can do that for Switchgrass's lanes", "I can do that for Quillmoor's lanes")
        code, out, _ = self.check()
        self.assertFails(out, "The salutation names \"Quillmoor Freight\"")
        self.assertFails(out, "\"Quillmoor\" (paragraph 4) isn't in the three files")

    def test_a_name_the_person_gave_passes_with_given(self):
        self.edit("Dear Switchgrass Freight hiring team,", "Dear Maria Lopez,")
        code, out, _ = self.check()
        self.assertFails(out, "The salutation names \"Maria Lopez\"")
        code, out, _ = self.check("--given", "Maria Lopez")
        self.assertEqual(code, 0, out)

    def test_names_split_at_and(self):
        self.edit("I rebuilt it in SQL and Excel", "I rebuilt it in Excel and Power BI")
        code, out, _ = self.check()
        self.assertNotIn("Excel and Power BI", out)

    def test_a_stale_count_of_years_fails(self):
        self.edit("which is the work I've done at Brightwell Grocers Distribution since 2021.",
                  "which is the work I've done at Brightwell Grocers Distribution for eight years.")
        code, out, _ = self.check()
        self.assertFails(out, "a count of 8 years that the three files don't give")

    def test_a_count_of_years_the_file_works_out_passes(self):
        self.edit("which is the work I've done at Brightwell Grocers Distribution since 2021.",
                  "which is the work I've done at Brightwell Grocers Distribution for about five years.")
        code, out, _ = self.check()
        self.assertNotIn("count of 5 years", out)

    def test_a_keep_off_phrase_fails(self):
        self.edit("Before I forecast anything,", "I'm new to freight, but before I forecast anything,")
        code, out, _ = self.check()
        self.assertFails(out, "\"new to freight\" is in the letter")

    def test_a_restated_resume_line_fails(self):
        self.edit("I ran the cycle counts in Manhattan WMS for a Brightwell warehouse,",
                  "Ran cycle counts in Manhattan WMS for a 410,000-square-foot warehouse. Also,")
        code, out, _ = self.check()
        self.assertFails(out, "restates resume line 14")

    def test_the_firm_or_the_seat_comes_early(self):
        self.edit("Last year Switchgrass's forecasts missed", "Last year the forecasts missed")
        code, out, _ = self.check()
        self.assertFails(out, "name neither the firm nor the seat")

    def test_a_referral_comes_early(self):
        code, out, _ = self.check("--referral", "Dana Ruiz")
        self.assertFails(out, "The referral, Dana Ruiz, belongs in the first two sentences")

    def test_the_last_sentence_asks(self):
        self.edit("I'd like to talk about the lanes your forecasts miss most, and what the weekly forecast "
                  "would need to get right to staff the Saturday docks at your six terminals.",
                  "Thank you for reading about the Saturday docks at your six terminals.")
        code, out, _ = self.check()
        self.assertIn("The last sentence should ask for a conversation", out)


class ShapeTests(Base):
    def test_a_placeholder_fails(self):
        self.edit("and I write the one-page weekly note", "and [a second result] and I write the one-page weekly note")
        code, out, _ = self.check()
        self.assertFails(out, "a bracketed slot is still in the letter")

    def test_a_sentence_said_twice_fails(self):
        self.edit("I find the input behind a forecast miss and fix it, and I can do that for Switchgrass's lanes.",
                  "I find the input behind a forecast miss and fix it, and I can do that for Switchgrass's lanes. "
                  "I rebuilt it in SQL and Excel and added store promotions as an input, since the old "
                  "forecast never saw them.")
        code, out, _ = self.check()
        self.assertFails(out, "word for word")

    def test_over_the_cap_fails_and_under_the_floor_fails(self):
        para = example_letter().split("\n\n")[5]
        self.edit(para, "\n\n".join([para] * 3))
        code, out, _ = self.check()
        self.assertFails(out, "over the 500-word cap")
        self.write(example_letter().replace(para + "\n\n", ""))
        code, out, _ = self.check()
        self.assertFails(out, "under plainspeak-writer's floor of 250")

    def test_to_whom_it_may_concern_fails(self):
        self.edit("Dear Switchgrass Freight hiring team,", "To Whom It May Concern:")
        code, out, _ = self.check()
        self.assertFails(out, "name a person, or else the firm's hiring team")

    def test_the_header_matches_the_resume(self):
        self.edit("(816) 555-0172", "(816) 555-0199")
        code, out, _ = self.check()
        self.assertFails(out, "The header's phone doesn't match")
        self.edit("Best,\nDmitri Okafor", "Best,\nDmitri O. Kafor")
        code, out, _ = self.check()
        self.assertFails(out, "The letter is signed \"Dmitri O. Kafor\"")

    def test_no_salutation_stops_the_checks(self):
        self.edit("Dear Switchgrass Freight hiring team,\n", "")
        code, out, _ = self.check()
        self.assertFails(out, "No salutation found")


class ChannelTests(Base):
    def text_box(self):
        text = example_letter()
        self.write(text[text.index("Dear "):])

    def test_a_text_box_letter_fits_its_limit(self):
        self.text_box()
        code, out, _ = self.check("--channel", "textbox", "--limit", "2500")
        self.assertEqual(code, 0, out)
        self.assertIn("inside the limit of 2,500", out)
        code, out, _ = self.check("--channel", "textbox", "--limit", "1500")
        self.assertFails(out, "the limit is 1,500")

    def test_a_text_box_drops_bold_and_curly_quotes(self):
        self.text_box()
        self.edit("I find the input", "I **find** the input")
        self.edit("Switchgrass's lanes", "Switchgrass" + chr(0x2019) + "s lanes")
        code, out, _ = self.check("--channel", "textbox")
        self.assertFails(out, "drops bold and bullets")
        self.assertFails(out, "Use straight quotes")

    def test_an_upload_letter_has_its_contact_block(self):
        self.text_box()
        code, out, _ = self.check("--channel", "upload")
        self.assertFails(out, "opens with the contact block")

    def test_an_email_letter_has_a_subject(self):
        self.text_box()
        code, out, _ = self.check("--channel", "email")
        self.assertFails(out, "needs a first line like 'Subject:")
        self.write("Subject: Supply Chain Planning Analyst application\n\n" + self.letter.read_text(encoding="utf-8"))
        code, out, _ = self.check("--channel", "email")
        self.assertEqual(code, 0, out)


class ReuseTests(Base):
    def test_a_shared_frame_fails_and_a_shared_proof_is_listed(self):
        other = self.dir / "letter-other.txt"
        first = example_letter().split("\n\n")[3]
        proof = "I rebuilt it in SQL and Excel and added store promotions as an input, since the old forecast never saw them."
        other.write_text("Dear Quillmoor Logistics hiring team,\n\n" + first + "\n\n" + proof +
                         "\n\nI'd like to talk.\n\nBest,\nDmitri Okafor\n", encoding="utf-8")
        code, out, _ = self.check("--compare", other)
        self.assertFails(out, "The frame shares a sentence with letter-other.txt")
        self.assertIn("Paragraph 2 shares a sentence with letter-other.txt", out)

    def test_a_shared_sentence_from_a_sample_must_hold_its_fact(self):
        sample = self.dir / "old-letter.txt"
        sample.write_text("March 2, 2023\n\nDear Hiring Team,\n\nI've forecast weekly demand at Brightwell for "
                          "two years now.\n\nBest,\nDmitri\n", encoding="utf-8")
        self.edit("Before I forecast anything,", "I've forecast weekly demand at Brightwell for two years now. "
                  "Before I forecast anything,")
        code, out, _ = self.check("--sample", sample, "--voice-dir", self.voice())
        self.assertFails(out, "a count of 2 years that the three files don't give")
        self.assertIn("runs on time", out)

    def test_a_blocked_sample_sentence_is_set_aside_and_never_moves(self):
        sample = self.dir / "old-letter.txt"
        sample.write_text("Dear Hiring Team,\n\nWe BADWORD the forecast every single week to stay ahead.\n\n"
                          "Best,\nDmitri\n", encoding="utf-8")
        code, out, _ = run(cl, ["--positioning", self.pos, "--sample", sample, "--voice-dir", self.voice()])
        self.assertIn("set aside: \"We BADWORD the forecast every single week to stay ahead.\"", out)
        self.edit("Before I forecast anything,", "We BADWORD the forecast every single week to stay ahead. "
                  "Before I forecast anything,")
        code, out, _ = self.check("--sample", sample, "--voice-dir", self.voice_again())
        self.assertFails(out, "holds a sentence plainspeak-writer blocks in old-letter.txt")

    def voice_again(self):
        return self.dir / "skills" / "plainspeak-writer"


class VoiceTests(Base):
    def test_the_voice_check_maps_hard_hits(self):
        self.edit("I find the input", "I BADWORD find the input")
        code, out, _ = self.check("--voice", "--voice-dir", self.voice())
        self.assertFails(out, "[X01 test word]")

    def test_the_real_checker_passes_the_example(self):
        real = REPO.parent / "plainspeak-writer"
        if not (real / "scripts" / "check_voice.py").is_file():
            self.skipTest("plainspeak-writer isn't next to this repository")
        code, out, _ = self.check("--voice", "--voice-dir", real)
        self.assertEqual(code, 0, out)
        self.assertIn("0 HARD hit(s)", out)


class WordTests(Base):
    def build(self, *extra):
        return run(bl, [self.letter, "--company", "Switchgrass Freight Co.", "--out", self.dir / "out", *extra])

    def test_the_word_file(self):
        code, out, _ = self.build("--resume", self.dir / "resume.txt")
        self.assertEqual(code, 0, out)
        docx = self.dir / "out" / "Dmitri_Okafor_CoverLetter_SwitchgrassFreight.docx"
        self.assertTrue(docx.is_file(), out)
        self.assertIn("Calibri 11 and one-inch margins, since the resume isn't a Word file", out)
        with zipfile.ZipFile(docx) as archive:
            self.assertEqual(set(archive.namelist()), set(bl.PARTS))
            core = archive.read("docProps/core.xml").decode("utf-8")
            app = archive.read("docProps/app.xml").decode("utf-8")
        self.assertIn("<dc:creator>Dmitri Okafor</dc:creator>", core)
        self.assertNotIn("<Application>", app)
        self.assertIn("Author: Dmitri Okafor", out)
        text = (self.dir / "out" / "Dmitri_Okafor_CoverLetter_SwitchgrassFreight.txt").read_text(encoding="utf-8")
        self.assertNotIn(chr(0x2019), text)
        code, out, _ = run(cl, [docx, "--positioning", self.pos])
        self.assertEqual(code, 0, out)
        self.assertIn("Body: 350 words in 4 paragraph(s)", out)
        self.assertFalse(list((self.dir / "out").glob("*.pdf")))

    def test_the_word_file_takes_a_word_resume_look(self):
        resume = self.dir / "resume.docx"
        paras = [("Dmitri Okafor", 16, True, 0, 3), ("Kansas City, MO | (816) 555-0172", 10.5, False, 0, 3),
                 ("Planning analyst who rebuilt a weekly forecast and cut its error from 31% to 19%.", 10.5, False, 0, 3)]
        layout = dict(bl.DEFAULT, font="Georgia", size=10.5, margins=(720, 720, 720, 720))
        resume.write_bytes(bl.docx_bytes(paras, layout, "Dmitri Okafor"))
        code, out, _ = self.build("--resume", resume)
        self.assertEqual(code, 0, out)
        self.assertIn("the font, size and margins of resume.docx (Georgia 10.5 point)", out)

    def test_the_build_refuses_a_placeholder_and_a_long_letter(self):
        self.edit("I find the input", "[your opener] I find the input")
        code, out, _ = self.build()
        self.assertEqual(code, 1)
        self.assertIn("BUILD REFUSED", out)
        self.write(example_letter())
        para = example_letter().split("\n\n")[5]
        self.edit(para, "\n\n".join([para] * 6))
        code, out, _ = self.build()
        self.assertIn("Cut words, not spacing", out)
        self.assertFalse((self.dir / "out").exists() and list((self.dir / "out").iterdir()))

    def test_an_author_field_that_names_a_tool_fails(self):
        self.build()
        docx = self.dir / "out" / "Dmitri_Okafor_CoverLetter_SwitchgrassFreight.docx"
        bad = self.dir / "bad.docx"
        with zipfile.ZipFile(docx) as src, zipfile.ZipFile(bad, "w") as dst:
            for name in src.namelist():
                data = src.read(name)
                if name == "docProps/core.xml":
                    data = data.replace(b"<dc:creator>Dmitri Okafor</dc:creator>", b"<dc:creator>python-docx</dc:creator>")
                if name == "word/document.xml":
                    data = data.replace(b"<w:body>", b"<w:body><w:tbl><w:tr><w:tc><w:p/></w:tc></w:tr></w:tbl>")
                dst.writestr(name, data)
        code, out, _ = run(cl, [bad])
        self.assertFails(out, "a tool rather than the writer")
        self.assertFails(out, "holds a table")

    def test_the_estimate_leans_toward_more_lines(self):
        words = ("forecast " * 400).strip()
        pages, lines = cl.estimate_pages([(words, 11, 0, 0)], "calibri", (1440,) * 4, (12240, 15840))
        # 400 nine-letter words at 11 point Calibri fill about 34 lines of 6.5 inches.
        self.assertGreaterEqual(lines, 34)
        self.assertLess(pages, 1)
        self.assertGreater(cl.estimate_pages([(words, 11, 0, 0)] * 2, "calibri", (1440,) * 4,
                                             (12240, 15840))[0], 1)


class TextTests(unittest.TestCase):
    def test_numbers(self):
        digits, spelled = cl.numbers("Cut variance from 2.8% to 0.9% across 1,900 items, 44 percent, for four years.")
        self.assertEqual(digits, {"2.8%", "0.9%", "1900", "44%"})
        self.assertEqual(spelled, {"4"})

    def test_year_counts_and_month_years(self):
        self.assertEqual(cl.year_counts("eight years of teaching, and for the last two I've led it; 13 years"),
                         {"8", "2", "13"})
        self.assertEqual(cl.month_years("Opened it in March 2022 and by Aug 2022 it held."), {"mar 2022", "aug 2022"})

    def test_name_runs(self):
        runs = dict(cl.name_runs("At Cottonwood Springs Middle School I've led Basalt Creek's sessions."))
        self.assertIn("Cottonwood Springs Middle School", runs)
        self.assertIn("Basalt Creek", runs)
        self.assertNotIn("I've", runs)

    def test_file_stem(self):
        self.assertEqual(bl.file_stem("GRAHAM WHITFIELD, PE", "Calder Basin Water Authority"),
                         "GRAHAM_WHITFIELD_CoverLetter_CalderBasinWaterAuthority")
        self.assertEqual(bl.file_stem("Renata Castillo", "Ironwood Trail Supply Co."),
                         "Renata_Castillo_CoverLetter_IronwoodTrailSupply")


if __name__ == "__main__":
    unittest.main(verbosity=2)
