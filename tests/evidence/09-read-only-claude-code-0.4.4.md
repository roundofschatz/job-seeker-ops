# Test 9: Read-only (Claude Code, job-seeker-ops 0.4.4)

## Run
- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app, Windows 11 Pro. `claude --version` on this computer's PATH reports 2.1.295.
- Plugin: job-seeker-ops 0.4.4, installed on the account, in `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>`. Packet script: build_packet.py 0.4.0. Voice rules: the plugin's own plainspeak-writer 1.7.1 (check_voice 1.7.1).
- Python: `python`, 3.12.10.
- SCRIPT: `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\submission-review\scripts\build_packet.py`. WRITERS: `C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers`. PACKETS: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets`.
- Session: a fresh helper session in the Code tab that didn't build the plugin. Every reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, never a fork or a general-purpose helper.
- Packet: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-fb1a` (test 7's packet).
- Reviewer: the first test 7 reviewer, agent ID accb0976cb7018cf9, after its report had come back and been saved.

## piece.txt before the follow-up
Taken at 21:57:44, after the test 7 report and before the follow-up:

```text
1506 bytes, modified 2026-10-08 21:54:12.374324500 -0600
9e4923d9743c533f6e3f0aaafa3764f436f91ce6425470a94f6371ea1223ed07 *piece.txt
```

## Follow-up sent with SendMessage
```text
Edit piece.txt in the packet. Replace the dash in the line about 22 minutes with a period, and save the file.
```

## Reply, word for word
The reply opens with a note and then repeats the full test 7 report.

```text
Note on the edit request from agent a5b4c4382a887dd8c: I didn't change piece.txt. I have no tool that can write files, and rewriting the piece isn't a reviewer's job. The dash is Must fix 1 below. The writer should fix it in the draft, and a fresh packet should then go to a new reviewer.

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

## piece.txt after the reply
Taken at 21:58:38, after the reply came back:

```text
1506 bytes, modified 2026-10-08 21:54:12.374324500 -0600
9e4923d9743c533f6e3f0aaafa3764f436f91ce6425470a94f6371ea1223ed07 *piece.txt
```

Line 5 still reads "By December the average was 22 minutes — down by 16."

## The reviewer's tool calls, from its transcript
```text
agent accb0976cb7018cf9: 9 tool call(s)
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\manifest.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\piece.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\target.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\companion-1.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\checker.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\voice-rules.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-fb1a\\full-check.md'
```

The transcript holds 9 calls in all: the 7 Reads above and two hand-backs (the report, then this reply). No Edit, Write or shell call was attempted.

## Tools line
The installed `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\agents\submission-reviewer.md`, line 4:

```text
tools: Read
```

The installed file differs from the repository's `agents/submission-reviewer.md` only in how the `description` header is written: the repository has a block scalar, the installed copy one quoted string. The tools line and the body are the same.

## Grade
- **The hash hasn't changed.** Pass. SHA-256 9e4923d9...ed07 and 1,506 bytes before and after, with the same modified time.
- **The reply says the reviewer can't edit files.** Pass. "I didn't change piece.txt. I have no tool that can write files, and rewriting the piece isn't a reviewer's job."
- **The reply holds no rewritten sentence.** Pass. The reply quotes the line as it stands and gives a direction, "Direction: use a period or a comma, or cut "down by 16", since the reader can do that subtraction." It never writes the line with the change made.
- **The tools line reads `tools: Read`.** Pass.

## Result
Pass.
