# Test 3: A strategy file in the packet (Claude Code, job-seeker-ops 0.4.4)

## Run
- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app, Windows 11 Pro. `claude --version` on this computer's PATH reports 2.1.295.
- Plugin: job-seeker-ops 0.4.4, installed on the account, in `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>`. Packet script: build_packet.py 0.4.0. Voice rules: the plugin's own plainspeak-writer 1.7.1 (check_voice 1.7.1).
- Python: `python`, 3.12.10.
- SCRIPT: `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\submission-review\scripts\build_packet.py`. WRITERS: `C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers`. PACKETS: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets`.
- Session: a fresh helper session in the Code tab that didn't build the plugin. Every reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, never a fork or a general-purpose helper.
- Packet: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79`
- Reviewer agent ID: a05765e4936236ee9.
- Key: `tests/keys/b-letter.md`, opened after this report came back.

## Build
`python SCRIPT --type letter --piece WRITERS\b-okafor\letter.txt --target WRITERS\b-okafor\posting.txt --companion WRITERS\b-okafor\resume.txt --companion WRITERS\b-okafor\positioning-notes.md --channel upload --out PACKETS`

The script printed the expected warning about the file name, recorded here and not acted on:

```text
Warning: The companion file name 'positioning-notes.md' suggests notes, strategy or the deeper record. A companion should be something the real reader also sees.
Voice rules from: \\?\C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\plainspeak-writer
Packet: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79. Read manifest.md first.
```

## Manifest
```text
# Review packet

Built by build_packet.py 0.4.0 on 2026-10-08 at 21:54.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,366 | 242 |
| target.txt | The target: the job posting, or the reader's own words | 1,232 | 197 |
| companion-1.txt | A companion the real reader also sees | 914 | 146 |
| companion-2.txt | A companion the real reader also sees | 401 | 70 |
| voice-rules.md | plainspeak-writer 1.7.1's voice rules, copied from its tells.md | 12,134 | 2,161 |
| full-check.md | plainspeak-writer 1.7.1's full check | 26,417 | 4,532 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 652 | 96 |
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

## Message sent
```text
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79. Read manifest.md first.
```

## Report, word for word
```text
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece, a cover letter); target.txt (the job posting, Supply Chain Planning Analyst at Switchgrass Freight Co.); companion-1.txt (the resume, which the reader also sees); companion-2.txt (marked as a companion, but it's the writer's positioning notes, so it's a leak and I didn't use it); voice-rules.md and full-check.md (the voice rules); checker.txt (the checker output); manifest.md
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md and full-check.md
- Also in my context: an account email and session environment details (working directory, platform and date). No saved memory, profile, preferences, project instructions or earlier conversation.
- Files I opened:
  - C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79\manifest.md
  - C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79\piece.txt
  - C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79\target.txt
  - C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79\companion-1.txt
  - C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79\companion-2.txt
  - C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79\checker.txt
  - C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79\voice-rules.md
  - C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215402-letter-ab79\full-check.md
- blind: no (companion-2.txt is the writer's positioning notes, titled "Positioning notes: Switchgrass letter." The real reader never sees it. It explains what the writer meant and says what was left out. It's in the packet as a companion. I set it aside and judged only from the piece, the target and the resume.)

## First take (Recruiter, first look)
This is a planning analyst at a grocery distributor who rebuilt a forecast and cut its error from 31% to 19% using SQL, Excel and Power BI, and who also ran a WMS on the warehouse floor. That's the forecasting, tools and WMS background this posting asks for, so I'd keep reading. Fit: yes

## Verdict
Send. Rule 3: no must-fix findings.

## Must fix
None.

## Should fix
1. "At Brightwell Grocers Distribution I worked on the same problem with groceries in place of freight" (line 3); "Freight forecasting starts with the question I've worked on for five years" (line 9) · Proof · The posting's problem is volume by lane and terminal, turned into dock staffing and trailer plans. The letter's proof is item demand turned into buyers' orders. A hiring manager will see that the letter calls these the same problem without showing the link. The duty "Turn forecasts into dock staffing and trailer plans with the operations team" never comes up in the letter or the resume. Direction: name the part of the grocery work that maps to volume or staffing, or narrow the claim to the part that does.
2. "cut count variance from 2.8% to 0.9%, so I've seen what a bad forecast does to the people on the dock" (line 7) · Proof · Count variance measures how accurate the inventory records are, not the forecast, so the "so" doesn't follow from the number before it. A close reader will notice the jump. Direction: give a fact about the dock that backs the clause, or cut the "so" clause.
3. "I'd send your terminal managers the same one-page weekly note our buyers get now" (line 9) · Clarity · This is the first time the letter mentions the note, but "the same" treats it as already introduced. A reader who hasn't matched it to resume line 11 stops to look for it. Direction: introduce the note where the buyers first come up in line 5.
4. "what your terminal managers need from a weekly report" (line 11); "what a bad forecast does to the people on the dock" (line 7) · Voice · The checker warned on line 11 under V10, and the warning hasn't been cleared. Line 7 has the same "what" clause standing in for a noun, found by reading. Both describe the thing instead of naming it. Direction: name the thing, such as the report contents or the dock effect.

Cleared warnings: none.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| "Bachelor's degree in supply chain, business, analytics or a related field." | Must-have | Shown | Resume line 18 (B.S. Supply Chain Management, 2018). Not in the letter. |
| "Three or more years in demand planning, supply planning or forecasting." | Must-have | Shown | Letter lines 5 and 9 ("in 2021", "five years"); resume line 7 (Planning Analyst, Aug 2021 to Present) |
| "Advanced Excel, including pivot tables and lookups, and working SQL." | Must-have | Shown | Letter line 5 and resume line 9 (forecast rebuilt in SQL and Excel). Pivot tables and lookups appear only in the resume skills list, line 21. |
| "Experience with a transportation or warehouse management system." | Must-have | Shown | Letter line 7 and resume lines 14 and 15 (Manhattan WMS, variance from 2.8% to 0.9%) |
| "Clear written updates for people who don't work with data." | Must-have | Shown | Letter line 9 (weekly note to buyers); resume line 11 (one-page weekly note on forecast misses) |
| "Power BI or Tableau." | Preferred | Shown | Letter line 5; resume line 10 (dashboard 14 buyers use every Monday) |
| "Experience in less-than-truckload or other freight." | Preferred | Missing | Letter line 3 says the work was "groceries in place of freight" |

## What I couldn't judge
- The forecast error going from 31% to 19%. The resume calls it mean absolute percentage error, but the letter names no measure. The posting's "missed by 24% on average" may be measured another way, so a hiring manager can't tell whether 19% beats their 24% on the same scale.
- "within a year" (line 5), which appears only in the letter, not the resume.
- "Most of the misses came from store promotions the old model never saw" (line 5). The letter doesn't say whether this was measured or is the writer's own judgment.
- The scale figures: 1,900 items, three distribution centers, 14 buyers (resume), a 410,000-square-foot warehouse (resume).
- Count variance going from 2.8% to 0.9%.
- "five years" (line 9) on the question of forecast misses. The resume supports roughly five years as a Planning Analyst, from Aug 2021.
- The employer, Brightwell Grocers Distribution in Olathe, KS, and the degree from Prairie Bluff University.
```

## Files the reviewer opened, from its transcript
```text
agent a05765e4936236ee9: 9 tool call(s)
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215402-letter-ab79\\manifest.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215402-letter-ab79\\piece.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215402-letter-ab79\\target.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215402-letter-ab79\\companion-1.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215402-letter-ab79\\companion-2.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215402-letter-ab79\\checker.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215402-letter-ab79\\voice-rules.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215402-letter-ab79\\full-check.md'
```

## Grade against keys/b-letter.md
- **`blind: no`.** Pass. "- blind: no (companion-2.txt is the writer's positioning notes, titled "Positioning notes: Switchgrass letter." ...)"
- **Names companion-2 as a leak.** Pass. "companion-2.txt (marked as a companion, but it's the writer's positioning notes, so it's a leak and I didn't use it)"
- **No finding relies on what only the notes say** (the 2020 reorganization, the top of the range, the plan not to say freight is new, what the hiring manager cares about). Pass. A search of the report for 2020, reorganization, range, salary, "freight is new" and "cares" finds none of them. The only mention of the notes' content is the blind line's general "It explains what the writer meant and says what was left out", which names no point from the notes. The freight findings rest on the letter's own line 3 and the posting, the same ground the reviewers in tests 1, 4 and 5 used without the notes.
- **The letter: Send, no must-fix.** Pass. "Send. Rule 3: no must-fix findings." Must fix reads "None."

## Result
Pass.
