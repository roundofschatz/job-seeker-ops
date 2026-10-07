# Test 11: Voice source, with no `--voice-dir` (Claude Code, 0.2.2)

A rerun of test 11 after the fix in 0.2.2. In the 0.2.1 round, the packet script didn't find plainspeak-writer uploaded to the desktop app, and test 11 passed only with `--voice-dir`. This run builds test 7's packet exactly as RUN-TESTS.md gives it.

## Run

- Date: 2026-10-07
- Product: Claude Code 2.1.289, in the Code tab of the Claude desktop app on Windows 11. The same session that ran the 0.2.1 round and wrote the fix. It didn't help build the plugin's earlier versions, and the planted flaws in writer A's letter were already known to it from the 0.2.1 round's grading. The reviewer is a new helper and knows none of that.
- Plugin: job-seeker-ops 0.2.2, uploaded to the app from `dist/job-seeker-ops.zip`, built from commit `f99c7d5`. The Code tab installed it at `~/.claude/plugins/marketplaces/local-desktop-app-uploads/job-seeker-ops/`, and `installed_plugins.json` names that folder with version 0.2.2. Its `plugin.json` reads 0.2.2, `build_packet.py --version` prints 0.2.2, and the folder matches the repository file for file.
- Where the upload went. The 0.2.1 round's SCRIPT was the copy under `%APPDATA%\Claude\local-agent-mode-sessions\<ids>\rpm\plugin_<id>\`, the app's other copy of the plugin. That folder is gone since this upload, and the `rpm` manifest now lists only another plugin. Both copies of 0.2.1 were the same file, byte for byte, so the 0.2.1 results stand.
- plainspeak-writer: 1.5, uploaded to the app as a skill, unchanged since the 0.2.1 round.
- Working folder: the job-seeker-ops repository, on `main`, with nothing changed. The reviewer's git snapshot read "(clean)".
- The report was copied by script from the reviewer's hand-back call, word for word. The Windows user name in each path is written as `<user>`. Nothing else in it was changed.

## Step 1: the build, with no `--voice-dir`

````
python SCRIPT --type letter --piece tests/writers/a-quintero/letter-seeded.txt --target tests/writers/a-quintero/posting.txt --companion tests/writers/a-quintero/resume.txt --channel upload --out jso-tests/packets
````

````
Packet: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261007-001232-letter-27cd
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261007-001232-letter-27cd. Read manifest.md first.
````

### Manifest

````
# Review packet

Built by build_packet.py 0.2.2 on 2026-10-07 at 00:12.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,503 | 268 |
| target.txt | The target: the job posting, or the reader's own words | 1,430 | 234 |
| companion-1.txt | A companion the real reader also sees | 1,569 | 260 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 1,185 | 190 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
- Full check: C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Checker: Ran with surface letter, exit code 1.
````

The "Voice rules" line names plainspeak-writer, its version and the installed copy's path, and the "Full check" line names that copy's `full-check.md`. In the 0.2.1 round the same command gave "Voice rules: not found. Voice is unchecked."

## Step 2: the reviewer

Started with the Agent tool as `job-seeker-ops:submission-reviewer`, with the printed line and nothing else:

````
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261007-001232-letter-27cd. Read manifest.md first.
````

Its transcript holds seven Read calls, on the five packet files, `tells.md` and `full-check.md`, then its hand-back.

### The report

````
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter), target.txt (the target: job posting), companion-1.txt (a companion the reader also sees: the resume), checker.txt (plainspeak-writer checker output for piece.txt), manifest.md (the manifest)
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md. Full check: C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Also in my context: an account email; a git snapshot (it says nothing about this piece, its target or how it was written); instructions from connected tool servers (about the tools, nothing about the person or the piece). No saved memory, profile, preferences, project instructions or earlier conversation.
- Files I opened:
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261007-001232-letter-27cd\manifest.md
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261007-001232-letter-27cd\piece.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261007-001232-letter-27cd\target.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261007-001232-letter-27cd\companion-1.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261007-001232-letter-27cd\checker.txt
  - the tells.md and full-check.md paths above
- blind: yes

## First take (Recruiter, first look)
An emergency department nurse manager who cut door-to-provider time from 38 to 22 minutes and runs a 52-person team and a $4.1 million budget, applying to run three primary care clinics. The opening line could go to any employer, but the wait-time numbers right after it match this posting's top problem, so I'd keep reading. Fit: yes

## Verdict
Fix first. The letter fits and has exactly five must-fix findings, so rule 2 (one to five must-fix) sets the verdict.

## Must fix
1. "By December the average was 22 minutes — down by 16." (line 5) · Voice · Checker HARD hit R01: an em dash. Direction: use a period or comma, or cut "down by 16", which only restates the math.
2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · Checker HARD hit R02: the "not just X but Y" shape. The second half also names nothing a hiring manager can check, because it never says what changed in the department. Direction: state the department-wide change with a fact, or cut the line.
3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first." (line 7) · Voice (internal method name, a full-check block), also Clarity · No reader has heard of "Q-Ladder". The coined name tells the hiring manager nothing the plain description doesn't already say. "Every new patient" also reads as overreach for a manager of 52 staff. Direction: describe what the method does and drop the name.
4. "Since becoming nurse manager in 2017" (line 7) vs. the resume's "Nurse Manager, Emergency Department | Mar 2019 - Present" (companion line 10) · Risk · The letter and the resume give different start years for the same title. A close reader or a background check will catch it, and it puts every other figure in doubt. Direction: make the two documents agree.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · This names a gap outright, nine years back and nine months long (Sep 2013 to Jun 2014 on the resume), and then never explains it. The reader gets a reason to worry and nothing to settle it. It also breaks up the run from proof to Spanish to the ask. Direction: cut the paragraph.

## Should fix
1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · This is the line the recruiter reads first, and it would work for any health system unchanged. "Commitment to patients" points at nothing Juniper Ridge actually does. Direction: open on the posting's own problem (the 34-minute wait, the evening hours) or go straight to the 38-to-22 result.
2. "I'm known across the hospital as a leader people want to work for." (line 9) · Proof · This is a reputation claim with nothing behind it: no retention figure, no turnover figure, no award. A hiring manager can't check it and will discount it. Direction: give a number or a named example, or cut the line.
3. "In 2022 our door-to-provider time averaged 38 minutes." (line 5) and the target's "Cut the average wait from check-in to seeing a provider, now 34 minutes" (target line 10) · Proof (why this firm) · The letter never ties its emergency department results to primary care clinics. It never names the three sites, the 40 staff, the $6.2 million budget or the 34-minute baseline. The hiring manager has to work out for themselves why an ED result carries over to clinics. Direction: tie the 38-to-22 result to their 34 minutes and say what carries over to clinic check-in.
4. "where you want the wait to be by fall" (line 15) · Clarity · The posting sets no fall target, and the evening hours start "this spring." The reader may think the writer misread the posting. Direction: tie the ask to a date or goal the posting actually gives.
5. "I know what it takes to keep the room calm when the waiting area is full." (line 9) · Voice · Checker WARN R44 (the vague place), not cleared. "The room" is unclear, and the sentence claims a skill without naming any time it was used. Direction: name the place and the time it happened, or cut the line.
6. (whole piece) · Voice · Checker WARN V06, short flat lines after long ones: "In 2022 our door-to-provider time averaged 38 minutes." and "Your posting asks for Spanish, and I'm fluent."
7. (whole piece) · Voice · Checker WARN V04, staccato layout ("5 of 9 paragraphs are one sentence"), for example lines 3, 11 and 15.

Cleared warnings: none.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume line 26 (BSN, 2011); not in the letter |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Letter line 7; resume lines 10 and 17 (charge nurse from 2014, nurse manager from 2019). The start year conflicts, see Must fix 4 |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7 ($4.1M closed under plan, built the fast-track schedule); resume lines 13, 14, 18 |
| Working knowledge of Epic or a similar EHR | Must-have | Shown | Letter line 7 (2020 go-live); resume line 15 (Epic ASAP go-live, trained 140 staff) |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5; resume line 12 (38 to 22 minutes) |
| Fluent in English and Spanish | Preferred | Shown | Letter line 13 (explains discharge plans in Spanish now); resume line 33 |
| Lean or Six Sigma training | Preferred | Shown | Resume line 30 (Green Belt, 2023) only; not in the letter |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7; resume line 14 (six-bed fast-track area, 2021) |

## What I couldn't judge
- The year she became nurse manager: 2017 in the letter, 2019 on the resume.
- Door-to-provider time falling from 38 to 22 minutes in 2022, and the claim that sitting patients "never took a bed."
- The $4.1 million staffing budget closed under plan for three years (2023 to 2025 on the resume).
- 52 nurses and technicians, eight nurses hired for the fast-track area, 140 staff trained on Epic.
- What the "Q-Ladder" is, and whether she personally sorted "every new patient."
- "Known across the hospital as a leader people want to work for."
- Spanish fluency and her current practice of explaining discharge plans without the interpreter line.
- What happened between Sep 2013 and Jun 2014.
````

## Step 3: unit tests

`python tests/unit/test_build_packet.py`, Python 3.12.10:

````
Ran 25 tests in 3.167s

OK
````

## Grade

| Condition | Result | Evidence |
|---|---|---|
| The "Voice rules" line names plainspeak-writer, its version and the installed copy, with no `--voice-dir` | Pass | "Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\...\plainspeak-writer\references\tells.md" |
| A "Full check" line names that copy's `full-check.md` | Pass | "Full check: ...\plainspeak-writer\references\full-check.md" |
| "Files I opened" lists the packet's files, the rules file and the full check file, and nothing else | Pass | The five packet files, then "the tells.md and full-check.md paths above", which matches its seven Read calls. |
| The report meets `keys/a-seeded.md`: Fix first, `Fit: yes` | Pass | "Fix first. The letter fits and has exactly five must-fix findings" and "... so I'd keep reading. Fit: yes" |
| Flaws 1, 2, 4, 7 and 8 are must-fix, and nothing else | Pass | Must fix 1 "22 minutes — down by 16", 2 "wasn't just a triage fix but", 3 "Q-Ladder", 4 "Since becoming nurse manager in 2017", 5 "I was out of work for most of a year". |
| Flaws 3, 5 and 6 are should-fix | Pass | Should fix 1 "I'm excited to apply for the Clinic Operations Manager position at your organization", 2 "I'm known across the hospital as a leader people want to work for." and 5 "keep the room calm". |
| No replacement wording or sample sentence | Pass | Each direction says what to do without wording, such as "Direction: describe what the method does and drop the name." |
| `blind: yes` | Pass | "- blind: yes", with the git snapshot listed and none of it quoted. |
| Unit tests | Pass | 25 of 25 OK. |

**Test 11: pass, with no `--voice-dir`.** 0.2.2 fixes what the 0.2.1 round found.
