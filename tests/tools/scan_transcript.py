#!/usr/bin/env python3
"""List what a test helper did, from its saved transcript: every tool call, the
files it read, the helpers it started, and the message it handed back.

    python tests/tools/scan_transcript.py SUBAGENTS_FOLDER AGENT_ID --forbid master-resume.md
    python tests/tools/scan_transcript.py SUBAGENTS_FOLDER AGENT_ID --handback out.md

The transcripts sit in ~/.claude/projects/<project>/<session>/subagents/, one
agent-<id>.jsonl per helper, with a meta.json beside it. A helper the test
helper started, like submission-review's reviewer or plainspeak-writer's fresh
reader, is listed under it, found by the tool call that started it.

--forbid names a file the helper must never open. The scan fails, exit 1, when
any tool call's input names it. --handback writes the helper's last message to
the person, byte for byte, for the evidence file. It isn't part of the plugin.
"""
import argparse
import json
import sys
from pathlib import Path

OPENING_TOOLS = {"Read", "Bash", "PowerShell", "Grep", "Glob", "Edit", "Write", "NotebookEdit"}


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


def scan(folder, agent, forbid, depth=0):
    path = folder / f"agent-{agent}.jsonl"
    found = calls(path)
    bad = []
    pad = "  " * depth
    print(f"{pad}agent {agent}: {len(found)} tool call(s)")
    for _id, name, data in found:
        text = json.dumps(data)
        # Only a tool that opens, searches or writes files can touch a file; a
        # report or a message that names one doesn't open it.
        hit = [f for f in forbid if f in text] if name in OPENING_TOOLS else []
        flag = "   << names " + ", ".join(hit) if hit else ""
        print(f"{pad}  {name}: {short(data)}{flag}")
        bad += hit
    for child, meta in children(folder, {i for i, n, _d in found if n == "Agent"}):
        print(f"{pad}  started {meta.get('agentType')}: {meta.get('description')}")
        bad += scan(folder, child, forbid, depth+1)
    return bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("agent")
    ap.add_argument("--forbid", action="append", default=[])
    ap.add_argument("--handback")
    args = ap.parse_args()
    folder = Path(args.folder)
    bad = scan(folder, args.agent, args.forbid)
    if args.handback:
        Path(args.handback).write_bytes(handback(folder / f"agent-{args.agent}.jsonl").encode("utf-8"))
        print(f"Hand-back written to {args.handback}")
    if args.forbid:
        print("FORBIDDEN FILE NAMED: " + ", ".join(sorted(set(bad))) if bad else "No call names a forbidden file.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
