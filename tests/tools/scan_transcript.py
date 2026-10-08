#!/usr/bin/env python3
"""List what a test helper did, from its saved transcript: every tool call, the
files it read, the helpers it started, and the message it handed back.

    python tests/tools/scan_transcript.py SUBAGENTS_FOLDER AGENT_ID --forbid master-resume.md
    python tests/tools/scan_transcript.py SUBAGENTS_FOLDER AGENT_ID --forbid master-resume.md --run-folder RUN
    python tests/tools/scan_transcript.py SUBAGENTS_FOLDER AGENT_ID --handback out.md

The transcripts sit in ~/.claude/projects/<project>/<session>/subagents/, one
agent-<id>.jsonl per helper, with a meta.json beside it. A helper the test
helper started, like submission-review's reviewer or plainspeak-writer's fresh
reader, is listed under it, found by the tool call that started it.

--forbid names a file the helper must never open. The scan fails, exit 1, when
any tool call's input names it. A search or a command over the whole folder
(Grep or Glob there, or a shell glob such as cat *) can read a file without
naming it, so those calls are listed as broad. With --run-folder, the scan also
looks through every tool result for the forbidden files' own lines, the ones no
other file in the folder holds, and fails when one shows up. Without it, a
broad call fails the scan, since nothing shows it stayed clear. --handback
writes the helper's last message to the person, byte for byte, for the
evidence file. It isn't part of the plugin.
"""
import argparse
import json
import re
import sys
from pathlib import Path

OPENING_TOOLS = {"Read", "Bash", "PowerShell", "Grep", "Glob", "Edit", "Write", "NotebookEdit"}
SHELL_TOOLS = {"Bash", "PowerShell"}
# A shell command that can read more than the files it names: a reading command
# with a wildcard, a recursive search, or a loop over a wildcard.
BROAD_SHELL = re.compile(
    r"\b(?:cat|head|tail|type|more|less|grep|sed|awk|strings|Get-Content|gc)\b[^|;&\n]*[*?]"
    r"|\bgrep\s+-\w*[rR]|\brg\s|\bfind\s|Get-ChildItem\s[^|;&\n]*-Recurse|\bxargs\b|\bfor\s+\w+\s+in\s[^;\n]*[*?]")
MIN_LINE = 25  # a forbidden file's line this long or longer counts as its own
REPO = Path(__file__).resolve().parents[2]


def calls(path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        content = row.get("message", {}).get("content")
        if row.get("type") != "assistant" or not isinstance(content, list):
            continue
        for part in content:
            if part.get("type") == "tool_use":
                out.append((part["id"], part["name"], part.get("input", {})))
    return out


def results(path):
    """Every tool result's text in a transcript."""
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        content = row.get("message", {}).get("content")
        if not isinstance(content, list):
            continue
        for part in content:
            if part.get("type") != "tool_result":
                continue
            body = part.get("content")
            if isinstance(body, list):
                body = "\n".join(b.get("text", "") for b in body if isinstance(b, dict))
            out.append(str(body or ""))
    return out


def own_lines(run_folder, forbid):
    """For each forbidden file, its lines that no other file holds: not the other
    files in the folder, and not the plugin's own skills, which a helper reads on
    purpose and which quote some test pieces as examples."""
    files = {p.name: p.read_text(encoding="utf-8", errors="replace") for p in run_folder.iterdir()
             if p.is_file() and p.suffix.lower() in (".txt", ".md")}
    known = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in (REPO / "skills").rglob("*")
                      if p.is_file() and p.suffix.lower() in (".md", ".py"))
    out = {}
    for name in forbid:
        if name not in files:
            continue
        others = "\n".join(text for other, text in files.items() if other != name) + "\n" + known
        out[name] = [line.strip() for line in files[name].splitlines()
                     if len(line.strip()) >= MIN_LINE and line.strip() not in others]
    return out


def is_broad(name, data, run_folder):
    """A call that can read files it doesn't name."""
    if name in ("Grep", "Glob"):
        where = str(data.get("path") or "")
        return not where or (run_folder is not None and Path(where).resolve() == run_folder.resolve())
    if name in SHELL_TOOLS:
        return bool(BROAD_SHELL.search(str(data.get("command", ""))))
    return False


def handback(path):
    """The helper's last message to the person: its hand-back, or its last text."""
    last = None
    for _id, name, data in calls(path):
        if name == "SubagentHandback":
            last = data.get("message") or data.get("report") or json.dumps(data)
    if last is None:
        for line in path.read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            content = row.get("message", {}).get("content")
            if row.get("type") == "assistant" and isinstance(content, list):
                texts = [p["text"] for p in content if p.get("type") == "text"]
                if texts:
                    last = "\n".join(texts)
    return last or ""


def children(folder, tool_ids):
    out = []
    for meta in folder.glob("agent-*.meta.json"):
        data = json.loads(meta.read_text(encoding="utf-8"))
        if data.get("toolUseId") in tool_ids:
            out.append((meta.name[len("agent-"):-len(".meta.json")], data))
    return out


def short(data):
    for key in ("file_path", "command", "pattern", "path", "skill", "subagent_type", "url", "query"):
        if key in data:
            return f"{key}={str(data[key])[:160]!r}"
    return json.dumps(data)[:160]


def scan(folder, agent, forbid, run_folder=None, lines=None, depth=0):
    """Returns (forbidden names, broad calls, forbidden lines seen in results)."""
    path = folder / f"agent-{agent}.jsonl"
    found = calls(path)
    bad, broad, seen = [], [], []
    pad = "  " * depth
    print(f"{pad}agent {agent}: {len(found)} tool call(s)")
    for _id, name, data in found:
        text = json.dumps(data)
        # Only a tool that opens, searches or writes files can touch a file; a
        # report or a message that names one doesn't open it.
        hit = [f for f in forbid if f in text] if name in OPENING_TOOLS else []
        wide = is_broad(name, data, run_folder)
        flag = ("   << names " + ", ".join(hit) if hit else "") + ("   << broad" if wide else "")
        print(f"{pad}  {name}: {short(data)}{flag}")
        bad += hit
        if wide:
            broad.append(f"{name}: {short(data)}")
    for result in results(path):
        for file_name, own in (lines or {}).items():
            seen += [f"{file_name}: {line[:60]}" for line in own if line in result]
    for child, meta in children(folder, {i for i, n, _d in found if n == "Agent"}):
        print(f"{pad}  started {meta.get('agentType')}: {meta.get('description')}")
        child_bad, child_broad, child_seen = scan(folder, child, forbid, run_folder, lines, depth+1)
        bad, broad, seen = bad + child_bad, broad + child_broad, seen + child_seen
    return bad, broad, seen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("agent")
    ap.add_argument("--forbid", action="append", default=[])
    ap.add_argument("--run-folder", help="the person's folder, to look for the forbidden files' lines in results")
    ap.add_argument("--handback")
    args = ap.parse_args()
    folder = Path(args.folder)
    run_folder = Path(args.run_folder) if args.run_folder else None
    lines = own_lines(run_folder, args.forbid) if run_folder else None
    bad, broad, seen = scan(folder, args.agent, args.forbid, run_folder, lines)
    if args.handback:
        Path(args.handback).write_bytes(handback(folder / f"agent-{args.agent}.jsonl").encode("utf-8"))
        print(f"Hand-back written to {args.handback}")
    failed = bool(bad)
    if args.forbid:
        print("FORBIDDEN FILE NAMED: " + ", ".join(sorted(set(bad))) if bad else "No call names a forbidden file.")
        if broad:
            print(f"{len(broad)} broad call(s) that could read files without naming them.")
        if lines is not None:
            counted = sum(len(v) for v in lines.values())
            if seen:
                failed = True
                print("FORBIDDEN TEXT IN A RESULT: " + "; ".join(sorted(set(seen))))
            else:
                print(f"None of the forbidden files' {counted} own line(s) shows up in any tool result.")
        elif broad:
            failed = True
            print("Give --run-folder to check what the broad calls returned.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
