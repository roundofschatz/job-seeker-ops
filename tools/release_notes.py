"""Write a release's title and notes from CHANGELOG.md.

    python tools/release_notes.py VERSION [LAST_RELEASED] --out notes.md

Prints the release title. The notes hold every changelog entry newer than the
last released version, newest first, then how to install. The newest entry
must be VERSION, so a release never ships under a number the changelog
doesn't describe. The release workflow in .github/workflows runs this.
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

INSTALL = """In Claude Code:

```
/plugin marketplace add roundofschatz/job-seeker-ops
/plugin install job-seeker-ops@roundofschatz
```

To install in the Claude desktop app or Cowork, add the marketplace `roundofschatz/job-seeker-ops` under Customize, Plugins, and install Job Seeker Ops alone, since it already includes resume-ops and plainspeak-writer. Or upload `job-seeker-ops.zip` or `job-seeker-ops.plugin`. They're the same file, built from this release's commit. The scripts need Python 3.8 or newer and nothing outside its standard library.
"""


def entries(text):
    """Each changelog entry as (version, heading, body), newest first."""
    out = []
    for part in re.split(r"(?m)^## ", text)[1:]:
        heading, _, body = part.partition("\n")
        out.append((heading.split(" ", 1)[0], heading.strip(), body.strip()))
    return out


def build(version, last, text):
    """The title and the notes for releasing VERSION after LAST."""
    log = entries(text)
    if not log or log[0][0] != version:
        raise ValueError(f"CHANGELOG.md's newest entry is {log[0][0] if log else 'missing'}, not {version}")
    last = last.lstrip("v")
    versions = [v for v, _, _ in log]
    new = []
    for entry in log:
        if entry[0] == last or (new and last not in versions):
            break
        new.append(entry)
    name = new[0][1].split("·", 1)[1].strip() if "·" in new[0][1] else ""
    title = f"job-seeker-ops {version}" + (f": {name[:1].lower()}{name[1:]}" if name else "")
    if len(new) == 1:
        notes = [new[0][2]]
    else:
        earlier = ", ".join(v for v, _, _ in new[1:])
        notes = [f"This release also covers {earlier}, which had no release of its own."]
        notes += [f"## {heading}\n\n{body}" for _, heading, body in new]
    notes.append("`CHANGELOG.md` lists every change and why.")
    notes.append(INSTALL)
    return title, "\n\n".join(notes)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Write a release's title and notes from CHANGELOG.md.")
    ap.add_argument("version", help="the version being released, like 0.4.9")
    ap.add_argument("last", nargs="?", default="", help="the last released tag or version, like v0.4.7")
    ap.add_argument("--out", required=True, help="where to write the notes")
    args = ap.parse_args(argv)
    try:
        title, notes = build(args.version, args.last, (REPO / "CHANGELOG.md").read_text(encoding="utf-8"))
    except ValueError as err:
        sys.exit(f"error: {err}")
    Path(args.out).write_text(notes, encoding="utf-8")
    print(title)


if __name__ == "__main__":
    main()
