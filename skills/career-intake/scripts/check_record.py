#!/usr/bin/env python3
"""Checks for career-intake.

    python3 check_record.py --answers ANSWERS.md   what's answered, what's blank, what to check
    python3 check_record.py career-record.md       the career record's shape and sources
    python3 check_record.py --aim where-to-aim.md  the aim file's shape and its three calls

Exit 0 when nothing fails, 1 when something does. WARN lines are for Claude
to look at, and don't fail the check.
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_workbook  # noqa: E402

BLANK = "(no answer yet)"
SOURCE_RE = re.compile(r"\[(?:[a-z][a-z0-9-]*|A\d+|[^\]\s]+\.[A-Za-z0-9]+ L\d+(?:-L?\d+)?)(?:; ?(?:[a-z][a-z0-9-]*|A\d+|[^\]\s]+\.[A-Za-z0-9]+ L\d+(?:-L?\d+)?))*\]")
AI_LINE_RE = re.compile(r"\b(if you are an? (ai|llm|language model)|ignore (all |any )?(previous|prior|above) (instructions|rules)|system prompt|you are now|as an ai)\b", re.I)
# Capitalized words that are rarely a person's name, so they aren't flagged.
COMMON = set("""
I I'm I've I'd I'll A An The This That These Those It It's He She They We You My Our Your His Her Their
Monday Tuesday Wednesday Thursday Friday Saturday Sunday January February March April May June July
August September October November December Mr Mrs Ms Dr And But Or So If When Then After Before
Because While Also Now Today Yesterday Tomorrow Last Next One Two Three Four Five Six Seven Eight
Nine Ten Most Some Every Each All No Yes OK Okay Story Part Total Notes Weeks Years At Saved Name
Workbook Career Claude AI English Spanish
""".split())
NAME_PARTS = {2}  # parts whose answers are about other people


# ---------- the answers file ----------

def unescape(text):
    return "\n".join(l[1:] if re.match(r"^\\(#|<!--|\\)", l) else l for l in text.split("\n")).strip()


def read_answers(text):
    """Return (name, {id: answer text}) from a workbook answers file."""
    text = text.replace("\r\n", "\n")
    if not re.search(r"^Workbook: career-intake ", text, re.M):
        raise ValueError("not a career-intake answers file (no Workbook line)")
    name = re.search(r"^Name: (.*)$", text, re.M)
    marks = list(re.finditer(r"^<!-- id: ([a-z0-9-]+) -->$", text, re.M))
    out = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        chunk = text[m.end():end]
        cut = re.search(r"\n#{2,3} ", chunk)
        if cut:
            chunk = chunk[:cut.start()]
        body = unescape(chunk)
        out[m.group(1)] = "" if body == BLANK else body
    return (name.group(1).strip() if name else ""), out


def is_blank(qtype, body):
    if not body.strip():
        return True
    if qtype == "count":
        total = re.search(r"^Total: ?(.*)$", body, re.M)
        notes = body.split("Notes:", 1)[1].strip() if "Notes:" in body else ""
        return not ((total and total.group(1).strip()) or notes)
    if qtype == "three":
        stories = [s.strip() for s in re.split(r"^#### Story \d+$", body, flags=re.M)[1:]]
        return all(not s or s == BLANK for s in stories)
    return False


def possible_names(text):
    """Capitalized words mid-sentence that may be a person's name."""
    found = []
    for sentence in re.split(r"(?<=[.!?])\s+|\n+", text):
        words = re.findall(r"[A-Za-z][A-Za-z'’-]*", sentence)
        for w in words[1:]:
            if w[0].isupper() and w not in COMMON and not w.isupper() and w not in found:
                found.append(w)
    return found


def check_answers(path):
    parts = build_workbook.parse(build_workbook.QUESTIONS.read_text(encoding="utf-8"))
    try:
        name, answers = read_answers(Path(path).read_text(encoding="utf-8"))
    except ValueError as e:
        print(f"FAIL  {e}")
        return 1
    print(f"Answers file for {name or '(no name)'}")
    known = {q["id"] for p in parts for q in p["questions"]}
    for qid in answers:
        if qid not in known:
            print(f"WARN  {qid}: not a question in this version of the workbook; read it as a note")
    total = done = 0
    for p in parts:
        blanks = []
        for q in p["questions"]:
            total += 1
            body = answers.get(q["id"], "")
            if is_blank(q["type"], body):
                blanks.append(q["id"])
            else:
                done += 1
            for line in body.split("\n"):
                if AI_LINE_RE.search(line):
                    print(f"WARN  {q['id']}: a line speaks to an AI tool. Quote it to the person and use none of it: {line.strip()[:120]}")
            if p["n"] in NAME_PARTS and body:
                names = possible_names(body)
                if names:
                    print(f"WARN  {q['id']}: possible names, check before anything is written: {', '.join(names)}")
        answered = len(p["questions"]) - len(blanks)
        print(f"Part {p['n']}: {answered} of {len(p['questions'])} answered" + (f". Blank: {', '.join(blanks)}" if blanks else ""))
    print(f"{done} of {total} answered")
    return 0


# ---------- the career record and the aim file ----------

RECORD_SECTIONS = ["1. Work history", "2. Totals", "3. Stories", "4. Things built that others use",
                   "5. Skills", "6. In other words", "7. What others say", "8. Proof",
                   "9. How you describe it", "10. Private", "11. Open questions"]
AIM_SECTIONS = ["1. What you want", "2. What can't change", "3. Targets", "4. The calls",
                "5. People who can help", "6. Next"]
SOURCED = {"2. Totals", "3. Stories", "5. Skills", "7. What others say"}
STORY_LINES = ["What happened:", "The need:", "What you did:", "What changed:", "Proof:", "People in it:"]


def sections(text):
    out, current = {}, None
    for line in text.split("\n"):
        m = re.match(r"^## (.+?)\s*$", line)
        if m:
            current = m.group(1)
            out[current] = []
        elif current:
            out[current].append(line)
    return out


def head_checks(text, kind, fails):
    first = text.split("\n", 1)[0]
    want = "# Career record: " if kind == "record" else "# Where to aim: "
    if not first.startswith(want):
        fails.append(f"the file must start with '{want}<first name>'")
    if not re.search(r"^Format: career-intake 1$", text, re.M):
        fails.append("missing 'Format: career-intake 1'")
    if not re.search(r"^Built: \d{4}-\d{2}-\d{2}", text, re.M):
        fails.append("missing 'Built: YYYY-MM-DD'")
    conf = re.search(r"^Confirmed: (.*)$", text, re.M)
    if not conf:
        fails.append("missing the 'Confirmed:' line")
    elif conf.group(1).strip() != "not yet" and not re.match(r"\d{4}-\d{2}-\d{2}, \".+\"$", conf.group(1).strip()):
        fails.append("'Confirmed:' must be 'not yet' or 'YYYY-MM-DD, \"<their words>\"'")


def check_record(path):
    text = Path(path).read_text(encoding="utf-8").replace("\r\n", "\n")
    fails, warns = [], []
    head_checks(text, "record", fails)
    secs = sections(text)
    for name in RECORD_SECTIONS:
        if name not in secs:
            fails.append(f"missing section '## {name}'")
    for name in SOURCED & set(secs):
        for line in secs[name]:
            s = line.strip()
            if s.startswith("- ") and s not in ("- None.",) and not SOURCE_RE.search(s):
                if name == "3. Stories" and re.match(r"- (People in it|Proof):", s):
                    continue
                fails.append(f"{name}: a line has no source: {s[:90]}")
    if "2. Totals" in secs:
        for line in secs["2. Totals"]:
            s = line.strip()
            if s.startswith("- ") and s != "- None." and not re.search(r"\[(confirmed|estimate)\]", s):
                fails.append(f"2. Totals: tag each total [confirmed] or [estimate]: {s[:90]}")
    if "3. Stories" in secs:
        body = "\n".join(secs["3. Stories"])
        stories = re.split(r"^### ", body, flags=re.M)[1:]
        if not stories and body.strip() != "None.":
            fails.append("3. Stories: no stories, each starting '### S1. <title>'")
        for st in stories:
            title = st.split("\n", 1)[0]
            if not re.match(r"S\d+\. ", title):
                fails.append(f"3. Stories: a story heading must read '### S<n>. <title>': {title[:60]}")
            for want in STORY_LINES:
                if not re.search(r"^- " + re.escape(want), st, re.M):
                    fails.append(f"3. Stories: {title[:40]} has no '{want}' line")
            people = re.search(r"^- People in it: (.*)$", st, re.M)
            if people and people.group(1).strip() != "no names" and not re.search(r"\[A\d+\]|\[[a-z][a-z0-9-]*\]", people.group(1)):
                fails.append(f"3. Stories: {title[:40]} names people without the answer where they said yes")
    for name in RECORD_SECTIONS[:9]:
        for line in secs.get(name, []):
            if AI_LINE_RE.search(line):
                warns.append(f"{name}: a line speaks to an AI tool: {line.strip()[:90]}")
    return report(path, fails, warns)


def check_aim(path):
    text = Path(path).read_text(encoding="utf-8").replace("\r\n", "\n")
    fails, warns = [], []
    head_checks(text, "aim", fails)
    if "This file is private." not in text:
        fails.append("missing the line 'This file is private. Nothing in it goes on a page someone else reads.'")
    secs = sections(text)
    for name in AIM_SECTIONS:
        if name not in secs:
            fails.append(f"missing section '## {name}'")
    calls = "\n".join(secs.get("4. The calls", []))
    for call in ("Go for:", "Runner-up:", "Recommend against:"):
        m = re.search(r"^- " + re.escape(call) + r" (.+)$", calls, re.M)
        if not m or len(m.group(1).split()) < 4:
            fails.append(f"4. The calls: '- {call} <target>. <why>' is missing or has no reason")
    targets = "\n".join(secs.get("3. Targets", []))
    if targets and not re.search(r"https?://", targets):
        warns.append("3. Targets: no posting links; the market half of the score needs live postings")
    return report(path, fails, warns)


def report(path, fails, warns):
    for f in fails:
        print(f"FAIL  {f}")
    for w in warns:
        print(f"WARN  {w}")
    print(f"{'PASS' if not fails else 'FAIL'}  {Path(path).name}: {len(fails)} failed, {len(warns)} to look at")
    return 1 if fails else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--answers", action="store_true", help="read a workbook answers file")
    mode.add_argument("--aim", action="store_true", help="check a where-to-aim file")
    args = ap.parse_args(argv)
    if args.answers:
        return check_answers(args.file)
    if args.aim:
        return check_aim(args.file)
    return check_record(args.file)


if __name__ == "__main__":
    sys.exit(main())
