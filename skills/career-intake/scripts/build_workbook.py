#!/usr/bin/env python3
"""Build career-intake's workbook from its questions file.

    python3 scripts/build_workbook.py            write assets/workbook.html
    python3 scripts/build_workbook.py --check    exit 1 when workbook.html is out of date
    python3 scripts/build_workbook.py --json     print the questions as JSON

references/questions.md is the one home of the questions. The workbook is
built from it, so the chat and the workbook always ask the same thing. Never
edit workbook.html by hand: edit the questions or the template, then build.
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
QUESTIONS = HERE / "references" / "questions.md"
TEMPLATE = HERE / "assets" / "workbook.template.html"
OUTPUT = HERE / "assets" / "workbook.html"
WORKBOOK_VERSION = "1"
TYPES = {"", "count", "three"}
ID_RE = re.compile(r"^[a-z][a-z0-9-]*$")


def parse(text):
    """Read the parts and questions. Raises ValueError on a malformed file."""
    parts, part, q = [], None, None
    for n, raw in enumerate(text.replace("\r\n", "\n").split("\n"), 1):
        line = raw.rstrip()
        m = re.match(r"^## Part (\d+): (.+)$", line)
        if m:
            part = {"n": int(m.group(1)), "title": m.group(2).strip(), "intro": [], "questions": []}
            parts.append(part)
            q = None
            continue
        if line.startswith("## "):
            part, q = None, None
            continue
        if part is None:
            continue
        m = re.match(r"^### (.+)$", line)
        if m:
            qid = m.group(1).strip()
            if not ID_RE.match(qid):
                raise ValueError(f"line {n}: question id {qid!r} must be lowercase letters, numbers and hyphens")
            q = {"id": qid, "text": "", "hint": "", "type": ""}
            part["questions"].append(q)
            continue
        if not line.strip():
            continue
        if q is None:
            part["intro"].append(line.strip())
        elif line.startswith("Hint:"):
            q["hint"] = line[5:].strip()
        elif line.startswith("Type:"):
            q["type"] = line[5:].strip()
            if q["type"] not in TYPES:
                raise ValueError(f"line {n}: unknown type {q['type']!r}")
        else:
            q["text"] = (q["text"] + " " + line.strip()).strip()
    if not parts:
        raise ValueError("no parts found")
    seen = set()
    for i, part in enumerate(parts, 1):
        if part["n"] != i:
            raise ValueError(f"part {part['n']} is out of order")
        if not part["questions"]:
            raise ValueError(f"part {i} has no questions")
        for q in part["questions"]:
            if q["id"] in seen:
                raise ValueError(f"question id {q['id']!r} appears twice")
            seen.add(q["id"])
            if not q["text"]:
                raise ValueError(f"question {q['id']!r} has no text")
    return parts


def build(parts, template):
    data = json.dumps(parts, ensure_ascii=False, indent=1).replace("</", "<\\/")
    for mark in ("__QUESTIONS_JSON__", "__VERSION__"):
        if template.count(mark) != 1:
            raise ValueError(f"the template must hold {mark} exactly once")
    return template.replace("__QUESTIONS_JSON__", data).replace("__VERSION__", WORKBOOK_VERSION)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 when workbook.html doesn't match a fresh build")
    ap.add_argument("--json", action="store_true", help="print the parsed questions as JSON")
    args = ap.parse_args(argv)
    try:
        parts = parse(QUESTIONS.read_text(encoding="utf-8"))
        html = build(parts, TEMPLATE.read_text(encoding="utf-8"))
    except ValueError as e:
        print(f"FAIL  {e}")
        return 1
    if args.json:
        print(json.dumps(parts, ensure_ascii=False, indent=2))
        return 0
    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != html:
            print("FAIL  assets/workbook.html is out of date. Run scripts/build_workbook.py")
            return 1
        print(f"PASS  workbook.html matches the questions ({sum(len(p['questions']) for p in parts)} questions)")
        return 0
    with open(OUTPUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print(f"wrote assets/workbook.html: {len(parts)} parts, {sum(len(p['questions']) for p in parts)} questions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
