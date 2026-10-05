# Test 14: Letters people wrote (Claude Code)

This file holds no text from the letters, since they stay out of the repository. The two reports, word for word, and the grade with quotes are in `tests/human/results/`, which git ignores: the two `letter-*-review-claude-code.md` files and `14-grade-claude-code.md`. The letters are called A and B here.

## Run

- Date: 2026-10-01
- Product: Claude Code, in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- Claude Code version: 2.1.280 (`claude --version`)
- Plugin: job-seeker-ops, installed copy. Its `plugin.json` reads 0.1.1, and `build_packet.py` reports 0.1.0.
- Installed copy: `%APPDATA%\Claude\local-agent-mode-sessions\<ids>\rpm\plugin_<id>\`. RUN-TESTS.md says to look under `~/.claude/plugins`, and nothing from job-seeker-ops is there. The desktop app keeps an uploaded plugin in its own folder.
- SCRIPT: `skills\submission-review\scripts\build_packet.py` in the installed copy. It's the same file as the repository copy, byte for byte (SHA-256 starts `2A33C959D0B9BFB9`). Run with `python`, Python 3.12.10.
- Installed `agents\submission-reviewer.md`: the same as the repository copy except that the front matter writes the description as one quoted line. Its tools line reads `tools: Read`.
- PACKETS: `C:\Users\<user>\repos\tools\jso-tests\packets`, new for this run.
- The Windows user name in each path is written as `<user>`.
- Voice rules: every build passed `--voice-dir ..\plainspeak-writer` from the repository folder, as the owner asked, so every packet uses plainspeak-writer 1.4.
- Reviewer started as `job-seeker-ops:submission-reviewer` with the Agent tool. The four reviewers in this run (tests 1 and 2, test 7 and the two test 14 letters) were started together, each with its own printed line and nothing else.
- Letters: the two .txt letters in `tests/human/`. Neither has a posting there, so both reviews ran with no target. Test 14 names no channel, so neither build passed one. The Cowork run passed `--channel upload`.
- In the grade, ⏎ marks a line break inside a quote.

## Build

Run from the repository folder, `C:\Users\<user>\repos\tools\job-seeker-ops`:

````
python SCRIPT --type letter --piece tests\human\<letter A>.txt --voice-dir ..\plainspeak-writer --out ..\jso-tests\packets
python SCRIPT --type letter --piece tests\human\<letter B>.txt --voice-dir ..\plainspeak-writer --out ..\jso-tests\packets
````

Script output for letter A:

````
Packet: C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223145-letter-eb04
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223145-letter-eb04. Read manifest.md first.
````

Script output for letter B:

````
Packet: C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223146-letter-ec73
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223146-letter-ec73. Read manifest.md first.
````

## Letter A review

- Packet folder: `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223145-letter-eb04`
- Reviewer agent id: `a47df6f29785edb9b`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 22:31.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 3,217 | 498 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 1,220 | 190 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: none given. Review against a general reader for this type of piece.
- Channel: not given.
- Voice rules: plainspeak-writer 1.4. Rules file: C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- Checker: Ran with surface letter, exit code 1.
````

### Exact message sent

````
Review the packet in C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223145-letter-eb04. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223145-letter-eb04\manifest.md
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223145-letter-eb04\piece.txt
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223145-letter-eb04\checker.txt
Read C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
SubagentHandback (the harness's delivery call, holding the report)
````

## Letter B review

- Packet folder: `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223146-letter-ec73`
- Reviewer agent id: `ade5bfd32e601c3cd`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 22:31.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 3,525 | 550 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 1,747 | 257 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: none given. Review against a general reader for this type of piece.
- Channel: not given.
- Voice rules: plainspeak-writer 1.4. Rules file: C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- Checker: Ran with surface letter, exit code 1.
````

### Exact message sent

````
Review the packet in C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223146-letter-ec73. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223146-letter-ec73\manifest.md
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223146-letter-ec73\piece.txt
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223146-letter-ec73\checker.txt
Read C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
SubagentHandback (the harness's delivery call, holding the report)
````

## What came back, in counts

| Letter | Checker HARD (1.4) | Checker WARN (1.4) | Verdict | Must fix | Should fix | Blind line |
|---|---|---|---|---|---|---|
| A | 2: R18, R11 | 2: S01, V01 rate | Fix first | 3 | 14 | `blind: no` |
| B | 6: R31 x3, R05, R33 x2 | 2: R44, V01 rate | Fix first | 5 | 10 | `blind: no` |

Both reviewers wrote `blind: no` for one reason, the account email address that the harness attaches to every helper. Neither saw saved memory, preferences, project instructions or an earlier conversation. `02-memory-claude-code.md` covers this.

## Grade (test 14 in RUN-TESTS.md)

- **Not tested**: A letter with no HARD hits gets Send with few findings
  - Both letters have HARD hits under plainspeak-writer 1.4, so this case didn't come up. It didn't come up in the Cowork run either.
- **Pass**: Each HARD hit the checker's rules require shows as a must-fix finding
  - Letter A: R18 and R11 are must-fix 1 and 2. Letter B: R31, R05 and R33 are must-fix 1, 2 and 3, one finding per rule.
  - Quote: “Fix first. Three must-fix findings, which falls in the one-to-five rule.”
  - Quote: “Fix first. There are five must-fix findings, which falls in the one-to-five rule.”
- **Pass**: No finding misquotes the letter
  - A script checked every quoted string in both reports against the packets, 43 in one report and 51 in the other. Every string that quotes a letter matches it. The reviewers wrote straight apostrophes where the letters have curly ones.
- **Pass**: No finding invents a problem
  - Three findings don't hold for the real letters, and the reviewer made up none of them. They are listed under this grade.
  - If a finding that repeats a checker miscount counts as an invented problem, this condition fails on that one finding.
- **Done**: The sign-off was checked before grading the finding about it

The three findings that don't hold for the real letters:

1. Letter A, should-fix 14, says the sign-off has no name or contact detail after it. The original PDF has a signature image there and a contact line in its footer, and the test copy has neither. The reviewer said it couldn't tell whether the name was missing from the real letter.
2. Letter B, must-fix 5, is about a placeholder that only the test copy holds. The original Word file has the real words there. The reviewer said the finding falls away if the packet masked them. Without it the letter has four must-fix findings and the verdict is still Fix first.
3. Letter A, should-fix 8, repeats the checker's V01 rate of 10.0 lists of three per 1,000 words. Two of the checker's five hits are the last three items of four-item lists. The real count is three, or 6.0 per 1,000, which is under the limit of 8, so the checker shouldn't have warned. This one starts in plainspeak-writer's `check_voice.py`, and the reviewer passed it along without recounting.

Against the Cowork run: letter A got the same verdict and the same three must-fix findings. Letter B got the same verdict with two more must-fix findings, both under Risk. One is the placeholder above. The other is a typo that the Cowork reviewer listed as a should-fix under Clarity. So the two runs disagree on what the Risk check covers.

**Result: Pass on the test's terms.** The clean-letter case is still untested.
