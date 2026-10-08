#!/usr/bin/env python3
"""Copy one cover-letter test run's files into its own folder, outside this
repository, so the helper running the skill can't open the keys.

    python tests/tools/stage_run.py cl-f1 ../jso-tests/cover-letter/runs/cl-f1
    python tests/tools/stage_run.py cl-f2 RUN --from ../jso-tests/cover-letter/runs/cl-f2-positioning
    python tests/tools/stage_run.py --list

Each run copies made-up writers' files from tests/writers/ and the extra pieces
for the letter tests from tests/letters/. Writer B's positioning file is the
example at the end of candidate-positioning's references/format.md, so it's
taken from there. The folder must not exist yet.
"""
import argparse
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WRITERS = REPO / "tests" / "writers"
LETTERS = REPO / "tests" / "letters"
F_POS = "positioning-silver-larch-school-district-math-curriculum-coordinator-grades-6-to-8.md"
E_POS = "positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md"
G_POS = "positioning-calder-basin-water-authority-senior-project-engineer-capital-programs.md"
B_POS = "positioning-switchgrass-freight-supply-chain-planning-analyst.md"
F_FILES = ["posting.txt", "resume.txt", "master-resume.md", "letter-2021.txt"]
E_FILES = ["posting.txt", "resume.txt", "firm-pages.md"]

RUNS = {
    "cl-f1": [(WRITERS / "f-haddad", F_FILES), (LETTERS / "f-haddad", [F_POS, "note-to-families.txt"])],
    "cl-f2-positioning": [(WRITERS / "f-haddad", ["resume.txt", "master-resume.md", "letter-2021.txt"]),
                          (LETTERS / "f-haddad" / "juniper-flats", ["posting.txt", "firm-pages.md"])],
    "cl-e1": [(WRITERS / "e-castillo", E_FILES), (LETTERS / "e-castillo", [E_POS, "Renata-Castillo-Resume.docx"])],
    "cl-e2": [(WRITERS / "e-castillo", E_FILES), (LETTERS / "e-castillo", [E_POS, "resume-updated.txt"])],
    "cl-g1": [(WRITERS / "g-whitfield", ["posting.txt", "resume.txt", "linkedin.md"]), (LETTERS / "g-whitfield", [G_POS])],
    "cl-b1": [(WRITERS / "b-okafor", ["posting.txt", "resume.txt", "career-record.md", "positioning-notes.md"])],
    "cl-n1": [(WRITERS / "f-haddad", F_FILES)],
    "cl-n2": [(WRITERS / "f-haddad", F_FILES), (LETTERS / "f-haddad" / "one-fact", [F_POS])],
    "cl-f2": [],
    "cl-ai1": [(WRITERS / "f-haddad", ["resume.txt", "master-resume.md", "letter-2021.txt"]),
               (LETTERS / "f-haddad" / "no-ai", ["posting.txt", F_POS])],
}


def format_example():
    text = (REPO / "skills" / "candidate-positioning" / "references" / "format.md").read_text(encoding="utf-8")
    body = text.split("## A full example", 1)[1]
    return re.search(r"```markdown\n(.*?)\n```\s*$", body, re.S).group(1) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run", nargs="?", choices=sorted(RUNS))
    ap.add_argument("folder", nargs="?")
    ap.add_argument("--from", dest="source", help="for cl-f2: the cl-f2-positioning run folder")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    if args.list or not args.run:
        for name, parts in RUNS.items():
            print(name, ", ".join(f for _d, files in parts for f in files))
        return 0
    out = Path(args.folder).resolve()
    if REPO in out.parents or out == REPO:
        sys.exit("Stage the run outside this repository, so the helper can't open the keys.")
    out.mkdir(parents=True, exist_ok=False)
    for folder, files in RUNS[args.run]:
        for name in files:
            shutil.copy2(folder / name, out / name)
    if args.run == "cl-b1":
        (out / B_POS).write_bytes(format_example().encode("utf-8"))
    if args.run == "cl-f2":
        if not args.source:
            sys.exit("cl-f2 needs --from, the cl-f2-positioning run folder with its new positioning file.")
        for path in Path(args.source).iterdir():
            if path.is_file():
                shutil.copy2(path, out / path.name)
    print(f"Staged {args.run} in {out}:")
    for path in sorted(out.iterdir()):
        print(" ", path.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
