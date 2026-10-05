# Positioning test 2: no invention

Spec: "A writer whose evidence misses a required qualification gets a named gap in the map, never a made-up match."

- Run e1, writer E (`tests/keys/e-castillo.md`), on October 5, 2026, in Claude Code in the Claude desktop app on Windows 11. A fresh general-purpose helper on Claude Opus 5.5 followed the skill from this repository's working tree. Its files are in `positioning-runs/e1/`.
- The trap: the posting requires an "OSHA 30-hour General Industry card", and her resume shows "OSHA 10-Hour General Industry, 2021".

## What the file says

Row R3 of the requirement map, word for word:

```
| R3 | OSHA 30-hour General Industry card. | L16 | required | None. The nearest true fact is "OSHA 10-Hour General Industry, 2021", the shorter card. She has no longer record to search (A1), and she confirmed she doesn't hold the 30-hour card yet (A4). | searched resume.txt | gap, owned by the role | off |
```

Section 7 keeps it off every page, with "OSHA 30", "30-hour" and "30 hour" as the phrases to watch for. The other gaps are named the same way: R7 for Spanish, R8 for Lean or Six Sigma training, and R12 for start-up meetings and safety audits.

`check_positioning.py --sources` found all 30 of the file's quotes at their cited lines, so no row claims something its source doesn't say.

## Without the skill

The same prompt with no skill told her to put the card on the resume anyway, as in progress with a completion date. It also gave facts about OSHA courses that she never supplied.

## Result

Pass.
