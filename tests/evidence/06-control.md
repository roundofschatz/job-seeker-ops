# Test 6: The control letter

## Run

- Date: 2026-10-01 (America/Denver)
- Product: Cowork (a cloud Cowork task linked to the owner's computer). This session didn't help build the plugin.
- Claude Code version in the session: 2.1.287 (`claude --version`)
- job-seeker-ops 0.1.0, installed copy at `/root/.claude/plugins/synced/<account>/job-seeker-ops`
- SCRIPT: `/root/.claude/plugins/synced/<account>/job-seeker-ops/skills/submission-review/scripts/build_packet.py` (build_packet.py 0.1.0), run with Python 3.13.15
- WRITERS: `/mnt/user-data/uploads/tools/job-seeker-ops/tests/writers` (the eleven files staged from the computer)
- PACKETS: `/home/claude/jso-tests/packets`
- Reviewer started as `job-seeker-ops:submission-reviewer` with the Agent tool. Reports and replies below are copied from the reviewer's own hand-back call in the session transcript, word for word.
- In the grades, ⏎ marks a line break inside a quote.

## Build

````
/root/.claude/plugins/synced/<account>/job-seeker-ops/skills/submission-review/scripts/build_packet.py --type letter --piece /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/a-quintero/letter-clean.txt --target /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/a-quintero/posting.txt --companion /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/a-quintero/resume.txt --channel upload --out /home/claude/jso-tests/packets
````

Script output:

````
Packet: /home/claude/jso-tests/packets/20261001-165235-letter-d426
Message for the reviewer (send exactly this line and nothing else):
Review the packet in /home/claude/jso-tests/packets/20261001-165235-letter-d426. Read manifest.md first.
````

## Review

- Packet folder: `/home/claude/jso-tests/packets/20261001-165235-letter-d426`
- Reviewer agent id: `a7b209347053304c1`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 16:52.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,443 | 248 |
| target.txt | The target: the job posting, or the reader's own words | 1,430 | 234 |
| companion-1.txt | A companion the real reader also sees | 1,569 | 260 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 718 | 117 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.3. Rules file: /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Checker: Ran with surface letter, exit code 0.
````

### Exact message sent

````
Review the packet in /home/claude/jso-tests/packets/20261001-165235-letter-d426. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-d426/manifest.md"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-d426/piece.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-d426/target.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-d426/companion-1.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-d426/checker.txt"}
Read {"file_path": "/root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md"}
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter); target.txt (the job posting, Clinic Operations Manager at Juniper Ridge Health Partners); companion-1.txt (the resume the reader also sees); checker.txt (plainspeak-writer 1.3 checker output, surface letter, exit 0); manifest.md (the manifest)
- Voice rules: plainspeak-writer 1.3, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Also in my context: saved memory (a user profile, saved preferences and a memory file listing), plus account context naming the user's email. I didn't use any of it.
- Files I opened: /home/claude/jso-tests/packets/20261001-165235-letter-d426/manifest.md, /home/claude/jso-tests/packets/20261001-165235-letter-d426/piece.txt, /home/claude/jso-tests/packets/20261001-165235-letter-d426/target.txt, /home/claude/jso-tests/packets/20261001-165235-letter-d426/companion-1.txt, /home/claude/jso-tests/packets/20261001-165235-letter-d426/checker.txt, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- blind: no (my context held saved memory: a user profile, saved preferences and a memory file listing. The message and the packet were clean.)

## First take (Recruiter, first look)
She's an ER nurse manager who already knows our 34-minute number and cut her own wait from 38 to 22 minutes. She also has Epic, a budget and Spanish, so she goes on the call list. Fit: yes

## Verdict
Send. Rule 3: there are no must-fix findings.

## Must fix
None.

## Should fix
1. "Run daily operations for three clinics with 40 staff" (target line 7) · Fit · The job is three sites. The letter shows one department across "three shifts" (line 7) and never shows work across separate locations, so the hiring manager has to guess whether she can run three buildings. Direction: name any work across sites or units, if it exists.
2. "Lean or Six Sigma training" (target line 22) and "Lean Six Sigma Green Belt, 2023" (resume line 30) · Fit · The AI grader finds this on the resume, but the letter never connects it to the triage change in line 5, where it would add the most to the strongest result. Direction: tie the Green Belt to the split-flow change.
3. "I've spent the last seven years running the emergency department at Sonoran Valley Medical Center" (line 3) · Proof · The resume title is "Nurse Manager, Emergency Department." A healthcare hiring manager knows a nurse manager doesn't run the whole department, so "running the emergency department" sounds bigger than the title backs up. Direction: make the scope match the title.
4. "so patients who could sit in a chair never took a bed" (line 5) and "I'd explain discharge plans myself" (line 9) · Proof · All the proof uses ER terms: beds, discharges, a fast-track area. A primary care clinic runs on appointments and exam rooms, so the hiring manager has to work out for themselves how a fix built for the ER would cut their check-in-to-provider wait. Direction: say what the same move would look like at clinic check-in.
5. "It held through two winter surges because the charge nurses ran it on every shift." (line 5) · Proof · "Held" has no number behind it. A reader wants the wait figure after the surges, or a later year's average. Direction: give the number.
6. Line 3 "I'd like to bring", line 7 "that's the order I'd follow", line 9 "I'd explain", line 11 "I'd welcome" · Voice · The letter keeps reaching for the same "I'd" shape, and three paragraphs in a row end on it. "Your posting" also opens a clause twice (lines 3 and 9).

Cleared warnings: V01 at line 3 ("Oracle Road, Grant Road and Valencia") is three named clinics, and each one does work. V01 at line 7 ("built the schedule and hired the first eight nurses") lists specific actions with a number. The colon list in line 7 is a real sequence and sits before a list, which the rules allow.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume line 26 (BSN, 2011). Not in the letter. |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Letter line 3; resume line 10 (Nurse Manager since Mar 2019) and line 17 (Charge Nurse 2014 to 2019) |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7 ($4.1 million, under plan three years; built the fast-track schedule); resume lines 13 and 14 |
| Working knowledge of Epic or a similar electronic health record | Must-have | Shown | Letter line 7 (2020 go-live); resume line 15 (Epic ASAP go-live, 140 staff trained) |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5 (38 to 22 minutes); resume line 12 |
| Fluent in English and Spanish | Preferred | Shown | Letter line 9 (how she uses it now); resume line 33 |
| Lean or Six Sigma training | Preferred | Shown on the resume only | Resume line 30 |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7 (six-bed fast-track area, 2021); resume line 14 |

## What I couldn't judge
- The 38 to 22 minute drop in 2022, and whether it really held through "two winter surges."
- The $4.1 million staffing budget closed under plan in 2023, 2024 and 2025.
- The 52-person team, the 38-bed department and the 61,000 visits a year (resume).
- The 2020 Epic ASAP go-live, the 140 staff trained, and how much of that went into the fast-track workflows.
- Spanish fluency, which the reader can only test in an interview.
- "the wait is the first thing every patient judges us on" (line 3): a broad claim with nothing behind it.
- The resume shows no role from Sep 2013 to Jun 2014. A reader may ask about it. The letter doesn't raise it and doesn't need to.
- Her budget is a staffing budget. The posting's $6.2 million is an operating budget. A hiring manager may ask whether she has owned spending beyond payroll.

Nothing from this run needs saving to memory.
````

## Grade (keys/a-clean.md)

- **Pass**: Verdict: Send
  - Quote: “Send. Rule 3: there are no must-fix findings.”
- **Pass**: First take ends Fit: yes
  - Quote: “so she goes on the call list. Fit: yes”
- **Pass**: Must fix: none
  - Quote: “## Must fix ⏎ None.”
- **Pass**: Should-fix findings quote the piece
  - Quote: “"I've spent the last seven years running the emergency department at Sonoran Valley Medical Center" (line 3)”
  - Quote: “"so patients who could sit in a chair never took a bed" (line 5)”
  - Quote: “"It held through two winter surges because the charge nurses ran it on every shift." (line 5)”
- **Pass, as cleared warnings**: List-of-three warnings on “Oracle Road, Grant Road and Valencia” and “I built the schedule and hired the first eight”
  - Quote: “V01 at line 3 ("Oracle Road, Grant Road and Valencia") is three named clinics, and each one does work.”
  - Quote: “V01 at line 7 ("built the schedule and hired the first eight nurses") lists specific actions with a number.”
- **Pass**: All five must-haves shown (degree in resume; five years and Epic in both; schedules, budget, wait times in letter)
  - Quote: “| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume line 26 (BSN, 2011). Not in the letter. |”
  - Quote: “| Working knowledge of Epic or a similar electronic health record | Must-have | Shown | Letter line 7 (2020 go-live); resume line 15”
  - Quote: “| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5 (38 to 22 minutes); resume line 12 |”
- **Pass**: Preferred: Spanish and Lean Six Sigma show; new site in part through the fast-track area
  - Quote: “| Fluent in English and Spanish | Preferred | Shown”
  - Quote: “| Lean or Six Sigma training | Preferred | Shown on the resume only | Resume line 30 |”
  - Quote: “| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7 (six-bed fast-track area, 2021)”

Notes:

- The key expects the two list-of-three warnings. The reviewer handled both, but cleared them with reasons instead of listing them as should-fix. That fits its rules for cleared warnings, so I count it as met.
- Should fix 2 quotes the posting and the resume, not the letter. It's a fit finding about something the letter leaves out, so there's no letter line to quote. Not a fail.
- No must-fix finding, so the seeded letter's base needs no change.

**Result: Pass**
