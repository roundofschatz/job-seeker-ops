#!/usr/bin/env python3
"""Checks for career-intake.

    python3 check_record.py --answers ANSWERS.md   what's answered, what's blank, what to check
    python3 check_record.py career-record.md       the career record's shape and sources
    python3 check_record.py --aim where-to-aim.md  the aim file's shape and its three calls

Exit 0 when nothing fails, 1 when something does. WARN lines are for Claude
to look at, and don't fail the check. The name check is a list of words to
look at, never a guarantee: lowercase names and names that are also common
words get past it, so Claude still reads every line.
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_workbook  # noqa: E402

BLANK = "(no answer yet)"
QID = r"[a-z][a-z0-9]*(?:-[a-z0-9]+)+"
FILE_SRC = r"[^\[\];,]+?\.[A-Za-z0-9]+ (?:L\d+(?:-L?\d+)?|p\d+(?:-p?\d+)?)"
ONE_SRC = r"(?:" + QID + r"|A\d+|" + FILE_SRC + r")"
SOURCE_RE = re.compile(r"\[(" + ONE_SRC + r"(?:[;,] ?" + ONE_SRC + r")*)\]")
AI_LINE_RE = re.compile(r"\b(if you are an? (ai|llm|language model)|ignore (all |any )?(previous|prior|above) (instructions|rules)|system prompt|you are now|as an ai)\b", re.I)

# Capitalized words that are rarely a person's or a place's name.
COMMON = set("""
I I'm I've I'd I'll A An The This That These Those It It's He She They We You My Our Your His Her Their
Him Them Me Us There Here What When Where Why How Who Which Not Never Always Sometimes Maybe Then
Monday Tuesday Wednesday Thursday Friday Saturday Sunday January February March April May June July
August September October November December And But Or So If After Before Because While Also Now
Today Yesterday Tomorrow Last Next One Two Three Four Five Six Seven Eight Nine Ten Most Some Every
Each All No Yes OK Okay Story Part Total Notes Weeks Years At Saved Name Workbook Career Claude AI
English Spanish To In On Of For With From By As Up Out Over Once Twice First Second Third Lots Many
Mostly Usually Probably Sure Thanks Well Just Still Even Only Again Being Got Get Went Did Do Does Had
Has Have Was Were Is Are Be Been Can Could Would Should Will Let Lets Let's Like Talk Tell Help Helped
Worked Work Working Managed Built Trained Led Ran Made Kept Started Took Gave Said Told Asked Called
Center Health Medical Mental Hospital County School District Program Department Services Service
University College Clinic Crisis Team Office Unit State City Board Court Police Fire Church Group
Excel Word Outlook Teams Zoom Google Microsoft PowerPoint What's That's There's Don't Didn't Can't
None Open Proof Before After Health Plans Plan Manager Director Coordinator Specialist Lead Senior
Assistant Associate Analyst Counselor Teacher Supervisor Case Worker Social Clinical Customer Success
""".split())
TITLES = {"Dr", "Mr", "Mrs", "Ms", "Miss", "Mx", "Prof", "Officer", "Judge", "Pastor", "Coach", "Nurse"}
NAME_VERBS = re.compile(r"^(said|says|called|calls|told|asked|was|is|had|has|came|went|got|stopped|started|stayed|left|died|lived|lives|wanted|needed|would|could|didn't|wasn't|and)$", re.I)


def parts():
    return build_workbook.parse(build_workbook.QUESTIONS.read_text(encoding="utf-8"))


def question_ids():
    ps = parts()
    return ({q["id"] for p in ps for q in p["questions"]},
            {q["id"] for p in ps for q in p["questions"] if q.get("private")})


def read_text(path):
    return Path(path).read_text(encoding="utf-8-sig").replace("\r\n", "\n")


def possible_names(text):
    """Words that may be a person's or a place's name."""
    found = []
    for line in text.split("\n"):
        line = re.sub(r"^\s*(?:[-*•]|\d+[.)])\s+", "", line)
        line = re.sub(r"^[A-Z][a-z]+(?: [a-z]+){0,3}: ", "", line)
        line = re.sub(r"\b(" + "|".join(TITLES) + r")\.", r"\1", line)
        for sentence in re.split(r"(?<=[.!?:;])\s+", line):
            words = re.findall(r"[A-Za-z][A-Za-z'’-]*", sentence)
            for i, w in enumerate(words):
                base = re.sub(r"['’]s$", "", w)
                if len(base) < 2 or not base[:1].isupper() or base.isupper():
                    continue
                if base in COMMON or w in COMMON or base in TITLES:
                    continue
                after_title = i > 0 and words[i - 1] in TITLES
                if i == 0 and not after_title:
                    nxt = words[i + 1] if i + 1 < len(words) else ""
                    if not (NAME_VERBS.match(nxt) or (nxt[:1].isupper() and nxt not in COMMON)):
                        continue
                if base not in found:
                    found.append(base)
    return found


# ---------- the answers file ----------

def unescape(text):
    return "\n".join(l[1:] if re.match(r"^\\(#|<!--|\\)", l) else l for l in text.split("\n")).strip()


def read_answers(text):
    """Return (name, {id: answer text}) from a workbook answers file."""
    text = text.lstrip("﻿").replace("\r\n", "\n")
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


def check_answers(path):
    ps = parts()
    try:
        name, answers = read_answers(Path(path).read_text(encoding="utf-8"))
    except ValueError as e:
        print(f"FAIL  {e}")
        return 1
    print(f"Answers file for {name or '(no name)'}")
    known = {q["id"] for p in ps for q in p["questions"]}
    for qid in answers:
        if qid not in known:
            print(f"WARN  {qid}: not a question in this version of the workbook; read it as a note")
    total = done = 0
    for p in ps:
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
            names = possible_names(body) if body else []
            if names:
                print(f"WARN  {q['id']}: possible names or places, check before anything is written: {', '.join(names)}")
        answered = len(p["questions"]) - len(blanks)
        print(f"Part {p['n']}: {answered} of {len(p['questions'])} answered" + (f". Blank: {', '.join(blanks)}" if blanks else ""))
    print(f"{done} of {total} answered")
    private = [q["id"] for p in ps for q in p["questions"] if q.get("private")]
    print(f"Private, for where-to-aim.md only: {', '.join(private)}")
    return 0


# ---------- the career record and the aim file ----------

RECORD_SECTIONS = ["1. Work history", "2. Totals", "3. Stories", "4. Things built that others use",
                   "5. Skills", "6. In other words", "7. What others say", "8. Proof",
                   "9. How you describe it", "10. Open questions"]
AIM_SECTIONS = ["1. What you want", "2. What can't change", "3. Private notes", "4. Targets",
                "5. The calls", "6. People who can help", "7. Next"]
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


def bullet(line):
    m = re.match(r"^\s*(?:[-*]|\d+[.)])\s+(.*)$", line)
    return m.group(1).strip() if m else None


def is_none(s):
    return s.strip().rstrip(".").lower() == "none"


def cited_ids(line):
    out = []
    for m in SOURCE_RE.finditer(line):
        out += [p for p in re.split(r"[;,] ?", m.group(1)) if re.fullmatch(QID, p)]
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
    elif conf.group(1).strip() != "not yet" and not re.match(r"\d{4}-\d{2}-\d{2}, [\"“].+[\"”]$", conf.group(1).strip()):
        fails.append("'Confirmed:' must be 'not yet' or 'YYYY-MM-DD, \"<their words>\"'")


def source_checks(secs, known, fails):
    for name, lines in secs.items():
        for line in lines:
            for cited in cited_ids(line):
                if cited not in known:
                    fails.append(f"{name}: [{cited}] isn't a question in references/questions.md")


def check_record(path):
    text = read_text(path)
    fails, warns = [], []
    known, private = question_ids()
    head_checks(text, "record", fails)
    secs = sections(text)
    for name in RECORD_SECTIONS:
        if name not in secs:
            fails.append(f"missing section '## {name}'")
    for name in secs:
        if re.match(r"\d+\. Private", name):
            fails.append(f"'## {name}': private material goes in where-to-aim.md, never in the record, which other skills read")
    source_checks(secs, known, fails)
    for name, lines in secs.items():
        for line in lines:
            for cited in set(cited_ids(line)) & private:
                fails.append(f"{name}: cites the private answer [{cited}]; it belongs in where-to-aim.md")
    for name in SOURCED & set(secs):
        for line in secs[name]:
            s = bullet(line)
            if s is None or is_none(s):
                continue
            if name == "3. Stories" and re.match(r"(People in it|Proof):", s):
                continue
            if not SOURCE_RE.search(s):
                fails.append(f"{name}: a line has no source: {s[:90]}")
    for line in secs.get("2. Totals", []):
        s = bullet(line)
        if s and not is_none(s) and not re.search(r"\[(confirmed|estimate)\]", s):
            fails.append(f"2. Totals: tag each total [confirmed] or [estimate]: {s[:90]}")
    named_ok = set()
    if "3. Stories" in secs:
        body = "\n".join(secs["3. Stories"])
        stories = re.split(r"^### ", body, flags=re.M)[1:]
        if not stories and not is_none(body):
            fails.append("3. Stories: no stories, each starting '### S1. <title>'")
        for st in stories:
            title = st.split("\n", 1)[0]
            if not re.match(r"S\d+\. ", title):
                fails.append(f"3. Stories: a story heading must read '### S<n>. <title>': {title[:60]}")
            for want in STORY_LINES:
                if not re.search(r"^\s*[-*] " + re.escape(want), st, re.M):
                    fails.append(f"3. Stories: {title[:40]} has no '{want}' line")
            people = re.search(r"^\s*[-*] People in it: (.*)$", st, re.M)
            if people and people.group(1).strip().rstrip(".").lower() != "no names":
                if not SOURCE_RE.search(people.group(1)):
                    fails.append(f"3. Stories: {title[:40]} names people without the answer where they said yes")
                else:
                    named_ok.update(re.findall(r"[A-Z][a-z]+", SOURCE_RE.sub("", people.group(1))))
    head_name = text.split("\n", 1)[0].split(":", 1)[-1].strip()
    for name in [n for n in RECORD_SECTIONS if n != "10. Open questions"] + ["Answers in this session"]:
        body = "\n".join(secs.get(name, []))
        body = re.sub(r"https?://\S+", "", SOURCE_RE.sub("", body))
        names = [n for n in possible_names(body) if n not in named_ok and n != head_name]
        if names:
            warns.append(f"{name}: possible names or places; keep only the ones with a yes: {', '.join(names)}")
        for line in body.split("\n"):
            if AI_LINE_RE.search(line):
                warns.append(f"{name}: a line speaks to an AI tool: {line.strip()[:90]}")
    return report(path, fails, warns)


def check_aim(path):
    text = read_text(path)
    fails, warns = [], []
    known, _ = question_ids()
    head_checks(text, "aim", fails)
    if "This file is private." not in text:
        fails.append("missing the line 'This file is private. Nothing in it goes on a page someone else reads.'")
    secs = sections(text)
    for name in AIM_SECTIONS:
        if name not in secs:
            fails.append(f"missing section '## {name}'")
    source_checks(secs, known, fails)
    calls = "\n".join(secs.get("5. The calls", []))
    for call in ("Go for:", "Runner-up:", "Recommend against:"):
        m = re.search(r"^\s*[-*] " + re.escape(call) + r" (.+)$", calls, re.M)
        if not m or len(m.group(1).split()) < 4:
            fails.append(f"5. The calls: '- {call} <target>. <why>' is missing or has no reason")
    targets = "\n".join(secs.get("4. Targets", []))
    if targets and not re.search(r"https?://", targets):
        warns.append("4. Targets: no posting links; the market half of the score needs live postings")
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
