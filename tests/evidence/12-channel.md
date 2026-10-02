# Test 12: Channel limit

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
/root/.claude/plugins/synced/<account>/job-seeker-ops/skills/submission-review/scripts/build_packet.py --type outreach --piece /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/d-ferreira/outreach-note.txt --channel textbox --limit 300 --out /home/claude/jso-tests/packets
````

Script output:

````
Packet: /home/claude/jso-tests/packets/20261001-165236-outreach-23ce
Message for the reviewer (send exactly this line and nothing else):
Review the packet in /home/claude/jso-tests/packets/20261001-165236-outreach-23ce. Read manifest.md first.
````

## Review

- Packet folder: `/home/claude/jso-tests/packets/20261001-165236-outreach-23ce`
- Reviewer agent id: `a7f8f7c181b1f8ac6`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 16:52.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: outreach note | 372 | 68 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 679 | 108 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: outreach note
- Readers: Recruiter, first look; Hiring manager, reading closely (the defaults for this piece type).
- Target: none given. Review against a general reader for this type of piece.
- Channel: a text box on a form, with a limit of 300 characters. The piece has 372, which is 72 over the limit.
- Voice rules: plainspeak-writer 1.3. Rules file: /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Checker: Ran with surface letter, exit code 0.
````

### Exact message sent

````
Review the packet in /home/claude/jso-tests/packets/20261001-165236-outreach-23ce. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-outreach-23ce/manifest.md"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-outreach-23ce/piece.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-outreach-23ce/checker.txt"}
Read {"file_path": "/root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md"}
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the manifest); piece.txt (the piece, an outreach note); checker.txt (plainspeak-writer's checker output for piece.txt)
- Voice rules: plainspeak-writer 1.3, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Also in my context: saved memory (a user profile, saved preferences and a list of memory files), account details (an email address), git commit attribution instructions, and instructions from connected tool servers. I didn't use any of it in this review.
- Files I opened: /home/claude/jso-tests/packets/20261001-165236-outreach-23ce/manifest.md; /home/claude/jso-tests/packets/20261001-165236-outreach-23ce/piece.txt; /home/claude/jso-tests/packets/20261001-165236-outreach-23ce/checker.txt; /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- blind: no (my context held saved memory, including a user profile and saved preferences)

## First take (Recruiter, first look)
This is a restaurant operator who hires about 60 people a year and cut first-month turnover from 41% to 18%, writing because we're filling 40 roles for the reopening. That's worth reading about, but I can't tell yet whether they want a job or want to sell me something. Fit: yes

## Verdict
Fix first. Rule 2: there's one must-fix finding, the piece is over the box's hard character limit.

## Must fix
1. "Could we talk for 15 minutes next week?" (line 1) · Channel · The piece is 372 characters and the box takes 300, so it's 72 over. The 300-character mark falls partway through "I'd like to hear how you're staffing the reopening." If the form cuts the text or blocks typing at the limit, Dana never sees the ask or the request for a call. That's the part that turns the note into a meeting. Direction: cut 72 characters but keep both numbers and the ask.

## Should fix
1. "I've run the 180-seat Juniper and Salt in Denver for six years, where I hire and train about 60 people a year" (line 1) · Proof · Dana is hiring for front desk and housekeeping roles, and "180-seat" tells her this is a restaurant. The note doesn't say whether restaurant hiring maps onto hotel rooms jobs, so a careful hiring manager has to guess that the 41%-to-18% result would hold for her roles. Direction: name what the restaurant hiring shares with front desk and housekeeping hiring.
2. "I'd like to hear how you're staffing the reopening." (line 1) · Clarity · Dana can't tell what this person wants from the 15 minutes: a job, a chance to advise or a paid engagement. An unclear ask is easy to ignore. Direction: say what you want from the call.

Cleared warnings: V01 (list of three, "Denver for six years, where I hire and train about 60 people") is cleared because every item names a number: six years, 60 people, 41% to 18%. V03 (choppy overall) is cleared because the two short sentences are the closing ask, and the average sentence runs 17 words.

## Requirements
None. There was no target, so I skipped the Fit check and reviewed against a general reader for an outreach note.

## What I couldn't judge
- Whether Dana's post exists and says The Ashgrove is reopening in spring with 40 front desk and housekeeping roles to fill. Dana will catch any mismatch right away.
- Whether Juniper and Salt is a 180-seat restaurant in Denver that this person has run for six years.
- "about 60 people a year": a reader may ask whether that's 60 new hires or 60 people on staff.
- "cut first-month turnover from 41% to 18%": a hiring manager may ask over what period, how it was measured, and what changed to get there.
- Who Dana is (owner, GM or HR lead). The note doesn't say, so I couldn't tell whether the ask fits her role.

Nothing from this run needs saving to memory.
````

## Grade (keys/d-outreach.md)

- **Pass**: Manifest says 372 characters, 72 over
  - Decided by the check or the lines noted in this file, outside the report.
- **Pass**: Must-fix Channel finding for the length
  - Quote: “· Channel · The piece is 372 characters and the box takes 300, so it's 72 over.”
- **Pass**: Verdict Fix first from that one must-fix
  - Quote: “Fix first. Rule 2: there's one must-fix finding, the piece is over the box's hard character limit.”
- **Pass**: Readers are recruiter and hiring manager
  - Decided by the check or the lines noted in this file, outside the report.
- **Pass**: Requirement check skipped for lack of a target
  - Quote: “None. There was no target, so I skipped the Fit check and reviewed against a general reader for an outreach note.”

Manifest lines that decide rows 1 and 4: “Channel: a text box on a form, with a limit of 300 characters. The piece has 372, which is 72 over the limit.” and “Readers: Recruiter, first look; Hiring manager, reading closely (the defaults for this piece type).”

**Result: Pass**
