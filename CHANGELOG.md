# Changelog

Every change to this plugin is logged here: what was added, changed or removed, and why. Nothing comes out without a line saying so. Newest first.

## 0.1.1 · Fixes from the first live tests

Twelve live tests ran in Cowork on 0.1.0 and all twelve passed. The evidence is in `tests/evidence/` and the summary is in `tests/RESULTS.md`. These changes fix what the runs showed.

Changed:

- The reviewer writes "(whole piece)" in place of a line number when a checker hit is marked L0. One run showed "Line 0" with no direction, and plainspeak-writer 1.4 marks every rate warning L0, so this now comes up often.
- The reviewer numbers findings past the fifth on from 6. One report put all of them under a single number, which hid how many there were.
- The reviewer ends its report with "What I couldn't judge" and adds nothing after it. In Cowork, reports ended with a stray line about saved memory.
- "When the caller pushes back" is now "After the report", and a follow-up question gets a short answer instead of the whole report sent again. Every follow-up in the live tests got the full report back.
- `tests/keys/a-clean.md`, `a-seeded.md` and `c-letter.md`: a checker warning counts as met when the report lists it as should-fix or clears it with a reason. The reviewer's rules allow both, and test 6 cleared its warnings with sound reasons.
- `tests/keys/a-seeded.md`: the label for flaw 2 sits in quotation marks, so the checker reads it as a quoted example.
- `tests/RUN-TESTS.md`: test 14 says a PDF can lose its signature in its text layer, and adds an optional check of published letters by well-known writers, with counts only. The Claude Code run now includes the letters people wrote.
- `tests/evidence/` and `tests/RESULTS.md`: the computer's name, the account folder IDs and the owner's first name are replaced with plain stand-ins, so nothing personal ships in the repository.

Added:

- `tests/evidence/01-isolation.md` to `12-channel.md` and `tests/RESULTS.md`, from the live run.
- `tests/evidence/14-human-letters.md`, counts only. Two letters a person wrote got Fix first, every HARD finding was one the rules require, no quote was wrong, and the one false alarm came from the PDF's missing signature. The letters, the reports and the quotes stay in `tests/human/`, which git ignores.

Checked against plainspeak-writer 1.4:

- The 19 unit tests pass with the 1.4 checker next to the repository.
- The checker's HARD hits on the test pieces match the keys: R01 and R02 on the seeded letter, none on the others. 1.4 turns per-hit warnings into one rate warning per piece.

## 0.1.0 · Submission review

Added:

- `agents/submission-reviewer.md`, the reviewer. It reads a packet and nothing else, runs seven checks for up to three readers, and reports in a fixed shape under fixed verdict rules.
- `skills/submission-review/SKILL.md`, the skill that checks the reviewer is installed, collects the files, builds the packet, starts the reviewer by name and hands back its report.
- `skills/submission-review/scripts/build_packet.py`, which builds the packet. It turns Word files into text, finds plainspeak-writer, runs its checker and writes the manifest. It has no field for notes.
- `tests/unit/test_build_packet.py`, with 19 tests for the script.
- `tests/RUN-TESTS.md` and the test pieces, for the live tests with made-up writers.
- `README.md`, `LICENSE` (MIT), `.gitignore` and `.claude-plugin/plugin.json`.

Where this build departs from the spec, and why:

- Names: `submission-reviewer` for the reviewer and `submission-review` for the skill replace the spec's working names. The owner named them.
- The reviewer's only tool is Read, where the spec allowed read and search tools. The manifest names every path, so search adds nothing, and without search the reviewer can't find files outside the packet.
- The reviewer has no shell, and the skill runs the checker. Current docs say a plugin's helper can't hold its own permission rules or hooks, so no setting could limit a shell to one script. The spec named this fallback.
- The reviewer skips project instruction files (CLAUDE.md), which helpers load by default.
- The skill starts the reviewer by name with the Agent tool. It avoids the skill setting that runs a skill in its own context, which has an open bug where plugin skills run inside the main conversation (anthropics/claude-code issue 49559). It never starts a fork, which copies the conversation.
- Cowork is supported in 0.1, where the spec listed it for later. Current docs say Cowork loads plugin helpers, and the same files work in both products.
- The report says whether the reviewer saw saved memory. A test in Cowork showed that every helper gets the account's saved memory, whatever its tools, and the spec's isolation test only checked the conversation.
- The manifest leaves original file names out, because a file name can say what the writer meant.
- With no reviewer available, as in claude.ai chat or after an upload under Skills, the skill stops instead of sending the person to a fresh chat. Chat ignores plugin helpers, and a fresh chat still has saved memory.
- The skill asks once for a missing target. The reviewer can't ask the person anything, so with no target it reviews against a general reader and says so.
- Every block in plainspeak-writer's rules counts as must-fix, including the ones only a reader can catch, such as an internal method name. The spec named checker blocks only.
- One finding per problem: a rule that hits several lines is one finding that quotes each line. Otherwise one repeated punctuation habit could push a piece to Rethink.
- Requirement checks: a resume is judged alone, and any other piece sent with a resume is judged across both, because the AI grader sees both. Requirement findings count as must-fix only when the AI grader is one of the readers. Without this, every letter would have to repeat the resume to pass.
- The first take ends on `Fit: yes` or `Fit: no`, so the verdict rules run the same way every time.
- Findings past the fifth in a section are listed one line each, with a short quote, where the spec capped each section at five. A finding cut from the report can't be fixed or tested.
- A checker warning is a should-fix finding unless the reviewer clears it with a stated reason, the way plainspeak-writer's rules treat warnings. A dry run showed the reviewer doing this on its own, so the rule now says so.
