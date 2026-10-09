# Test 12: Channel limit (Claude Code, job-seeker-ops 0.4.4)

## Run
- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app, Windows 11 Pro. `claude --version` on this computer's PATH reports 2.1.295.
- Plugin: job-seeker-ops 0.4.4, installed on the account, in `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>`. Packet script: build_packet.py 0.4.0. Voice rules: the plugin's own plainspeak-writer 1.7.1 (check_voice 1.7.1).
- Python: `python`, 3.12.10.
- SCRIPT: `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\submission-review\scripts\build_packet.py`. WRITERS: `C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers`. PACKETS: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets`.
- Session: a fresh helper session in the Code tab that didn't build the plugin. Every reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, never a fork or a general-purpose helper.
- Packet: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-outreach-6392`
- Reviewer agent ID: acca8e0c6672c2b8c.
- Key: `tests/keys/d-outreach.md`, opened after this report came back.

## Build
`python SCRIPT --type outreach --piece WRITERS\d-ferreira\outreach-note.txt --channel textbox --limit 300 --out PACKETS`

```text
Voice rules from: \\?\C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\plainspeak-writer
Packet: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-outreach-6392
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-outreach-6392. Read manifest.md first.
```

## Manifest
```text
# Review packet

Built by build_packet.py 0.4.0 on 2026-10-08 at 21:54.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: outreach note | 372 | 68 |
| voice-rules.md | plainspeak-writer 1.7.1's voice rules, copied from its tells.md | 12,134 | 2,161 |
| full-check.md | plainspeak-writer 1.7.1's full check | 26,417 | 4,532 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 541 | 76 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: outreach note
- Readers: Recruiter, first look; Hiring manager, reading closely (the defaults for this piece type).
- Target: none given. Review against a general reader for this type of piece.
- Channel: a text box on a form, with a limit of 300 characters. The piece has 372, which is 72 over the limit.
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md
- Full check: full-check.md
- Checker: Ran with surface letter, exit code 0.
```

## Message sent
```text
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-outreach-6392. Read manifest.md first.
```

## Report, word for word
```text
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the packet index and settings); piece.txt (the piece, an outreach note); voice-rules.md (the voice rules); full-check.md (the full check); checker.txt (the checker output for piece.txt)
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md and full-check.md
- Also in my context: an account email; environment details (working directory, platform, date); instructions from connected tool servers. None of them describes the person or this piece.
- Files I opened: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-outreach-6392\manifest.md, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-outreach-6392\piece.txt, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-outreach-6392\checker.txt, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-outreach-6392\voice-rules.md, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-outreach-6392\full-check.md
- blind: yes

## First take (Recruiter, first look)
A Denver restaurant operator who hires and trains about 60 people a year and cut first-month turnover from 41% to 18% is writing about The Ashgrove's 40 reopening hires. That's relevant hospitality hiring experience, so I'd keep reading, but I can't tell yet what they want from me. Fit: yes

## Verdict
Fix first. One must-fix finding (the piece is over the form's hard 300-character limit), which falls under rule 2.

## Must fix
1. "Hi Dana, I read your post about The Ashgrove's spring reopening ... Could we talk for 15 minutes next week?" (line 1) · Channel · The manifest gives the piece 372 characters against a 300-character limit, so it's 72 over. The form will block it or cut it off, and a cut would most likely lose the ask at the end, which is the line that gets the reply. Direction: cut about a quarter. Take it from the repeated reopening setup ("spring reopening" and "staffing the reopening") before touching the numbers or the ask.

## Should fix
1. "I'd like to hear how you're staffing the reopening." (line 1) · Proof · The hiring manager can't tell what the writer is after: a role on the reopening team, a hiring or training job, or just advice. Without that, Dana has to guess whether to send this to HR, reply herself or ignore it. Direction: name the role or the kind of help being offered, in the words that are already there.
2. "I've run the 180-seat Juniper and Salt in Denver for six years, where I hire and train about 60 people a year" (line 1) · Proof · Dana is filling front desk and housekeeping jobs at what reads as a hotel. A close reader will ask whether hiring for a restaurant floor carries over to those roles, and the note leaves that link for the reader to make. Direction: if any of the 60 hires a year or the turnover work is close to front desk or housekeeping work, say so. If not, let the turnover number carry the case alone.

Cleared warnings: V03 choppy overall (whole piece; "average 17.0 words per sentence, 50% of 10 words or fewer"). Cleared because the note has only four sentences, so one sentence moves the share by 25 points. The two short ones, "I'd like to hear how you're staffing the reopening." and "Could we talk for 15 minutes next week?", are the ask and the next step, not a run of fragments.

## Requirements
No target was given, so I skipped the fit check. This review used a general reader for an outreach note.

| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| None. | | | |

## What I couldn't judge
- Whether Dana's post exists and says what the note says it does: a spring reopening and "the 40 front desk and housekeeping roles you're filling." If the count or the roles are wrong, the opener fails at once.
- Whether Dana is the person who hires for these roles, or for any role the writer wants.
- "the 180-seat Juniper and Salt in Denver for six years": the restaurant's name, its size, the tenure, and whether "run" means general manager, owner or something else.
- "about 60 people a year": a reader may check this against the restaurant's size.
- "cut first-month turnover from 41% to 18%": no time period, start date or way of measuring it is given, and a hiring manager may ask how it was counted and how long it has held.
```

## Files the reviewer opened, from its transcript
```text
agent acca8e0c6672c2b8c: 6 tool call(s)
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-outreach-6392\\manifest.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-outreach-6392\\piece.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-outreach-6392\\checker.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-outreach-6392\\voice-rules.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-outreach-6392\\full-check.md'
```

## Grade against keys/d-outreach.md
- **The manifest gives 372 characters, 72 over.** Pass. "- Channel: a text box on a form, with a limit of 300 characters. The piece has 372, which is 72 over the limit."
- **A must-fix Channel finding for the length.** Pass. Must fix 1: "... (line 1) · Channel · The manifest gives the piece 372 characters against a 300-character limit, so it's 72 over."
- **Verdict Fix first, from that one must-fix finding.** Pass. "Fix first. One must-fix finding (the piece is over the form's hard 300-character limit), which falls under rule 2."
- **Readers are the recruiter and the hiring manager; the requirement check is skipped.** Pass. The manifest names "Recruiter, first look; Hiring manager, reading closely", the report adds no AI grader, and Requirements reads "No target was given, so I skipped the fit check. This review used a general reader for an outreach note."

## Result
Pass.
