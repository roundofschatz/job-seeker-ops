# Test 8: The same verdict three times

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

- Packet: the test 7 packet, `/home/claude/jso-tests/packets/20261001-165236-letter-93dc`. Run 1 is the test 7 review (agent `ace09bea07ce3f22e`); runs 2 and 3 are new reviewers started at the same time with the same printed line.

## Run 1

The run 1 report is saved word for word in `07-seeded.md` and repeated here so this file holds all three.

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter); target.txt (the target: Clinic Operations Manager posting, Juniper Ridge Health Partners); companion-1.txt (resume the reader also sees); checker.txt (plainspeak-writer checker output, surface letter, exit code 1); manifest.md (the manifest)
- Voice rules: plainspeak-writer 1.3, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Also in my context: saved memory (a user profile, saved preferences, a memory file listing), the account email address, and memory-tool instructions in my system prompt
- Files I opened: /home/claude/jso-tests/packets/20261001-165236-letter-93dc/manifest.md; /home/claude/jso-tests/packets/20261001-165236-letter-93dc/piece.txt; /home/claude/jso-tests/packets/20261001-165236-letter-93dc/target.txt; /home/claude/jso-tests/packets/20261001-165236-letter-93dc/companion-1.txt; /home/claude/jso-tests/packets/20261001-165236-letter-93dc/checker.txt; /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- blind: no (my context held saved memory: a profile, preferences and a memory listing, plus the account email. I used none of it. The message and the packet were clean, and no file in the packet leaked.)

## First take (Recruiter, first look)
She's an emergency department nurse manager who cut wait time from 38 to 22 minutes, runs a $4.1 million budget and speaks Spanish, so she matches the core of this clinic role. The generic first line costs her a few seconds, but the number in the second paragraph keeps me reading. Fit: yes

## Verdict
Fix first. Rule 2 set it: there are five must-fix findings, which falls in the one-to-five range.

## Must fix
1. "By December the average was 22 minutes — down by 16." (line 5) · Voice · The checker flags this as a HARD hit (R01, em dash). Direction: use a period or comma.
2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · The checker flags this as a HARD hit (R02, "not just X but Y"). The sentence also closes the paragraph with a summary claim that has no proof behind it, right after a paragraph that had real numbers. Direction: cut the line, or name what changed in the department and give the figure.
3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first" (line 7) · Voice (also Clarity) · This is a coined internal method name, which the rules file blocks. The hiring manager has never heard of "Q-Ladder," and the resume doesn't mention it either, so it reads as a label they can't check. Direction: say what the method does in plain words and drop the name.
4. "Since becoming nurse manager in 2017" (line 7) vs. resume "Nurse Manager, Emergency Department | Mar 2019 - Present" and "Charge Nurse, Emergency Department | Jun 2014 - Feb 2019" (companion lines 10, 17) · Risk · The letter and the resume give different years for the same title. A hiring manager who spots this will doubt every other date and number. Direction: make the letter match the resume.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · This names a gap outright, starts an exit story and apologizes, all in a paragraph by itself. The reader may not have noticed the nine months between Sep 2013 and Jun 2014 on the resume, and now they will. The line also promises an explanation that never comes. Direction: cut the line.

## Should fix
1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · This could go to any employer unchanged. It's also the line a recruiter reads first. Nowhere does the letter name Oracle Road, Grant Road or Valencia, primary care, the 40 staff, or the posting's 34-minute wait (target lines 4 and 10). Line 15's "evening launch" is the only tie to this firm. A hiring manager has to work out alone how an ED result maps onto three primary care clinics. Direction: open on their 34-minute wait or the three-clinic evening launch, and tie the 38-to-22 result to it.
2. "I'm known across the hospital as a leader people want to work for." (line 9) · Proof · This is a reputation label the reader can't check, and nothing near it backs it up, such as a retention or vacancy figure. Direction: give the number behind it, or cut the line.
3. "In 2022 our door-to-provider time averaged 38 minutes." (line 5) · Clarity · "Our" points to a department and hospital the letter never names. A reader of the letter alone learns that she works in an emergency department, and where, only from the resume. Direction: name Sonoran Valley's emergency department where the number first appears.
4. "I know what it takes to keep the room calm when the waiting area is full." (line 9) · Voice · The checker flags this as a WARN (R44, vague place). "The room" isn't the waiting area the sentence names, and "what it takes" names no action or result. Direction: name the place and what she does there, or cut the line.
5. "which I have long admired" (line 3) · Voice · The checker flags this as a WARN (R41, uncontracted form). Nothing is gained by the emphasis. Direction: contract it, or let it go when line 3 is reworked.

Cleared warnings: P10 "just" (line 5) is part of the R02 hit and goes when that line is fixed. Both V01 lists on line 7 pass because each item is specific (52 staff, three shifts, $4.1 million; built the schedule, hired eight nurses). V04 staccato passes because only 3 of the 7 body paragraphs are one sentence, and the checker's count of 5 of 9 includes the greeting and the sign-off.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume line 26 (BSN, 2011). Not in the letter. |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Resume lines 10 and 17 (charge nurse from 2014, nurse manager from 2019). Letter line 7, but its 2017 date conflicts with the resume. |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7 ($4.1M under plan for three years; built the fast-track schedule). Resume lines 13 and 14. |
| Working knowledge of Epic or a similar EHR | Must-have | Shown | Letter line 7. Resume line 15 (led the 2020 Epic ASAP go-live, trained 140 staff). |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5 (38 to 22 minutes). Resume line 12. |
| Fluent in English and Spanish | Preferred | Shown | Letter line 13 (explains discharge plans herself). Resume lines 5 and 33. |
| Lean or Six Sigma training | Preferred | Shown | Resume line 30 (Green Belt, 2023). Not in the letter. |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7 (six-bed fast-track area, 2021). Resume line 14. |

## What I couldn't judge
- Which nurse manager start date is right, 2017 or March 2019.
- The cut from 38 to 22 minutes door-to-provider in 2022, and whether 22 held after December.
- The $4.1 million staffing budget closed under plan in 2023, 2024 and 2025.
- 52 nurses and technicians across three shifts, the 38-bed department and 61,000 visits a year.
- That she set up the Epic workflows and trained 140 staff in the 2020 go-live.
- What "Q-Ladder" is, and whether anyone outside her department uses it.
- "Known across the hospital as a leader people want to work for."
- Spanish fluency at the level of explaining discharge plans to patients.
- The Lean Six Sigma Green Belt (2023) and CEN (2016).

Nothing from this review is worth saving to memory.
````

## Run 2

- Packet folder: `/home/claude/jso-tests/packets/20261001-165236-letter-93dc`
- Reviewer agent id: `ab8f13fac2455fb94`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 16:52.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,503 | 268 |
| target.txt | The target: the job posting, or the reader's own words | 1,430 | 234 |
| companion-1.txt | A companion the real reader also sees | 1,569 | 260 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 1,325 | 215 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.3. Rules file: /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Checker: Ran with surface letter, exit code 1.
````

### Exact message sent

````
Review the packet in /home/claude/jso-tests/packets/20261001-165236-letter-93dc. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-93dc/manifest.md"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-93dc/piece.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-93dc/target.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-93dc/companion-1.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-93dc/checker.txt"}
Read {"file_path": "/root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md"}
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece, a cover letter); target.txt (the job posting, Clinic Operations Manager at Juniper Ridge Health Partners); companion-1.txt (the resume sent with the letter, which the reader also sees); checker.txt (plainspeak-writer 1.3 checker output, surface letter, exit code 1); manifest.md
- Voice rules: plainspeak-writer 1.3, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Also in my context: saved memory (a user profile, saved preferences and a memory file listing), plus the account email. I didn't use any of it in a finding.
- Files I opened:
  - /home/claude/jso-tests/packets/20261001-165236-letter-93dc/manifest.md
  - /home/claude/jso-tests/packets/20261001-165236-letter-93dc/piece.txt
  - /home/claude/jso-tests/packets/20261001-165236-letter-93dc/target.txt
  - /home/claude/jso-tests/packets/20261001-165236-letter-93dc/companion-1.txt
  - /home/claude/jso-tests/packets/20261001-165236-letter-93dc/checker.txt
  - /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Leaks in the packet: none. The only companion is the resume.
- blind: no (my context held saved memory: a user profile, saved preferences and a memory listing, plus the account email)

## First take (Recruiter, first look)
This is an ER nurse manager who cut wait times from 38 to 22 minutes, runs 52 staff and a $4.1 million budget, and led an Epic go-live. That's close to what this posting asks for, though the opening line could go to any employer. Fit: yes

## Verdict
Fix first. Rule 2: there are five must-fix findings (one to five).

## Must fix
1. "By December the average was 22 minutes — down by 16." (line 5) · Voice · Checker HARD hit R01, em dash. Direction: use a period or a comma.
2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · Checker HARD hit R02, "not just X but Y." The second half is also an abstraction: "how the whole department runs" names no change a reader can check. Direction: say what changed in the department, or cut the line.
3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first" (line 7) · Voice and Clarity · This is an internal method name, which the rules file blocks. No reader knows what the Q-Ladder is. It isn't on the resume either, so the hiring manager can't connect it to anything. Direction: describe what the sorting does in plain words, or cut the name.
4. Letter: "Since becoming nurse manager in 2017" (line 7). Resume: "Nurse Manager, Emergency Department | Mar 2019 - Present" and "Charge Nurse, Emergency Department | Jun 2014 - Feb 2019" (companion lines 10 and 17) · Risk · The letter and resume give different start dates for the same title. A hiring manager reading both will wonder which one is true and whether other figures are inflated too. Direction: make the date match the resume.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · This names a gap outright and adds an exit story. The letter then never explains it, so the reader keeps only the gap. Direction: cut the line.

## Should fix
1. Target: "Run daily operations for three clinics with 40 staff, including medical assistants, nurses and front desk teams." Letter: "I'd explain discharge plans myself, the way I do now" (line 13) · Fit · Every example comes from one hospital emergency department. The letter never shows how that work carries over to three primary care clinics. "Discharge plans" is a hospital term, which makes the mismatch more visible. A hiring manager will ask whether she has run anything outside the ED or across sites. Direction: tie the ED work to clinic visits and to more than one site.
2. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · This opening could go to any employer unchanged, and it's the line the recruiter reads first. The letter never uses the posting's own facts, such as the 34-minute wait, the 40 staff, the $6.2 million budget or the three named clinics. Her 38-to-22 result maps directly onto the 34-minute problem, but the letter never links them. Direction: open on Juniper Ridge's wait number and her result against it.
3. "I'm known across the hospital as a leader people want to work for." (line 9) · Proof · This is a label a reader can't check. It doesn't land on a name, a number or a result. Direction: give a retention, vacancy or survey figure, or cut the line.
4. "In 2022 our door-to-provider time averaged 38 minutes." (line 5) · Clarity · "Our" refers to a department the letter never names. Also, if all of 2022 averaged 38 minutes, the reader can't tell when the 22-minute December fell. Direction: name the hospital and department, and give the starting point as a period before the change.
5. "which I have long admired" (line 3) · Voice · Checker WARN R41: the uncontracted form where speech would contract. Direction: contract it, or cut it along with the rest of the generic opener.
6. Past the fifth: line 9, Voice, checker WARN R44 on "keep the room calm". "The room" isn't the waiting area the sentence names, so the place isn't built. Whole letter, Voice, checker WARN V04: "5 of 9 paragraphs are one sentence" (lines 3, 11, 13 and 15 among them), which reads choppy.

Cleared warnings: P10 "just" on line 5 is part of the R02 hit and is counted there. Both V01 lists of three on line 7 pass because each item is specific (52 staff, three shifts, $4.1 million; built the schedule, hired eight nurses).

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume: BSN, Saguaro State University, 2011. Not in the letter. |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Resume: charge nurse from 2014, nurse manager from 2019. The letter's 2017 date conflicts with this (Must fix 4). |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7: $4.1 million budget closed under plan, schedule built for fast-track. Resume lines 13 and 14. |
| Working knowledge of Epic or a similar electronic health record | Must-have | Shown | Letter line 7: 2020 go-live. Resume line 15: led the Epic ASAP go-live, trained 140 staff. |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5 and resume line 12: 38 to 22 minutes. |
| Fluent in English and Spanish | Preferred | Shown | Letter line 13, with how she uses it. Resume Languages section. |
| Lean or Six Sigma training | Preferred | Shown | Resume only: Lean Six Sigma Green Belt, 2023. The letter doesn't mention it. |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7 and resume line 14: six-bed fast-track area, 2021. |

## What I couldn't judge
- The 38-to-22-minute cut in door-to-provider time, and when in 2022 it happened.
- The $4.1 million staffing budget closed under plan in 2023, 2024 and 2025.
- The 52 nurses and technicians, and the 61,000 visits a year.
- Which nurse manager start date is right: 2017 (letter) or March 2019 (resume).
- Whether the Q-Ladder is a real, documented process.
- "Known across the hospital as a leader people want to work for." Nothing on the page supports it.
- The 2020 Epic go-live and the 140 staff trained.
- Spanish fluency and the Lean Six Sigma Green Belt. A reader may want proof of both.
- How long the 2013 to 2014 gap lasted. The resume shows September 2013 to June 2014.

Nothing from this run needs saving to memory.
````

## Run 3

- Packet folder: `/home/claude/jso-tests/packets/20261001-165236-letter-93dc`
- Reviewer agent id: `aaf9262da31fe5776`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 16:52.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,503 | 268 |
| target.txt | The target: the job posting, or the reader's own words | 1,430 | 234 |
| companion-1.txt | A companion the real reader also sees | 1,569 | 260 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 1,325 | 215 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.3. Rules file: /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Checker: Ran with surface letter, exit code 1.
````

### Exact message sent

````
Review the packet in /home/claude/jso-tests/packets/20261001-165236-letter-93dc. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-93dc/manifest.md"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-93dc/piece.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-93dc/target.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-93dc/companion-1.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-93dc/checker.txt"}
Read {"file_path": "/root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md"}
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the manifest); piece.txt (the piece, a cover letter); target.txt (the target, a job posting for Clinic Operations Manager at Juniper Ridge Health Partners); companion-1.txt (a companion the reader also sees: the candidate's resume); checker.txt (plainspeak-writer checker output, surface letter, exit code 1)
- Voice rules: plainspeak-writer 1.3, tells.md, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Also in my context: saved user memory (a profile, saved preferences and a list of memory files), account context (the user's email address), and session instructions about git commit attribution. I didn't use any of it in a finding.
- Files I opened:
  - /home/claude/jso-tests/packets/20261001-165236-letter-93dc/manifest.md
  - /home/claude/jso-tests/packets/20261001-165236-letter-93dc/piece.txt
  - /home/claude/jso-tests/packets/20261001-165236-letter-93dc/target.txt
  - /home/claude/jso-tests/packets/20261001-165236-letter-93dc/companion-1.txt
  - /home/claude/jso-tests/packets/20261001-165236-letter-93dc/checker.txt
  - /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- blind: no (my context held saved user memory: a profile, preferences and a memory file listing. The message and the packet were clean, and the packet had no leaks.)

## First take (Recruiter, first look)
An emergency department nurse manager in Tucson who cut door-to-provider time from 38 to 22 minutes, runs a $4.1 million budget and speaks Spanish. That fits a role built around cutting wait times, though the opening line is boilerplate and the real hook doesn't come until the second paragraph. Fit: yes

## Verdict
Fix first. Rule 2: there are five must-fix findings (one to five), the first take is Fit: yes, and no must-have requirement is missing.

## Must fix
1. "By December the average was 22 minutes — down by 16." (line 5) · Voice (checker HARD, R01 em dash) · The em dash is a block in the voice rules. Direction: use a period or comma.
2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice (checker HARD, R02 "not just X but Y") · This is a blocked construction. It's also a summary line closing the paragraph, and it names no result. A hiring manager learns nothing new from it. Direction: state the department-wide change and what it produced, or cut the line.
3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first." (line 7) · Voice (block: internal method name), also Clarity · The reader has never heard of "Q-Ladder." A coined name sends them looking for something they can't find, and it's on the voice rules' block list. Direction: describe what the method does in plain words and drop the name.
4. "Since becoming nurse manager in 2017, I've managed 52 nurses..." (line 7) against the resume's "Nurse Manager, Emergency Department | Mar 2019 - Present" and "Charge Nurse, Emergency Department | Jun 2014 - Feb 2019" · Risk · The letter and the resume disagree on when she became nurse manager. A hiring manager or background check will catch a two-year difference, and it makes the other figures look shaky too. Direction: make the year match the resume.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · This names a gap outright, tells an exit story and apologizes, all in one line. It shows the reader a disqualifier they may not have looked for, and then never explains it. Direction: cut the line.

## Should fix
1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · This line could go to any employer unchanged. It's also the recruiter's first ten seconds, and it uses them on boilerplate. Nothing in it is specific to Juniper Ridge: not the three clinics, not the evening hours, not the 34-minute wait. Direction: open on the 38-to-22 result or on the posting's wait problem, and drop the admiration line.
2. "In 2022 our door-to-provider time averaged 38 minutes. I moved triage to a split-flow model, so patients who could sit in a chair never took a bed." (line 5) · Proof · The result comes from an emergency department with beds. The posting asks to cut the "check-in to seeing a provider" wait in primary care clinics, which is "now 34 minutes." The letter never connects the two, so a hiring manager has to work out for themselves whether the method carries over. Direction: tie the result to the clinic's check-in-to-provider measure.
3. "I'm known across the hospital as a leader people want to work for. I know what it takes to keep the room calm when the waiting area is full." (line 9) · Proof · A reader can't check either claim. No retention figure, turnover number or named result backs them, and the paragraph sits between two paragraphs full of numbers. Direction: give the number that proves it, or cut the paragraph.
4. "I have long admired" (line 3) · Voice (checker WARN, R41) · This is an uncontracted form where speech would contract, and it isn't there for emphasis. Direction: contract it, or cut the clause per Should fix 1.
5. "keep the room calm" (line 9) · Voice (checker WARN, R44 vague place) · It's unclear which room is meant. The waiting area is named in the same sentence, so "the room" seems to be some other place. Direction: name the place.
6. Line 0 · Voice (checker WARN, V04 staccato layout) · "5 of 9 paragraphs are one sentence".

Cleared warnings: P10 "just" (line 5) sits inside the R02 hit in Must fix 2 and goes when that's fixed. V01 list of three (line 7, both hits): each item is specific (52 staff, three shifts, $4.1 million; built the schedule, hired eight nurses).

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| "Bachelor's degree in nursing, health administration or a related field." | Must-have | Shown | Resume: BSN, Saguaro State University, 2011. Not in the letter. |
| "Five or more years in clinical operations or nurse leadership." | Must-have | Shown | Resume: Charge Nurse from 2014, Nurse Manager from 2019. Letter line 7, but its 2017 date conflicts with the resume (Must fix 4). |
| "Experience managing staff schedules and a budget for a unit or clinic." | Must-have | Shown | Letter line 7 ($4.1M budget, fast-track schedule). Resume. |
| "Working knowledge of Epic or a similar electronic health record." | Must-have | Shown | Letter line 7 (2020 go-live). Resume (Epic ASAP go-live, 140 staff trained). |
| "A record of improving patient wait times or throughput." | Must-have | Shown | Letter line 5 (38 to 22 minutes). Resume. |
| "Fluent in English and Spanish." | Preferred | Shown | Letter line 13, with a working example. Resume, Languages. |
| "Lean or Six Sigma training." | Preferred | Shown | Resume only (Lean Six Sigma Green Belt, 2023). Not in the letter. |
| "Experience opening a new clinic site or service." | Preferred | Shown | Letter line 7 (six-bed fast-track area, 2021). Resume. |

## What I couldn't judge
- The 38-to-22-minute drop in door-to-provider time in 2022, and whether it held after December.
- The $4.1 million staffing budget closed under plan in 2023, 2024 and 2025.
- 52 nurses and technicians across three shifts. The resume also gives a 38-bed department and 61,000 visits a year.
- Which nurse manager start date is right, 2017 (letter) or March 2019 (resume).
- The six-bed fast-track opening in 2021 and the eight nurses hired for it.
- Leading the 2020 Epic go-live and training 140 staff (resume).
- "Known across the hospital as a leader people want to work for."
- Spanish fluency, and the claim that she explains discharge plans herself today.
- The length of the 2013 to 2014 gap. The resume shows Sep 2013 to Jun 2014.

Nothing from this review needs saving to the user's memory.
````

## Grade (keys/a-seeded.md)

### The three must-fix lists side by side

| Must-fix | Run 1 (test 7) | Run 2 | Run 3 |
|---|---|---|---|
| “22 minutes — down by 16” | 1 · Voice (R01) | 1 · Voice (R01) | 1 · Voice (R01) |
| “wasn't just a triage fix but” | 2 · Voice (R02) | 2 · Voice (R02) | 2 · Voice (R02) |
| “Q-Ladder” | 3 · Voice (also Clarity) | 3 · Voice and Clarity | 3 · Voice (block), also Clarity |
| “Since becoming nurse manager in 2017” vs resume Mar 2019 | 4 · Risk | 4 · Risk | 4 · Risk |
| “I was out of work for most of a year” | 5 · Risk | 5 · Risk | 5 · Risk |
| Verdict | Fix first | Fix first | Fix first |
| First take | Fit: yes | Fit: yes | Fit: yes |

- **Pass**: All three verdicts the same
  - Decided by the check or the lines noted in this file, outside the report.
- **Pass**: Must-fix lists name the same problems: same quoted words under the same checks
  - Decided by the check or the lines noted in this file, outside the report.

### Run 2 against the test 7 conditions

- **Pass**: Verdict Fix first
  - Quote: “Fix first.”
- **Pass**: First take ends Fit: yes
  - Quote: “Fit: yes”
- **Pass**: Flaw 1 (dash) is must-fix, quoted, checker R01
  - Quote: “1. "By December the average was 22 minutes — down by 16." (line 5) · Voice”
- **Pass**: Flaw 2 (not just X but Y) is must-fix, quoted, checker R02
  - Quote: “2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice”
- **Pass**: Flaw 4 (Q-Ladder) is must-fix, Voice
  - Quote: “3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first”
- **Pass**: Flaw 8 (2017 vs Mar 2019) is must-fix, Risk
  - Quote: “Since becoming nurse manager in 2017”
  - Quote: “Nurse Manager, Emergency Department | Mar 2019 - Present”
- **Pass**: Flaw 7 (gap) is must-fix, Risk
  - Quote: “5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk”
- **Pass**: No other finding is must-fix (exactly five)
  - Quote: “five must-fix findings”
- **Pass**: Flaw 6 (any-firm opening) is should-fix, Proof
  - Quote: “2. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof”
- **Pass**: Flaw 3 (claim with no proof) is should-fix, Proof
  - Quote: “3. "I'm known across the hospital as a leader people want to work for." (line 9) · Proof”
- **Pass**: Flaw 5 (vague place) is should-fix, Voice R44 (one-line entry past the fifth)
  - Quote: “6. Past the fifth: line 9, Voice, checker WARN R44 on "keep the room calm".”
- **Pass**: No finding supplies replacement wording or a sample sentence
  - Decided by the check or the lines noted in this file, outside the report.

### Run 3 against the test 7 conditions

- **Pass**: Verdict Fix first
  - Quote: “Fix first.”
- **Pass**: First take ends Fit: yes
  - Quote: “Fit: yes”
- **Pass**: Flaw 1 (dash) is must-fix, quoted, checker R01
  - Quote: “1. "By December the average was 22 minutes — down by 16." (line 5) · Voice”
- **Pass**: Flaw 2 (not just X but Y) is must-fix, quoted, checker R02
  - Quote: “2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice”
- **Pass**: Flaw 4 (Q-Ladder) is must-fix, Voice
  - Quote: “3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first”
- **Pass**: Flaw 8 (2017 vs Mar 2019) is must-fix, Risk
  - Quote: “Since becoming nurse manager in 2017”
  - Quote: “Nurse Manager, Emergency Department | Mar 2019 - Present”
- **Pass**: Flaw 7 (gap) is must-fix, Risk
  - Quote: “5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk”
- **Pass**: No other finding is must-fix (exactly five)
  - Quote: “five must-fix findings”
- **Pass**: Flaw 6 (any-firm opening) is should-fix, Proof
  - Quote: “1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof”
- **Pass**: Flaw 3 (claim with no proof) is should-fix, Proof
  - Quote: “3. "I'm known across the hospital as a leader people want to work for. I know what it takes to keep the room calm when the waiting area is full." (line 9) · Proof”
- **Pass**: Flaw 5 (vague place) is should-fix, Voice R44
  - Quote: “5. "keep the room calm" (line 9) · Voice (checker WARN, R44 vague place)”
- **Pass**: No finding supplies replacement wording or a sample sentence
  - Decided by the check or the lines noted in this file, outside the report.

Notes:

- The should-fix lists differ, which the key allows. Run 2 added a fit finding on ED versus three clinics; run 3 added a proof finding on the same gap.
- Run 3's Should fix 6 reads “Line 0 · Voice (checker WARN V04 staccato layout)” with no Direction. “Line 0” comes straight from the checker's output for a whole-letter warning. It's harmless here but reads oddly to a person.

**Result: Pass**
