# Test 7: Seeded flaws (Claude Code, 0.2.1)

## Run

- Date: 2026-10-06
- Product, plugin, script and working folder: as in `01-isolation-claude-code-0.2.1.md`. Claude Code 2.1.289 in the Code tab of the Claude desktop app on Windows 11, job-seeker-ops 0.2.1 installed, plainspeak-writer 1.5 installed as a skill, and the session in the job-seeker-ops repository.
- The reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, with the printed line and nothing else, at the same time as the test 1 reviewer. Its context held the account email and the same git snapshot as the test 1 reviewer's.
- The report below was copied by script from the reviewer's own hand-back call in its transcript, word for word. The Windows user name in each path is written as `<user>`. Nothing else in it was changed.
- The key, `keys/a-seeded.md`, was opened after this review had finished.

## Build

Run from the repository folder as RUN-TESTS.md gives it:

````
python SCRIPT --type letter --piece tests/writers/a-quintero/letter-seeded.txt --target tests/writers/a-quintero/posting.txt --companion tests/writers/a-quintero/resume.txt --channel upload --out jso-tests/packets
````

As in test 1, the manifest read "Voice rules: not found. Voice is unchecked." and "Checker: Didn't run, because plainspeak-writer wasn't found." The packet was built again with `--voice-dir` pointing at the installed plainspeak-writer, as submission-review's SKILL.md says, and the reviewer got the second packet.

Script output:

````
Packet: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5. Read manifest.md first.
````

### Manifest

````
# Review packet

Built by build_packet.py 0.2.1 on 2026-10-06 at 23:35.

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
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
- Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Checker: Ran with surface letter, exit code 1.
````

## The message sent

````
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5. Read manifest.md first.
````

The reviewer read the five packet files, `tells.md` and `full-check.md`, and nothing else, as the tool calls in its transcript show.

## The report

````
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the manifest); piece.txt (the piece: cover letter); target.txt (the target: the Juniper Ridge Health Partners job posting); companion-1.txt (a companion the reader also sees: the candidate's resume); checker.txt (plainspeak-writer 1.5 checker output, surface letter, exit code 1)
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md. Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Also in my context: an account email; a git snapshot (branch, git user name, an untracked folder, recent commit titles), none of which names this piece, its target or how it was written; instructions from connected tool servers, which say nothing about the person or the piece
- Files I opened:
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5\manifest.md
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5\piece.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5\target.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5\companion-1.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-75f5\checker.txt
  - the tells.md and full-check.md paths above
- blind: yes

## First take (Recruiter, first look)
This is an emergency department nurse manager in Tucson who cut door-to-provider time from 38 to 22 minutes and runs a $4.1 million staffing budget, which matches the wait-time and budget work this posting is hiring for. The first line could go to any employer, but the second paragraph gets me to keep reading. Fit: yes

## Verdict
Fix first. Rule 2: five must-fix findings (the letter fits, and five isn't more than five).

## Must fix
1. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first." (line 7) · Clarity and Voice · "Q-Ladder" is an internal method name, which the full check blocks. The reader has never heard of it, and it isn't on the resume, so there's nothing to check it against. "Every new patient" also reads as overreach coming from a manager of 52 staff, and the hiring manager will wonder whether it's meant literally. Direction: say what the method does in plain words, or cut the name.
2. "By December the average was 22 minutes — down by 16." (line 5) · Voice · Checker HARD R01: an em dash. Direction: use a period or a comma.
3. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · Checker HARD R02: a "not just X but Y" construction. It's also a summary line closing the paragraph, and it makes a bigger claim than anything shown. The hiring manager reads it as a claim with nothing under it. Direction: give the concrete department-wide change, or cut the line.
4. "Since becoming nurse manager in 2017" (line 7) against "Nurse Manager, Emergency Department | Mar 2019 - Present" and "Charge Nurse, Emergency Department | Jun 2014 - Feb 2019" (resume, lines 10 and 17) · Risk · The letter and the resume give different start dates for the same title. A reader holding both will catch it and start doubting the other figures. Direction: make the date match the resume.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · This names a gap outright, apologizes for it and then never explains it. It sends the recruiter looking for a problem they might not have noticed, and it sits in the middle of the letter's proof. Direction: cut the line.

## Should fix
1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · This is the line the recruiter reads first, and it would fit any health system unchanged. "Commitment to patients" is a label nobody can check. Direction: open on something specific to Juniper Ridge or on the wait-time result.
2. "I'm known across the hospital as a leader people want to work for. I know what it takes to keep the room calm when the waiting area is full." (line 9) · Proof · Both claims name no number, no person and no result. Next to the hard numbers in lines 5 and 7, they read as filler. Direction: give a fact that backs them, such as retention or a staffing figure, or cut the paragraph.
3. "I'd welcome a conversation about the evening launch and where you want the wait to be by fall." (line 15) against "Cut the average wait from check-in to seeing a provider, now 34 minutes" and "three primary care clinics" (target, lines 10 and 4) · Proof · Apart from Spanish and this closing line, the letter never ties the emergency department record to the posting's three primary care sites or its 34-minute figure. A hiring manager has to work out for themselves how emergency triage carries over to clinic check-in. Direction: connect the 38-to-22 result to their number and their sites.
4. "In 2022 our door-to-provider time averaged 38 minutes." / "By December the average was 22 minutes" (line 5); "Since becoming nurse manager in 2017," / "When we opened a six-bed fast-track area in 2021," (line 7); "After I left Saint Anselm in 2013," (line 11) · Voice · Five sentences open on a time phrase, and read top to bottom, the letter sounds like a timeline. Direction: vary how these sentences open.
5. "keep the room calm" (line 9) · Voice · Checker WARN R44, a vague place. "The room" names no real place, and "the waiting area" in the same sentence doesn't fix it. Direction: name the real place.

Cleared warnings: V06 (whole piece), because both flagged short lines, "In 2022 our door-to-provider time averaged 38 minutes." and "Your posting asks for Spanish, and I'm fluent.", add a new fact and neither restates the line before; V04 (whole piece), because the checker's count includes the salutation and signature, and only 3 of the 7 body paragraphs are one sentence long.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| "Bachelor's degree in nursing, health administration or a related field." | Must-have | Shown | Resume line 26 (BSN, Saguaro State University, 2011) |
| "Five or more years in clinical operations or nurse leadership." | Must-have | Shown | Resume lines 10 and 17 (charge nurse from 2014, nurse manager from 2019); letter line 7 gives a different start year (see Must fix 4) |
| "Experience managing staff schedules and a budget for a unit or clinic." | Must-have | Shown | Letter line 7 ($4.1 million budget, fast-track schedule); resume lines 13, 14 and 18 |
| "Working knowledge of Epic or a similar electronic health record." | Must-have | Shown | Letter line 7 (2020 go-live); resume line 15 (led the go-live, trained 140 staff) |
| "A record of improving patient wait times or throughput." | Must-have | Shown | Letter line 5 (38 to 22 minutes); resume line 12 |
| "Fluent in English and Spanish." | Preferred | Shown | Letter line 13 (explains discharge plans in Spanish now); resume line 33 |
| "Lean or Six Sigma training." | Preferred | Shown | Resume line 30 (Green Belt, 2023); the letter doesn't mention it |
| "Experience opening a new clinic site or service." | Preferred | Shown | Letter line 7 (fast-track area, 2021, hired the first eight nurses); resume line 14 |

## What I couldn't judge
- Which nurse manager start date is right: 2017 in the letter or March 2019 on the resume.
- The cut in door-to-provider time from 38 to 22 minutes in 2022, and whether it held after December.
- 52 nurses and technicians, the $4.1 million staffing budget, and closing under plan in 2023, 2024 and 2025.
- The fast-track area: six beds, opened in 2021, eight nurses hired.
- The 2020 Epic go-live and the 140 staff trained.
- What the "Q-Ladder" is, and whether "every new patient" is literal.
- "Known across the hospital as a leader people want to work for": nothing on the page backs it.
- Spanish fluency and the Lean Six Sigma Green Belt (2023).
- The break between Saint Anselm (ended Sep 2013) and Sonoran Valley (started Jun 2014), and why it happened.
````

## Grade against `keys/a-seeded.md`

plainspeak-writer 1.5 still lists R01 and R02 under HARD, and the checker output in the packet shows both as HARD, so flaws 1 and 2 stay must-fix.

| Condition | Result | Evidence |
|---|---|---|
| Verdict Fix first | Pass | "Fix first. Rule 2: five must-fix findings" |
| First take ends `Fit: yes` | Pass | "... gets me to keep reading. Fit: yes" |
| Flaw 1, the dash, must-fix with the planted words | Pass | Must fix 2: "By December the average was 22 minutes — down by 16." · Voice · "Checker HARD R01" |
| Flaw 2, "not just X but Y", must-fix | Pass | Must fix 3: "Split-flow wasn't just a triage fix but a change in how the whole department runs." · Voice · "Checker HARD R02" |
| Flaw 4, Q-Ladder, must-fix | Pass | Must fix 1: "I sorted every new patient with the Q-Ladder, ..." · Clarity and Voice · "an internal method name, which the full check blocks" |
| Flaw 7, the gap, must-fix | Pass | Must fix 5: "After I left Saint Anselm in 2013, I was out of work for most of a year, ..." · Risk |
| Flaw 8, the 2017 date, must-fix | Pass | Must fix 4: "Since becoming nurse manager in 2017" against "Nurse Manager, Emergency Department \| Mar 2019 - Present" · Risk |
| No other must-fix finding | Pass | The must-fix list holds those five and no others. |
| Flaw 3, the unproved claim, should-fix | Pass | Should fix 2: "I'm known across the hospital as a leader people want to work for. ..." · Proof |
| Flaw 5, the vague place, should-fix | Pass | Should fix 5: "keep the room calm" · Voice · "Checker WARN R44, a vague place" |
| Flaw 6, the opening for any firm, should-fix | Pass | Should fix 1: "I'm excited to apply for the Clinic Operations Manager position at your organization, ..." · Proof |
| No replacement wording or sample sentence | Pass | Each direction says what to do and supplies no wording, such as "Direction: say what the method does in plain words, or cut the name." and "Direction: make the date match the resume." The nearest is must fix 2's "use a period or a comma", which names punctuation and supplies no sentence. Should fix 2's "such as retention or a staffing figure" names a kind of fact and gives no wording. |

The other findings are ones the key allows: should-fix 3 on tying the record to the posting's clinics and its 34 minutes, should-fix 4 on time-phrase openings, and V06 and V04 cleared with a reason on the "Cleared warnings" line.

**Test 7: pass.**
