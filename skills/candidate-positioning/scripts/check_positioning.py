#!/usr/bin/env python3
"""Check a positioning file from the candidate-positioning skill.

    python check_positioning.py positioning-acme-demand-planner.md
    python check_positioning.py FILE --sources       each quote against its file and line
    python check_positioning.py FILE --current       whether a source changed since the stamp
    python check_positioning.py FILE --against old-letter.txt
    python check_positioning.py FILE --voice         plainspeak-writer on the reused sentences
    python check_positioning.py FILE --for cover-letter
    python check_positioning.py FILE --piece letter.docx --as letter
    python check_positioning.py FILE --check-links   open each firm-fact link
    python check_positioning.py FILE --json
    python check_positioning.py --name "Acme Co." "Demand Planner"

The shape check always runs. It wants the eight sections in order, a source on
every requirement row and every proof, a story and a date on every proof, each
gap and the concern in section 7 with phrases to watch for, the case in four
lines, and the stamp. It also fails a sentence of the file's own that shows up
twice, word for word. When cover-letter has added section 9, each letter's
record there needs its labelled lines and its map, and a finished record needs
its checks and its text.

Exit code 0 means no FAIL, 1 means at least one, and 2 means the input needs
fixing. Python 3.8 or newer, standard library only. The format is described in
references/format.md, next to this script's folder.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

__version__ = "0.3.0"
FORMAT = "1"

SECTIONS = ["Target", "Requirement map", "The hiring team's view", "The case in four lines",
            "Proof bank", "Words to use", "Keep off the page", "Stamp"]
CASE_LABELS = ["What they want", "Where the candidate stands", "The story the evidence tells",
               "What the reader should believe"]
TARGET_LABELS = ["Company", "Role", "Posting", "Measure of the job", "Channel", "Reader",
                 "What matters to the person"]
PROOF_FIELDS = ["Result", "Story", "Source", "On the resume being sent", "Use on", "Answers"]
KINDS = ("required", "preferred", "responsibility")
SHOW_ON = ("resume", "letter", "both", "off")
USE_ON = ("resume", "letter", "both")
ROLES = ("posting", "resume being sent", "deeper record", "past letter", "notes",
         "firm pages", "rulings", "other")
# Section 9, which cover-letter writes: one record per letter.
LETTER_LABELS = ["Role", "Date", "Channel", "Reader", "Resume", "Voice samples", "Status", "Built"]
MOVEMENTS = ["Frame", "Proof", "Fit and why now", "Invitation", "Referral", "Off the page"]
LETTER_HEAD = re.compile(r"^###\s+Letter\s+(\d+)\s+·\s+(.+?)\s+·\s+(\d{4}-\d{2}-\d{2})\s*$")
STATUS = re.compile(r"^(draft|ready|open findings|not reviewed|sent \d{4}-\d{2}-\d{2})\.?$", re.I)
TEXT_SUFFIXES = {".txt", ".md", ".markdown", ".text", ".csv"}
MIN_WORDS = 6          # a sentence this long or longer counts for repeats and sharing
WINDOW = 2             # lines either side of a cited line where a quote may sit
MADE_UP_HOSTS = (".example", ".test", ".invalid", ".localhost")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
MAX_DEPTH = 8
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

DATE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
QUOTE = re.compile(r'"([^"]+)"')
FIELD = re.compile(r"^\s*[-*]\s+\*\*(.+?)\*\*\s*(.*)$")
SECTION = re.compile(r"^##\s+(\d+)\.\s+(.+?)\s*$")
SUBHEAD = re.compile(r"^###\s+(.+?)\s*$")
FILE_REF = re.compile(r"^(?P<file>.+?)\s+L(?P<a>\d+)(?:-L?(?P<b>\d+))?(?:\s*\((?P<date>[^)]*)\))?$")
ANSWER_REF = re.compile(r"^A\d+$")
CURLY = str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'"})


class InputError(Exception):
    """A file the script can't read, or a format it doesn't know."""


# Reading files

def decode(data):
    for encoding in ("utf-8-sig", "cp1252"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def text_lines(text):
    return text.replace("\r\n", "\n").replace("\r", "\n").split("\n")


def docx_text(path):
    """Paragraph text from a Word file, one paragraph per line."""
    try:
        with zipfile.ZipFile(path) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
    except (zipfile.BadZipFile, KeyError, ET.ParseError) as exc:
        raise InputError(f"{path.name} isn't a readable Word file ({exc.__class__.__name__}).")
    lines = []
    for para in root.iter(W + "p"):
        parts = []
        for node in para.iter():
            if node.tag == W + "t":
                parts.append(node.text or "")
            elif node.tag == W + "tab":
                parts.append("\t")
            elif node.tag in (W + "br", W + "cr"):
                parts.append("\n")
        lines.append("".join(parts))
    return "\n".join(lines)


def read_source(path):
    """Lines of a source file, or None when it can't be read as text."""
    suffix = path.suffix.lower()
    if suffix in TEXT_SUFFIXES:
        return text_lines(decode(path.read_bytes()))
    if suffix == ".docx":
        return text_lines(docx_text(path))
    return None


def file_hash(path, length=12):
    """SHA-256 of a file. Text files are hashed with their line endings read as
    a newline and any byte-order mark dropped, so a copy saved on Windows or by
    git with CRLF line endings gets the same hash."""
    data = path.read_bytes()
    if path.suffix.lower() in TEXT_SUFFIXES:
        if data.startswith(b"\xef\xbb\xbf"):
            data = data[3:]
        data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()[:length]


# Text helpers

def norm(text):
    """Lowercase, straight quotes, one space, no pipe escapes, no list markers."""
    text = text.translate(CURLY).replace("\\|", "|").lower()
    text = re.sub(r"^\s*(?:[-*•]|\d+[.)])\s+", "", text)
    return re.sub(r"\s+", " ", text).strip().rstrip(".").strip()


def words_only(text):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s%$]", " ", text.lower())).strip()


def strip_quotes(text):
    return QUOTE.sub(" ", text.translate(CURLY))


def sentences(text):
    """Sentences of six or more words, compared in lowercase without punctuation."""
    text = re.sub(r"\s+", " ", text.translate(CURLY))
    for part in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", text):
        key = words_only(part)
        if len(key.split()) >= MIN_WORDS:
            yield key, part.strip()


def numbers_in(text):
    return {n.replace(",", "").rstrip(".") for n in re.findall(r"\d[\d,]*(?:\.\d+)?%?", text)}


def split_cells(line):
    """Cells of one row of a Markdown grid. A pipe written as \\| stays in its cell."""
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|") and not inner.endswith("\\|"):
        inner = inner[:-1]
    cells = re.split(r"(?<!\\)\|", inner)
    return [c.strip().replace("\\|", "|") for c in cells]


def is_separator(line):
    return bool(re.match(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$", line))


def slug(text):
    words = re.sub(r"[^a-z0-9]+", " ", text.lower()).split()
    while words and words[-1] in {"inc", "llc", "co", "corp", "corporation", "company",
                                  "ltd", "lp", "llp", "plc"}:
        words.pop()
    return "-".join(words)


def file_name(company, role):
    return f"positioning-{slug(company)}-{slug(role)}.md"


def is_home_page(url):
    path = urlparse(url).path.strip("/").lower()
    return path in ("", "index.html", "index.htm", "home", "en", "en-us")


# The positioning file

class Report:
    def __init__(self):
        self.fails, self.warns, self.infos = [], [], []

    def fail(self, line, tag, msg):
        self.fails.append((line, tag, msg))

    def warn(self, line, tag, msg):
        self.warns.append((line, tag, msg))

    def info(self, line, tag, msg):
        self.infos.append((line, tag, msg))


class Positioning:
    """The parsed file. Line numbers are 1-based, as an editor shows them."""

    def __init__(self, path):
        self.path = Path(path)
        if not self.path.is_file():
            raise InputError(f"{self.path} doesn't exist.")
        self.lines = text_lines(decode(self.path.read_bytes()))
        self.report = Report()
        self.sections = {}       # number: (title, first body line, last body line)
        self.format = None
        self.target = {}
        self.facts = []
        self.rows = []
        self.view = []
        self.case = {}
        self.proofs = []
        self.terms = []
        self.descriptions = []
        self.keep_off = []
        self.files = []
        self.answers = {}
        self.not_mapped = set()
        self.stamp = {}
        self.letters = []
        self.parse()

    def line(self, n):
        return self.lines[n-1] if 0 < n <= len(self.lines) else ""

    def body(self, number):
        if number not in self.sections:
            return []
        _title, start, end = self.sections[number]
        return [(n, self.line(n)) for n in range(start, end+1)]

    def parse(self):
        rep = self.report
        for n, text in enumerate(self.lines, 1):
            m = re.match(r"^Format:\s*candidate-positioning\s+(\S+)", text.strip())
            if m:
                self.format = m.group(1).rstrip(".")
                break
        if self.format is None:
            rep.fail(1, "format", "No 'Format: candidate-positioning 1' line under the title.")
        elif self.format != FORMAT:
            raise InputError(f"{self.path.name} is format {self.format}. This script reads "
                             f"format {FORMAT}.")
        if not self.lines or not self.lines[0].startswith("# Positioning:"):
            rep.fail(1, "title", "The first line should be '# Positioning: <Company> · <Role>'.")
        heads = [(n, SECTION.match(t)) for n, t in enumerate(self.lines, 1)]
        heads = [(n, m) for n, m in heads if m]
        bad = [(n, m) for n, m in heads if m.group(1) != "9" and
               (int(m.group(1)) > 8 or norm(m.group(2)) != norm(SECTIONS[int(m.group(1))-1]))]
        for n, m in bad:
            rep.fail(n, "sections", f"Unexpected section '## {m.group(1)}. {m.group(2)}'.")
        order = [int(m.group(1)) for _n, m in heads]
        expected = list(range(1, 9))
        if order[:8] != expected:
            missing = [str(i) for i in expected if i not in order]
            rep.fail(1, "sections", "The eight sections must run 1 to 8 in order"
                     + (f"; missing {', '.join(missing)}." if missing else "."))
        others = [(n, t) for n, t in enumerate(self.lines, 1)
                  if t.startswith("## ") and not SECTION.match(t)]
        for n, t in others:
            rep.fail(n, "sections", f"A '## ' heading outside the eight sections: {t.strip()}")
        for i, (n, m) in enumerate(heads):
            end = heads[i+1][0]-1 if i+1 < len(heads) else len(self.lines)
            self.sections.setdefault(int(m.group(1)), (m.group(2), n+1, end))
        self.parse_target()
        self.parse_map()
        self.parse_view()
        self.parse_case()
        self.parse_proofs()
        self.parse_words()
        self.parse_keep_off()
        self.parse_stamp()
        self.parse_letters()
        self.cross_checks()
        self.repeats()

    # Shared pieces

    def table(self, rows, need, tag, start_line):
        """The first Markdown grid in rows: a list of (line, cells), checked
        against the header names in need. Returns [] and a FAIL when absent."""
        lines = [(n, t) for n, t in rows if t.strip()]
        for i, (n, t) in enumerate(lines):
            if t.strip().startswith("|") and i+1 < len(lines) and is_separator(lines[i+1][1]):
                header = [norm(c) for c in split_cells(t)]
                if [norm(h) for h in need] != header[:len(need)]:
                    self.report.fail(n, tag, "The columns should be: " + ", ".join(need) + ".")
                    return []
                out = []
                for m, row in lines[i+2:]:
                    if not row.strip().startswith("|"):
                        break
                    cells = split_cells(row)
                    cells += [""] * (len(need)-len(cells))
                    out.append((m, cells))
                return out
        return None

    def fields(self, rows):
        """Bold-labelled bullet fields, with any continuation lines joined."""
        out, current = {}, None
        for n, t in rows:
            m = FIELD.match(t)
            if m:
                label = m.group(1).strip()
                rest = m.group(2).strip()
                if label.endswith(":"):
                    label = label[:-1].strip()
                elif rest.startswith(":"):
                    rest = rest[1:].strip()
                current = [n, rest]
                out[label] = current
            elif current is not None and t.strip() and not t.strip().startswith(("#", "|", "-", "*")):
                current[1] = (current[1] + " " + t.strip()).strip()
            elif not t.strip():
                current = None
        return out

    def refs(self, text, line, tag, allow_searched=False):
        """Parse a Source cell: file and line refs, answer IDs, or a searched list."""
        text = text.strip()
        parts = [p.strip() for p in text.split(";") if p.strip()]
        if allow_searched and any(p.lower().startswith("searched ") for p in parts):
            # A gap names what was searched, and the answer that confirmed it when
            # the person gave one, in either order: 'searched resume.txt; A2'.
            names, answers = [], []
            for part in parts:
                if part.lower().startswith("searched "):
                    names += [x.strip() for x in re.split(r",|\band\b", part[9:]) if x.strip()]
                elif ANSWER_REF.match(part):
                    answers.append(part)
                else:
                    self.report.fail(line, tag, f"Can't read '{part}' in a gap's source. A gap names "
                                     "what was searched, and the person's answer when they confirmed "
                                     "it, like 'searched resume.txt; A2'.")
            return {"searched": names, "files": [], "answers": answers}
        files, answers = [], []
        for part in [p.strip() for p in text.split(";") if p.strip()]:
            if ANSWER_REF.match(part.split()[0] if part.split() else ""):
                answers.append(part.split()[0])
                continue
            m = FILE_REF.match(part)
            if not m:
                self.report.fail(line, tag, f"Can't read the source '{part}'. Use a file and line "
                                 "like 'resume.txt L12', or an answer ID like 'A2'.")
                continue
            a = int(m.group("a"))
            b = int(m.group("b")) if m.group("b") else a
            files.append({"file": m.group("file").strip(), "from": a, "to": b,
                          "date": m.group("date") or ""})
        if not files and not answers:
            self.report.fail(line, tag, "No source.")
        return {"searched": [], "files": files, "answers": answers}

    # Sections

    def parse_target(self):
        rep = self.report
        rows = self.body(1)
        if not rows:
            return
        sub = next((n for n, t in rows if SUBHEAD.match(t) and "firm facts" in t.lower()), None)
        head = [(n, t) for n, t in rows if sub is None or n < sub]
        fields = self.fields(head)
        for label in TARGET_LABELS:
            if label not in fields:
                rep.fail(rows[0][0], "target", f"Section 1 needs '- **{label}:** ...'"
                         + (" (write 'not given' when you don't know it)."
                            if label in ("Channel", "Reader", "What matters to the person") else "."))
        self.target = {k: {"line": v[0], "text": v[1]} for k, v in fields.items()}
        measure = fields.get("Measure of the job")
        if measure:
            quotes = QUOTE.findall(measure[1].translate(CURLY))
            ref = re.search(r"\(([^()]*\bL\d+[^()]*)\)\s*$", measure[1])
            if not quotes or not ref:
                rep.fail(measure[0], "target", "The measure of the job is a quote from the posting "
                         "with its line, like: \"...\" (posting.txt L4).")
            else:
                self.target["Measure of the job"]["quotes"] = quotes
                self.target["Measure of the job"]["refs"] = self.refs(ref.group(1), measure[0], "target")
        if sub is None:
            rep.fail(rows[0][0], "facts", "Section 1 needs a '### Firm facts' part.")
            return
        facts_rows = [(n, t) for n, t in rows if n > sub]
        if any(t.strip() == "None." for _n, t in facts_rows):
            rep.warn(sub, "facts", "No firm facts. The file still serves a resume, and "
                     "cover-letter will stop until there are two.")
            return
        table = self.table(facts_rows, ["#", "Fact", "Why it matters here", "Source", "Checked"],
                           "facts", sub)
        if table is None:
            rep.fail(sub, "facts", "Firm facts need a table, or 'None.'")
            return
        for n, cells in table:
            fid, fact, why, source, checked = cells[:5]
            fact_rec = {"id": fid, "line": n, "fact": fact, "why": why, "source": source,
                        "checked": checked, "url": None, "refs": None}
            if not re.match(r"^F\d+$", fid):
                rep.fail(n, "facts", f"A firm fact's ID should be F1, F2 and so on, not '{fid}'.")
            if not fact:
                rep.fail(n, "facts", f"{fid} has no fact.")
            if not why:
                rep.fail(n, "facts", f"{fid} needs a line on why it matters to this case.")
            if not DATE.search(checked):
                rep.fail(n, "facts", f"{fid} needs the date it was checked, as YYYY-MM-DD.")
            url = re.search(r"https?://[^\s)]+", source)
            if url:
                fact_rec["url"] = url.group(0).rstrip(".,")
                if is_home_page(fact_rec["url"]):
                    rep.fail(n, "facts", f"{fid} comes from a home page. Every applicant reads "
                             "the home page, so its facts don't count.")
                # A saved copy of the page, or the answer that gave the link, can
                # follow the address in brackets: (firm-pages.md L11) or (A2).
                rest = source[url.end():]
                fact_rec["refs"] = {
                    "searched": [], "answers": re.findall(r"\bA\d+\b", rest),
                    "files": [{"file": m.group(1), "from": int(m.group(2)),
                               "to": int(m.group(3) or m.group(2)), "date": ""}
                              for m in re.finditer(r"([\w.-]+\.\w+)\s+L(\d+)(?:-L?(\d+))?", rest)]}
            elif source:
                fact_rec["refs"] = self.refs(source, n, "facts")
            else:
                rep.fail(n, "facts", f"{fid} has no source.")
            self.facts.append(fact_rec)
        if len(self.facts) < 2:
            rep.warn(sub, "facts", f"{len(self.facts)} firm fact(s). The file still serves a resume, "
                     "and cover-letter will stop until there are two.")

    def parse_map(self):
        rep = self.report
        rows = self.body(2)
        if not rows:
            return
        table = self.table(rows, ["#", "Requirement", "Line", "Kind", "Evidence", "Source",
                                  "Strength", "Show on"], "map", rows[0][0])
        if not table:
            if table is None:
                rep.fail(rows[0][0], "map", "Section 2 needs the requirement map: a row for every "
                         "requirement, preferred qualification and responsibility.")
            return
        seen = set()
        for n, cells in table:
            rid, req, line, kind, evidence, source, strength, show = [c.strip() for c in cells[:8]]
            row = {"id": rid, "line": n, "requirement": req, "posting_line": None, "kind": kind.lower(),
                   "evidence": evidence, "quotes": QUOTE.findall(evidence.translate(CURLY)),
                   "strength": "", "owner": "", "show": show.lower(), "refs": None}
            if not re.match(r"^R\d+$", rid) or rid in seen:
                rep.fail(n, "map", f"Each row needs its own ID, R1, R2 and so on ('{rid}').")
            seen.add(rid)
            if not req:
                rep.fail(n, "map", f"{rid} has no requirement.")
            m = re.match(r"^L(\d+)$", line)
            if m:
                row["posting_line"] = int(m.group(1))
            else:
                rep.fail(n, "map", f"{rid} needs the posting line it comes from, like L12.")
            if row["kind"] not in KINDS:
                rep.fail(n, "map", f"{rid}: kind is required, preferred or responsibility.")
            sm = re.match(r"^(strong|partial|gap)(?:\s*,\s*(.+))?$", strength.strip(), re.I)
            if not sm:
                rep.fail(n, "map", f"{rid}: strength is strong, partial, or gap with its owner.")
            else:
                row["strength"] = sm.group(1).lower()
                row["owner"] = (sm.group(2) or "").strip()
            if row["show"] not in SHOW_ON:
                rep.fail(n, "map", f"{rid}: show on is resume, letter, both, or off.")
            if row["strength"] == "gap":
                if not re.match(r"^(owned by the role|shared with .+)$", row["owner"], re.I):
                    rep.fail(n, "map", f"{rid} is a gap. Say whether it's 'owned by the role' or "
                             "'shared with' a named team.")
                if row["show"] != "off":
                    rep.fail(n, "map", f"{rid} is a gap, so it shows nowhere: 'off'.")
                row["refs"] = self.refs(source, n, "map", allow_searched=True)
                if not row["refs"]["searched"]:
                    rep.fail(n, "map", f"{rid} is a gap. Its source names what was searched, "
                             "like 'searched resume.txt, record.md'.")
            else:
                if row["show"] == "off":
                    rep.warn(n, "map", f"{rid} isn't a gap but shows nowhere. Check that's meant.")
                row["refs"] = self.refs(source, n, "map")
                if not row["quotes"]:
                    rep.fail(n, "map", f"{rid} needs its evidence quoted, with the words that "
                             "state the fact.")
            self.rows.append(row)
        for n, text in rows:
            if text.strip().lower().startswith("not mapped:"):
                listed = text.split(":", 1)[1]
                for a, b in re.findall(r"L(\d+)\s*(?:to|-)\s*L?(\d+)", listed):
                    self.not_mapped.update(range(int(a), int(b)+1))
                self.not_mapped.update(int(a) for a in re.findall(r"L(\d+)", listed))
                if not re.search(r"[,;]\s*[a-z]", listed, re.I):
                    rep.warn(n, "map", "Say why the lines listed as not mapped get no row.")

    def parse_view(self):
        rows = self.body(3)
        text = " ".join(t.strip() for _n, t in rows if t.strip())
        self.view = [(n, t) for n, t in rows if t.strip()]
        if not text or text == "None.":
            self.report.fail(rows[0][0] if rows else 1, "view", "Section 3 needs the hiring team's view.")
            return
        count = len(text.split())
        if count < 120 or count > 300:
            self.report.warn(rows[0][0], "view", f"The hiring team's view runs {count} words. "
                             "Aim for 150 to 250.")
        for n, t in self.view:
            if re.search(r"\d", strip_quotes(t)):
                self.report.warn(n, "view", "The hiring team's view recites no stats. Take out "
                                 "the number and say what it shows.")

    def parse_case(self):
        rows = self.body(4)
        found = []
        for n, t in rows:
            m = re.match(r"^\s*(\d)\.\s+(.*)$", t)
            if not m:
                continue
            body = m.group(2).replace("**", "").strip()
            label = next((lab for lab in CASE_LABELS if body.lower().startswith(lab.lower())), None)
            value = body.split(":", 1)[1].strip() if ":" in body else ""
            found.append((n, int(m.group(1)), label, value))
        start = rows[0][0] if rows else 1
        if [f[2] for f in found] != CASE_LABELS:
            self.report.fail(start, "case", "Section 4 needs four numbered lines, in order: "
                             + "; ".join(CASE_LABELS) + ".")
        for n, _num, label, value in found:
            if label and not value:
                self.report.fail(n, "case", f"'{label}' has no line.")
            if label:
                self.case[label] = {"line": n, "text": value}

    def parse_proofs(self):
        rep = self.report
        rows = self.body(5)
        heads = [(n, SUBHEAD.match(t)) for n, t in rows]
        heads = [(n, m) for n, m in heads if m]
        if not heads:
            rep.fail(rows[0][0] if rows else 1, "proofs", "Section 5 needs the proof bank: "
                     "three to five proofs, each under '### P1. <name>'.")
            return
        for i, (n, m) in enumerate(heads):
            end = heads[i+1][0] if i+1 < len(heads) else (rows[-1][0]+1)
            pm = re.match(r"^P(\d+)\.\s+(.+)$", m.group(1))
            if not pm:
                rep.fail(n, "proofs", "A proof's heading reads '### P1. <name>'.")
                continue
            fields = self.fields([(k, t) for k, t in rows if n < k < end])
            proof = {"id": f"P{pm.group(1)}", "line": n, "name": pm.group(2).strip()}
            for label in PROOF_FIELDS:
                if label not in fields or not fields[label][1]:
                    rep.fail(n, "proofs", f"{proof['id']} needs '{label}'.")
            for label, (k, text) in fields.items():
                proof[label] = {"line": k, "text": text}
            story = proof.get("Story", {}).get("text", "")
            if story and len(re.findall(r"[.!?](?:\s|$)", story)) < 2:
                rep.warn(proof.get("Story", {}).get("line", n), "proofs", f"{proof['id']}'s story "
                         "is one sentence. Give the problem, what the candidate did and what changed.")
            src = proof.get("Source")
            if src:
                if not DATE.search(src["text"]):
                    rep.fail(src["line"], "proofs", f"{proof['id']} needs the date its source came from.")
                proof["refs"] = self.refs(re.sub(r"\s*\((?=\d{4}-)", " (", src["text"]),
                                          src["line"], "proofs")
            on = proof.get("On the resume being sent", {}).get("text", "").lower().rstrip(".")
            if on and on not in ("yes", "no"):
                rep.fail(proof["On the resume being sent"]["line"], "proofs",
                         f"{proof['id']}: 'On the resume being sent' is yes or no.")
            use = proof.get("Use on", {}).get("text", "").lower().rstrip(".")
            if use and use not in USE_ON:
                rep.fail(proof["Use on"]["line"], "proofs", f"{proof['id']}: 'Use on' is resume, "
                         "letter or both.")
            answers = proof.get("Answers", {}).get("text", "")
            proof["answers"] = re.findall(r"\bR\d+\b", answers)
            if answers and not proof["answers"]:
                rep.fail(proof["Answers"]["line"], "proofs", f"{proof['id']}: 'Answers' lists the "
                         "requirement IDs it proves, like R2, R5.")
            self.proofs.append(proof)
        ids = [p["id"] for p in self.proofs]
        if ids != [f"P{i}" for i in range(1, len(ids)+1)]:
            rep.fail(heads[0][0], "proofs", "Number the proofs P1, P2 and so on, in rank order.")
        if self.proofs and not 3 <= len(self.proofs) <= 5:
            rep.warn(heads[0][0], "proofs", f"{len(self.proofs)} proofs. The bank holds three to "
                     "five; say why when the evidence holds fewer.")

    def parse_words(self):
        rep = self.report
        rows = self.body(6)
        if not rows:
            return
        sub = next((n for n, t in rows if SUBHEAD.match(t) and "plain descriptions" in t.lower()), None)
        top = [(n, t) for n, t in rows if sub is None or n < sub]
        if any(t.strip() == "None." for _n, t in top):
            rep.warn(rows[0][0], "words", "No words to use. Check the posting's terms again.")
        else:
            table = self.table(top, ["Posting term", "Claim it with"], "words", rows[0][0])
            if table is None:
                rep.fail(rows[0][0], "words", "Section 6 needs the words to use, or 'None.'")
            for n, cells in table or []:
                ids = re.findall(r"\b[RP]\d+\b", cells[1])
                self.terms.append({"line": n, "term": cells[0], "ids": ids})
                if not cells[0]:
                    rep.fail(n, "words", "A row with no term.")
                if not ids:
                    rep.fail(n, "words", f"'{cells[0]}' needs the requirement or proof that backs it.")
        if sub is None:
            rep.fail(rows[0][0], "words", "Section 6 needs a '### Plain descriptions' part, "
                     "or that part with 'None.'")
            return
        low = [(n, t) for n, t in rows if n > sub]
        if any(t.strip() == "None." for _n, t in low):
            return
        table = self.table(low, ["Internal name", "Plain description"], "words", sub)
        if table is None:
            rep.fail(sub, "words", "Plain descriptions need a table, or 'None.'")
        for n, cells in table or []:
            self.descriptions.append({"line": n, "name": cells[0], "description": cells[1]})
            if not cells[1]:
                rep.fail(n, "words", f"'{cells[0]}' needs a plain description.")

    def parse_keep_off(self):
        rep = self.report
        rows = self.body(7)
        for n, t in rows:
            m = re.match(r"^\s*[-*]\s+\*\*(Gap \((R\d+)\)|Concern|Sensitive)[^*]*?:?\*\*:?\s*(.*)$", t)
            if not m:
                if t.strip() and t.strip() != "None." and t.lstrip().startswith(("-", "*")):
                    rep.fail(n, "keep off", "Each item starts '- **Gap (R7):**', '- **Concern:**' "
                             "or '- **Sensitive:**'.")
                continue
            kind = "gap" if m.group(2) else m.group(1).lower()
            rest = m.group(3)
            watch = []
            wm = re.search(r"Watch for:\s*(.+)$", rest)
            if wm:
                watch = QUOTE.findall(wm.group(1).translate(CURLY))
            item = {"line": n, "kind": kind, "row": m.group(2), "text": rest, "watch": watch}
            if kind in ("gap", "concern") and not watch:
                rep.fail(n, "keep off", f"The {kind} needs phrases to watch for, in quotes: the "
                         "words that would put it on a page.")
            self.keep_off.append(item)
        if not any(i["kind"] == "concern" for i in self.keep_off):
            rep.fail(rows[0][0] if rows else 1, "keep off", "Section 7 needs the concern from the "
                     "hiring team's view.")
        if sum(i["kind"] == "concern" for i in self.keep_off) > 1:
            rep.warn(rows[0][0], "keep off", "More than one concern. The hiring team's view raises one.")

    def parse_stamp(self):
        rep = self.report
        rows = self.body(8)
        if not rows:
            return
        sub = next((n for n, t in rows if SUBHEAD.match(t) and "answers" in t.lower()), None)
        top = [(n, t) for n, t in rows if sub is None or n < sub]
        table = self.table(top, ["File", "Role", "Date", "SHA-256"], "stamp", rows[0][0])
        if table is None:
            rep.fail(rows[0][0], "stamp", "The stamp needs every file the case was built from: "
                     "file, role, date and SHA-256.")
        table = table or []
        for n, cells in table:
            name, role, date, sha = cells[:4]
            rec = {"line": n, "file": name, "role": role.lower(), "date": date, "sha256": sha.lower()}
            if not any(r in rec["role"] for r in ROLES):
                rep.fail(n, "stamp", f"{name}: the role is one of " + ", ".join(ROLES) + ".")
            if not DATE.search(date):
                rep.fail(n, "stamp", f"{name} needs its date, as YYYY-MM-DD.")
            if not re.match(r"^[0-9a-f]{12,64}$", rec["sha256"]):
                rep.fail(n, "stamp", f"{name} needs the first 12 or more characters of its SHA-256.")
            self.files.append(rec)
        for role in ("posting", "resume being sent"):
            if not any(role in f["role"] for f in self.files):
                rep.fail(rows[0][0], "stamp", f"The stamp has no file with the role '{role}'.")
        fields = self.fields(rows)
        for label in ("Built", "Voice check", "Confirmed"):
            if label not in fields:
                rep.fail(rows[0][0], "stamp", f"The stamp needs '- **{label}:** ...'.")
        self.stamp = {k: {"line": v[0], "text": v[1]} for k, v in fields.items()}
        confirmed = self.stamp.get("Confirmed", {}).get("text", "")
        if confirmed and not (confirmed.lower().startswith("not yet") or
                              (DATE.match(confirmed) and QUOTE.search(confirmed.translate(CURLY)))):
            rep.fail(self.stamp["Confirmed"]["line"], "stamp", "Confirmed reads 'not yet', or the "
                     "date and the person's words in quotes.")
        if sub is None:
            rep.fail(rows[0][0], "stamp", "The stamp needs '### Answers in this session', "
                     "with a table or 'None.'")
            return
        low = [(n, t) for n, t in rows if n > sub]
        if any(t.strip() == "None." for _n, t in low):
            return
        answers = self.table(low, ["#", "Answer", "Date"], "stamp", sub) or []
        for n, cells in answers:
            if not re.match(r"^A\d+$", cells[0]):
                rep.fail(n, "stamp", f"An answer's ID reads A1, A2 and so on, not '{cells[0]}'.")
            if not DATE.search(cells[2]):
                rep.fail(n, "stamp", f"{cells[0]} needs its date.")
            self.answers[cells[0]] = {"line": n, "text": cells[1], "date": cells[2]}

    def parse_letters(self):
        """Section 9, which cover-letter adds: a record per letter, each under
        '### Letter 1 · <Role> · YYYY-MM-DD'. Lines inside a fenced block are
        the letter's text and never count as headings."""
        if 9 not in self.sections:
            return
        rep = self.report
        title, start, end = self.sections[9]
        if norm(title) != "letters":
            rep.fail(start-1, "letters", "Section 9 is '## 9. Letters'.")
        rows = self.body(9)
        fenced, inside = set(), False
        for n, t in rows:
            if t.strip().startswith("```"):
                fenced.add(n)
                inside = not inside
            elif inside:
                fenced.add(n)
        heads = [(n, t) for n, t in rows if n not in fenced and re.match(r"^###\s", t)]
        if not heads:
            rep.fail(start, "letters", "Section 9 holds one record per letter, each under "
                     "'### Letter 1 · <Role> · YYYY-MM-DD'.")
            return
        for i, (n, t) in enumerate(heads):
            stop = heads[i+1][0] if i+1 < len(heads) else end+1
            self.parse_letter(n, t, [(k, x) for k, x in rows if n < k < stop], fenced)
        numbers = [r["number"] for r in self.letters if r["number"]]
        if numbers != list(range(1, len(numbers)+1)):
            rep.warn(heads[0][0], "letters", "Number the letters 1, 2 and so on, in the order "
                     "they were written.")

    def parse_letter(self, n, heading, rows, fenced):
        rep = self.report
        m = LETTER_HEAD.match(heading.strip())
        record = {"line": n, "number": int(m.group(1)) if m else None,
                  "role": m.group(2) if m else "", "started": m.group(3) if m else "",
                  "fields": {}, "map": {}, "checks": [], "text": ""}
        if not m:
            rep.fail(n, "letters", "A letter's record starts '### Letter 1 · <Role> · YYYY-MM-DD'.")
        parts, current = {}, None
        for k, t in rows:
            if k not in fenced and re.match(r"^####\s", t):
                current = norm(t.strip("# \t"))
                parts[current] = []
                continue
            if current is None:
                parts.setdefault("", []).append((k, t))
            else:
                parts[current].append((k, t))
        fields = self.fields(parts.get("", []))
        for label in LETTER_LABELS:
            if label not in fields or not fields[label][1]:
                rep.fail(n, "letters", f"Letter {record['number'] or '?'} needs '- **{label}:** ...'.")
        record["fields"] = {k: v[1] for k, v in fields.items()}
        date = fields.get("Date")
        if date and not DATE.search(date[1]):
            rep.fail(date[0], "letters", "A letter's date is written YYYY-MM-DD.")
        status = fields.get("Status")
        state = status[1].strip() if status else ""
        if status and not STATUS.match(state):
            rep.fail(status[0], "letters", "Status reads draft, ready, open findings, not reviewed, "
                     "or sent with its date, like 'sent 2026-10-09'.")
        table = self.table(parts.get("map", []), ["Movement", "What it says", "From"], "letters", n)
        if not table:
            rep.fail(n, "letters", f"Letter {record['number'] or '?'} needs '#### Map', a table with "
                     "a row for each of: " + ", ".join(MOVEMENTS) + ".")
        else:
            for k, cells in table:
                record["map"][norm(cells[0])] = {"line": k, "says": cells[1], "from": cells[2]}
                if not cells[1]:
                    rep.fail(k, "letters", f"The map's {cells[0]} row says nothing.")
            missing = [mv for mv in MOVEMENTS if norm(mv) not in record["map"]]
            if missing:
                rep.fail(n, "letters", "The map has no row for " + ", ".join(missing) + ".")
        record["checks"] = [t.strip() for _k, t in parts.get("checks", []) if t.strip()]
        text_rows = [t for k, t in parts.get("text", []) if k in fenced and not t.strip().startswith("```")]
        record["text"] = "\n".join(text_rows).strip()
        if state and not state.lower().startswith("draft"):
            if not record["checks"]:
                rep.fail(n, "letters", f"Letter {record['number'] or '?'} is past draft, so it needs "
                         "'#### Checks' with each check's result.")
            if not record["text"]:
                rep.fail(n, "letters", f"Letter {record['number'] or '?'} is past draft, so it needs "
                         "'#### Text' with the letter in a fenced block.")
        self.letters.append(record)

    @property
    def confirmed(self):
        text = self.stamp.get("Confirmed", {}).get("text", "")
        return bool(DATE.match(text)) and not text.lower().startswith("not yet")

    def file_refs(self):
        """Every (line, ref) that points at a file, across the sections."""
        out = []
        measure = self.target.get("Measure of the job", {})
        for ref in (measure.get("refs") or {}).get("files", []):
            out.append((measure["line"], ref))
        for fact in self.facts:
            for ref in (fact["refs"] or {}).get("files", []):
                out.append((fact["line"], ref))
        for row in self.rows:
            for ref in (row["refs"] or {}).get("files", []):
                out.append((row["line"], ref))
        for proof in self.proofs:
            for ref in (proof.get("refs") or {}).get("files", []):
                out.append((proof["line"], ref))
        return out

    def cross_checks(self):
        rep = self.report
        stamped = {f["file"] for f in self.files}
        for line, ref in self.file_refs():
            if ref["file"] not in stamped:
                rep.fail(line, "stamp", f"{ref['file']} is cited but isn't in the stamp.")
        cited = set()
        for row in self.rows:
            cited.update((row["refs"] or {}).get("answers", []))
            for name in (row["refs"] or {}).get("searched", []):
                if name not in stamped:
                    rep.fail(row["line"], "stamp", f"{row['id']} searched {name}, which isn't in the stamp.")
        for proof in self.proofs:
            cited.update((proof.get("refs") or {}).get("answers", []))
        for fact in self.facts:
            cited.update((fact["refs"] or {}).get("answers", []))
        for aid in sorted(cited):
            if aid not in self.answers:
                rep.fail(1, "stamp", f"{aid} is cited but isn't under 'Answers in this session'.")
        ids = {r["id"]: r for r in self.rows}
        gaps = {r["id"] for r in self.rows if r["strength"] == "gap"}
        listed = {i["row"] for i in self.keep_off if i["kind"] == "gap"}
        for rid in sorted(gaps.difference(listed), key=lambda x: int(x[1:])):
            rep.fail(ids[rid]["line"], "keep off", f"{rid} is a gap, so section 7 lists it as "
                     f"'Gap ({rid})' with phrases to watch for.")
        for item in self.keep_off:
            if item["kind"] == "gap" and item["row"] not in gaps:
                rep.fail(item["line"], "keep off", f"{item['row']} isn't a gap in the requirement map.")
        for proof in self.proofs:
            for rid in proof.get("answers", []):
                if rid not in ids:
                    rep.fail(proof["line"], "proofs", f"{proof['id']} answers {rid}, which isn't in the map.")
                elif rid in gaps:
                    rep.fail(proof["line"], "proofs", f"{proof['id']} answers {rid}, which is a gap.")
        pids = {p["id"] for p in self.proofs}
        for term in self.terms:
            known = [i for i in term["ids"] if i in ids or i in pids]
            if len(known) != len(term["ids"]):
                rep.fail(term["line"], "words", f"'{term['term']}' points at an ID that doesn't exist.")
            if known and all(i in gaps for i in known):
                rep.fail(term["line"], "words", f"'{term['term']}' rests on a gap, so the candidate "
                         "can't claim it.")
        roles = {f["file"]: f["role"] for f in self.files}
        for fact in self.facts:
            refs = fact["refs"] or {}
            from_posting = (bool(refs.get("files")) and not refs.get("answers") and
                            all("posting" in roles.get(r["file"], "") for r in refs["files"]))
            if not fact["url"] and not from_posting and (refs.get("files") or refs.get("answers")):
                rep.warn(fact["line"], "facts", f"{fact['id']} comes from beyond the posting but has no "
                         "link. Give the page's address, with any saved copy's file and line in brackets.")
        company, role = (self.target.get("Company", {}).get("text", ""),
                         self.target.get("Role", {}).get("text", ""))
        if company and role and self.path.name != file_name(company, role):
            rep.warn(1, "name", f"The file is named {self.path.name}; for this company and role "
                     f"it would be {file_name(company, role)}.")

    def prose_units(self):
        """The file's own sentences: every place the skill writes rather than quotes."""
        units = []
        for fact in self.facts:
            units += [(fact["line"], fact["fact"]), (fact["line"], fact["why"])]
        units += self.view
        units += [(v["line"], v["text"]) for v in self.case.values()]
        for proof in self.proofs:
            for label in ("Result", "Story"):
                if label in proof:
                    units.append((proof[label]["line"], proof[label]["text"]))
        units += [(d["line"], d["description"]) for d in self.descriptions]
        units += [(i["line"], re.sub(r"Watch for:.*$", "", i["text"])) for i in self.keep_off]
        return units

    def repeats(self):
        seen = {}
        for line, text in self.prose_units():
            for key, shown in sentences(strip_quotes(text)):
                if key in seen and seen[key] != line:
                    self.report.fail(line, "repeat", f"This sentence is also on line {seen[key]}, "
                                     f"word for word: \"{shown[:80]}\"")
                seen.setdefault(key, line)

    def to_json(self):
        return {"file": self.path.name, "format": self.format, "target": self.target,
                "firm_facts": self.facts, "requirement_map": self.rows,
                "not_mapped": sorted(self.not_mapped),
                "hiring_team_view": " ".join(t.strip() for _n, t in self.view),
                "case": self.case, "proof_bank": self.proofs,
                "words_to_use": self.terms, "plain_descriptions": self.descriptions,
                "keep_off_the_page": self.keep_off, "stamp": {"files": self.files,
                "answers": self.answers, **self.stamp}, "letters": self.letters}


# Checks that open the person's files

class Sources:
    """The person's files, found beside the positioning file or in --dir."""

    def __init__(self, folder):
        self.folder = Path(folder)
        self.cache = {}

    def lines(self, name):
        if name not in self.cache:
            path = self.folder / name
            try:
                self.cache[name] = read_source(path) if path.is_file() else None
            except InputError:
                self.cache[name] = None
        return self.cache[name]

    def window(self, ref):
        lines = self.lines(ref["file"])
        if lines is None:
            return None
        a = max(1, ref["from"]-WINDOW)
        b = min(len(lines), ref["to"]+WINDOW)
        return " ".join(lines[a-1:b])


def home_page_text(pos, src):
    """The text of each home page saved in a firm pages file, found by the address above it."""
    out = []
    for f in pos.files:
        if "firm pages" not in f["role"]:
            continue
        lines = src.lines(f["file"]) or []
        inside = False
        for text in lines:
            url = re.search(r"https?://[^\s)>\]]+", text)
            if url or text.lstrip().startswith("#"):
                inside = bool(url) and is_home_page(url.group(0).rstrip(".,"))
                continue
            if inside:
                out.append(text)
    return norm(" ".join(out))


def home_claims(text):
    """A number with the word after it ("42 stores") and a founding year ("since 1987"),
    each keyed without commas and kept as written."""
    text = norm(text)
    found = {}
    for m in re.finditer(r"(?<![\w.])(\d[\d,]*(?:\.\d+)?%?)\s+([a-z]+)", text):
        found[f"{m.group(1).replace(',', '')} {m.group(2)}"] = m.group(0)
    for m in re.finditer(r"\b(since|founded in|established in|est\.)\s+(1[6-9]\d\d|20\d\d)\b", text):
        found[m.group(0)] = m.group(0)
    return found


def check_home_facts(pos, src, rep):
    """A fact the home page also states doesn't count, even when it's cited to another page."""
    home = home_page_text(pos, src)
    if not home:
        return
    claims = home_claims(home)
    for fact in pos.facts:
        mine = home_claims(fact["fact"])
        shared = sorted(set(mine) & set(claims))
        if shared:
            rep.fail(fact["line"], "facts", f"{fact['id']} states \"{mine[shared[0]]}\", which the home "
                     "page states too. Every applicant reads the home page, so leave that part out.")


def check_sources(pos, src, rep):
    check_home_facts(pos, src, rep)
    posting = next((f["file"] for f in pos.files if "posting" in f["role"]), None)
    found = missing = 0

    def look(quote, refs, line, what):
        nonlocal found, missing
        target = norm(quote)
        places = []
        for ref in refs.get("files", []):
            text = src.window(ref)
            if text is None:
                rep.warn(line, "sources", f"Can't open {ref['file']} to check {what}.")
                return
            places.append(norm(text))
        places += [norm(pos.answers[a]["text"]) for a in refs.get("answers", []) if a in pos.answers]
        if any(target in p for p in places):
            found += 1
        else:
            missing += 1
            rep.fail(line, "sources", f"{what} isn't at its source: \"{quote[:70]}\"")

    measure = pos.target.get("Measure of the job", {})
    for q in measure.get("quotes", []):
        look(q, measure.get("refs") or {}, measure["line"], "The measure of the job")
    for row in pos.rows:
        if posting and row["posting_line"]:
            ref = {"file": posting, "from": row["posting_line"], "to": row["posting_line"]}
            look(row["requirement"], {"files": [ref]}, row["line"], f"{row['id']}'s requirement")
        if row["strength"] != "gap":
            for q in row["quotes"]:
                look(q, row["refs"] or {}, row["line"], f"{row['id']}'s quote")
    for fact in pos.facts:
        for q in QUOTE.findall(fact["fact"].translate(CURLY)):
            look(q, fact["refs"] or {}, fact["line"], f"{fact['id']}'s quote")
    for proof in pos.proofs:
        refs = proof.get("refs") or {}
        texts = [w for w in (src.window(r) for r in refs.get("files", [])) if w]
        texts += [pos.answers[a]["text"] for a in refs.get("answers", []) if a in pos.answers]
        pool = set()
        for t in texts:
            pool |= numbers_in(t)
        for label in ("Result", "Story"):
            if label not in proof:
                continue
            for num in sorted(numbers_in(proof[label]["text"]).difference(pool)):
                rep.warn(proof[label]["line"], "sources", f"{proof['id']}: the number {num} isn't in "
                         "the lines its source cites. Check it, or cite the line that holds it.")
    if posting:
        lines = src.lines(posting)
        if lines is not None:
            cited = {r["posting_line"] for r in pos.rows}
            for n, text in enumerate(lines, 1):
                if (re.match(r"^\s*(?:[-*•]|\d+[.)])\s+\S", text) and n not in cited
                        and n not in pos.not_mapped):
                    rep.warn(n, "sources", f"Posting line {n} has no row in the map: "
                             f"\"{text.strip()[:60]}\"")
            whole = norm(" ".join(lines))
            for term in pos.terms:
                if norm(term["term"]) not in whole:
                    rep.warn(term["line"], "sources", f"'{term['term']}' isn't in the posting.")
    if pos.not_mapped:
        rep.info(0, "sources", f"{len(pos.not_mapped)} posting line(s) listed as not mapped, "
                 "with the reason in the file.")
    rep.info(0, "sources", f"{found} quotes found at their sources, {missing} not found.")


def check_current(pos, src, rep):
    changed = 0
    for f in pos.files:
        path = src.folder / f["file"]
        if not path.is_file():
            changed += 1
            rep.fail(f["line"], "current", f"{f['file']} is missing from {src.folder}.")
            continue
        now = file_hash(path, len(f["sha256"]))
        if now != f["sha256"]:
            changed += 1
            rep.fail(f["line"], "current", f"{f['file']} has changed since the stamp.")
    if not changed:
        rep.info(0, "current", f"All {len(pos.files)} sources match the stamp.")


def check_against(pos, paths, rep):
    mine = {}
    for line, text in pos.prose_units():
        for key, shown in sentences(text):
            mine.setdefault(key, (line, shown))
    if not paths:
        rep.info(0, "against", "No past letters in the stamp, and none named.")
    for path in paths:
        lines = read_source(path)
        if lines is None:
            rep.warn(0, "against", f"Can't read {path.name}.")
            continue
        theirs = {key for key, _shown in sentences(" ".join(lines))}
        shared = [(mine[k][0], mine[k][1]) for k in mine if k in theirs]
        rep.info(0, "against", f"{path.name}: {len(shared)} sentence(s) shared with this file.")
        for line, shown in shared:
            if re.search(r"\d|\byears?\b", shown, re.I):
                rep.warn(line, "against", f"Shared with {path.name}, and it holds a number or "
                         f"years. Check it's still true: \"{shown[:80]}\"")
            else:
                rep.info(line, "against", f"Shared with {path.name}: \"{shown[:80]}\"")
    for line, text in pos.prose_units():
        for m in re.finditer(r"\b(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|"
                             r"twelve|thirteen|fourteen|fifteen|twenty)\s+(?:or\s+more\s+)?years?\b",
                             text, re.I):
            rep.info(line, "years", f"'{m.group(0)}': check it's worked out from the dates.")


# plainspeak-writer

def default_roots():
    roots = []
    config = os.environ.get("CLAUDE_CONFIG_DIR")
    if config:
        roots += [Path(config) / "skills", Path(config) / "plugins"]
    home = Path.home()
    roots += [home / ".claude" / "skills", home / ".claude" / "plugins", Path.cwd() / ".claude" / "skills"]
    appdata = os.environ.get("APPDATA")
    if appdata:
        roots.append(Path(appdata) / "Claude" / "local-agent-mode-sessions")
    roots += [home / "Library" / "Application Support" / "Claude" / "local-agent-mode-sessions",
              home / ".config" / "Claude" / "local-agent-mode-sessions"]
    out = []
    for root in roots:
        if root not in out:
            out.append(root)
    return out


def voice_version(folder):
    log = folder / "CHANGELOG.md"
    if log.is_file():
        m = re.search(r"^##\s+v?(\d+(?:\.\d+)+)", log.read_text(encoding="utf-8", errors="replace"), re.M)
        if m:
            return m.group(1)
    return "unknown"


def is_voice_dir(folder):
    skill = folder / "SKILL.md"
    if not (skill.is_file() and (folder / "references" / "tells.md").is_file()):
        return False
    head = skill.read_text(encoding="utf-8", errors="replace")[:2000]
    return bool(re.search(r"^name:\s*['\"]?plainspeak-writer\b", head, re.M))


def find_voice_dir(roots):
    found = []
    for root in roots:
        if not Path(root).is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            here = Path(dirpath)
            depth = len(here.relative_to(root).parts)
            if here.name == "plainspeak-writer" and "SKILL.md" in filenames and is_voice_dir(here):
                found.append(here)
                dirnames[:] = []
                continue
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and depth < MAX_DEPTH]
    if not found:
        return None

    def key(folder):
        version = voice_version(folder)
        parts = tuple(int(p) for p in version.split(".")) if version != "unknown" else (-1,)
        return parts, (folder / "references" / "tells.md").stat().st_mtime
    return max(found, key=key)


def voice_extract(pos):
    """The sentences other pages reuse: sections 3 and 4, each proof's result
    and story, and the plain descriptions. Returns the text and, for each of
    its lines, the line of the positioning file it came from."""
    out, where = [], []

    def add(line, text):
        out.append(text.replace("**", "").strip())
        where.append(line)

    def gap():
        if out and out[-1] != "":
            out.append("")
            where.append(0)
    for n, t in pos.body(3):
        if t.strip():
            add(n, t)
        else:
            gap()
    gap()
    for label in CASE_LABELS:
        if label in pos.case:
            add(pos.case[label]["line"], pos.case[label]["text"])
    for proof in pos.proofs:
        gap()
        for label in ("Result", "Story"):
            if label in proof:
                add(proof[label]["line"], proof[label]["text"])
    if pos.descriptions:
        gap()
        for d in pos.descriptions:
            add(d["line"], d["description"].rstrip(".") + ".")
    return "\n".join(out) + "\n", where


def check_voice(pos, voice_dir, rep):
    if voice_dir is None:
        rep.warn(0, "voice", "plainspeak-writer wasn't found, so the voice check didn't run. "
                 "Point --voice-dir at the folder that holds its SKILL.md.")
        return None
    checker = voice_dir / "scripts" / "check_voice.py"
    if not checker.is_file():
        rep.warn(0, "voice", f"{voice_dir} has no scripts/check_voice.py.")
        return None
    text, where = voice_extract(pos)
    with tempfile.TemporaryDirectory() as tmp:
        piece = Path(tmp) / "reused-sentences.txt"
        piece.write_bytes(text.encode("utf-8"))
        env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
        proc = subprocess.run([sys.executable, str(checker), "--surface", "letter", str(piece)],
                              capture_output=True, text=True, encoding="utf-8", errors="replace",
                              env=env, timeout=120)
    version = voice_version(voice_dir)
    if proc.returncode not in (0, 1):
        rep.warn(0, "voice", f"plainspeak-writer {version}'s checker stopped with an error.")
        return None
    section = None
    hard = 0
    for raw in proc.stdout.splitlines():
        if raw.startswith("HARD FAIL"):
            section = "hard"
        elif raw.startswith("WARN"):
            section = "warn"
        elif not raw.strip():
            section = None
        m = re.match(r"^\s+L(\d+):\s+(\[.+)$", raw)
        if m and section:
            n = int(m.group(1))
            line = where[n-1] if 0 < n <= len(where) and where[n-1] else 0
            if section == "hard":
                hard += 1
                rep.fail(line, "voice", m.group(2))
            else:
                rep.warn(line, "voice", m.group(2))
    rep.info(0, "voice", f"plainspeak-writer {version}, letter surface, {hard} HARD hit(s). "
             f"Rules file: {voice_dir / 'references' / 'tells.md'}")
    return version


# Other readers

def check_for(pos, reader, rep):
    if not pos.confirmed:
        rep.fail(pos.stamp.get("Confirmed", {}).get("line", 0), "for", f"{reader} reads a confirmed "
                 "file only, and this one isn't confirmed yet.")
    if reader == "resume-ops":
        if not any(p.get("Use on", {}).get("text", "").lower().rstrip(".") in ("resume", "both")
                   for p in pos.proofs):
            rep.fail(0, "for", "No proof is marked for the resume.")
        return
    roles = {f["file"]: f["role"] for f in pos.files}

    def from_posting(fact):
        refs = fact["refs"] or {}
        if fact["url"] or refs.get("answers"):
            return False
        files = refs.get("files", [])
        return bool(files) and all("posting" in roles.get(r["file"], "") for r in files)
    beyond = [f for f in pos.facts if not from_posting(f)]
    if len(pos.facts) < 2:
        rep.fail(0, "for", f"cover-letter needs two firm facts, and the file has {len(pos.facts)}.")
    elif not beyond:
        rep.warn(0, "for", "Every firm fact comes from the posting. Look for one beyond it.")
    letter = [p for p in pos.proofs if p.get("Use on", {}).get("text", "").lower().rstrip(".")
              in ("letter", "both")]
    if len(letter) < 2:
        rep.fail(0, "for", f"cover-letter uses two or three proofs, and {len(letter)} are marked "
                 "for the letter.")
    for label in ("Channel", "Reader"):
        value = pos.target.get(label, {}).get("text", "")
        if value.lower().startswith("not given"):
            rep.info(0, "for", f"{label}: not given, so cover-letter will ask for it.")


def check_piece(pos, path, kind, rep):
    lines = read_source(path)
    if lines is None:
        raise InputError(f"{path.name} isn't a .txt, .md or .docx file.")
    joined = [(n, norm(t)) for n, t in enumerate(lines, 1)]
    whole = norm(" ".join(lines))
    for item in pos.keep_off:
        for phrase in item["watch"]:
            target = norm(phrase)
            if target and target in whole:
                n = next((k for k, t in joined if target in t), 0)
                rep.fail(n, "piece", f"\"{phrase}\" is on the page, from the keep-off list "
                         f"({item['kind']}{' ' + item['row'] if item['row'] else ''}).")
    marks = ("resume", "both") if kind == "resume" else ("letter", "both") if kind in (
        "letter", "outreach") else USE_ON
    digits = {n.replace(",", "") for n in numbers_in(" ".join(lines))}
    for proof in pos.proofs:
        use = proof.get("Use on", {}).get("text", "").lower().rstrip(".")
        if use not in marks:
            continue
        nums = numbers_in(proof.get("Result", {}).get("text", ""))
        hit = sorted(n for n in nums if n in digits)
        shown = bool(nums) and len(hit) == len(nums)
        rep.info(0, "piece", f"{proof['id']} ({proof['name']}): "
                 + ("shows" if shown else "partly shows" if hit else "doesn't show")
                 + (f", numbers found: {', '.join(hit)}" if hit else ""))
    for term in pos.terms:
        t = norm(term["term"])
        found = bool(re.search(r"\b" + re.escape(t) + r"s?\b", whole))
        rep.info(0, "piece", f"Word to use '{term['term']}': " + ("on the page" if found else "not on the page"))
    seen, para, start = {}, [], 0
    for n, text in enumerate(lines + [""], 1):
        if text.strip():
            para.append(text.strip())
            start = start or n
            continue
        for key, shown in sentences(" ".join(para)):
            if key in seen:
                rep.fail(start, "piece", f"This sentence is also in the paragraph at line "
                         f"{seen[key]}: \"{shown[:80]}\"")
            seen.setdefault(key, start)
        para, start = [], 0


def check_links(pos, rep, timeout=15):
    for fact in pos.facts:
        url = fact["url"]
        if not url:
            continue
        host = (urlparse(url).hostname or "").lower()
        if host.endswith(MADE_UP_HOSTS) or host in ("example.com", "example.org", "example.net"):
            rep.info(fact["line"], "links", f"{fact['id']}: {host} is a made-up test address, not opened.")
            continue
        status, reason = None, ""
        for method in ("HEAD", "GET"):
            req = Request(url, method=method, headers={"User-Agent": f"check_positioning/{__version__}"})
            try:
                with urlopen(req, timeout=timeout) as resp:
                    status = resp.status
                break
            except HTTPError as exc:
                status, reason = exc.code, exc.reason
                if method == "HEAD" and exc.code in (403, 405, 501):
                    continue
                break
            except (URLError, OSError, ValueError) as exc:
                status, reason = None, str(getattr(exc, "reason", exc))
                break
        if status is not None and status < 400:
            rep.info(fact["line"], "links", f"{fact['id']}: {status} {url}")
        else:
            rep.fail(fact["line"], "links", f"{fact['id']}: {status or 'no answer'} {reason} {url}".strip())


# Command line

def print_report(pos_name, rep):
    print(f"check_positioning {__version__}   {pos_name}")

    def show(title, items):
        if not items:
            return
        print(f"{title} ({len(items)}):")
        for line, tag, msg in sorted(items, key=lambda x: x[0]):
            where = f"L{line}" if line else "(file)"
            print(f"  {where}: [{tag}] {msg}")
    show("FAIL", rep.fails)
    show("WARN", rep.warns)
    show("INFO", rep.infos)
    print()
    if rep.fails:
        print("RESULT: FAIL")
    elif rep.warns:
        print(f"RESULT: PASS, with {len(rep.warns)} warning(s) to fix or clear with a reason.")
    else:
        print("RESULT: PASS")


def parser():
    ap = argparse.ArgumentParser(prog="check_positioning.py", allow_abbrev=False,
                                 description="Check a positioning file from candidate-positioning.")
    ap.add_argument("file", nargs="?", help="the positioning file")
    ap.add_argument("--dir", help="where the person's files are (default: the file's folder)")
    ap.add_argument("--sources", action="store_true", help="check each quote against its file and line")
    ap.add_argument("--current", action="store_true", help="check that no source changed since the stamp")
    ap.add_argument("--against", nargs="*", metavar="FILE",
                    help="list sentences shared with past letters (default: the stamp's past letters)")
    ap.add_argument("--voice", action="store_true", help="run plainspeak-writer's check on the reused sentences")
    ap.add_argument("--voice-dir", help="the plainspeak-writer folder, when it isn't found on its own")
    ap.add_argument("--for", dest="reader", choices=("resume-ops", "cover-letter"),
                    help="check what that reader needs")
    ap.add_argument("--piece", help="a finished piece to check against the file")
    ap.add_argument("--as", dest="kind", default="letter",
                    choices=("letter", "resume", "outreach", "other"), help="what the piece is")
    ap.add_argument("--check-links", action="store_true", help="open each firm-fact link")
    ap.add_argument("--json", action="store_true", help="print the file as JSON")
    ap.add_argument("--name", nargs=2, metavar=("COMPANY", "ROLE"), help="print the file name to use")
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return ap


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        # A record heading in section 9 holds a middle dot, and a Windows console
        # would write it in its own code page; a reader of --json expects UTF-8.
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    if args.name:
        print(file_name(*args.name))
        return 0
    if not args.file:
        print("Name the positioning file to check.", file=sys.stderr)
        return 2
    try:
        pos = Positioning(args.file)
        if args.json:
            print(json.dumps(pos.to_json(), indent=2, ensure_ascii=False))
            return 0
        rep = pos.report
        src = Sources(Path(args.dir) if args.dir else pos.path.resolve().parent)
        if args.sources:
            check_sources(pos, src, rep)
        if args.current:
            check_current(pos, src, rep)
        if args.against is not None:
            names = args.against or [f["file"] for f in pos.files if "past letter" in f["role"]]
            paths = [Path(n) if Path(n).is_file() else src.folder / n for n in names]
            check_against(pos, paths, rep)
        if args.voice:
            voice_dir = Path(args.voice_dir).resolve() if args.voice_dir else find_voice_dir(default_roots())
            if args.voice_dir and not is_voice_dir(voice_dir):
                raise InputError(f"{voice_dir} doesn't hold plainspeak-writer.")
            check_voice(pos, voice_dir, rep)
        if args.reader:
            check_for(pos, args.reader, rep)
        if args.piece:
            check_piece(pos, Path(args.piece), args.kind, rep)
        if args.check_links:
            check_links(pos, rep)
    except InputError as exc:
        print(f"The file can't be checked, because {exc}", file=sys.stderr)
        return 2
    print_report(pos.path.name, rep)
    return 1 if rep.fails else 0


if __name__ == "__main__":
    sys.exit(main())
