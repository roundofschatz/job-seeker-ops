# Test 7: Seeded flaws (Claude Code, job-seeker-ops 0.4.4)

## Run
- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app, Windows 11 Pro. `claude --version` on this computer's PATH reports 2.1.295.
- Plugin: job-seeker-ops 0.4.4, installed on the account, in `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>`. Packet script: build_packet.py 0.4.0. Voice rules: the plugin's own plainspeak-writer 1.7.1 (check_voice 1.7.1).
- Python: `python`, 3.12.10.
- SCRIPT: `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\submission-review\scripts\build_packet.py`. WRITERS: `C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers`. PACKETS: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets`.
- Session: a fresh helper session in the Code tab that didn't build the plugin. Every reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, never a fork or a general-purpose helper.
- Packet: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a` (tests 8 and 9 reuse it).
- Reviewer agent ID: accb0976cb7018cf9 (the first test 7 reviewer, used again in test 9).
- Key: `tests/keys/a-seeded.md`, opened after this report and both test 8 reports came back.

## Build
`python SCRIPT --type letter --piece WRITERS\a-quintero\letter-seeded.txt --target WRITERS\a-quintero\posting.txt --companion WRITERS\a-quintero\resume.txt --channel upload --out PACKETS`

```text
Voice rules from: \\?\C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\plainspeak-writer
Packet: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a. Read manifest.md first.
```

## Manifest
```text
# Review packet

Built by build_packet.py 0.4.0 on 2026-10-08 at 21:54.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,503 | 268 |
| target.txt | The target: the job posting, or the reader's own words | 1,430 | 234 |
| companion-1.txt | A companion the real reader also sees | 1,569 | 260 |
| voice-rules.md | plainspeak-writer 1.7.1's voice rules, copied from its tells.md | 12,134 | 2,161 |
| full-check.md | plainspeak-writer 1.7.1's full check | 26,417 | 4,532 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 1,229 | 199 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md
- Full check: full-check.md
- Checker: Ran with surface letter, exit code 1.
```

## Checker output in the packet (checker.txt)
```text
plainspeak-writer 1.7.1 checker output for piece.txt, surface letter, exit code 1 (0 means no HARD hits, 1 means at least one).

check_voice 1.7.1   surface: letter

=== C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a\piece.txt ===
Words: 268
HARD FAIL (2):
  L5: [R01 em dash or other dash] "—": no dash of any kind, and no double hyphen or spaced hyphen typed as one; a period, comma, colon, or semicolon
  L5: [R02 negative corollary] "wasn't just": state the positive claim directly
WARN (3), each cleared by a named decision or fixed:
  L9: [R44 'the room' or 'the table' as an idiom] "keep the room": name the people and what they did: 'the council agreed', not 'the room agreed'
  L0: [V06 short flat line after a long one (rate)] "2 in 268 words, 7.5 per 1,000, where 9 in 10 pieces of edited human writing stay at or under 5: "In 2022 our door-to-provider time averaged 38 minutes.", "Your posting asks for Spanish, and I'm fluent."": fold the point into the long sentence, or cut the short line if it only restates it
  L0: [V04 staccato layout] "5 of 9 paragraphs are one sentence": join one-line paragraphs into paragraphs that finish a thought

RESULT: FAIL: hard violations present.
```

## Message sent
```text
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a. Read manifest.md first.
```

## Report, word for word
Saved from the transcript before test 9's follow-up went to the same reviewer.

```text
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter); target.txt (the job posting); companion-1.txt (resume, a companion the reader also sees); voice-rules.md (voice rules); full-check.md (full check); checker.txt (checker output, surface letter, exit code 1); manifest.md
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md and full-check.md
- Also in my context: an account email
- Files I opened: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a\manifest.md, \piece.txt, \target.txt, \companion-1.txt, \checker.txt, \voice-rules.md, \full-check.md
- blind: yes

## First take (Recruiter, first look)
The opening line is a stock "excited to apply" sentence that could go to any clinic, but the next line puts a cut from 38 to 22 minutes in front of a posting whose top complaint is wait times. This reads as an ED nurse manager who has run staff, a budget, Epic and a wait-time fix, so the recruiter keeps reading. Fit: yes

## Verdict
Fix first. Rule 2: there are five must-fix findings, which is within one to five, the first take is Fit: yes, and no must-have requirement is missing.

## Must fix
1. "By December the average was 22 minutes — down by 16." (line 5) · Voice · Checker HARD hit R01, an em dash. Direction: use a period or a comma, or cut "down by 16", since the reader can do that subtraction.
2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · Checker HARD hit R02, the "not just X but Y" shape. The second half also makes a claim bigger than the facts around it: nothing in the letter or resume shows a change beyond triage. Direction: state the department-wide change with a fact, or cut the line.
3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first." (line 7) · Voice, Clarity · An internal method name, which the full check blocks. The reader has never heard of "Q-Ladder", and it doesn't appear anywhere in the resume. Direction: describe what the method does in plain words, or drop the name.
4. "Since becoming nurse manager in 2017" (line 7) against the resume's "Nurse Manager, Emergency Department | Mar 2019 - Present" and "Charge Nurse, Emergency Department | Jun 2014 - Feb 2019" · Risk · The letter and the resume give different start years for the title. A hiring manager who spots it will doubt the other dates and figures too. Direction: make the two documents match.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · This names a gap and an exit outright. It promises an explanation and then never gives one. The resume shows the gap (Sep 2013 to Jun 2014), but the letter is what points the reader at it. Direction: cut the line.

## Should fix
1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · The recruiter's first ten seconds land on a line that could go to any employer unchanged. "Commitment to patients" names nothing about Juniper Ridge, and the 34-minute wait, the three clinics and the evening hours only show up later or not at all. Direction: open on the firm's own problem from the posting.
2. "I sorted every new patient" (line 7) · Proof · This reads as overreach. A manager of 52 staff in an ED with 61,000 visits a year (resume, line 11) wouldn't personally sort every patient, so a hiring manager will question it. Direction: say what she built or ran, and who did the sorting.
3. "I'm known across the hospital as a leader people want to work for. I know what it takes to keep the room calm when the waiting area is full." (line 9) · Proof · Both sentences are claims about herself with no name, number or result a reader can check. Direction: give a fact such as retention or turnover, or cut the paragraph.
4. "I'd explain discharge plans myself" (line 13), and "patients who could sit in a chair never took a bed" (line 5), against the target's "three primary care clinics" and "now 34 minutes" · Proof · All of the proof comes from an emergency department: beds, triage, discharge. The letter never says how it carries over to check-in-to-provider waits at three primary care clinics, or to a $6.2 million operating budget when her $4.1 million budget is staffing only. A hiring manager will ask that question first. Direction: link the split-flow result to their 34-minute wait and their three sites.
5. "keep the room calm" (line 9) · Voice · Checker WARN R44: "the room" stands in for the people in it. Direction: name who stays calm, or cut it along with Should fix 3.

Cleared warnings: V06 (short flat lines "In 2022 our door-to-provider time averaged 38 minutes." and "Your posting asks for Spanish, and I'm fluent."), because each adds a new fact rather than restating the line before. V04 (staccato layout), because the checker counted the greeting and the signature block; in the body, 3 of 7 paragraphs are one sentence, which is under half.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume line 26 (BSN, 2011); not in the letter |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Letter line 7; resume lines 10 and 17. The start year conflicts (Must fix 4) |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7 ($4.1 million, built the schedule); resume lines 13–14 |
| Working knowledge of Epic or a similar electronic health record | Must-have | Shown | Letter line 7; resume line 15 (2020 go-live, 140 staff trained) |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5 (38 to 22 minutes); resume line 12 |
| Fluent in English and Spanish | Preferred | Shown | Letter line 13; resume lines 5 and 33 |
| Lean or Six Sigma training | Preferred | Shown | Resume line 30 (Green Belt, 2023) only; the letter doesn't use it |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7 (six-bed fast-track, 2021); resume line 14 |

## What I couldn't judge
- Whether she became nurse manager in 2017 or March 2019.
- The cut in door-to-provider time from 38 to 22 minutes in 2022, and whether it lasted after December.
- The 52 staff, the $4.1 million staffing budget closed under plan for three years, and the 61,000 visits a year.
- What the "Q-Ladder" is, and whether anyone outside her department uses it.
- Her role in the 2020 Epic go-live: the letter says she set up workflows, the resume says she led the go-live and trained 140 staff.
- "Known across the hospital as a leader people want to work for": nothing in the packet backs it up.
- How fluent her Spanish is, and whether she explains discharge plans without an interpreter today.
- Why she was out of work after Saint Anselm.
- "By fall" in the close against the posting's "This spring": the posting has no date, so I can't tell whether the timing in the letter fits.
```

## Files the reviewer opened, from its transcript
```text
agent accb0976cb7018cf9: 8 tool call(s)
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\manifest.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\piece.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\target.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\companion-1.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\checker.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\voice-rules.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\full-check.md'
```

## Grade against keys/a-seeded.md
The checker is plainspeak-writer 1.7.1, and it lists R01 and R02 under HARD, so flaws 1 and 2 stay must-fix.

| # | Planted flaw | Expected | Report | Pass |
|---|---|---|---|---|
| 1 | "22 minutes — down by 16" | Must fix, Voice R01 | Must fix 1: "By December the average was 22 minutes — down by 16." (line 5) · Voice · Checker HARD hit R01 | Yes |
| 2 | "wasn't just a triage fix but" | Must fix, Voice R02 | Must fix 2: "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · Checker HARD hit R02 | Yes |
| 3 | "known across the hospital as a leader people want to work for" | Should fix, Proof | Should fix 3: "I'm known across the hospital as a leader people want to work for. ..." (line 9) · Proof | Yes |
| 4 | "Q-Ladder" | Must fix, Voice block found by reading (Clarity may name it too) | Must fix 3: "I sorted every new patient with the Q-Ladder, ..." (line 7) · Voice, Clarity · "An internal method name, which the full check blocks." | Yes |
| 5 | "keep the room calm" | Should fix, Voice R44 | Should fix 5: "keep the room calm" (line 9) · Voice · Checker WARN R44 | Yes |
| 6 | "I'm excited to apply ... at your organization" | Should fix, Proof | Should fix 1: "I'm excited to apply for the Clinic Operations Manager position at your organization, ..." (line 3) · Proof | Yes |
| 7 | "I was out of work for most of a year" | Must fix, Risk | Must fix 5: "After I left Saint Anselm in 2013, I was out of work for most of a year, ..." (line 11) · Risk | Yes |
| 8 | "Since becoming nurse manager in 2017" | Must fix, Risk | Must fix 4: "Since becoming nurse manager in 2017" (line 7) against the resume's March 2019 start date · Risk | Yes |

- **Verdict Fix first, first take ends `Fit: yes`.** Pass. "Fix first. Rule 2: there are five must-fix findings, which is within one to five, the first take is Fit: yes, and no must-have requirement is missing." The first take ends "so the recruiter keeps reading. Fit: yes".
- **Flaws 1, 2, 4, 7 and 8 are must-fix, quoting the planted words, and nothing else is must-fix.** Pass. Must fix holds exactly those five, as the table shows.
- **Flaws 3, 5 and 6 are should-fix.** Pass. Should fix 3, 5 and 1.
- **No finding supplies replacement wording or a sample sentence.** Pass. Every direction says where the fix lies, for example "Direction: use a period or a comma, or cut "down by 16", since the reader can do that subtraction." and "Direction: open on the firm's own problem from the posting." None writes a new sentence.

Other findings: should-fix 2 ("I sorted every new patient", overreach) and 4 (emergency-department proof against three primary care clinics) quote the piece. The report clears V06 and V04 with reasons, which the key allows.

## Result
Pass.
