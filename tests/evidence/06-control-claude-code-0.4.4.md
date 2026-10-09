# Test 6: The control letter (Claude Code, job-seeker-ops 0.4.4)

## Run
- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app, Windows 11 Pro. `claude --version` on this computer's PATH reports 2.1.295.
- Plugin: job-seeker-ops 0.4.4, installed on the account, in `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>`. Packet script: build_packet.py 0.4.0. Voice rules: the plugin's own plainspeak-writer 1.7.1 (check_voice 1.7.1).
- Python: `python`, 3.12.10.
- SCRIPT: `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\submission-review\scripts\build_packet.py`. WRITERS: `C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers`. PACKETS: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets`.
- Session: a fresh helper session in the Code tab that didn't build the plugin. Every reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, never a fork or a general-purpose helper.
- Packet: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-bbff`
- Reviewer agent ID: a05dc85560862fc5b.
- Key: `tests/keys/a-clean.md`, opened after this report came back.

## Build
`python SCRIPT --type letter --piece WRITERS\a-quintero\letter-clean.txt --target WRITERS\a-quintero\posting.txt --companion WRITERS\a-quintero\resume.txt --channel upload --out PACKETS`

```text
Voice rules from: \\?\C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\plainspeak-writer
Packet: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-bbff
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-bbff. Read manifest.md first.
```

## Manifest
```text
# Review packet

Built by build_packet.py 0.4.0 on 2026-10-08 at 21:54.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,443 | 248 |
| target.txt | The target: the job posting, or the reader's own words | 1,430 | 234 |
| companion-1.txt | A companion the real reader also sees | 1,569 | 260 |
| voice-rules.md | plainspeak-writer 1.7.1's voice rules, copied from its tells.md | 12,134 | 2,161 |
| full-check.md | plainspeak-writer 1.7.1's full check | 26,417 | 4,532 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 1,263 | 212 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md
- Full check: full-check.md
- Checker: Ran with surface letter, exit code 0.
```

The checker (1.7.1) found no HARD hits and three warnings: V11 on line 7, V01 (list of three, whole piece) and V06 (short flat line, whole piece).

## Message sent
```text
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-bbff. Read manifest.md first.
```

## Report, word for word
```text
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter); target.txt (the target: Clinic Operations Manager posting, Juniper Ridge Health Partners); companion-1.txt (a companion the reader also sees: the resume); voice-rules.md (voice rules); full-check.md (full check); checker.txt (checker output, surface letter, exit code 0); manifest.md
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md and full-check.md
- Also in my context: an account email; environment details (working folder, platform, date); instructions for connected tool servers. There's no saved memory, user profile, preferences, project instructions or earlier conversation. None of these say anything about this piece.
- Files I opened: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-bbff\manifest.md, \piece.txt, \target.txt, \companion-1.txt, \checker.txt, \voice-rules.md, \full-check.md
- blind: yes

## First take (Recruiter, first look)
This is an ED nurse manager in Tucson who cut door-to-provider time from 38 to 22 minutes, runs 52 staff and a $4.1 million budget, and speaks Spanish. The letter opens on our 34-minute wait and our three clinics by name. Fit: yes

## Verdict
Send. Rule 3: there are no must-fix findings.

## Must fix
None.

## Should fix
1. "I've spent the last seven years running the emergency department at Sonoran Valley Medical Center" (line 3) · Proof · The resume gives the title as "Nurse Manager, Emergency Department". A hiring manager in healthcare knows a nurse manager doesn't run the whole ED, so "running the emergency department" reads as a step past the title on the resume. Direction: match the claim to the resume title and scope.
2. "I manage 52 nurses and technicians across three shifts and a $4.1 million staffing budget" (line 7), set against the target's "Run daily operations for three clinics with 40 staff" and "Own the clinics' $6.2 million operating budget" · Proof · Every proof point comes from one hospital department. The letter never speaks to running three separate sites, to primary care rather than emergency care, or to an operating budget rather than a staffing budget. A close reader will notice that the role is wider. Direction: say what in the record carries over to several sites and a full operating budget, or let the 2021 fast-track opening do that work explicitly.
3. "In 2022 our door-to-provider time averaged 38 minutes." (line 5), with "by December the average was 22 minutes" · Clarity · If the 2022 average was 38 and it hit 22 by December of that year, the two numbers don't fit together. A careful reader stops to work out the starting point. Direction: say when the 38 was measured (the start of 2022, or 2021).
4. "Your three clinics add evening hours this spring" (line 3) and "where you want the wait to be by fall" (line 11) · Clarity · The packet was built on 2026-10-08. If the letter goes out in October, "this spring" may already have passed, and it's unclear which fall "by fall" means. Direction: tie both to dates that are right on the day it's sent.
5. "and that's the order I'd follow for your evening hours: the schedule first, then the hires, then the check-in flow before the doors open" (line 7) · Voice (checker WARN V11) · The clause points back at the sentence before it instead of naming the plan. It also makes a long sentence that holds the 2021 hiring, the 2020 go-live and the plan for evening hours all at once. Direction: make the plan the subject of its own sentence.

Cleared warnings: V01, lists of three (whole piece). "Oracle Road, Grant Road and Valencia" names the target's three real sites. "fast-track area in 2021, I built the schedule and hired the first eight" is two items, not a list of three. V06, short line after a long one (whole piece). "In 2022 our door-to-provider time averaged 38 minutes." adds the baseline, and "Your posting asks for Spanish, and I'm fluent." adds a new fact. Neither restates the line before it. checker.txt says each WARN was "cleared by a named decision or fixed", but the packet names no decisions, so I judged all three myself.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume: BSN, Saguaro State University, 2011 |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Letter line 3 (seven years); resume: Nurse Manager since Mar 2019, Charge Nurse 2014–2019 |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7 ($4.1 million budget closed under plan, built the fast-track schedule); resume |
| Working knowledge of Epic or a similar electronic health record | Must-have | Shown | Letter line 7 (2020 go-live, Epic workflows); resume (led the go-live, trained 140 staff) |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5 (38 to 22 minutes, split-flow triage); resume |
| Fluent in English and Spanish | Preferred | Shown | Letter line 9 (explains discharge plans in Spanish); resume |
| Lean or Six Sigma training | Preferred | Shown | Resume only: Lean Six Sigma Green Belt, 2023. Not in the letter. |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7 and resume: six-bed fast-track area opened in 2021 |

## What I couldn't judge
- The drop from 38 to 22 minutes in door-to-provider time, and "It held through two winter surges" (line 5). The second claim isn't on the resume.
- The $4.1 million staffing budget "closed under plan for three years", and the 52 staff across three shifts.
- The 2021 fast-track opening, including hiring "the first eight nurses".
- The Epic go-live in 2020 and the 140 staff trained (resume). The resume says "Epic ASAP", which a clinic recruiter may not know.
- Fluent Spanish, and explaining discharge plans "instead of waiting for the interpreter line" (line 9).
- The resume shows no role between Sep 2013 and Jun 2014. The letter doesn't raise it, but a reader comparing dates may ask.
- The target has no date, so I can't tell whether its "This spring" means a spring that's still ahead when the letter is sent.
```

## Files the reviewer opened, from its transcript
```text
agent a05dc85560862fc5b: 8 tool call(s)
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-bbff\\manifest.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-bbff\\piece.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-bbff\\target.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-bbff\\companion-1.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-bbff\\checker.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-bbff\\voice-rules.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-bbff\\full-check.md'
```

## Grade against keys/a-clean.md
- **Verdict: Send.** Pass. "Send. Rule 3: there are no must-fix findings."
- **First take ends `Fit: yes`.** Pass. "The letter opens on our 34-minute wait and our three clinics by name. Fit: yes"
- **Must fix: none.** Pass. "None."
- **Should fix quotes the piece; the list-of-three warning is listed or cleared with a reason.** Pass. All five should-fix findings quote the letter. The warning is cleared with a reason: "Cleared warnings: V01, lists of three (whole piece). "Oracle Road, Grant Road and Valencia" names the target's three real sites. "fast-track area in 2021, I built the schedule and hired the first eight" is two items, not a list of three." V11 is should-fix 5 and V06 is cleared with a reason.
- **Requirements: all five must-haves shown, with the degree in the resume, the five years and Epic in both, and schedules, budget and wait times in the letter.** Pass. Degree: "Resume: BSN, Saguaro State University, 2011". Five years: "Letter line 3 (seven years); resume". Schedules and budget: "Letter line 7 ($4.1 million budget closed under plan, built the fast-track schedule); resume". Epic: "Letter line 7 (2020 go-live, Epic workflows); resume". Wait times: "Letter line 5 (38 to 22 minutes, split-flow triage); resume".
- **Preferred: Spanish and Lean Six Sigma show, and a new site shows in part through the fast-track area.** Pass. Spanish "Shown", Lean Six Sigma "Shown" ("Resume only"), new site "Shown" ("six-bed fast-track area opened in 2021").

Should-fix 3 (the 38-minute average "In 2022" against "by December") and should-fix 4 ("this spring" and "by fall" against the packet date) are reasonable readings that quote the piece. Neither is must-fix, so the key's note about fixing the clean letter doesn't come into play.

## Result
Pass.
