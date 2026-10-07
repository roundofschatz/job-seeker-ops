"""cover-letter's sources: every ID a file cites has a row in
references/sources.md, every row is cited somewhere, and each row's "Used in"
list names exactly the files that cite it.

    python tests/unit/test_cover_letter_sources.py
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SKILL = REPO / "skills" / "cover-letter"
SOURCES = SKILL / "references" / "sources.md"
CITED_IN = [SKILL / "SKILL.md", SKILL / "references" / "letter.md", SKILL / "references" / "checks.md",
            REPO / "README.md"]


def rows():
    out = {}
    for line in SOURCES.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(r"C\d\d", cells[0]):
            out[cells[0]] = {c.strip() for c in cells[-1].split(",") if c.strip()}
    return out


def citations():
    found = {}
    for path in CITED_IN:
        text = path.read_text(encoding="utf-8")
        for group in re.findall(r"\[(C\d\d(?:,\s*C\d\d)*)\]", text):
            for cid in re.findall(r"C\d\d", group):
                found.setdefault(cid, set()).add(path.name)
    return found


class Sources(unittest.TestCase):
    def test_every_cited_id_has_a_row(self):
        missing = sorted(set(citations()).difference(rows()))
        self.assertEqual(missing, [], "cited but not in sources.md")

    def test_every_row_is_cited(self):
        unused = sorted(set(rows()).difference(citations()))
        self.assertEqual(unused, [], "in sources.md but cited nowhere")

    def test_used_in_lists_are_right(self):
        cited = citations()
        for cid, used in rows().items():
            self.assertEqual(used, cited.get(cid, set()), f"{cid}'s 'Used in' list")

    def test_every_row_has_a_web_address_and_a_date(self):
        for line in SOURCES.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells and re.fullmatch(r"C\d\d", cells[0]):
                self.assertRegex(cells[6], r"https?://", cells[0])
                self.assertRegex(cells[2], r"\d{4}|undated", cells[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
