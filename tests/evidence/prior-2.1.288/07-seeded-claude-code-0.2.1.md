# Test 7: Seeded flaws (Claude Code, 0.2.1)

## Run

- Date: 2026-10-06
- Product, plugin, script and working folder: as in `01-isolation-claude-code-0.2.1.md`. Claude Code 2.1.288 in the Code tab of the Claude desktop app on Windows 11, job-seeker-ops 0.2.1 installed, plainspeak-writer 1.5 installed as a skill, and the session in the job-seeker-ops repository.
- The reviewer was started as `job-seeker-ops:submission-reviewer` with the Agent tool, with the printed line and nothing else, at the same time as the test 1 reviewer. Its transcript shows the account email and the git snapshot in its context.
- The report below was copied by script from the reviewer's own hand-back call in its transcript, word for word.
- The Windows user name in each path is written as `<user>`, inside the report too. Nothing else in it was changed.
- In the grades, “ and ” mark quotes, and a finding's quote of the letter and its label are given separately.
- The key, `keys/a-seeded.md`, was opened after this review had finished.

## Build

Run from the repository folder, `C:\Users\<user>\repos\tools\job-seeker-ops`, as RUN-TESTS.md gives it:

````
python SCRIPT --type letter --piece tests/writers/a-quintero/letter-seeded.txt --target tests/writers/a-quintero/posting.txt --companion tests/writers/a-quintero/resume.txt --channel upload --out jso-tests/packets
````

Script output:

````
Packet: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002532-letter-9a13
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002532-letter-9a13. Read manifest.md first.
````

As with test 1, that manifest said "Voice rules: not found. Voice is unchecked." The script doesn't look in the folder where the desktop app keeps uploaded skills; `01-isolation-claude-code-0.2.1.md` has the detail. No reviewer was started on that packet. Following submission-review's SKILL.md, it was built again with `--voice-dir` pointing at the installed plainspeak-writer:

````
python SCRIPT --type letter --piece tests/writers/a-quintero/letter-seeded.txt --target tests/writers/a-quintero/posting.txt --companion tests/writers/a-quintero/resume.txt --channel upload --voice-dir "C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\plainspeak-writer" --out jso-tests/packets
````

Script output:

````
Packet: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961. Read manifest.md first.
````

## Test 7 review

- Packet folder: `C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961`
- `piece.txt` in the packet: 1,506 bytes, SHA-256 `9E4923D9743C533F6E3F0AAAFA3764F436F91CE6425470A94F6371EA1223ED07`, the same bytes as `tests\writers\a-quintero\letter-seeded.txt`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.2.1 on 2026-10-06 at 00:27.

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

### Checker output in the packet (checker.txt)

````
plainspeak-writer 1.5 checker output for piece.txt, surface letter, exit code 1 (0 means no HARD hits, 1 means at least one).

check_voice 1.5   surface: letter

=== C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\piece.txt ===
Words: 268
HARD FAIL (2):
  L5: [R01 em dash or other dash] "—": no dash of any kind, and no double hyphen or spaced hyphen typed as one; a period, comma, colon, or semicolon
  L5: [R02 negative corollary] "wasn't just": state the positive claim directly
WARN (3), each cleared by a named decision or fixed:
  L9: [R44 the vague place] "the room": a real, named place, or one the sentence itself just built
  L0: [V06 short flat line after a long one (rate)] "2 in 268 words, 7.5 per 1,000, where 9 in 10 pieces of edited human writing stay at or under 5: "In 2022 our door-to-provider time averaged 38 minutes.", "Your posting asks for Spanish, and I'm fluent."": fold the point into the long sentence, or cut the short line if it only restates it
  L0: [V04 staccato layout] "5 of 9 paragraphs are one sentence": join one-line paragraphs into paragraphs that finish a thought

RESULT: FAIL: hard violations present.
````

plainspeak-writer 1.5's checker still lists R01 and R02 under HARD, so flaws 1 and 2 stay must-fix under the key.

### Exact message sent

````
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\manifest.md
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\piece.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\target.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\companion-1.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\checker.txt
Read C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
Read C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
SubagentHandback (the harness's delivery call, holding the report or reply)
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the manifest); piece.txt (the piece, a cover letter); target.txt (the target, a job posting for Clinic Operations Manager at Juniper Ridge Health Partners); companion-1.txt (the resume sent with the letter, which the reader also sees); checker.txt (plainspeak-writer checker output, surface letter, exit code 1)
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md. Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Also in my context: an account email, and a git snapshot (branch, git user name, recent commit titles) that says nothing about this piece
- Files I opened:
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\manifest.md
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\piece.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\target.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\companion-1.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002718-letter-5961\checker.txt
  - the tells.md and full-check.md paths above
- blind: yes

## First take (Recruiter, first look)
This is an emergency department nurse manager who cut a wait from 38 to 22 minutes, applying to run three clinics whose wait times are the top patient complaint. The opening line says nothing, but the second paragraph makes the fit plain. Fit: yes

## Verdict
Fix first. Rule 2 applies: there are five must-fix findings, which falls in the one-to-five range, and the first take ends Fit: yes.

## Must fix
1. "By December the average was 22 minutes — down by 16." (line 5) · Voice · Checker HARD hit R01 (em dash). It falls in the strongest paragraph of the letter. Direction: use a period or comma, and cut "down by 16" if it only restates the math.
2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · Checker HARD hit R02 ("not just X, but Y"). The line also closes the paragraph with a summary claim that nothing in the letter backs up. A hiring manager reads "how the whole department runs" as a bigger claim than the facts before it support. Direction: state what changed in the department and give the fact, or cut the line.
3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first." (line 7) · Voice and Clarity · This is an internal method name, which the full check lists under its blocks. No reader outside her department knows what the Q-Ladder is. A clinical hiring manager may also wonder how a personal method fits alongside standard triage acuity scoring. The resume doesn't mention it, so the grader can't connect it to anything. Direction: describe what the method does in plain words, or cut the name.
4. "Since becoming nurse manager in 2017" (line 7) vs resume "Nurse Manager, Emergency Department | Mar 2019 - Present" and "Charge Nurse, Emergency Department | Jun 2014 - Feb 2019" · Risk · The letter and resume give different years for the same title. A reader who checks one against the other will doubt both, and the five-years-of-leadership requirement depends on this date. Direction: make the year match the resume.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · The letter names the gap outright and apologizes for it, then never explains it. A roughly nine-month gap twelve years ago that most readers would never notice is now a paragraph of its own, between her best proof and her Spanish. Direction: cut the paragraph.

## Should fix
1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · This line could go to any employer unchanged, and it's the first thing the recruiter reads. "Long admired" and "commitment to patients" name nothing about Juniper Ridge. Direction: open on their wait, their three clinics or the evening launch.
2. "In 2022 our door-to-provider time averaged 38 minutes." (line 5) with target "Cut the average wait from check-in to seeing a provider, now 34 minutes" and "runs three primary care clinics" · Proof · The letter never connects her emergency department result to their 34-minute clinic wait, and never says how ED work carries over to three outpatient sites. The hiring manager has to make both connections alone. Her budget is "a $4.1 million staffing budget" (line 7), while the posting asks her to "Own the clinics' $6.2 million operating budget". The letter leaves that gap in scope and type unaddressed too. Direction: tie her 38-to-22 result to their 34 and say what transfers to a multi-site clinic.
3. "I'm known across the hospital as a leader people want to work for. I know what it takes to keep the room calm when the waiting area is full." (line 9) · Proof · Neither line points to a name, a number or a result, so a hiring manager can't check either one. Direction: give a retention, turnover or survey figure, or cut the paragraph.
4. "keep the room calm" (line 9) · Voice · Checker WARN R44 (vague place). Readers have to guess which room is meant. Direction: name the place or cut it with the line above.
5. "In 2022 our door-to-provider time averaged 38 minutes." and "Your posting asks for Spanish, and I'm fluent." (whole piece) · Voice · Checker WARN V06. The rate of short flat lines after long ones is 7.5 per 1,000 words, above the 5 limit. Direction: fold each short line into the sentence next to it.
6. (whole piece) · Voice · Checker WARN V04, "5 of 9 paragraphs are one sentence" (lines 3, 11, 15 among them). The letter reads as a stack of separate statements.

Cleared warnings: none.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume line 26 (BSN, 2011). The letter doesn't mention it. |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Letter line 7, resume lines 10 and 17. The start year conflicts (2017 vs 2019), see Must fix 4. |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7 ($4.1 million, under plan three years; built fast-track schedule), resume lines 13-14 |
| Working knowledge of Epic or a similar electronic health record | Must-have | Shown | Letter line 7, resume line 15 (2020 go-live, 140 staff trained) |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5, resume line 12 (38 to 22 minutes) |
| Fluent in English and Spanish | Preferred | Shown | Letter line 13 (explains discharge plans herself), resume line 33 |
| Lean or Six Sigma training | Preferred | Shown | Resume line 30 (Green Belt, 2023). The letter doesn't mention it. |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7, resume line 14 (six-bed fast-track area, 2021) |

## What I couldn't judge
- Whether she became nurse manager in 2017 or 2019.
- The 38-to-22-minute result in 2022, and whether ED door-to-provider time is measured the way the clinics measure check-in to provider.
- 52 nurses and technicians, the $4.1 million staffing budget closed under plan in 2023, 2024 and 2025, and how much of a $6.2 million operating budget she has run outside staffing.
- The 2020 Epic go-live, the 140 staff trained, and the eight nurses hired for the 2021 fast-track area.
- What the Q-Ladder is, and whether a nurse manager personally "sorted every new patient" with it.
- "I'm known across the hospital as a leader people want to work for": nothing in the packet backs it.
- Spanish fluency: no certification is named, and I can't tell whether Juniper Ridge would let her explain discharge plans without the interpreter line.
````

## Grade (keys/a-seeded.md)

Every quote of the letter, the posting and the resume in the report was checked against the packet's files by script. Each one is there word for word, apart from a capital at the start of a sentence.

- **Pass**: Verdict Fix first
  - Quote: “Fix first. Rule 2 applies: there are five must-fix findings, which falls in the one-to-five range, and the first take ends Fit: yes.”
- **Pass**: First take ends `Fit: yes`
  - Quote: “The opening line says nothing, but the second paragraph makes the fit plain. Fit: yes”
- **Pass**: Flaw 1 (the dash) is must-fix, quoted, checker R01
  - Must-fix 1 quotes: “By December the average was 22 minutes — down by 16.”
  - Its label: “Voice · Checker HARD hit R01 (em dash).”
- **Pass**: Flaw 2 ("not just X but Y") is must-fix, quoted, checker R02
  - Must-fix 2 quotes: “Split-flow wasn't just a triage fix but a change in how the whole department runs.”
  - Its label: “Voice · Checker HARD hit R02”
- **Pass**: Flaw 4 (Q-Ladder) is must-fix, Voice, as a block found by reading
  - Must-fix 3 quotes: “I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first.”
  - Its label: “Voice and Clarity · This is an internal method name, which the full check lists under its blocks.”
- **Pass**: Flaw 8 (2017 against Mar 2019) is must-fix, Risk
  - Must-fix 4 quotes: “Since becoming nurse manager in 2017”, against the resume's “Nurse Manager, Emergency Department | Mar 2019 - Present”
  - Its label: “Risk · The letter and resume give different years for the same title.”
- **Pass**: Flaw 7 (the gap) is must-fix, Risk
  - Must-fix 5 quotes: “After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain.”
  - Its label: “Risk · The letter names the gap outright and apologizes for it, then never explains it.”
- **Pass**: No other finding is must-fix
  - The Must fix list holds those five and nothing else.
- **Pass**: Flaw 6 (an opening any firm could get) is should-fix, Proof
  - Should-fix 1 quotes: “I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients.”
  - Its label: “Proof · This line could go to any employer unchanged”
- **Pass**: Flaw 3 (a claim with no proof) is should-fix, Proof
  - Should-fix 3 quotes: “I'm known across the hospital as a leader people want to work for.”
  - Its label: “Proof · Neither line points to a name, a number or a result, so a hiring manager can't check either one.”
- **Pass**: Flaw 5 (the vague place) is should-fix, Voice, checker R44
  - Should-fix 4 quotes: “keep the room calm”
  - Its label: “Voice · Checker WARN R44 (vague place).”
- **Pass**: No finding supplies replacement wording or a sample sentence
  - Every direction points at the fix without writing it:
  - Quote: “Direction: use a period or comma, and cut "down by 16" if it only restates the math.”
  - Quote: “Direction: state what changed in the department and give the fact, or cut the line.”
  - Quote: “Direction: describe what the method does in plain words, or cut the name.”
  - Quote: “Direction: make the year match the resume.”
  - Quote: “Direction: cut the paragraph.”
  - Quote: “Direction: open on their wait, their three clinics or the evening launch.”
  - Quote: “Direction: tie her 38-to-22 result to their 34 and say what transfers to a multi-site clinic.”
  - Quote: “Direction: give a retention, turnover or survey figure, or cut the paragraph.”
  - Quote: “Direction: name the place or cut it with the line above.”
  - Quote: “Direction: fold each short line into the sentence next to it.”

The other should-fix findings are ones the key allows: should-fix 2 on the clinic wait and the budget, and the checker's V06 and V04 warnings as should-fix 5 and 6. Should-fix 6 is the sixth, given in one line as the report's rules say.

## Result

Test 7 passes. Must-fix holds the five planted must-fix flaws and nothing else, the three planted should-fix flaws are all there, and the verdict is Fix first.
