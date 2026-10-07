# Cover letter test 14: its own files

Spec: "Every file passes plainspeak-writer's checker with no blocks apart from quoted examples, holds nothing personal, and has its change logged."

## The checker

plainspeak-writer 1.6.2's `check_voice.py --surface general`, pinned at commit 577a985, ran on every text file this release adds or changes, in the skills as well as the tests and the evidence.

HARD hits are left only in quoted material:

| File | What the checker blocks | Why it stays |
|---|---|---|
| `tests/letters/f-haddad/note-to-families.txt` | A dash and "not just a number, but" | Test 13's voice sample, written with both on purpose |
| `cover-letter-runs/*/scan.txt` | Dashes | Each scan lists a helper's tool calls word for word, with their command flags and Claude's own folder names, such as `C--Users-<user>-repos-tools` |
| `cover-letter-runs/cl-f1/handback.md`, `cl-e1/handback.md` | Dashes, and "not just a gap" in cl-e1 | The blind reviewer's report as the skill passed it on: the dashes are in the folder names of its "Files I opened" list, and the phrase is the reviewer's own |

Warnings were fixed where the writing was mine and cleared where it wasn't:

- **Fixed:** "carry" as a verb and a colon reveal in a code comment, and short flat lines and choppy runs in the keys and the evidence.
- **Code:** U04 counts `!=` and `#!` as exclamation marks, and V04 counts a script's lines as one-sentence paragraphs.
- **The positioning files:** V08 counts the labelled lines that repeat in every proof, such as "On the resume being sent: yes", which the format requires.
- **Keys and evidence:** the rest of V03, V04 and V06 come from the writers' messages quoted word for word, tables, and one labelled test per paragraph.
- **The test pieces:** Juniper Flats' posting and firm pages are written the way such pages read, and `resume-updated.txt` is resume lines.
- **The README:** no warning.
- **Earlier entries:** in `CHANGELOG.md` and `tests/RESULTS.md`, "carried", the repeated "Where this build departs from the spec, and why:" and a repeated product line sit in entries for earlier releases and stay as logged.
- **`format.md`:** the rate of lists of three fell from 12.7 to 10.4 per 1,000 words with the section 9 text, and the lists name the parts of the format.
- **The watermark line:** "carry" there is word for word what the owner approved.

## Nothing personal

A search of every added and changed file for the owner's name and email, the user name on this computer, and the app's and the session's IDs found only generic descriptions of where the desktop app keeps skills, such as `%APPDATA%\Claude\`. The writers are made up, with example.com addresses and 555 phone numbers, and the Word files' author fields hold their names. In the copies under `cover-letter-runs/`, the user name became `<user>`, the app's folder became `Claude_<id>`, and session IDs became `<id>`.

## The changelog

The 0.3.0 entry in `CHANGELOG.md` lists each file added and changed and why, every place the build departs from the spec with the owner's approval, and each fix the live runs led to.

## Result

Pass.
