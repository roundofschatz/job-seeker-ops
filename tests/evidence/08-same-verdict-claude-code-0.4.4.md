# Test 8: The same verdict three times (Claude Code, job-seeker-ops 0.4.4)

## Run
- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app, Windows 11 Pro. `claude --version` on this computer's PATH reports 2.1.295.
- Plugin: job-seeker-ops 0.4.4, installed on the account, in `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>`. Packet script: build_packet.py 0.4.0. Voice rules: the plugin's own plainspeak-writer 1.7.1 (check_voice 1.7.1).
- Python: `python`, 3.12.10.
- SCRIPT: `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\submission-review\scripts\build_packet.py`. WRITERS: `C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers`. PACKETS: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets`.
- Session: a fresh helper session in the Code tab that didn't build the plugin. Every reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, never a fork or a general-purpose helper.
- Packet: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a` (test 7's packet, not rebuilt).
- Run 1 is the test 7 reviewer, accb0976cb7018cf9. Runs 2 and 3 are new reviewers, a8ef60f3c4ba135bb and a07225f1b7803eef4, started at the same moment as run 1 with the same printed line.
- Key: `tests/keys/a-seeded.md`, opened after all three reports came back.

## Message sent to each run
```text
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a. Read manifest.md first.
```

## Run 1 report, word for word
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

## Run 2 report, word for word
```text
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter); target.txt (the target: Clinic Operations Manager posting, Juniper Ridge Health Partners); companion-1.txt (the resume, which the real reader also sees); voice-rules.md (voice rules); full-check.md (full check); checker.txt (checker output, surface letter, exit code 1); manifest.md (manifest)
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md and full-check.md
- Also in my context: an account email; session environment details (working folder, platform, date), which say nothing about the person or the piece
- Files I opened: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a\manifest.md, ...\piece.txt, ...\target.txt, ...\companion-1.txt, ...\checker.txt, ...\voice-rules.md, ...\full-check.md
- blind: yes

## First take (Recruiter, first look)
This is an emergency department nurse manager who cut door-to-provider time from 38 to 22 minutes and runs a 52-person team, and that lines up with a posting built around cutting a 34-minute wait. The opening line could go to any employer, so the case only starts at paragraph two. Fit: yes

## Verdict
Fix first. There are five must-fix findings, which falls in the one-to-five range for rule 2.

## Must fix
1. "By December the average was 22 minutes — down by 16." (line 5) · Voice · Checker HARD hit R01, an em dash. Direction: use a period or comma.
2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · Checker HARD hit R02, the "not just X, but Y" shape. It also claims a department-wide change with nothing behind it, so a hiring manager gets a big claim with no proof. Direction: state what changed in the department and give the fact, or cut the line.
3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first." (line 7) · Voice (internal method name, a block in the full check) · "Q-Ladder" is a coined name the reader has never seen and can't look up. It reads as in-house shorthand, and it isn't on the resume either. Direction: describe what the method does in plain words and drop the name.
4. "Since becoming nurse manager in 2017" (line 7) vs. the resume's "Nurse Manager, Emergency Department | Mar 2019 - Present" (companion line 10) · Risk · The letter and the resume disagree by two years on the title start date. Before March 2019 the resume shows "Charge Nurse ... Jun 2014 - Feb 2019". A recruiter who spots this starts doubting the other numbers too. Direction: make the two documents match.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · This names a gap outright and calls it something that needs explaining, then never explains it. The gap is from Sep 2013 to Jun 2014 on the resume, twelve years back, and most readers wouldn't have noticed it. Direction: cut the paragraph.

## Should fix
1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · This line could go to any employer unchanged, and it's the line the recruiter reads first. The posting gives plenty to use: three named clinics, the 34-minute wait, the evening hours this spring. Direction: open on something only Juniper Ridge's posting holds.
2. "I sorted every new patient" (line 7) · Proof · This reads as overreach. A manager of 52 staff in a department the resume says "sees 61,000 visits a year" personally sorting every new patient will make a hiring manager doubt it, or wonder whether it means only the fast-track area. Direction: say which patients and over what period.
3. "I'm known across the hospital as a leader people want to work for. I know what it takes to keep the room calm when the waiting area is full." (line 9) · Proof · These are self-labels with no name, number or event behind them, so a reader can't check either claim. Direction: give a fact that shows it, such as retention or turnover, or cut the paragraph.
4. "I'd explain discharge plans myself, the way I do now, instead of waiting for the interpreter line." (line 13) · Proof · The target role runs operations across three primary care clinics. A hiring manager may read this as a nurse picturing bedside work rather than the manager's job, and "discharge plans" is a hospital term. Direction: tie the Spanish to something the operations role does.
5. "Run daily operations for three clinics with 40 staff, including medical assistants, nurses and front desk teams." (target line 7) · Proof · The letter never shows work across more than one site or in outpatient or primary care. All its proof comes from one hospital emergency department. That's the first question a hiring manager will have, and the letter leaves it open. Direction: name any multi-site or clinic experience, or show why the triage and fast-track work carries over to clinic check-in.
6. "In 2022 our door-to-provider time averaged 38 minutes." (line 5) · Clarity · The letter never names the current employer or says the work is in an emergency department. "our" and "across the hospital" (line 9) point at a place the reader of the letter alone never sees.
7. "In 2022 our door-to-provider time averaged 38 minutes ... By December the average was 22 minutes" (line 5) · Clarity · If 2022 averaged 38, it's unclear which December reached 22. The resume says the cut happened "in 2022", so the timeline reads two ways.
8. "down by 16" (line 5) · Voice · This repeats arithmetic the reader just did, which is saying it twice.
9. "keep the room calm" (line 9) · Voice · Checker WARN R44: "the room" used as an idiom.
10. (whole piece) · Voice · Checker WARN V04: "5 of 9 paragraphs are one sentence", for example lines 3, 11 and 15.

Cleared warnings: V06 on "In 2022 our door-to-provider time averaged 38 minutes." and "Your posting asks for Spanish, and I'm fluent." is cleared, because each short line adds a new fact and doesn't restate the line before.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume line 26 (BSN, 2011); not in the letter |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Resume lines 10 and 17; letter line 7 (start date conflicts with the resume) |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7 ($4.1 million staffing budget, fast-track schedule); resume lines 13 and 14 |
| Working knowledge of Epic or a similar electronic health record | Must-have | Shown | Letter line 7; resume line 15 (Epic ASAP go-live, 140 staff trained) |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5 (38 to 22 minutes); resume line 12 |
| Fluent in English and Spanish | Preferred | Shown | Letter line 13, with an example of daily use; resume line 33 |
| Lean or Six Sigma training | Preferred | Shown | Resume line 30 (Green Belt, 2023); not in the letter |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7 and resume line 14 (six-bed fast-track area, 2021) |

## What I couldn't judge
- Which date is right for the nurse manager title: 2017 in the letter or March 2019 on the resume.
- The 38-to-22-minute result: how it was measured, over what period, and whether it held after December.
- The $4.1 million staffing budget closed under plan in 2023, 2024 and 2025, the 52 staff, and the 61,000 annual visits.
- The 2020 Epic ASAP go-live and the 140 staff trained.
- Whether "Q-Ladder" is a method anyone outside the writer would recognize.
- "Known across the hospital as a leader people want to work for": nothing a reader can check.
- Spanish fluency: no certification or test is named.
- The resume moves from a medical-surgical staff nurse at Saint Anselm (ending Sep 2013) straight to emergency department charge nurse at Sonoran Valley (Jun 2014). A reader may wonder whether an earlier staff role at Sonoran Valley is missing.
- Whether a hospital emergency department staffing budget is comparable to the posting's "$6.2 million operating budget" across three clinics.
```

## Run 3 report, word for word
```text
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (manifest); piece.txt (the piece: cover letter); target.txt (the target: Clinic Operations Manager posting, Juniper Ridge Health Partners); companion-1.txt (resume the reader also sees); voice-rules.md (voice rules); full-check.md (full check); checker.txt (checker output, surface letter, exit code 1)
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md and full-check.md
- Also in my context: an account email
- Files I opened: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a\manifest.md, ...\piece.txt, ...\target.txt, ...\companion-1.txt, ...\voice-rules.md, ...\full-check.md, ...\checker.txt
- blind: yes

## First take (Recruiter, first look)
An ER nurse manager who cut door-to-provider time from 38 to 22 minutes and runs a 52-person team and a $4.1 million budget. That matches a posting built around cutting a 34-minute wait, even if the opening line could have gone to any employer. Fit: yes

## Verdict
Fix first. Rule 2: there are five must-fix findings, which is between one and five, and the first take ends Fit: yes.

## Must fix
1. "By December the average was 22 minutes — down by 16." (line 5) · Voice · Checker HARD hit R01, an em dash. The "down by 16" after the dash repeats math the reader just did. Direction: cut the dash and the restated number.
2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · Checker HARD hit R02, "not just X but Y". It also ends the paragraph on a summary line and makes the result bigger than the resume does, since the resume only claims the wait-time cut. A hiring manager would ask what else changed. Direction: say what changed beyond triage, or cut the line.
3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first." (line 7) · Voice · This is an internal method name, which the full check blocks. No reader knows what the Q-Ladder is, and the resume never mentions it. "Every new patient" from a manager over 52 staff and 61,000 visits a year also reads as overreach. Direction: describe what the method does in plain words, or cut it.
4. "Since becoming nurse manager in 2017" (line 7) vs. resume "Nurse Manager, Emergency Department | Mar 2019 - Present" and "Charge Nurse, Emergency Department | Jun 2014 - Feb 2019" (companion-1, lines 10 and 17) · Risk · The letter and the resume give different start dates for the manager role. A recruiter checking dates will catch it and wonder which one is true. Direction: make the year match the resume.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · This names a gap outright and apologizes for it. Then it explains nothing, so the reader gets a reason to doubt and no answer. The resume shows Sep 2013 to Jun 2014, a gap a recruiter would likely skim past. Direction: cut the line.

## Should fix
1. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · This line could go to any employer unchanged. It's the line the recruiter reads first, and it says nothing about Juniper Ridge, its three clinics or the evening launch. The letter's best fact doesn't come until the next paragraph. Direction: open on something only this posting has, or start with the wait-time result.
2. "In 2022 our door-to-provider time averaged 38 minutes." (line 5) vs. the target's "Cut the average wait from check-in to seeing a provider, now 34 minutes" and "Run daily operations for three clinics with 40 staff" (target lines 10 and 7) · Proof · The hiring manager will ask whether an ER triage fix carries over to three primary care clinics. The letter never ties its 38-to-22 result to their 34 minutes, and never addresses the move from one department to three sites. Direction: say how the split-flow work applies to a clinic wait.
3. "I'm known across the hospital as a leader people want to work for." (line 9) · Proof · No reader can check this label, and no name, retention figure or other fact backs it. Direction: give the fact behind it or cut the line.
4. "Lean or Six Sigma training." (target line 22) · Proof · This preferred requirement appears only on the resume ("Lean Six Sigma Green Belt, 2023"). The letter never links it to the wait-time work, though that's the natural place to show it. Direction: tie the Green Belt to the split-flow result.
5. "In 2022 our door-to-provider time averaged 38 minutes." (line 5) · Clarity · The letter never names the current employer. The only hospital it names is Saint Anselm, in line 11, so a reader of the letter alone could take "our" to mean a job she left in 2013. Direction: name Sonoran Valley Medical Center.
6. "I know what it takes to keep the room calm when the waiting area is full." (line 9) · Voice · Checker WARN R44. "The room" is a vague place, and "what it takes" names nothing.
7. (whole piece) · Voice · Checker WARN V04: 5 of 9 paragraphs are one sentence, for example lines 3, 11 and 15.

Cleared warnings: V06 ("In 2022 our door-to-provider time averaged 38 minutes." and "Your posting asks for Spanish, and I'm fluent."). Each short line adds a new fact instead of repeating the line before.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume line 26 (BSN, 2011); not in the letter |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Letter line 7 (its start year disagrees with the resume); resume lines 10 and 17 |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7; resume lines 13 and 14 |
| Working knowledge of Epic or a similar EHR | Must-have | Shown | Letter line 7; resume line 15 |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5; resume line 12 |
| Fluent in English and Spanish | Preferred | Shown | Letter line 13 (with an example of use); resume line 33 |
| Lean or Six Sigma training | Preferred | Shown | Resume line 30 only |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7 (fast-track area, 2021); resume line 14 |

## What I couldn't judge
- The 38-to-22-minute door-to-provider result in 2022, and whether an ER door-to-provider time compares with a clinic's check-in-to-provider time.
- The $4.1 million budget closed under plan in 2023, 2024 and 2025; the 52 staff; 61,000 visits a year; the 140 staff trained on Epic.
- The year the nurse manager role began: 2017 in the letter, March 2019 on the resume.
- "Known across the hospital as a leader people want to work for."
- The Q-Ladder and the claim that she sorted every new patient with it.
- Spanish fluency, the 2023 Lean Six Sigma Green Belt and the 2011 BSN from Saguaro State University.
- The gap after Saint Anselm and the reason for it.
```

## Files each run opened, from the transcripts
Run 2:

```text
agent a8ef60f3c4ba135bb: 8 tool call(s)
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\manifest.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\piece.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\target.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\companion-1.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\checker.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\voice-rules.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\full-check.md'
```

Run 3:

```text
agent a07225f1b7803eef4: 8 tool call(s)
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\manifest.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\piece.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\target.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\companion-1.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\voice-rules.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\full-check.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\checker.txt'
```

Run 1's list is in `07-seeded-claude-code-0.4.4.md`. All three opened the same seven packet files and nothing else.

## Grade against keys/a-seeded.md
| | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Verdict | Fix first | Fix first | Fix first |
| First take ends | Fit: yes | Fit: yes | Fit: yes |
| "22 minutes — down by 16" | Must fix 1, Voice, R01 | Must fix 1, Voice, R01 | Must fix 1, Voice, R01 |
| "wasn't just a triage fix but" | Must fix 2, Voice, R02 | Must fix 2, Voice, R02 | Must fix 2, Voice, R02 |
| "Q-Ladder" | Must fix 3, Voice, Clarity | Must fix 3, Voice (internal method name, a block in the full check) | Must fix 3, Voice |
| "Since becoming nurse manager in 2017" | Must fix 4, Risk | Must fix 4, Risk | Must fix 4, Risk |
| "I was out of work for most of a year" | Must fix 5, Risk | Must fix 5, Risk | Must fix 5, Risk |
| Other must-fix | None | None | None |
| Flaw 6, the stock opening | Should fix 1 | Should fix 1 | Should fix 1 |
| Flaw 3, "known across the hospital" | Should fix 3 | Should fix 3 | Should fix 3 |
| Flaw 5, "keep the room calm" | Should fix 5 | Should fix 9 | Should fix 6 |
| Should-fix count | 5 | 10 | 7 |

- **Same verdict in all three runs.** Pass. Run 2: "Fix first. There are five must-fix findings, which falls in the one-to-five range for rule 2." Run 3: "Fix first. Rule 2: there are five must-fix findings, which is between one and five, and the first take ends Fit: yes."
- **The must-fix lists name the same problems: the same quoted words under the same checks.** Pass. All three hold the same five quotes under the same checks. Run 1 also names Clarity on the Q-Ladder finding; the key allows that ("Clarity may name it too"), and Voice is present in all three.
- **Each run against the test 7 conditions.** Pass for runs 2 and 3 as well: Fit: yes, exactly the five planted must-fix flaws, flaws 3, 5 and 6 as should-fix, and no replacement wording. The closest call is run 3's should-fix 5, "Direction: name Sonoran Valley Medical Center.", which names the employer from the resume and writes no new sentence.

The should-fix lists differ, as the key allows. Run 2 lists ten should-fix findings, and its entries 6 and 7 run two sentences each, where the reviewer's instructions ask for one line per finding past the fifth. The key doesn't grade that.

## Result
Pass.
