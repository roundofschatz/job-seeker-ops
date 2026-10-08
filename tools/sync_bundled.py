#!/usr/bin/env python3
"""Copy one release of plainspeak-writer or resume-ops into this plugin.

    python tools/sync_bundled.py plainspeak-writer --repo ../plainspeak-writer --ref v1.7
    python tools/sync_bundled.py resume-ops --repo ../resume-ops --ref <tag or commit>
    python tools/sync_bundled.py --check

The plugin holds both skills in skills/, so a person who installs only the
plugin gets every tool cover-letter and candidate-positioning work with. Each
copy is exact: the script takes the files from one commit of the skill's own
repository with git, writes them into skills/<name>/, and records the commit,
the version and each file's hash in bundled.json. Nobody edits a copy here. A
change goes into the skill's own repository and comes back through this
script, and tests/unit/test_bundled.py fails on a copy that differs from its
record.

The skills' tests stay in their own repositories, which run them, so the copy
holds only what Claude reads and runs.

Standard library and git only.
"""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "bundled.json"
SKILLS = {
    "plainspeak-writer": {
        "repository": "https://github.com/roundofschatz/plainspeak-writer",
        "source": "",  # the repository is the skill
        "left_out": [".gitignore", "tests/"],
    },
    "resume-ops": {
        "repository": "https://github.com/roundofschatz/resume-ops",
        "source": "skills/resume-ops",
        "left_out": ["tests/"],
    },
}
ABOUT = ("Skills this plugin carries as exact copies of one commit of their own repositories. "
         "tools/sync_bundled.py writes them and this record, and tests/unit/test_bundled.py checks "
         "both. Change a skill in its own repository, never here.")


class SyncError(Exception):
    pass


def git(repo, *args):
    proc = subprocess.run(["git", "--no-optional-locks", "-C", str(repo), *args],
                          capture_output=True)
    if proc.returncode:
        raise SyncError(f"git {' '.join(args)} in {repo} stopped: "
                        + proc.stderr.decode("utf-8", "replace").strip())
    return proc.stdout


def digest(data):
    """The file's hash, with line endings read as plain newlines, so a
    checkout that writes CRLF still matches."""
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def kept(rel, left_out):
    return not any(rel == x or (x.endswith("/") and rel.startswith(x)) for x in left_out)


def files_at(repo, commit, source, left_out):
    """{path in the copy: path in the repository} for the files the copy holds."""
    args = ["ls-tree", "-r", "-z", "--name-only", commit]
    if source:
        args += ["--", source]
    names = [n for n in git(repo, *args).decode("utf-8").split("\0") if n]
    prefix = f"{source}/" if source else ""
    out = {}
    for name in names:
        rel = name[len(prefix):]
        if kept(rel, left_out):
            out[rel] = name
    if not out:
        raise SyncError(f"{commit} holds no files under '{source or '.'}'.")
    return out


def version_of(name, files):
    """The version the copy states: plainspeak-writer's newest changelog
    heading, or resume-ops's version in SKILL.md."""
    if name == "plainspeak-writer":
        m = re.search(r"^##\s+v?(\d+(?:\.\d+)+)", files.get("CHANGELOG.md", b"").decode("utf-8"), re.M)
    else:
        m = re.search(r"^\s*version:\s*['\"]?(\d+(?:\.\d+)+)", files.get("SKILL.md", b"").decode("utf-8"), re.M)
    if not m:
        raise SyncError(f"{name} states no version.")
    return m.group(1)


def read_manifest():
    if not MANIFEST.is_file():
        return {"about": ABOUT, "skills": {}}
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def write_manifest(data):
    MANIFEST.write_bytes((json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))


def sync(name, repo, ref):
    spec = SKILLS[name]
    manifest = read_manifest()
    target = REPO / "skills" / name
    if target.exists() and name not in manifest["skills"]:
        raise SyncError(f"skills/{name} exists and bundled.json doesn't list it, so it isn't a copy "
                        "this script made. Move it first.")
    commit = git(repo, "rev-parse", "--verify", f"{ref}^{{commit}}").decode().strip()
    paths = files_at(repo, commit, spec["source"], spec["left_out"])
    files = {}
    for rel, name_in_repo in sorted(paths.items()):
        data = git(repo, "cat-file", "blob", f"{commit}:{name_in_repo}")
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            raise SyncError(f"{name_in_repo} isn't UTF-8 text, and the copy's hashes are for text.")
        files[rel] = data
    version = version_of(name, files)
    if target.exists():
        shutil.rmtree(target)
    for rel, data in files.items():
        path = target / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    manifest["about"] = ABOUT
    manifest["skills"][name] = {
        "version": version,
        "repository": spec["repository"],
        "ref": ref,
        "commit": commit,
        "source": spec["source"] or ".",
        "left_out": spec["left_out"],
        "files": {rel: digest(data) for rel, data in files.items()},
    }
    manifest["skills"] = dict(sorted(manifest["skills"].items()))
    write_manifest(manifest)
    return manifest["skills"][name]


def problems(name, entry):
    """What differs between skills/<name> and its record, as sentences."""
    folder = REPO / "skills" / name
    if not folder.is_dir():
        return [f"skills/{name} is missing."]
    on_disk = {p.relative_to(folder).as_posix(): p for p in folder.rglob("*")
               if p.is_file() and "__pycache__" not in p.parts}
    found = []
    for rel in sorted(set(entry["files"]).difference(on_disk)):
        found.append(f"skills/{name}/{rel} is in the record and missing from the copy.")
    for rel in sorted(set(on_disk).difference(entry["files"])):
        found.append(f"skills/{name}/{rel} is in the copy and not in the record.")
    for rel in sorted(set(on_disk) & set(entry["files"])):
        if digest(on_disk[rel].read_bytes()) != entry["files"][rel]:
            found.append(f"skills/{name}/{rel} differs from {entry['commit'][:7]}.")
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("name", nargs="?", choices=sorted(SKILLS), help="the skill to copy")
    ap.add_argument("--repo", help="a clone of the skill's own repository")
    ap.add_argument("--ref", help="the tag or commit to copy")
    ap.add_argument("--check", action="store_true", help="compare every copy with bundled.json")
    args = ap.parse_args()
    try:
        if args.check:
            entries = read_manifest()["skills"]
            found = [p for n, e in entries.items() for p in problems(n, e)]
            for p in found:
                print(p)
            print(f"{len(entries)} copies checked, {len(found)} problem(s).")
            return 1 if found else 0
        if not (args.name and args.repo and args.ref):
            ap.error("name the skill, --repo and --ref, or pass --check")
        entry = sync(args.name, Path(args.repo).resolve(), args.ref)
    except SyncError as exc:
        print(f"Nothing was copied, because {exc}", file=sys.stderr)
        return 2
    print(f"skills/{args.name}: {args.name} {entry['version']}, {len(entry['files'])} files "
          f"from {entry['commit'][:7]} ({args.ref}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
