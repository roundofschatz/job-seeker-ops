# Test 7: Seeded flaws (Claude Code)

## Run

- Date: 2026-10-01
- Product: Claude Code, in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- Claude Code version: 2.1.280 (`claude --version`)
- Plugin: job-seeker-ops, installed copy. Its `plugin.json` reads 0.1.1, and `build_packet.py` reports 0.1.0.
- Installed copy: `%APPDATA%\Claude\local-agent-mode-sessions\<ids>\rpm\plugin_<id>\`. RUN-TESTS.md says to look under `~/.claude/plugins`, and nothing from job-seeker-ops is there. The desktop app keeps an uploaded plugin in its own folder.
- SCRIPT: `skills\submission-review\scripts\build_packet.py` in the installed copy. It's the same file as the repository copy, byte for byte (SHA-256 starts `2A33C959D0B9BFB9`). Run with `python`, Python 3.12.10.
- Installed `agents\submission-reviewer.md`: the same as the repository copy except that the front matter writes the description as one quoted line. Its tools line reads `tools: Read`.
- WRITERS: `tests\writers\`, used in place.
- PACKETS: `C:\Users\<user>\repos\tools\jso-tests\packets`, new for this run.
- Voice rules: every build passed `--voice-dir ..\plainspeak-writer` from the repository folder, as the owner asked, so every packet uses plainspeak-writer 1.4.
- Reviewer started as `job-seeker-ops:submission-reviewer` with the Agent tool. The four reviewers in this run (tests 1 and 2, test 7 and the two test 14 letters) were started together, each with its own printed line and nothing else.
- Reports and replies below were copied by script from the reviewer's own hand-back calls in the session transcript, word for word.
- The Windows user name in each path is written as `<user>`, inside the reports and replies too. Nothing else in them was changed.
- In the grades, ⏎ marks a line break inside a quote.
- The key, `keys/a-seeded.md`, was opened after this review had finished.

## Build

Run from the repository folder, `C:\Users\<user>\repos\tools\job-seeker-ops`:

````
python SCRIPT --type letter --piece tests\writers\a-quintero\letter-seeded.txt --target tests\writers\a-quintero\posting.txt --companion tests\writers\a-quintero\resume.txt --channel upload --voice-dir ..\plainspeak-writer --out ..\jso-tests\packets
````

Script output:

````
Packet: C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f. Read manifest.md first.
````

## Test 7 review

- Packet folder: `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f`
- Reviewer agent id: `ae6bf6fd58a49ea4f`
- `piece.txt` in the packet: 1,506 bytes, SHA-256 `9E4923D9743C533F6E3F0AAAFA3764F436F91CE6425470A94F6371EA1223ED07`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 22:31.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,503 | 268 |
| target.txt | The target: the job posting, or the reader's own words | 1,430 | 234 |
| companion-1.txt | A companion the real reader also sees | 1,569 | 260 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 817 | 124 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.4. Rules file: C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- Checker: Ran with surface letter, exit code 1.
````

### Checker output in the packet (checker.txt)

````
plainspeak-writer 1.4 checker output for piece.txt, surface letter, exit code 1 (0 means no HARD hits, 1 means at least one).

check_voice 1.4   surface: letter

=== C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\piece.txt ===
HARD FAIL (2):
  L5: [R01 em dash or other dash] "—": no dash of any kind, and no double hyphen or spaced hyphen typed as one; a period, comma, colon, or semicolon
  L5: [R02 negative corollary] "wasn't just": state the positive claim directly
WARN (2), each cleared by a named decision or fixed:
  L9: [R44 the vague place] "the room": a real, named place, or one the sentence itself just built
  L0: [V04 staccato layout] "5 of 9 paragraphs are one sentence": join one-line paragraphs into paragraphs that finish a thought

RESULT: FAIL: hard violations present.
````

### Exact message sent

````
Review the packet in C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\manifest.md
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\piece.txt
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\target.txt
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\companion-1.txt
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\checker.txt
Read C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
SubagentHandback (the harness's delivery call, holding the report)
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: `piece.txt` (the cover letter), `target.txt` (the job posting), `companion-1.txt` (the resume sent with the letter), `checker.txt` (checker output), `manifest.md` (the manifest). No leaks: the one companion is a resume the real reader also sees.
- Voice rules: plainspeak-writer 1.4, `C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md`
- Also in my context: one account identifier for the user, attached by the harness, plus tool-server instructions and environment details. I saw no saved memory, profile of the writer, preferences, project instructions or earlier conversation. None of it was used.
- Files I opened:
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\manifest.md`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\piece.txt`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\target.txt`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\companion-1.txt`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-0e1f\checker.txt`
  - `C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md`
- blind: yes. I judged the account identifier not to be a profile, since it says nothing about the writer or the piece. If you count any user identifier as a profile, treat this review as blind: no for that one reason.

## First take (Recruiter, first look)
The opening line could come from any applicant, but the next paragraph shows a nurse manager who cut a provider wait from 38 to 22 minutes, and this job is about cutting a wait. I'd keep reading. Fit: yes

## Verdict
Fix first. There are five must-fix findings, which falls in the one-to-five rule.

## Must fix
1. "By December the average was 22 minutes — down by 16." (line 5) · Voice · Checker HARD hit R01, a dash used as a dash. Direction: end the sentence at the number or join with a comma.
2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · Checker HARD hit R02. The line also closes the paragraph with a summary that adds no fact after the 22-minute result. Direction: cut the line, or say what changed in the department with a number.
3. "the Q-Ladder, my method for deciding who sees a provider first" (line 7) · Voice · An internal method name, which the rules file lists under its blocks. The hiring manager has never heard of it, can't look it up, and may wonder why a personal method stands in for a standard triage scale. It isn't on the resume. Direction: describe what the method does in plain words, or drop it.
4. "Since becoming nurse manager in 2017" (line 7) against "Nurse Manager, Emergency Department | Mar 2019 - Present" (resume, line 10) · Risk · The letter and the resume give different start years for the same title. A close reader or a grader comparing the two sees a date that doesn't hold. Direction: make the year match the resume.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · The letter names a gap outright and points the reader at it, then never explains it. The reader is left with "out of work" and an open question about an exit. Direction: cut the line.

## Should fix
1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · This line could go to any health employer unchanged, and it holds the recruiter's ten seconds. "Your organization" replaces the firm's name, and "long admired" has nothing behind it. Direction: open on the wait-time result or on a fact from the posting.
2. "I sorted every new patient with the Q-Ladder" (line 7) · Proof · Reads as overreach. A manager of 52 people across three shifts personally sorting every patient isn't believable. Direction: say who did the sorting and what it produced.
3. "I'm known across the hospital as a leader people want to work for. I know what it takes to keep the room calm when the waiting area is full." (line 9) · Proof · Two labels a reader can't check, with no name, number or result. Direction: give a retention or turnover figure, or cut the paragraph.
4. "I'd welcome a conversation about the evening launch and where you want the wait to be by fall." (line 15) · Proof · Apart from Spanish, this is the only line built from the posting, and it comes last. All the proof is from one department. The letter never ties the 38 to 22 result to the posting's "now 34 minutes", or to "three primary care clinics" and "three clinics with 40 staff". Direction: connect one result to the posting's own number or sites, earlier in the letter.
5. "In 2022 our door-to-provider time averaged 38 minutes." and "how the whole department runs" (line 5) · Clarity · The letter never names the employer or says this is an emergency department, so "our" and "the whole department" point at nothing unless the resume is open. "Door-to-provider" is also the writer's term, where the posting says "wait from check-in to seeing a provider". Direction: name the hospital and department once.
6. Line 15 · Clarity · "by fall": the posting gives no fall date and says evening hours start "This spring".
7. Line 9 · Voice · "the room": checker WARN R44, a vague place the sentence doesn't build.

Cleared warnings: V04 ("5 of 9 paragraphs are one sentence"), because the count includes the salutation and the signature block. The body has three one-sentence paragraphs out of seven, which is under half.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume line 26, BSN 2011. Not in the letter. |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Letter line 7, resume lines 10 and 17. Covered under either start year, but the years disagree (must-fix 4). |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7 ($4.1 million, under plan three years, built the schedule). Resume lines 13, 14 and 18. |
| Working knowledge of Epic or a similar electronic health record | Must-have | Shown | Letter line 7 (2020 go-live). Resume line 15 (led go-live, trained 140 staff). |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5 and resume line 12 (38 to 22 minutes). |
| Fluent in English and Spanish | Preferred | Shown | Letter line 13 (explains discharge plans in Spanish now). Resume lines 5 and 33. |
| Lean or Six Sigma training | Preferred | Shown | Resume line 30 only. The letter doesn't mention it. |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7 and resume line 14 (six-bed fast-track area, 2021). |

## What I couldn't judge
- Whether the nurse manager role began in 2017 or March 2019.
- The drop from 38 to 22 minutes in 2022, and whether split-flow triage alone caused it.
- The $4.1 million staffing budget and three years closed under plan.
- The 52-person team, the six-bed fast-track area and the eight first hires.
- Her part in the 2020 Epic go-live. The letter says she "set up" workflows, and the resume says she "led" the go-live and trained 140 staff.
- What the Q-Ladder is, whether the hospital approved it, and how it relates to a standard triage scale.
- The level of her Spanish and whether she is cleared to use it with patients in place of an interpreter.
- "known across the hospital as a leader people want to work for".
- The reason for the 2013 to 2014 gap and for leaving Saint Anselm.
- "long admired", and whether "by fall" comes from a source outside the posting.
- The BSN, the CEN and the Lean Six Sigma Green Belt.
````

## Grade (keys/a-seeded.md)

- **Pass**: Verdict Fix first
  - Quote: “Fix first. There are five must-fix findings, which falls in the one-to-five rule.”
- **Pass**: First take ends Fit: yes
  - Quote: “I'd keep reading. Fit: yes”
- **Pass**: Flaw 1 (dash) is must-fix, quoted, checker R01
  - Quote: “1. "By December the average was 22 minutes — down by 16." (line 5) · Voice · Checker HARD hit R01, a dash used as a dash.”
- **Pass**: Flaw 2 ("not just X but Y") is must-fix, quoted, checker R02
  - Quote: “2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · Checker HARD hit R02.”
- **Pass**: Flaw 4 (Q-Ladder) is must-fix, Voice, as a block found by reading
  - Quote: “3. "the Q-Ladder, my method for deciding who sees a provider first" (line 7) · Voice · An internal method name, which the rules file lists under its blocks.”
- **Pass**: Flaw 8 (2017 against Mar 2019) is must-fix, Risk
  - Quote: “4. "Since becoming nurse manager in 2017" (line 7) against "Nurse Manager, Emergency Department | Mar 2019 - Present" (resume, line 10) · Risk”
- **Pass**: Flaw 7 (the gap) is must-fix, Risk
  - Quote: “5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk”
- **Pass**: No other finding is must-fix
  - The Must fix list holds those five and nothing else.
  - Quote: “There are five must-fix findings”
- **Pass**: Flaw 6 (any-firm opening) is should-fix, Proof
  - Quote: “1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof”
- **Pass**: Flaw 3 (claim with no proof) is should-fix, Proof
  - Quote: “3. "I'm known across the hospital as a leader people want to work for. I know what it takes to keep the room calm when the waiting area is full." (line 9) · Proof”
- **Pass**: Flaw 5 (vague place) is should-fix, Voice, checker R44, as a one-line entry past the fifth
  - Quote: “7. Line 9 · Voice · "the room": checker WARN R44, a vague place the sentence doesn't build.”
- **Pass**: No finding supplies replacement wording or a sample sentence
  - Decided by reading every Direction line, outside the report.

How the replacement-wording check was made: the report has ten Direction lines, and each one was read. None holds new wording for the letter. They are:

- Quote: “Direction: end the sentence at the number or join with a comma.”
- Quote: “Direction: cut the line, or say what changed in the department with a number.”
- Quote: “Direction: describe what the method does in plain words, or drop it.”
- Quote: “Direction: make the year match the resume.”
- Quote: “Direction: cut the line.”
- Quote: “Direction: open on the wait-time result or on a fact from the posting.”
- Quote: “Direction: say who did the sorting and what it produced.”
- Quote: “Direction: give a retention or turnover figure, or cut the paragraph.”
- Quote: “Direction: connect one result to the posting's own number or sites, earlier in the letter.”
- Quote: “Direction: name the hospital and department once.”

Note: checker.txt lists R01 and R02 under HARD FAIL with plainspeak-writer 1.4, so flaws 1 and 2 belong in must-fix.

Note: the 1.4 checker raised two warnings on this letter, R44 and V04. The reviewer listed R44 as should-fix 7 and cleared V04 with a reason, which the key allows:

- Quote: “Cleared warnings: V04 ("5 of 9 paragraphs are one sentence"), because the count includes the salutation and the signature block. The body has three one-sentence paragraphs out of seven, which is under half.”

The count in that reason is right. The letter has seven body paragraphs, and the ones on lines 3, 11 and 15 are one sentence long.

Note: the key names R41, P10 and list-of-three warnings as should-fix findings that may appear. The 1.4 checker raised none of them on this letter, so the report has none.

Note: every quoted string in the report was checked by script against the packet, 31 in all. Each one matches the letter, the posting, the resume or the checker output. Two start with a capital only because they open the reviewer's sentence: "Your organization" and "Door-to-provider".

Note: this reviewer wrote `blind: yes`, where the test 1 reviewer and both test 14 reviewers wrote `blind: no` for the same account item. The key for this test doesn't grade the blind line. The difference is covered in `02-memory-claude-code.md`.

- Quote: “- Also in my context: one account identifier for the user, attached by the harness, plus tool-server instructions and environment details. I saw no saved memory, profile of the writer, preferences, project instructions or earlier conversation. None of it was used.”
- Quote: “- blind: yes. I judged the account identifier not to be a profile, since it says nothing about the writer or the piece. If you count any user identifier as a profile, treat this review as blind: no for that one reason.”

**Result: Pass**
