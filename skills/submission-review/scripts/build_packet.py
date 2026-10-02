#!/usr/bin/env python3
"""Build a review packet for the submission-reviewer helper.

A packet is a folder that holds only what the piece's real reader sees: the
piece, the target, any companions the reader also gets, plainspeak-writer's
checker output for the piece, and a manifest. The script has no field for
notes, and it leaves original file names out, so nothing about what the writer
meant reaches the reviewer.

    python3 build_packet.py --type letter --piece letter.docx \
        --target posting.md --companion resume.docx --channel upload

It prints the packet folder and the one line to send the reviewer. Exit code 0
means the packet was built, and 2 means the input needs fixing. Python 3.8 or
newer, standard library only.
"""
import argparse
import datetime as dt
import os
import re
import secrets
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

__version__ = "0.1.0"

# type: (label for the manifest, checker surface, default readers)
TYPES = {
    "letter": ("cover letter", "letter", ("recruiter", "manager", "grader")),
    "resume": ("resume", "resume", ("recruiter", "grader")),
    "outreach": ("outreach note", "letter", ("recruiter", "manager")),
    "blurb": ("referral blurb", "blurb", ("recruiter", "manager")),
    "linkedin": ("LinkedIn About section or headline", "linkedin", ("recruiter", "manager")),
    "answer": ("application answer", "general", ("recruiter", "manager")),
    "other": ("other job-search piece", "general", ("recruiter", "manager")),
}
READERS = {
    "recruiter": "Recruiter, first look",
    "manager": "Hiring manager, reading closely",
    "grader": "AI grader",
}
CHANNELS = {
    "upload": "an uploaded file",
    "textbox": "a text box on a form",
    "email": "an email body",
}
TEXT_SUFFIXES = {".txt", ".md", ".markdown", ".text"}
MESSAGE = "Review the packet in {folder}. Read manifest.md first."
# Words in a companion's file name that suggest notes or strategy, not something
# the real reader sees. The script warns and goes on; the person decides.
LEAK_WORDS = ("positioning", "strategy", "notes", "brief", "draft", "career-record",
              "career_record", "talking-points")
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv"}
MAX_DEPTH = 8
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


class PacketError(Exception):
    """Input the person needs to fix."""


# ------------------------------------------------------------------ reading --

def normalize(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text.strip("\n") + "\n"


def read_text_file(path):
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "cp1252"):
        try:
            return normalize(data.decode(encoding))
        except UnicodeDecodeError:
            continue
    return normalize(data.decode("utf-8", errors="replace"))


def _word_xml_text(xml_bytes):
    """Paragraph text from a Word XML part, one paragraph per line."""
    root = ET.fromstring(xml_bytes)
    lines = []

    def walk(node, buf):
        for child in node:
            tag = child.tag
            if tag == W + "p":
                inner = []
                walk(child, inner)
                lines.append("".join(inner))
            elif tag == W + "t":
                buf.append(child.text or "")
            elif tag == W + "tab":
                buf.append("\t")
            elif tag in (W + "br", W + "cr"):
                buf.append("\n")
            elif tag == W + "noBreakHyphen":
                buf.append("-")
            elif tag in (W + "delText", W + "instrText", W + "softHyphen"):
                continue
            else:
                walk(child, buf)

    walk(root, [])
    return "\n".join(lines)


def read_docx(path):
    """Return (body text, characters found in headers and footers)."""
    try:
        with zipfile.ZipFile(path) as archive:
            body = _word_xml_text(archive.read("word/document.xml"))
            extra = 0
            for name in archive.namelist():
                if re.match(r"word/(header|footer)\d*\.xml$", name):
                    extra += len(_word_xml_text(archive.read(name)).strip())
    except (zipfile.BadZipFile, KeyError, ET.ParseError) as exc:
        raise PacketError(f"{path.name} isn't a readable Word file ({exc.__class__.__name__}).")
    return normalize(body), extra


def read_any(path):
    """Return (text, note) for a .txt, .md or .docx file."""
    if not path.is_file():
        raise PacketError(f"Can't find the file {path}.")
    suffix = path.suffix.lower()
    if suffix in TEXT_SUFFIXES:
        text, note = read_text_file(path), ""
    elif suffix == ".docx":
        text, extra = read_docx(path)
        note = (f"The Word file had {extra:,} characters in its header or footer, left out here."
                if extra else "")
    elif suffix == ".pdf":
        raise PacketError(f"{path.name} is a PDF, and its text can't be pulled out reliably. "
                          "Give the Word file, or save the text to a .txt file.")
    else:
        raise PacketError(f"{path.name} isn't a .txt, .md or .docx file. "
                          "Save the text to a .txt file and try again.")
    if not text.strip():
        raise PacketError(f"{path.name} has no text in it.")
    return text, note


def counts(text):
    body = text.rstrip("\n")
    return len(body), len(body.split())


# -------------------------------------------------------- plainspeak-writer --

def default_roots():
    roots = []
    config = os.environ.get("CLAUDE_CONFIG_DIR")
    if config:
        roots += [Path(config) / "skills", Path(config) / "plugins"]
    home = Path.home()
    roots += [home / ".claude" / "skills", home / ".claude" / "plugins",
              Path.cwd() / ".claude" / "skills"]
    unique = []
    for root in roots:
        if root not in unique:
            unique.append(root)
    return unique


def skill_name(skill_md):
    try:
        head = skill_md.read_text(encoding="utf-8", errors="replace")[:2000]
    except OSError:
        return ""
    match = re.search(r"^name:\s*['\"]?([\w.-]+)", head, re.MULTILINE)
    return match.group(1) if match else ""


def voice_version(folder):
    changelog = folder / "CHANGELOG.md"
    if changelog.is_file():
        text = changelog.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"^##\s+v?(\d+(?:\.\d+)+)", text, re.MULTILINE)
        if match:
            return match.group(1)
    skill = folder / "SKILL.md"
    if skill.is_file():
        match = re.search(r"version:\s*['\"]?(\d+(?:\.\d+)+)",
                          skill.read_text(encoding="utf-8", errors="replace")[:2000])
        if match:
            return match.group(1)
    return "unknown"


def version_key(version):
    if version == "unknown":
        return (-1,)
    return tuple(int(part) for part in version.split("."))


def is_voice_dir(folder):
    return ((folder / "SKILL.md").is_file()
            and (folder / "references" / "tells.md").is_file()
            and skill_name(folder / "SKILL.md") == "plainspeak-writer")


def find_voice_dirs(roots):
    """Every installed copy of plainspeak-writer under the roots."""
    found = []
    for root in roots:
        root = Path(root)
        if not root.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            here = Path(dirpath)
            depth = len(here.relative_to(root).parts)
            if here.name == "plainspeak-writer" and "SKILL.md" in filenames and is_voice_dir(here):
                found.append(here)
                dirnames[:] = []
                continue
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and depth < MAX_DEPTH]
    return found


def choose_voice_dir(found):
    """The newest version wins; on a tie, the most recently changed rules file."""
    if not found:
        return None
    return max(found, key=lambda d: (version_key(voice_version(d)),
                                     (d / "references" / "tells.md").stat().st_mtime))


def run_checker(voice_dir, surface, piece_path):
    """Return (checker text, surface used, exit code) or (None, reason, None)."""
    checker = voice_dir / "scripts" / "check_voice.py"
    if not checker.is_file():
        return None, "this copy of plainspeak-writer has no scripts/check_voice.py", None
    tried = [surface] if surface == "general" else [surface, "general"]
    last = ""
    for surf in tried:
        try:
            env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
            proc = subprocess.run(
                [sys.executable, str(checker), "--surface", surf, str(piece_path)],
                capture_output=True, text=True, encoding="utf-8", errors="replace",
                timeout=120, env=env)
        except (OSError, subprocess.TimeoutExpired) as exc:
            return None, f"the checker didn't run ({exc.__class__.__name__})", None
        if proc.returncode in (0, 1):
            return proc.stdout + (proc.stderr or ""), surf, proc.returncode
        last = (proc.stderr or proc.stdout).strip().splitlines()[-1:] or [""]
        last = last[0]
    return None, f"the checker stopped with an error: {last}", None


# ------------------------------------------------------------------- packet --

def build(args):
    kind_label, surface, default_readers = TYPES[args.type]
    readers = parse_readers(args.readers) if args.readers else list(default_readers)
    warnings = []

    piece_text, piece_note = read_any(Path(args.piece))
    target = read_any(Path(args.target)) if args.target else None
    companions = [read_any(Path(c)) for c in (args.companion or [])]
    for c in args.companion or []:
        lowered = Path(c).name.lower()
        if any(word in lowered for word in LEAK_WORDS):
            warnings.append(f"The companion file name '{Path(c).name}' suggests notes or strategy. "
                            "A companion should be something the real reader also sees.")

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    folder = (Path(args.out) / f"{stamp}-{args.type}-{secrets.token_hex(2)}").resolve()
    folder.mkdir(parents=True, exist_ok=False)

    rows = []

    def write(name, text, role):
        (folder / name).write_text(text, encoding="utf-8", newline="\n")
        chars, words = counts(text)
        rows.append((name, role, f"{chars:,}", f"{words:,}"))
        return chars

    piece_chars = write("piece.txt", piece_text, f"The piece: {kind_label}")
    notes = [f"Piece: {piece_note}"] if piece_note else []
    if target:
        write("target.txt", target[0], "The target: the job posting, or the reader's own words")
        if target[1]:
            notes.append(f"Target: {target[1]}")
    for i, (text, note) in enumerate(companions, start=1):
        write(f"companion-{i}.txt", text, "A companion the real reader also sees")
        if note:
            notes.append(f"Companion {i}: {note}")

    # Voice rules and the checker.
    if args.no_voice:
        voice_dir, found_count = None, 0
    elif args.voice_dir:
        voice_dir = Path(args.voice_dir).resolve()
        if not is_voice_dir(voice_dir):
            raise PacketError(f"{voice_dir} doesn't hold plainspeak-writer "
                              "(it needs SKILL.md and references/tells.md).")
        found_count = 1
    else:
        found = find_voice_dirs(default_roots())
        voice_dir, found_count = choose_voice_dir(found), len(found)

    if voice_dir:
        version = voice_version(voice_dir)
        rules = voice_dir / "references" / "tells.md"
        voice_line = (f"plainspeak-writer {version}. Rules file: {rules}"
                      + (f" (newest of {found_count} copies found)" if found_count > 1 else ""))
        output, used, code = run_checker(voice_dir, surface, folder / "piece.txt")
        if output is None:
            checker_line = f"Didn't run: {used}. Run the full check in the rules file by hand."
        else:
            header = (f"plainspeak-writer {version} checker output for piece.txt, "
                      f"surface {used}, exit code {code} "
                      "(0 means no HARD hits, 1 means at least one).\n\n")
            write("checker.txt", header + output, "plainspeak-writer's checker output for piece.txt")
            checker_line = f"Ran with surface {used}, exit code {code}."
            if used != surface:
                checker_line += f" The surface {surface} wasn't accepted, so general was used."
    else:
        voice_line = "not found. Voice is unchecked."
        checker_line = "Didn't run, because plainspeak-writer wasn't found."

    if args.channel:
        channel_line = CHANNELS[args.channel]
        if args.limit:
            over = piece_chars - args.limit
            channel_line += f", with a limit of {args.limit:,} characters. The piece has {piece_chars:,}"
            channel_line += (f", which is {over:,} over the limit." if over > 0 else ", which fits.")
        else:
            channel_line += "."
    elif args.limit:
        over = piece_chars - args.limit
        channel_line = (f"not given, with a limit of {args.limit:,} characters. The piece has {piece_chars:,}"
                        + (f", which is {over:,} over the limit." if over > 0 else ", which fits."))
    else:
        channel_line = "not given."

    reader_line = "; ".join(READERS[r] for r in readers)
    reader_line += " (the defaults for this piece type)." if not args.readers else " (chosen by the person)."
    target_line = ("given in target.txt." if target else
                   "none given. Review against a general reader for this type of piece.")

    lines = [
        "# Review packet",
        "",
        f"Built by build_packet.py {__version__} on {dt.datetime.now():%Y-%m-%d at %H:%M}.",
        "",
        "## Files",
        "",
        "| File | Role | Characters | Words |",
        "|---|---|---|---|",
    ]
    for name, role, chars, words in rows:
        lines.append(f"| {name} | {role} | {chars} | {words} |")
    lines.append("| manifest.md | This file | | |")
    lines += [
        "",
        "Characters count spaces and line breaks.",
        "",
        "## Settings",
        "",
        f"- Piece type: {kind_label}",
        f"- Readers: {reader_line}",
        f"- Target: {target_line}",
        f"- Channel: {channel_line}",
        f"- Voice rules: {voice_line}",
        f"- Checker: {checker_line}",
    ]
    for note in notes:
        lines.append(f"- Note: {note}")
    (folder / "manifest.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return folder, warnings


def parse_readers(value):
    readers = [r.strip().lower() for r in value.split(",") if r.strip()]
    bad = [r for r in readers if r not in READERS]
    if bad or not readers:
        raise PacketError(f"Unknown reader {', '.join(bad) or '(none)'}. "
                          f"Use any of: {', '.join(READERS)}.")
    return readers


def parser():
    ap = argparse.ArgumentParser(
        prog="build_packet.py", allow_abbrev=False,
        description="Build a review packet for the submission-reviewer helper. "
                    "There's no field for notes, on purpose.")
    ap.add_argument("--type", required=True, choices=sorted(TYPES), help="the kind of piece")
    ap.add_argument("--piece", required=True, help="the finished piece: .txt, .md or .docx")
    ap.add_argument("--target", help="the job posting, or the reader's own words")
    ap.add_argument("--companion", action="append",
                    help="a file the real reader also sees, such as the resume; repeat for more")
    ap.add_argument("--channel", choices=sorted(CHANNELS), help="where the piece goes")
    ap.add_argument("--limit", type=int, help="a hard character limit, such as a text box's")
    ap.add_argument("--readers", help="comma list from: recruiter, manager, grader")
    ap.add_argument("--voice-dir", help="the plainspeak-writer folder, when it isn't found on its own")
    ap.add_argument("--no-voice", action="store_true",
                    help="build the packet as if plainspeak-writer weren't installed")
    ap.add_argument("--out", default="review-packets", help="where packet folders go")
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return ap


def main(argv=None):
    args = parser().parse_args(argv)
    if args.limit is not None and args.limit <= 0:
        print("The limit has to be a positive number of characters.", file=sys.stderr)
        return 2
    try:
        folder, warnings = build(args)
    except PacketError as exc:
        print(f"Can't build the packet. {exc}", file=sys.stderr)
        return 2
    for warning in warnings:
        print(f"Warning: {warning}")
    print(f"Packet: {folder}")
    print("Message for the reviewer (send exactly this line and nothing else):")
    print(MESSAGE.format(folder=folder))
    return 0


if __name__ == "__main__":
    sys.exit(main())
