# Test 11: Voice source, with the full check in its own file (Claude Code, 0.2.1)

## Run

- Date: 2026-10-06
- Product, plugin and script: as in `01-isolation-claude-code-0.2.1.md`. Claude Code 2.1.289 in the Code tab of the Claude desktop app on Windows 11, with job-seeker-ops 0.2.1 installed.
- plainspeak-writer: 1.5, uploaded to the app as a skill. Its `references` folder holds `full-check.md` beside `tells.md`. Since the installed copy has the full check in its own file, this part grades test 7's report, and no packet was built from the frozen 1.5 build in `..\jso-tests\plainspeak-1.5-build\`.
- This part covers what 0.2.1 changed: the manifest's "Full check" line, and the reviewer opening that file as well as the rules file. Test 11's packet without voice rules, for writer C's letter, wasn't part of this round.
- The key, `keys/a-seeded.md`, was opened after test 7's review had finished.
- The Windows user name in each path is written as `<user>`. Nothing else in the quoted lines was changed.

## Step 1: the "Voice rules" line in test 7's manifest

### Built as RUN-TESTS.md gives it

With no `--voice-dir`, the manifest's settings end:

````
- Voice rules: not found. Voice is unchecked.
- Checker: Didn't run, because plainspeak-writer wasn't found.
````

RUN-TESTS.md expects this line to name plainspeak-writer, its version and the installed copy's path, and it names none of them. `default_roots()` in `build_packet.py` searches `CLAUDE_CONFIG_DIR` when it's set, then `~/.claude/skills`, `~/.claude/plugins` and `.claude\skills` in the working folder. The desktop app keeps a skill uploaded under Customize in `%APPDATA%\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\`, outside all of them, and `CLAUDE_CONFIG_DIR` isn't set. `~/.claude/skills` on this computer holds other skills and no plainspeak-writer.

The plugin's other script already looks there: `default_roots()` in candidate-positioning's `check_positioning.py` adds `%APPDATA%\Claude\local-agent-mode-sessions` and the Mac and Linux equivalents. The 2.1.288 run found the same gap.

### Built again with `--voice-dir`

submission-review's SKILL.md says: "When the script says plainspeak-writer wasn't found and the person has it installed, find the folder that holds its SKILL.md and rerun with `--voice-dir` pointing there." With `--voice-dir` pointing at the installed copy, the manifest's settings end:

````
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
- Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Checker: Ran with surface letter, exit code 1.
````

The path is the real folder behind `%APPDATA%` for the Store copy of the app. It names plainspeak-writer, its version and the installed copy, and the "Full check" line names that copy's `full-check.md`.

## Step 2: "Files I opened" in test 7's report

From the report in `07-seeded-claude-code-0.2.1.md`, word for word:

````
- Files I opened:
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5\manifest.md
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5\piece.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5\target.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5\companion-1.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5\checker.txt
  - the tells.md and full-check.md paths above
````

The reviewer's transcript holds seven Read calls, on those five packet files, `tells.md` and `full-check.md`, then its hand-back. The list matches the calls.

## Step 3: unit tests

`python tests/unit/test_build_packet.py`, Python 3.12.10:

````
Ran 22 tests in 1.715s

OK
````

## Grade

| Condition | Result | Evidence |
|---|---|---|
| The manifest has a "Full check" line naming the installed copy's `full-check.md` | Pass, with `--voice-dir` | "- Full check: C:\Users\<user>\...\skills\plainspeak-writer\references\full-check.md". Built as RUN-TESTS.md gives it, the manifest says "Voice rules: not found." |
| "Files I opened" lists the packet's files, the rules file and the full check file | Pass | The five packet files, then "the tells.md and full-check.md paths above". |
| Nothing else | Pass | The transcript holds no other Read call. |
| The report meets `keys/a-seeded.md` | Pass | See `07-seeded-claude-code-0.2.1.md`: Fix first, `Fit: yes`, flaws 1, 2, 4, 7 and 8 must-fix and nothing else, flaws 3, 5 and 6 should-fix, and no replacement wording. |
| Unit tests | Pass | 22 of 22 OK. |

**Test 11: pass with `--voice-dir`.** The script can't find plainspeak-writer in this app on its own, so a review run without that step goes ahead with voice unchecked.
