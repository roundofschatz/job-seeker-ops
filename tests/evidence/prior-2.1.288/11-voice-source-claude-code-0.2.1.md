# Test 11: Voice source, with the full check in its own file (Claude Code, 0.2.1)

## Run

- Date: 2026-10-06
- Product, plugin and script: as in `01-isolation-claude-code-0.2.1.md`. Claude Code 2.1.288 in the Code tab of the Claude desktop app on Windows 11, with job-seeker-ops 0.2.1 installed.
- plainspeak-writer: 1.5, uploaded to the app as a skill. Its `references` folder holds `full-check.md` (21,528 bytes) beside `tells.md` (11,121 bytes). Since the installed copy has the full check in its own file, this part grades test 7's report, and no packet was built from the frozen 1.5 build in `..\jso-tests\plainspeak-1.5-build\`.
- This part covers what 0.2.1 changed: the manifest's "Full check" line, and the reviewer opening that file as well as the rules file. Test 11's packet without voice rules, for writer C's letter, wasn't part of this round.
- The key, `keys/a-seeded.md`, was opened after test 7's review had finished.
- The Windows user name in each path is written as `<user>`. Nothing else in the quoted lines was changed.

## Step 1: the "Voice rules" line in test 7's manifest

### Built as RUN-TESTS.md gives it

The command with no `--voice-dir` gave a manifest that ends:

````
22:- Voice rules: not found. Voice is unchecked.
23:- Checker: Didn't run, because plainspeak-writer wasn't found.
````

RUN-TESTS.md expects this line to "name plainspeak-writer, its version and the installed copy's path", and it names none of them. `default_roots()` in the script searches `CLAUDE_CONFIG_DIR` when it's set, then `~/.claude/skills`, `~/.claude/plugins` and `.claude\skills` in the working folder. The desktop app keeps a skill uploaded under Customize in `%APPDATA%\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\`, outside all of them. `~/.claude/skills/synced\<bucket>\` holds an older sync from 2026-09-22 with resume-ops in it and no plainspeak-writer, and `CLAUDE_CONFIG_DIR` isn't set. The unit tests' discovery test covers a standalone copy, a copy inside a plugin and `skills/synced/<bucket>`, and nothing in the app's `skills-plugin` folder.

The plugin's other script already looks there. `default_roots()` in candidate-positioning's `check_positioning.py` adds `%APPDATA%\Claude\local-agent-mode-sessions` and the Mac and Linux equivalents, and in this round's positioning run its `--voice` check found the installed plainspeak-writer 1.5 on its own.

### Built again with `--voice-dir`

submission-review's SKILL.md says that when plainspeak-writer wasn't found and the person has it installed, the packet gets built again with `--voice-dir` pointing at its folder. With the installed copy, the reviewed packet's manifest ends:

````
23:- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
24:- Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
25:- Checker: Ran with surface letter, exit code 1.
````

The path is the installed copy as Python resolves it, under the app's own folder in `AppData\Local\Packages\`. The folder passed to `--voice-dir` was `%APPDATA%\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\plainspeak-writer`, and `full-check.md` has the same SHA-256 at both paths. The full manifest is in `07-seeded-claude-code-0.2.1.md`.

## What the reviewer opened

From the test 7 report, word for word:

````
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md. Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Files I opened:
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\manifest.md
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\piece.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\target.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\companion-1.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\checker.txt
  - the tells.md and full-check.md paths above
````

The reviewer's transcript holds seven Read calls and the hand-back, nothing else: the five packet files, then `tells.md`, then `full-check.md`, each at the manifest's path. The test 1 reviewer's transcript shows the same seven kinds of call on its own packet.

## Grade

- **Pass**: The manifest has a "Full check" line naming the installed copy's `full-check.md`
  - Quote: “- Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md”
  - This holds for the packet built with `--voice-dir`. The packet built without it has no "Voice rules" path and no "Full check" line.
- **Pass**: "Files I opened" lists the packet's files, the rules file and the full check file, and nothing else
  - It lists manifest.md, piece.txt, target.txt, companion-1.txt and checker.txt, then “the tells.md and full-check.md paths above”.
  - The transcript's Read calls are the same seven files.
- **Pass**: The report's "Voice rules" line names each rules file the reviewer used, as 0.2.1's agent file asks
  - Quote: “Voice rules: plainspeak-writer 1.5. Rules file: ...\references\tells.md. Full check: ...\references\full-check.md”
- **Pass**: The report meets `keys/a-seeded.md`
  - Every condition passes; `07-seeded-claude-code-0.2.1.md` has the grade with quotes.
  - Must-fix 3 takes its class from the full check file: “This is an internal method name, which the full check lists under its blocks.”
- **Fail**: The script finds the installed plainspeak-writer on its own
  - Quote from the first build's manifest: “- Voice rules: not found. Voice is unchecked.”

## Unit tests

`python tests/unit/test_build_packet.py`, run from the repository with Python 3.12.10: “Ran 22 tests in 1.392s”, then “OK”.

## Result

The reviewer's side passes, with the full check in its own file. Given a manifest with a "Full check" line, the reviewer opened that file and the rules file, listed both and nothing else beyond the packet, and took the class for the internal method name from the full check. The packet script's side fails in the desktop app's Code tab: on its own it doesn't find plainspeak-writer installed as an uploaded skill, so every packet comes out with voice unchecked unless the person, or the skill, passes `--voice-dir`. The fix belongs in `default_roots()`: the same roots `check_positioning.py` searches, with a unit test for the app's `local-agent-mode-sessions\skills-plugin\<ids>\skills\` layout.
