#!/usr/bin/env python3
"""Check a cover letter from the cover-letter skill against the three files it
rests on: the positioning file, the posting and the resume that goes with it.

    python check_letter.py --positioning P --resume R                 before drafting
    python check_letter.py --positioning P --resume R --sample old-letter.txt
    python check_letter.py letter.txt --positioning P --resume R --posting T
    python check_letter.py letter.txt --positioning P --channel textbox --limit 2500
    python check_letter.py letter.txt --positioning P --referral "Dana Ruiz"
    python check_letter.py letter.txt --positioning P --compare other-letter.txt
    python check_letter.py letter.txt --positioning P --voice --sentences
    python check_letter.py Nadia_Haddad_CoverLetter_SilverLarch.docx --resume R

Before drafting, it quotes any line in the posting about AI in application
materials and fails one that rules them out, compares the proofs marked for
the letter with the resume that goes with it, so a date or figure the two
disagree on is caught at the gate, and lists any sentence in a voice sample
that plainspeak-writer's checker blocks.

On a letter, it finds the header, the salutation, the body and the sign-off,
counts the body's words and the letter's characters, and fails a placeholder,
a sentence said twice, a body over 500 words, a header that doesn't match the
resume's contact block, and a channel's broken rule. With the positioning file
it also checks every number, date and name in the body against the three
files, a phrase from the keep-off list, a resume line restated, the firm or
the seat in the first two sentences, a referral in them, an ask that opens on
a stock phrase, a blocked sentence from a voice sample, and sentences shared
with another letter, along with an ask that opens the same way.

On a Word file, it checks the author field, tables, text boxes, columns,
headers and footers, and estimates whether the letter fits on one page.

Exit code 0 means no FAIL, 1 means at least one, and 2 means the input needs
fixing. Python 3.8 or newer, standard library only. It reads the positioning
file with candidate-positioning's own script, in the folder beside this
skill's, so the format has one reader.
"""
import argparse
import importlib.util
import os
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

__version__ = "0.3.1"

HERE = Path(__file__).resolve().parent
CP_PATH = HERE.parents[1] / "candidate-positioning" / "scripts" / "check_positioning.py"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
TEXT_SUFFIXES = {".txt", ".md", ".markdown", ".text"}
CURLY = str.maketrans({chr(0x201C): '"', chr(0x201D): '"', chr(0x2018): "'", chr(0x2019): "'"})

MAX_WORDS = 500           # the body's hard cap, by code
TARGET = (350, 450)       # the body's target range
FLOOR = 250               # plainspeak-writer's floor for a cover letter
MIN_WORDS = 6             # a sentence this long or longer counts as said twice
CHANNELS = ("upload", "textbox", "email")

SALUTATION = re.compile(r"^\s*(dear|to|hello|hi|greetings)\b.*[:,]\s*$", re.I)
SIGN_OFF = re.compile(r"^\s*[A-Z][A-Za-z']*(?:\s+[A-Za-z']+){0,3},\s*$")
BAD_SALUTATION = re.compile(r"to whom it may concern|dear sir or madam|dear sirs\b", re.I)
SUBJECT = re.compile(r"^\s*subject\s*:\s*(.*)$", re.I)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
PHONE = re.compile(r"(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
PLACEHOLDERS = [
    (re.compile(r"\[[^\]\n]{0,80}\]"), "a bracketed slot"),
    (re.compile(r"\b(?:TK|TBD|FIXME|PLACEHOLDER)\b"), "a working marker"),
    (re.compile(r"\bXX+\b"), "an XX placeholder"),
    (re.compile(r"\{\{[^}]*\}\}|<[A-Z][A-Za-z ]+>"), "a template slot"),
    (re.compile(r"lorem ipsum", re.I), "filler text"),
]
MONTH = (r"(jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|"
         r"sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)")
MONTH_YEAR = re.compile(r"\b" + MONTH + r"\.?\s+(?:\d{1,2},?\s+)?((?:19|20)\d{2})\b", re.I)
DATE_LINE = re.compile(r"^\s*(?:" + MONTH + r"\.?\s+\d{1,2},?\s+(?:19|20)\d{2}|\d{4}-\d{2}-\d{2})\s*$", re.I)
SPELLED = {w: n for n, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
    "fifteen sixteen seventeen eighteen nineteen twenty".split())}
SPELLED.update({"thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
                "eighty": 80, "ninety": 90})
TIME_WORDS = re.compile(r"\b(?:years?|months?|current(?:ly)?|now|today|recent(?:ly)?|since|"
                        r"for the (?:last|past)|present|so far|still|(?:this|last|next) (?:year|spring|"
                        r"summer|fall|autumn|winter|month|week|semester|quarter|term))\b", re.I)
ASK_WORDS = re.compile(r"\?|\b(?:talk|conversation|discuss|call|meet|meeting|chat|walk you through|"
                       r"hear how|compare notes)\b", re.I)
CLOSE_TELLS = re.compile(r"\bthank(?:s| you)\b|\blook(?:ing)? forward\b", re.I)
# The ask every letter ended on in the first live runs. It reads as a template.
STOCK_ASK = re.compile(r"^\s*I(?:'d| would) (?:(?:like|love) to (?:talk|discuss|speak|chat|connect|meet)|"
                       r"(?:welcome|appreciate|value|love|like) (?:the|a|an) (?:chance|opportunity|"
                       r"conversation|call|meeting))\b", re.I)
# A posting's rules on AI in application materials.
AI_TERM = re.compile(r"(?<![\w.])(?:AI(?:-\w+)?|A\.I\.|GenAI|LLMs?)(?![\w])|(?i:\b(?:artificial intelligence|"
                     r"generative|ChatGPT|GPT-?\d*|chatbots?|large language models?|Copilot|Gemini)\b)")
AI_MATERIALS = re.compile(r"\b(?:applications?|cover letters?|letters?|resumes?|r\u00e9sum\u00e9s?|CVs?|materials?|"
                          r"submissions?|responses?|answers?|essays?|writing|statements?|documents?|"
                          r"portfolios?|work samples?|assessments?|questions?)\b", re.I)
AI_BAR = re.compile(r"\b(?:do not|don't|must not|may not|should not|cannot|can't|never|"
                    r"not (?:be )?(?:permitted|allowed|accepted|considered|reviewed)|prohibit\w*|forbid\w*|"
                    r"disqualif\w*|(?:will|would) be (?:rejected|disqualified|removed)|"
                    r"won't be (?:considered|reviewed|accepted)|without (?:the )?(?:use|help|aid|assistance) of|"
                    r"without using|free (?:of|from)|written (?:entirely )?by you|your own (?:work|words|writing))\b",
                    re.I)
AI_DISCLOSE = re.compile(r"\b(?:disclose|disclosure|(?:tell us|let us know|indicate|note|state) "
                         r"(?:if|whether|how))\b", re.I)
AI_EMPLOYER = re.compile(r"\b(?:we|our (?:team|system|systems|process|recruiters?|hiring team))\b[^.]{0,40}"
                         r"\b(?:use|uses|may use|using|rely on)\b", re.I)
AI_UNCLEAR = re.compile(r"\b(?:policy|guidance|guidelines|permitted|allowed|acceptable|appropriate|"
                        r"responsib\w*|use of)\b", re.I)
OWN_WORDS = re.compile(r"\b(?:in your own words|written (?:entirely )?by you|your own (?:work|writing))\b", re.I)
# These two read as a rule on their own; "your own work" also turns up in a job's duties.
OWN_WORDS_ALONE = re.compile(r"\b(?:in your own words|written (?:entirely )?by you)\b", re.I)
WHO = re.compile(r"\b(?:applicants?|candidates?|you|your)\b", re.I)
CONNECTORS = {"of", "and", "&", "the", "for", "de", "la", "du", "von", "van", "on", "at"}
PRONOUNS = {"i", "i'm", "i've", "i'd", "i'll"}
YEAR_COUNT = re.compile(r"\b(\d+|" + "|".join(sorted(
    "two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
    "seventeen eighteen nineteen twenty thirty forty".split(), key=len, reverse=True)) +
    r")(?:\s+or\s+more)?(?:\s+(?:full|school|calendar))?\s+years?\b"
    r"|\b(?:the\s+)?(?:last|past)\s+(\d+|two|three|four|five|six|seven|eight|nine|ten)\b", re.I)
LEGAL = {"inc", "inc.", "llc", "co", "co.", "corp", "corp.", "corporation", "company", "ltd",
         "ltd.", "lp", "llp", "plc"}
MONTH_NAMES = {m.lower() for m in (
    "January February March April May June July August September October November December "
    "Jan Feb Mar Apr Jun Jul Aug Sep Sept Oct Nov Dec").split()}
DAY_NAMES = {d.lower() for d in "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()}
STARTERS = {w.lower() for w in (
    "A An The I I'm I've I'd I'll My Our Your Their His Her Its It It's We We've We'd You "
    "You'll You've They This That These Those There Here When While Since After Before Each "
    "Every Last Next Both With Without From For To As So But And Or If What How Why Where "
    "Which Who Then Now In On At By Over Under Into Across Most Many Some All Any No Not "
    "One Two Three Four Five Six Seven Eight Nine Ten That's There's What's Let Once Because "
    "Although Though Even Still Yet Instead Rather Than Through During Within Between Among "
    "Thank Thanks Please Today Also Again Together Whether Until Unless About Like Just "
    "Monday Tuesday Wednesday Thursday Friday Saturday Sunday").split()}
HEADERS = {"summary", "professional summary", "profile", "experience", "work experience",
           "professional experience", "education", "skills", "certification", "certifications",
           "license", "licenses", "licenses and certifications"}

# Average width of a character of English prose, as a share of the font size,
# measured from the fonts' own files on 2026-10-07, and each font's single line
# height as Word sets it. Fonts not listed use the widest.
FONT_WIDTH = {"calibri": 0.409, "arial": 0.448, "helvetica": 0.448, "georgia": 0.446,
              "times new roman": 0.408, "garamond": 0.40}
LINE_HEIGHT = {"calibri": 1.22, "arial": 1.15, "helvetica": 1.15, "georgia": 1.14,
               "times new roman": 1.15, "garamond": 1.13}
SAFETY = 1.06             # leans the estimate toward more lines, never fewer
LIBRARY_AUTHORS = re.compile(r"python-docx|docx4j|apache poi|openpyxl|phpword|aspose|un-?named|"
                             r"^docx$|^author$|^user$|^administrator$|microsoft office user|"
                             r"^claude$|anthropic|openai", re.I)


class InputError(Exception):
    """A file the script can't read."""


class Report:
    def __init__(self):
        self.fails, self.warns, self.infos = [], [], []

    def fail(self, tag, msg):
        self.fails.append((tag, msg))

    def warn(self, tag, msg):
        self.warns.append((tag, msg))

    def info(self, tag, msg):
        self.infos.append((tag, msg))


# Reading files

def decode(data):
    for encoding in ("utf-8-sig", "cp1252"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", errors="replace")


def docx_paragraphs(path):
    """Each paragraph of a Word file's body as its text, in order."""
    try:
        with zipfile.ZipFile(path) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
    except (zipfile.BadZipFile, KeyError, ET.ParseError) as exc:
        raise InputError(f"{Path(path).name} isn't a readable Word file ({exc.__class__.__name__}).")
    out = []
    for para in root.iter(W + "p"):
        parts = []
        for node in para.iter():
            if node.tag == W + "t":
                parts.append(node.text or "")
            elif node.tag == W + "tab":
                parts.append("\t")
            elif node.tag in (W + "br", W + "cr"):
                parts.append("\n")
        out.append("".join(parts))
    return out


def read_text(path):
    path = Path(path)
    if not path.is_file():
        raise InputError(f"Can't find {path}.")
    suffix = path.suffix.lower()
    if suffix in TEXT_SUFFIXES:
        return decode(path.read_bytes()).replace("\r\n", "\n").replace("\r", "\n")
    if suffix == ".docx":
        return "\n".join(docx_paragraphs(path))
    if suffix == ".pdf":
        raise InputError(f"{path.name} is a PDF. The skill never makes one; give the Word file "
                         "or the text.")
    raise InputError(f"{path.name} isn't a .txt, .md or .docx file.")


def load_cp():
    if not CP_PATH.is_file():
        raise InputError(f"candidate-positioning's script isn't at {CP_PATH}. cover-letter reads "
                         "the positioning file with it, so the two skills ship together.")
    spec = importlib.util.spec_from_file_location("check_positioning", CP_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# Text helpers

def words_only(text):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s%$]", " ", text.translate(CURLY).lower())).strip()


def split_sentences(text):
    text = re.sub(r"\s+", " ", text.translate(CURLY)).strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'(])", text) if s.strip()]


def text_sentences(text):
    """Sentences of a whole file, paragraph by paragraph, so a date line or a
    greeting never runs into the sentence after it."""
    out = []
    for block in re.split(r"\n\s*\n", text):
        out += split_sentences(block)
    return out


def numbers(text):
    """The numbers in a text, written out or in digits: '1,900' and '1900' match,
    '44 percent' is '44%', and 'four' is '4'. Returns (digits, spelled)."""
    t = text.translate(CURLY).lower()
    t = re.sub(r"\s*\bper\s?cent\b", "%", t)
    digits = set()
    for m in re.finditer(r"(?<![\w.])\$?(\d[\d,]*(?:\.\d+)?)(\s?%)?", t):
        n = m.group(1).replace(",", "").rstrip(".")
        if "." in n:
            n = n.rstrip("0").rstrip(".")
        digits.add(n + ("%" if m.group(2) else ""))
    spelled = set()
    for m in re.finditer(r"\b(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)-(one|two|three|"
                         r"four|five|six|seven|eight|nine)\b", t):
        spelled.add(str(SPELLED[m.group(1)] + SPELLED[m.group(2)]))
    t = re.sub(r"\b(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)-\w+\b", " ", t)
    for word, n in SPELLED.items():
        if n >= 2 and re.search(r"\b" + word + r"\b", t):
            spelled.add(str(n))
    return digits, spelled


def year_counts(text):
    """Counts of years, like 'eight years', '13 years' or 'the last two', as numbers.
    A count of years ages, so it has to be in the files as a count of years."""
    out = set()
    for m in YEAR_COUNT.finditer(text.translate(CURLY)):
        word = (m.group(1) or m.group(2)).lower()
        out.add(str(SPELLED.get(word, word)))
    return out


def month_years(text):
    out = set()
    for m in MONTH_YEAR.finditer(text.translate(CURLY)):
        month = m.group(1).lower()[:3]
        out.add(f"{month} {m.group(2)}")
    return out


def lcs(a, b):
    """Length of the longest common subsequence of two word lists."""
    if not a or not b:
        return 0
    prev = [0]*(len(b)+1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j]+1 if x == y else max(prev[j+1], cur[j]))
        prev = cur
    return prev[-1]


def longest_run(a, b):
    """Length of the longest run of words the two lists share, in order and unbroken."""
    best = 0
    prev = [0]*(len(b)+1)
    for x in a:
        cur = [0]*(len(b)+1)
        for j, y in enumerate(b):
            if x == y:
                cur[j+1] = prev[j]+1
                best = max(best, cur[j+1])
        prev = cur
    return best


def strip_credentials(name):
    return re.split(r",", name.strip())[0].strip()


def same_name(a, b):
    return words_only(strip_credentials(a)) == words_only(strip_credentials(b))


# The letter

class Letter:
    """A letter split into its parts. A text file's paragraphs are separated by
    blank lines; a Word file's paragraphs are its own."""

    def __init__(self, path):
        self.path = Path(path)
        suffix = self.path.suffix.lower()
        if suffix == ".docx":
            paras = [p.split("\n") for p in docx_paragraphs(self.path)]
            self.raw = "\n".join("\n".join(p) for p in paras)
            self.voice_text = "\n\n".join("\n".join(p) for p in paras if "".join(p).strip())
        else:
            self.raw = read_text(self.path)
            paras, block = [], []
            for line in self.raw.split("\n"):
                if line.strip():
                    block.append(line)
                elif block:
                    paras.append(block)
                    block = []
            if block:
                paras.append(block)
            self.voice_text = self.raw
        self.lines = []          # (paragraph index, line text), blank lines left out
        for i, para in enumerate(paras):
            for line in para:
                if line.strip():
                    self.lines.append((i, line.strip()))
        self.subject = None
        self.header = []
        self.date = None
        self.salutation = None
        self.sign_off = None
        self.name = None
        self.after_name = []
        self.paragraphs = []
        self.parse()
        if suffix == ".docx" and self.salutation:
            # Lay a Word file out the way its text form is written, so the voice
            # check reads the contact block and the sign-off as blocks, not as
            # one-line paragraphs.
            parts = ["\n".join(self.header)] if self.header else []
            parts += [self.date] if self.date else []
            parts += [self.salutation] + self.paragraphs
            if self.sign_off:
                parts.append("\n".join([self.sign_off + ",", self.name] + self.after_name))
            self.voice_text = "\n\n".join(parts) + "\n"

    def parse(self):
        lines = self.lines
        start = 0
        if lines and SUBJECT.match(lines[0][1]):
            self.subject = SUBJECT.match(lines[0][1]).group(1).strip()
            start = 1
        sal = next((k for k in range(start, min(len(lines), start+15)) if SALUTATION.match(lines[k][1])), None)
        if sal is None:
            return
        self.salutation = lines[sal][1]
        for _i, text in lines[start:sal]:
            if DATE_LINE.match(text):
                self.date = text
            else:
                self.header.append(text)
        close = None
        for k in range(len(lines)-1, sal, -1):
            if SIGN_OFF.match(lines[k][1]) and k+1 < len(lines) and len(lines)-k <= 5:
                close = k
                break
        end = close if close is not None else len(lines)
        if close is not None:
            self.sign_off = lines[close][1].rstrip(",").strip()
            self.name = lines[close+1][1]
            self.after_name = [t for _i, t in lines[close+2:]]
        groups = {}
        for i, text in lines[sal+1:end]:
            groups.setdefault(i, []).append(text)
        self.paragraphs = [" ".join(groups[i]) for i in sorted(groups)]

    @property
    def body(self):
        return "\n\n".join(self.paragraphs)

    @property
    def words(self):
        return len(self.body.split())

    @property
    def characters(self):
        """Every character a person pastes, counted the way build_packet.py counts."""
        return len(self.raw.strip("\n").replace("\r\n", "\n"))

    def sentences(self):
        """(paragraph number from 1, sentence) for the body."""
        out = []
        for k, para in enumerate(self.paragraphs, 1):
            out += [(k, s) for s in split_sentences(para)]
        return out


def name_runs(sentence):
    """Runs of capitalized words in a sentence, like 'Silver Larch School District',
    each with whether it opens the sentence."""
    tokens = [(m.start(), m.group(0)) for m in re.finditer(r"[A-Za-z0-9][\w'&.-]*", sentence.translate(CURLY))]
    runs, cur, cur_start = [], [], None
    text = sentence.translate(CURLY)
    for k, (pos, tok) in enumerate(tokens):
        # A comma right after a word ends a name: "Fernley, Nevada" is two places.
        comma = text[pos+len(tok):pos+len(tok)+1] == "," or tok.endswith(",")
        tok = re.sub(r"[.,]+$", "", tok) if not re.match(r"^(?:Co|Inc|Corp|Ltd|Jr|Sr)\.$", tok) else tok
        upper = tok[:1].isupper() and tok.lower() not in PRONOUNS
        nxt_upper = k+1 < len(tokens) and tokens[k+1][1][:1].isupper()
        if upper:
            if not cur:
                cur_start = k
            cur.append(tok)
            if comma:
                runs.append((cur, cur_start == 0))
                cur = []
        elif cur and tok.lower() in CONNECTORS and nxt_upper:
            cur.append(tok)
        else:
            if cur:
                runs.append((cur, cur_start == 0))
            cur = []
    if cur:
        runs.append((cur, cur_start == 0))
    out = []
    for toks, at_start in runs:
        toks = [re.sub(r"'s$", "", t).rstrip("'") for t in toks]
        if at_start and toks and toks[0].lower() in STARTERS:
            toks = toks[1:]
            at_start = False if toks else at_start
            if toks and toks[0].lower() in CONNECTORS:
                toks = toks[1:]
        toks = [t for t in toks if t]
        if not toks:
            continue
        if all(t.lower() in MONTH_NAMES | DAY_NAMES | {"i"} or len(t) == 1 for t in toks):
            continue
        out.append((" ".join(toks), at_start and len(toks) == 1))
    return out


# The three files

class Sources:
    """The positioning file, the posting and the resume, as text and as numbers."""

    def __init__(self, cp, positioning=None, resume=None, posting=None):
        self.cp = cp
        self.pos = cp.Positioning(positioning) if positioning else None
        folder = Path(positioning).resolve().parent if positioning else None
        stamped = {f["role"]: f["file"] for f in self.pos.files} if self.pos else {}
        if self.pos and not resume:
            name = next((f for r, f in stamped.items() if "resume being sent" in r), None)
            resume = folder / name if name and (folder / name).is_file() else None
        if self.pos and not posting:
            name = next((f for r, f in stamped.items() if "posting" in r), None)
            posting = folder / name if name and (folder / name).is_file() else None
        self.resume_path = Path(resume) if resume else None
        self.posting_path = Path(posting) if posting else None
        self.resume = read_text(resume) if resume else ""
        # The resume the case was built from, when the letter goes with another one.
        self.stamped_resume = ""
        if self.pos:
            name = next((f for r, f in stamped.items() if "resume being sent" in r), None)
            path = folder / name if name else None
            if path and path.is_file() and (not resume or path.resolve() != Path(resume).resolve()):
                self.stamped_resume = read_text(path)
        self.posting = read_text(posting) if posting else ""
        self.pos_text = ""
        if self.pos:
            lines = []
            for number in range(1, 7):
                lines += [t for _n, t in self.pos.body(number)]
            # The stamp's answers are the person's own words; its hashes and dates aren't facts.
            lines += [a["text"] for a in self.pos.answers.values()]
            self.pos_text = "\n".join(lines)
        # What the files say about the candidate, without the posting's words: the
        # resume, the map's evidence, the proofs, the case and the person's answers.
        mine = [self.resume]
        if self.pos:
            # A map note can name a count only to say it's out of date ("The 2021
            # letter's count of eight years is out of date"), so those notes don't count.
            stale = re.compile(r"out of date|no longer|outdated|isn't current|not current|old count", re.I)
            mine += [s for r in self.pos.rows for s in split_sentences(r["evidence"]) if not stale.search(s)]
            mine += [p.get(k, {}).get("text", "") for p in self.pos.proofs for k in ("Result", "Story")]
            mine += [v["text"] for v in self.pos.case.values()] + [a["text"] for a in self.pos.answers.values()]
            mine.append(self.facts_text())
        self.year_counts = year_counts("\n".join(mine))
        self.all_text = re.sub(r"\s+", " ", "\n".join([self.resume, self.posting, self.pos_text]).translate(CURLY))

    def facts_text(self):
        if not self.pos:
            return ""
        measure = self.pos.target.get("Measure of the job", {}).get("text", "")
        return " ".join([measure] + [f["fact"] for f in self.pos.facts])

    def resume_files(self):
        return {f["file"] for f in self.pos.files if "resume being sent" in f["role"]} if self.pos else set()

    def proofs(self):
        out = []
        resume_files = self.resume_files()
        for p in (self.pos.proofs if self.pos else []):
            refs = (p.get("refs") or {}).get("files", [])
            out.append({
                "only_resume": bool(refs) and all(r["file"] in resume_files for r in refs),
                "id": p["id"],
                "result": p.get("Result", {}).get("text", ""),
                "story": p.get("Story", {}).get("text", ""),
                "on_resume": p.get("On the resume being sent", {}).get("text", "").lower().startswith("yes"),
                "use_on": p.get("Use on", {}).get("text", "").lower().rstrip("."),
                "refs": (p.get("refs") or {}).get("files", []),
            })
        return out

    def resume_contact(self):
        """The resume's contact block: its first lines, up to the first section heading."""
        lines = [t.strip() for t in self.resume.split("\n") if t.strip()]
        block = []
        for k, t in enumerate(lines[:6]):
            plain = t.strip("#*: ").lower()
            if k > 0 and (plain in HEADERS or (t.isupper() and len(t.split()) <= 4 and not EMAIL.search(t)
                                                 and not PHONE.search(t))):
                break
            block.append(t)
        return block

    def resume_name(self):
        block = self.resume_contact()
        return strip_credentials(block[0].strip("# ")) if block else ""


def classify(n, sources, kind):
    """Where a number or a month and year from the letter sits in the three files."""
    def has(text):
        if kind == "date":
            return n in month_years(text)
        digits, spelled = numbers(text)
        return n in digits or n in spelled
    if has(sources.resume) or has(sources.posting) or has(sources.facts_text()):
        return "found", None
    hits = [p for p in sources.proofs() if has(p["result"] + " " + p["story"])]
    if hits:
        # The two files disagree when the case was built from a resume that held
        # the number and the resume going with the letter doesn't, or when the
        # proof rests on the resume alone. Otherwise the number came from the
        # deeper record the proof cites.
        if has(sources.stamped_resume):
            return "disagrees", hits[0]["id"]
        deeper = [p for p in hits if not p["on_resume"] or not p["only_resume"]]
        if deeper:
            return "deeper", deeper[0]["id"]
        return "disagrees", hits[0]["id"]
    if has(sources.pos_text):
        return "notes", None
    return "missing", None


# Checks

def check_shape(letter, rep, channel):
    if not letter.salutation:
        rep.fail("shape", "No salutation found, like 'Dear Ironwood Trail hiring team,'. The letter "
                 "opens with one, so the reader and the checks can find the body.")
        return False
    if BAD_SALUTATION.search(letter.salutation):
        rep.fail("shape", f"\"{letter.salutation}\": name a person, or else the firm's hiring team.")
    if not letter.sign_off:
        rep.fail("shape", "No sign-off found: one plain word and a comma, then the name on its own line.")
    elif len(letter.sign_off.split()) > 1:
        rep.warn("shape", f"\"{letter.sign_off},\" is more than one word. The sign-off is one plain word "
                 "and the name.")
    count = len(letter.paragraphs)
    if count < 4 or count > 6:
        rep.warn("shape", f"The body has {count} paragraph(s). Four movements fit in four to six.")
    words = letter.words
    if words > MAX_WORDS:
        rep.fail("length", f"The body runs {words} words, over the {MAX_WORDS}-word cap. Cut repeats "
                 "and lists, never the names, the figures or the first-person verbs.")
    elif words < FLOOR:
        rep.fail("length", f"The body runs {words} words, under plainspeak-writer's floor of {FLOOR} for "
                 "a cover letter.")
    elif not TARGET[0] <= words <= TARGET[1]:
        rep.warn("length", f"The body runs {words} words. The target is {TARGET[0]} to {TARGET[1]}.")
    for pat, label in PLACEHOLDERS:
        for m in pat.finditer(letter.raw):
            rep.fail("placeholder", f"{label} is still in the letter: \"{m.group(0)[:60]}\". Fill it, "
                     "or ask the person for the fact.")
    seen = {}
    for k, s in letter.sentences():
        key = words_only(s)
        if len(key.split()) >= MIN_WORDS:
            if key in seen:
                rep.fail("repeat", f"This sentence is in paragraph {seen[key]} and again in paragraph {k}, "
                         f"word for word: \"{s[:90]}\"")
            seen.setdefault(key, k)
    if channel == "textbox":
        if letter.header:
            rep.warn("channel", "A text box letter starts at the salutation. The form already holds "
                     "the contact details.")
        if re.search(r"\*\*|__", letter.raw) or re.search(r"(?m)^\s*(?:[-*•]|\d+[.)])\s", letter.raw):
            rep.fail("channel", "A text box drops bold and bullets. Write plain paragraphs.")
        curly = sorted({c for c in letter.raw if c in "".join(chr(x) for x in (0x201C, 0x201D, 0x2018, 0x2019))})
        if curly:
            rep.fail("channel", "Curly quotes in a text box letter can paste as stray symbols. Use "
                     "straight quotes.")
    if channel == "email":
        if not letter.subject:
            rep.fail("channel", "An email letter needs a first line like 'Subject: Operations "
                     "Supervisor application'.")
        if letter.header:
            rep.warn("channel", "An email letter leaves out the contact block; the signature carries it.")
    if channel == "upload" and not letter.header:
        rep.fail("channel", "An upload letter opens with the contact block from the resume.")
    return True


def check_limit(letter, rep, limit):
    if limit:
        chars = letter.characters
        if chars > limit:
            rep.fail("channel", f"The letter has {chars:,} characters and the limit is {limit:,}, so it's "
                     f"{chars-limit:,} over.")
        else:
            rep.info("channel", f"{chars:,} characters, inside the limit of {limit:,}.")


def check_against_resume(letter, src, rep, channel):
    contact = src.resume_contact()
    name = src.resume_name()
    if not contact:
        rep.warn("resume", "Couldn't find the resume's contact block to compare the header with.")
        return
    if letter.name and name and not same_name(letter.name, name):
        rep.fail("resume", f"The letter is signed \"{letter.name}\" and the resume says \"{name}\".")
    if channel in ("textbox", "email") or not letter.header:
        return
    header = " ".join(letter.header)
    if name and words_only(name) not in words_only(header):
        rep.fail("resume", f"The header doesn't name \"{name}\" as the resume does.")
    theirs = " ".join(contact)
    for label, pat in (("email", EMAIL), ("phone", PHONE)):
        want = {re.sub(r"\D", "", x) if label == "phone" else x.lower() for x in pat.findall(theirs)}
        have = {re.sub(r"\D", "", x) if label == "phone" else x.lower() for x in pat.findall(header)}
        if want != have:
            rep.fail("resume", f"The header's {label} doesn't match the resume's contact block "
                     f"({', '.join(sorted(have)) or 'none'} against {', '.join(sorted(want)) or 'none'}).")


def phrases(run):
    """A run of capitalized words split at its connectors: 'Excel and Power BI'
    is two names, 'Excel' and 'Power BI'. Each has to be in the files whole."""
    out, cur = [], []
    for t in run.split():
        if t.lower() in CONNECTORS:
            if cur:
                out.append(" ".join(cur))
            cur = []
        else:
            cur.append(t)
    if cur:
        out.append(" ".join(cur))
    return out


def missing_names(run, lower, given):
    """The parts of a name the three files don't hold, and the person didn't give."""
    out = []
    for part in phrases(run):
        bare = re.sub(r"\s+(?:" + "|".join(re.escape(x) for x in LEGAL) + r")$", "", part, flags=re.I)
        hit = re.search(r"(?<![\w])" + re.escape(bare.lower()) + r"(?![\w])", lower)
        if not hit and not any(words_only(bare) == words_only(g) or words_only(bare) in words_only(g).split()
                               for g in given):
            out.append(part)
    return out


def check_facts(letter, src, rep, given=()):
    """Every number, month and year, and name in the body, against the three files."""
    found = 0
    lower = src.all_text.lower()
    greeting = re.sub(r"^\s*(?:dear|to|hello|hi|greetings)\s+", "", letter.salutation or "", flags=re.I)
    greeting = re.sub(r"\b(?:hiring|search|recruiting)?\s*(?:team|manager|committee|panel)\b.*$", "",
                      greeting.rstrip(":,"), flags=re.I)
    for run, _loose in name_runs(greeting):
        if run.lower() in {"mr", "mrs", "ms", "mx", "dr"}:
            continue
        gone = missing_names(re.sub(r"^(?:Mr|Mrs|Ms|Mx|Dr)\.?\s+", "", run), lower, given)
        if gone:
            rep.fail("names", f"The salutation names \"{run}\", which isn't in the three files. A wrong "
                     "company or person in the greeting blocks the letter; a name the person gave in "
                     "the session goes in with --given.")
    for k, s in letter.sentences():
        digits, spelled = numbers(s)
        items = [(n, "number", True) for n in sorted(digits)] + [(n, "number", False) for n in sorted(spelled-digits)]
        items += [(d, "date", True) for d in sorted(month_years(s))]
        for n, kind, firm in items:
            where, proof = classify(n, src, kind)
            shown = n if kind == "number" else n.title()
            if where == "found":
                found += 1
            elif where == "deeper":
                rep.info("facts", f"{shown} (paragraph {k}) comes from {proof}'s deeper record, not the "
                         "resume. Check the letter tells it the way the story does.")
            elif where == "disagrees":
                rep.fail("facts", f"{shown} (paragraph {k}) is in {proof}, which says the resume shows it, "
                         "but the resume going with the letter doesn't. The positioning file and the "
                         "resume disagree; settle which is right before the letter goes out.")
            elif where == "notes":
                rep.warn("facts", f"{shown} (paragraph {k}) is only in the positioning file's working notes, "
                         "not in a proof, a firm fact, the posting or the resume. Check it.")
            elif firm:
                rep.fail("facts", f"{shown} (paragraph {k}) isn't in the three files: \"{s[:80]}\"")
            else:
                rep.warn("facts", f"'{shown}' written as a word (paragraph {k}) isn't in the three files. "
                         f"Check it: \"{s[:80]}\"")
        for c in sorted(year_counts(s)-src.year_counts):
            rep.fail("facts", f"Paragraph {k} gives a count of {c} years that the three files don't give: "
                     f"\"{s[:80]}\". A count of years ages, so it comes from the files' own dates.")
        for run, loose in name_runs(s):
            gone = missing_names(run, lower, given)
            if not gone:
                continue
            if loose:
                rep.warn("names", f"\"{run}\" (paragraph {k}) isn't in the three files. Check it's an "
                         "ordinary word and not a name.")
                continue
            shown = '", "'.join(gone)
            rep.fail("names", f"\"{shown}\" (paragraph {k}) isn't in the three files. A wrong "
                     "company, role or place name, or a name with no source, blocks the letter.")
    rep.info("facts", f"{found} number(s) and date(s) in the body found in the resume, the posting or "
             "the firm facts.")


def check_restated(letter, src, rep):
    lines = [re.sub(r"^\s*(?:[-*•]|\d+[.)])\s+", "", t) for t in src.resume.split("\n")]
    lines = [(n, t) for n, t in enumerate(lines, 1) if len(t.split()) >= 8]
    for k, s in letter.sentences():
        mine = words_only(s).split()
        for n, t in lines:
            theirs = words_only(t).split()
            share = lcs(mine, theirs) / len(theirs)
            if share >= 0.7:
                rep.fail("resume", f"Paragraph {k} restates resume line {n}: \"{s[:80]}\". Say what the "
                         "result meant for the people who paid for it, or tell its story.")
            elif share >= 0.5 and longest_run(mine, theirs) >= 6:
                rep.warn("resume", f"Paragraph {k} follows resume line {n} closely: \"{s[:80]}\". Check it "
                         "adds to the line instead of repeating it.")


def check_opening(letter, src, rep, referral):
    sentences = letter.sentences()
    first = " ".join(s for _k, s in sentences[:2])
    low = words_only(first)
    pos = src.pos
    company = pos.target.get("Company", {}).get("text", "") if pos else ""
    role = pos.target.get("Role", {}).get("text", "") if pos else ""
    forms = set()
    if company:
        words = [w for w in company.split() if w.lower().strip(".,") not in LEGAL]
        forms |= {" ".join(words), " ".join(words[:2]) if len(words) >= 3 else " ".join(words)}
    if role:
        forms |= {role, role.split(",")[0]}
    forms = {words_only(f) for f in forms if f.strip()}
    # The firm's own first word counts when the letter writes it as a name:
    # "Switchgrass" for Switchgrass Freight Co., "Ironwood" for Ironwood Trail Supply.
    lead = company.split()[0] if company.split() else ""
    named = bool(lead) and len(lead) >= 4 and re.search(r"(?<![\w])" + re.escape(lead) + r"(?![\w])",
                                                         first.translate(CURLY))
    if forms and not named and not any(f and f in low for f in forms):
        rep.fail("opening", "The first two sentences name neither the firm nor the seat. Name one of "
                 f"them early: {company or role}.")
    if referral and words_only(referral) not in low:
        rep.fail("opening", f"The referral, {referral}, belongs in the first two sentences.")
    if sentences:
        last = sentences[-1][1]
        if not ASK_WORDS.search(last):
            rep.warn("close", f"The last sentence should ask for a conversation about one named thing: "
                     f"\"{last[:90]}\"")
        stock = STOCK_ASK.search(last.translate(CURLY))
        if stock:
            rep.warn("close", f"The ask opens on a stock phrase, \"{stock.group(0).strip()}\". Write it the way "
                     "this writer would ask, starting from the named thing.")
        if letter.paragraphs and CLOSE_TELLS.search(letter.paragraphs[-1]):
            rep.warn("close", "The last paragraph thanks the reader or looks forward. The ask is the "
                     "last sentence.")


def check_keep_off(letter, src, rep):
    if not src.pos:
        return
    whole = src.cp.norm(letter.raw)
    for item in src.pos.keep_off:
        for phrase in item["watch"]:
            target = src.cp.norm(phrase)
            if target and target in whole:
                rep.fail("off the page", f"\"{phrase}\" is in the letter, from section 7's "
                         f"{item['kind']}{' ' + item['row'] if item['row'] else ''}.")


def check_sentence_list(letter, src, rep, show):
    terms = [src.cp.norm(t["term"]) for t in src.pos.terms] if src.pos else []
    empty = []
    for k, s in letter.sentences():
        named = [run for run, _loose in name_runs(s)]
        digits, spelled = numbers(s)
        named += sorted(digits | spelled)
        low = src.cp.norm(s) if src.pos else s.lower()
        named += [t for t in terms if t and t in low]
        if show:
            rep.info("sentences", f"Paragraph {k}: \"{s[:70]}\" names: " + (", ".join(named) or "nothing"))
        if not named:
            empty.append(f"\"{s[:60]}\" (paragraph {k})")
    if empty:
        rep.warn("sentences", f"{len(empty)} sentence(s) name no firm, number, tool, person or posting "
                 "term the script can see. Read each one, and give it its thing or cut it: " + "; ".join(empty))


def find_voice(cp, voice_dir):
    if voice_dir:
        folder = Path(voice_dir).resolve()
        if not cp.is_voice_dir(folder):
            raise InputError(f"{folder} doesn't hold plainspeak-writer.")
        return folder
    return cp.find_voice_dir(cp.default_roots())


def run_voice(folder, text, surface="letter", keep=()):
    """plainspeak-writer's checker on a text. Returns (hard, warn, version) where
    each hit is (line, message)."""
    checker = folder / "scripts" / "check_voice.py"
    with tempfile.TemporaryDirectory() as tmp:
        piece = Path(tmp) / "piece.txt"
        piece.write_bytes(text.encode("utf-8"))
        args = [sys.executable, str(checker), "--surface", surface, str(piece)]
        if keep:
            args[2:2] = ["--keep", ",".join(keep)]
        env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
        proc = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace",
                              env=env, timeout=120)
    if proc.returncode not in (0, 1):
        raise InputError("plainspeak-writer's checker stopped with an error: "
                         + (proc.stderr or proc.stdout).strip()[-200:])
    hard, warn, section = [], [], None
    for raw in proc.stdout.splitlines():
        if raw.startswith("HARD FAIL"):
            section = hard
        elif raw.startswith("WARN"):
            section = warn
        elif not raw.strip():
            section = None
        m = re.match(r"^\s+L(\d+):\s+(\[.+)$", raw)
        if m and section is not None:
            section.append((int(m.group(1)), m.group(2)))
    version = re.search(r"check_voice (\S+)", proc.stdout)
    return hard, warn, version.group(1) if version else "unknown"


def blocked_sentences(text, hard):
    """The sentences of a sample that hold a HARD hit."""
    lines = text.split("\n")
    out = []
    for line_no, message in hard:
        hit = re.search(r'\]\s+"(.+?)":', message)
        hit = hit.group(1) if hit else ""
        start = line_no
        while start > 1 and lines[start-2].strip():
            start -= 1
        stop = line_no
        while stop < len(lines) and lines[stop].strip():
            stop += 1
        para = " ".join(lines[start-1:stop])
        here = lines[line_no-1] if 0 < line_no <= len(lines) else ""
        picks = [s for s in split_sentences(para) if hit and hit.lower() in s.lower()]
        near = [s for s in picks if len(set(words_only(s).split()) & set(words_only(here).split())) >= 3]
        chosen = near or picks or ([here.strip()] if here.strip() else [])
        for s in chosen:
            if s not in out:
                out.append(s)
    return out


def check_samples(letter, src, rep, samples, voice):
    for path in samples:
        text = read_text(path)
        name = Path(path).name
        blocked = []
        if voice:
            hard, _warn, version = run_voice(voice, text)
            blocked = blocked_sentences(text, hard)
            if blocked:
                rep.info("samples", f"{name}: plainspeak-writer {version} blocks {len(blocked)} sentence(s), "
                         "set aside so they never move into the letter:")
                for s in blocked:
                    rep.info("samples", f"  set aside: \"{s[:100]}\"")
            else:
                rep.info("samples", f"{name}: plainspeak-writer {version} blocks nothing in it.")
        else:
            rep.warn("samples", f"plainspeak-writer wasn't found, so {name} wasn't checked for blocked phrases.")
        if letter is None:
            continue
        theirs = {words_only(s) for s in text_sentences(text)}
        blocked_keys = {words_only(s) for s in blocked}
        for k, s in letter.sentences():
            key = words_only(s)
            mine = key.split()
            if len(mine) >= MIN_WORDS and key in blocked_keys:
                rep.fail("samples", f"Paragraph {k} holds a sentence plainspeak-writer blocks in {name}: "
                         f"\"{s[:90]}\"")
                continue
            if any(longest_run(mine, words_only(b).split()) >= 8 for b in blocked):
                rep.fail("samples", f"Paragraph {k} holds most of a blocked sentence from {name}: \"{s[:90]}\"")
                continue
            if len(mine) >= MIN_WORDS and key in theirs:
                shared_sentence(k, s, name, letter, src, rep)


def shared_sentence(k, s, other, letter, src, rep):
    """A sentence the letter shares with earlier writing moves only with its fact."""
    rep.info("reuse", f"Paragraph {k} shares a sentence with {other}: \"{s[:90]}\"")
    if src and src.pos:
        digits, spelled = numbers(s)
        for n in sorted(digits | spelled):
            where, _p = classify(n, src, "number")
            if where in ("missing", "notes"):
                rep.fail("reuse", f"The shared sentence in paragraph {k} states {n}, which the three files "
                         "don't hold. A sentence moves only with a fact the files hold.")
    if TIME_WORDS.search(s):
        rep.warn("reuse", f"The shared sentence in paragraph {k} runs on time (\"{TIME_WORDS.search(s).group(0)}\"). "
                 "Check it against today's dates before it stays.")


def check_compare(letter, src, rep, other_path):
    other = Letter(other_path)
    theirs = {}
    for k, s in (other.sentences() if other.paragraphs else [(1, x) for x in text_sentences(other.raw)]):
        key = words_only(s)
        if len(key.split()) >= MIN_WORDS:
            theirs.setdefault(key, k)
    last = len(letter.paragraphs)
    shared = 0
    for k, s in letter.sentences():
        key = words_only(s)
        if key not in theirs:
            continue
        shared += 1
        if k in (1, last):
            part = "frame" if k == 1 else "invitation"
            rep.fail("reuse", f"The {part} shares a sentence with {Path(other_path).name}: \"{s[:90]}\". "
                     "The frame, the fit and the invitation are written for each firm.")
        else:
            shared_sentence(k, s, Path(other_path).name, letter, src, rep)
    rep.info("reuse", f"{shared} sentence(s) shared with {Path(other_path).name}. Any in a fit paragraph "
             "fails too; the map says which paragraph that is.")
    # Two letters whose asks open on the same words read as one template.
    mine = letter.sentences()
    if mine and other.paragraphs:
        ours, yours = (words_only(x).split()[:4] for x in (mine[-1][1], other.sentences()[-1][1]))
        if len(ours) == 4 and ours == yours:
            rep.warn("reuse", f"The ask opens the same way as in {Path(other_path).name}: "
                     f"\"{' '.join(mine[-1][1].split()[:4])}\". Write each letter's ask for its firm.")


def check_voice_on(letter, rep, voice, keep):
    if not voice:
        rep.warn("voice", "plainspeak-writer wasn't found, so the voice check didn't run. Point "
                 "--voice-dir at the folder that holds its SKILL.md.")
        return
    hard, warn, version = run_voice(voice, letter.voice_text, "letter", keep)
    for line, msg in hard:
        rep.fail("voice", f"L{line}: {msg}")
    for line, msg in warn:
        rep.warn("voice", f"L{line}: {msg}")
    rep.info("voice", f"plainspeak-writer {version}, letter surface, {len(hard)} HARD hit(s), "
             f"{len(warn)} warning(s).")


# Before drafting

def ai_policy_lines(posting):
    """Each posting sentence about AI in application materials, as (line, kind, sentence).

    kind is "bars" (the posting rules out AI-written materials), "disclose" (it
    asks applicants to say how they used AI), "unclear" (it speaks to AI use or
    the applicant's own words without a clear rule) or "employer" (it says the
    employer uses AI). A sentence that only names AI as a skill or a product,
    like "experience with generative AI tools", isn't listed."""
    found = []
    for n, line in enumerate(posting.translate(CURLY).splitlines(), 1):
        for s in text_sentences(line):
            if AI_TERM.search(s):
                bars = AI_BAR.search(s) and (AI_MATERIALS.search(s) or WHO.search(s))
                if AI_EMPLOYER.search(s) and not bars:
                    found.append((n, "employer", s))
                elif bars:
                    found.append((n, "bars", s))
                elif AI_DISCLOSE.search(s):
                    found.append((n, "disclose", s))
                elif AI_MATERIALS.search(s) and AI_UNCLEAR.search(s):
                    found.append((n, "unclear", s))
            elif OWN_WORDS.search(s) and (AI_MATERIALS.search(s) or OWN_WORDS_ALONE.search(s)):
                found.append((n, "unclear", s))
    return found


def check_ai_policy(src, rep):
    if not src.posting:
        rep.warn("ai-policy", "No posting to read for its rules on AI. Read the posting for them.")
        return
    lines = ai_policy_lines(src.posting)
    for n, kind, s in lines:
        quote = f"Posting line {n}: \"{s[:160]}\""
        if kind == "bars":
            rep.fail("ai-policy", f"The posting rules out AI-written application materials. {quote} Don't "
                     "draft. Tell the person, as SKILL.md step 1 says.")
        elif kind == "disclose":
            rep.warn("ai-policy", f"The posting asks applicants to disclose AI use. {quote} Remind the person "
                     "at hand-over.")
        elif kind == "unclear":
            rep.warn("ai-policy", f"The posting speaks to AI use or the applicant's own words. {quote} Quote "
                     "it to the person and ask how they read it before drafting.")
        else:
            rep.info("ai-policy", f"The posting says the employer uses AI. {quote} That's no rule on the "
                     "applicant's materials.")
    if not lines:
        rep.info("ai-policy", "The posting says nothing about AI in application materials.")


def check_proofs(src, rep):
    """The proofs marked for the letter against the resume that goes with it."""
    if not src.resume:
        rep.fail("gate", "No resume to compare the proofs with. Give the resume that goes with the letter.")
        return
    stamped = {f["file"]: f for f in src.pos.files}
    resume_roles = {f["file"] for f in src.pos.files if "resume being sent" in f["role"]}
    if src.resume_path and src.resume_path.name in stamped and src.resume_path.name in resume_roles:
        same = src.cp.file_hash(src.resume_path, len(stamped[src.resume_path.name]["sha256"]))
        if same == stamped[src.resume_path.name]["sha256"]:
            rep.info("gate", f"{src.resume_path.name} is the resume the case was built from, unchanged.")
        else:
            rep.fail("gate", f"{src.resume_path.name} has changed since the case was confirmed. Run "
                     "candidate-positioning again before the letter.")
    elif src.resume_path:
        rep.info("gate", f"{src.resume_path.name} isn't the resume the case was built from, so the proofs "
                 "were compared with it.")
    digits_r, spelled_r = numbers(src.resume)
    have = digits_r | spelled_r
    dates = month_years(src.resume)
    marked = [p for p in src.proofs() if p["use_on"] in ("letter", "both")]
    for p in marked:
        if not p["on_resume"]:
            rep.info("gate", f"{p['id']} is marked for the letter and isn't on the resume, so the letter "
                     "tells it from its story.")
            continue
        old_digits, old_spelled = numbers(src.stamped_resume)
        old_dates = month_years(src.stamped_resume)
        for part in ("result", "story"):
            digits, _spelled = numbers(p[part])
            missing = [d for d in sorted(digits) if d not in have]
            missing += [d.title() for d in sorted(month_years(p[part])) if d not in dates]
            if not missing:
                continue
            # The resume the case was built from held it, or the proof rests on the
            # resume alone, the two disagree. Otherwise it's from the deeper record.
            dropped = [d for d in missing if d in old_digits or d in old_spelled or d.lower() in old_dates]
            if dropped or p["only_resume"]:
                rep.fail("gate", f"{p['id']}'s {part} gives {', '.join(dropped or missing)}, and the resume "
                         "going with the letter doesn't. The positioning file and the resume disagree. "
                         "The resume being sent decides the facts, so bring the file in line before drafting.")
            else:
                rep.info("gate", f"{p['id']}'s {part} gives {', '.join(missing)} from the deeper record it "
                         "cites, not the resume.")
    contact = src.resume_contact()
    if contact:
        rep.info("gate", "The resume's contact block, for the letter's header: " + " / ".join(contact))


# The Word file

def docx_layout(path):
    """Font, size, margins, page size, and each paragraph's text, size and spacing."""
    with zipfile.ZipFile(path) as archive:
        doc = ET.fromstring(archive.read("word/document.xml"))
        styles = ET.fromstring(archive.read("word/styles.xml")) if "word/styles.xml" in archive.namelist() else None
    font, size = "calibri", 11.0
    if styles is not None:
        fonts = styles.find(f"{W}docDefaults/{W}rPrDefault/{W}rPr/{W}rFonts")
        if fonts is not None and fonts.get(W + "ascii"):
            font = fonts.get(W + "ascii").lower()
        sz = styles.find(f"{W}docDefaults/{W}rPrDefault/{W}rPr/{W}sz")
        if sz is not None:
            size = int(sz.get(W + "val")) / 2
    sect = doc.find(f".//{W}sectPr")
    page = (12240, 15840)
    margins = (1440, 1440, 1440, 1440)
    if sect is not None:
        pg = sect.find(W + "pgSz")
        if pg is not None:
            page = (int(pg.get(W + "w", 12240)), int(pg.get(W + "h", 15840)))
        mar = sect.find(W + "pgMar")
        if mar is not None:
            margins = tuple(int(mar.get(W + k, 1440)) for k in ("top", "right", "bottom", "left"))
    paras = []
    for p in doc.iter(W + "p"):
        text = "".join(t.text or "" for t in p.iter(W + "t"))
        szs = [int(s.get(W + "val")) / 2 for s in p.iter(W + "sz")]
        sp = p.find(f"{W}pPr/{W}spacing")
        before = int(sp.get(W + "before", 0)) / 20 if sp is not None else 0
        after = int(sp.get(W + "after", 0)) / 20 if sp is not None else 0
        paras.append((text, max(szs) if szs else size, before, after))
    return font, size, margins, page, paras


def estimate_pages(paras, font, margins, page):
    """Pages the paragraphs fill, by the font's average character width and line
    height. It leans toward more lines, so an estimate under one page fits."""
    key = font.lower()
    width_em = FONT_WIDTH.get(key, max(FONT_WIDTH.values()))*SAFETY
    height_em = LINE_HEIGHT.get(key, max(LINE_HEIGHT.values()))
    top, right, bottom, left = margins
    line_pt = (page[0]-left-right)/20
    avail = (page[1]-top-bottom)/20
    used = 0.0
    lines = 0
    for text, size, before, after in paras:
        per_line = max(1, int(line_pt/(width_em*size)))
        count, cur = 1, 0
        for word in text.split():
            need = len(word) if cur == 0 else cur+1+len(word)
            if need > per_line and cur:
                count += 1
                cur = len(word)
            else:
                cur = need
        lines += count
        used += before+after+count*size*height_em
    return used/avail, lines


def check_docx(path, rep, expected_name):
    try:
        archive = zipfile.ZipFile(path)
    except zipfile.BadZipFile:
        raise InputError(f"{Path(path).name} isn't a readable Word file.")
    with archive:
        names = archive.namelist()
        doc = archive.read("word/document.xml").decode("utf-8", errors="replace")
        core = archive.read("docProps/core.xml").decode("utf-8", errors="replace") if "docProps/core.xml" in names else ""
        app = archive.read("docProps/app.xml").decode("utf-8", errors="replace") if "docProps/app.xml" in names else ""
        for part in names:
            if re.match(r"word/(header|footer)\d*\.xml$", part):
                if re.search(r"<w:t[ >]", archive.read(part).decode("utf-8", errors="replace")):
                    rep.fail("word", f"{part} holds text. Letter text goes in the body, never in a header or footer.")
    if re.search(r"<w:tbl[ >]", doc):
        rep.fail("word", "The Word file holds a table. Letter text goes in plain paragraphs.")
    if re.search(r"txbxContent|<v:textbox|wps:txbx", doc):
        rep.fail("word", "The Word file holds a text box. Letter text goes in plain paragraphs.")
    if re.search(r'<w:cols[^>]*w:num="([2-9])"', doc):
        rep.fail("word", "The Word file is set in more than one column.")
    if re.search(r"<w:drawing|<w:pict", doc):
        rep.warn("word", "The Word file holds a picture or a drawing. A letter is one column of text.")
    creator = re.search(r"<dc:creator>([^<]*)</dc:creator>", core)
    creator = creator.group(1).strip() if creator else ""
    modified_by = re.search(r"<cp:lastModifiedBy>([^<]*)</cp:lastModifiedBy>", core)
    modified_by = modified_by.group(1).strip() if modified_by else ""
    if not creator:
        rep.fail("word", "The author field is empty. It names the writer.")
    elif LIBRARY_AUTHORS.search(creator):
        rep.fail("word", f"The author field reads \"{creator}\", a tool rather than the writer.")
    elif expected_name and not same_name(creator, expected_name):
        rep.fail("word", f"The author field reads \"{creator}\", and the writer is {expected_name}.")
    else:
        rep.info("word", f"Author: {creator}.")
    if modified_by and LIBRARY_AUTHORS.search(modified_by):
        rep.fail("word", f"'Last modified by' reads \"{modified_by}\", a tool rather than the writer.")
    application = re.search(r"<Application>([^<]*)</Application>", app)
    if application:
        rep.info("word", f"The file says it was made in {application.group(1)}.")
    font, _size, margins, page, paras = docx_layout(path)
    pages, lines = estimate_pages(paras, font, margins, page)
    if pages > 1:
        rep.fail("word", f"About {pages:.2f} pages by estimate ({lines} lines). A letter fits on one page; "
                 "cut words, not spacing.")
    elif pages > 0.95:
        rep.warn("word", f"About {pages:.2f} pages by estimate, close to the edge. Open it in Word to see the break.")
    else:
        rep.info("word", f"About {pages:.2f} of a page by estimate ({lines} lines, {font.title()}).")


# Command line

def print_report(title, rep):
    print(f"check_letter {__version__}   {title}")

    def show(head, items):
        if not items:
            return
        print(f"{head} ({len(items)}):")
        for tag, msg in items:
            print(f"  [{tag}] {msg}")
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


def channel_from(pos):
    text = pos.target.get("Channel", {}).get("text", "").lower() if pos else ""
    if text.startswith("upload"):
        return "upload", None
    if text.startswith("text box") or text.startswith("textbox"):
        limit = re.search(r"(\d[\d,]*)\s*(?:-|\s)?\s*character", text)
        return "textbox", int(limit.group(1).replace(",", "")) if limit else None
    if text.startswith("email"):
        return "email", None
    return None, None


def referral_from(pos):
    text = pos.target.get("Reader", {}).get("text", "") if pos else ""
    if not text.lower().startswith("warm"):
        return None
    m = re.search(r"\b([A-Z][a-z'-]+(?:\s+[A-Z][a-z'-]+)+)", text[4:])
    return m.group(1) if m else None


def parser():
    ap = argparse.ArgumentParser(prog="check_letter.py", allow_abbrev=False,
                                 description="Check a cover letter against the three files it rests on.")
    ap.add_argument("letter", nargs="?", help="the letter: .txt, .md or .docx (leave out to check before drafting)")
    ap.add_argument("--positioning", help="the positioning file for the posting")
    ap.add_argument("--resume", help="the resume that goes with the letter (default: the stamp's)")
    ap.add_argument("--posting", help="the posting (default: the stamp's)")
    ap.add_argument("--channel", choices=CHANNELS, help="upload, textbox or email (default: the file's)")
    ap.add_argument("--limit", type=int, help="a text box's character limit")
    ap.add_argument("--referral", help="the referrer's name, for a warm reader (default: the file's)")
    ap.add_argument("--sample", action="append", default=[], help="a voice sample the person picked; repeat for more")
    ap.add_argument("--compare", action="append", default=[], help="another letter by the same writer")
    ap.add_argument("--voice", action="store_true", help="run plainspeak-writer's checker on the letter")
    ap.add_argument("--voice-dir", help="the plainspeak-writer folder, when it isn't found on its own")
    ap.add_argument("--keep", action="append", default=[], help="names the voice check skips, as plainspeak-writer's --keep")
    ap.add_argument("--sentences", action="store_true", help="list every sentence with what it names")
    ap.add_argument("--given", action="append", default=[],
                    help="a name the person gave in this session, like the hiring manager's; repeat for more")
    ap.add_argument("--name", help="the writer's name, for a Word file's author field")
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return ap


def main(argv=None):
    args = parser().parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    rep = Report()
    cp = None
    try:
        cp = load_cp() if (args.positioning or args.voice or args.sample) else None
        src = Sources(cp, args.positioning, args.resume, args.posting) if cp else None
        if src is None and (args.resume or args.posting):
            cp = load_cp()
            src = Sources(cp, None, args.resume, args.posting)
        voice = find_voice(cp, args.voice_dir) if cp and (args.voice or args.sample) else None
        if not args.letter:
            if not (src and src.pos):
                print("Name the letter to check, or give --positioning to check before drafting.", file=sys.stderr)
                return 2
            check_ai_policy(src, rep)
            check_proofs(src, rep)
            check_samples(None, src, rep, args.sample, voice)
            print_report(Path(args.positioning).name + " (before drafting)", rep)
            return 1 if rep.fails else 0
        path = Path(args.letter)
        letter = Letter(path)
        file_channel, file_limit = channel_from(src.pos if src else None)
        channel = args.channel or file_channel
        limit = args.limit or file_limit
        rep.info("letter", f"Body: {letter.words} words in {len(letter.paragraphs)} paragraph(s). "
                 f"Letter: {letter.characters:,} characters. Channel: {channel or 'not given'}.")
        if check_shape(letter, rep, channel):
            check_limit(letter, rep, limit)
            if src and src.resume:
                check_against_resume(letter, src, rep, channel)
            if src and src.pos:
                check_facts(letter, src, rep, tuple(args.given))
                check_restated(letter, src, rep)
                check_opening(letter, src, rep, args.referral or referral_from(src.pos))
                check_keep_off(letter, src, rep)
                check_sentence_list(letter, src, rep, args.sentences)
                if channel == "email" and letter.subject:
                    role = src.pos.target.get("Role", {}).get("text", "")
                    if role and words_only(role.split(",")[0]) not in words_only(letter.subject):
                        rep.warn("channel", f"The subject line doesn't name the role, {role}.")
            elif src and src.resume:
                check_restated(letter, src, rep)
            check_samples(letter, src, rep, args.sample, voice)
            for other in args.compare:
                check_compare(letter, src, rep, other)
        if path.suffix.lower() == ".docx":
            expected = args.name or (src.resume_name() if src and src.resume else None) or letter.name
            check_docx(path, rep, expected)
        if args.voice:
            check_voice_on(letter, rep, voice, tuple(t.strip() for v in args.keep for t in v.split(",") if t.strip()))
    except InputError as exc:
        print(f"The letter can't be checked, because {exc}", file=sys.stderr)
        return 2
    except Exception as exc:  # a positioning file the script can't read
        if cp and isinstance(exc, getattr(cp, "InputError", ())):
            print(f"The letter can't be checked, because {exc}", file=sys.stderr)
            return 2
        raise
    print_report(Path(args.letter).name, rep)
    return 1 if rep.fails else 0


if __name__ == "__main__":
    sys.exit(main())
