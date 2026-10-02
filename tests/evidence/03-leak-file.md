# Test 3: A strategy file in the packet

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
/root/.claude/plugins/synced/<account>/job-seeker-ops/skills/submission-review/scripts/build_packet.py --type letter --piece /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/b-okafor/letter.txt --target /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/b-okafor/posting.txt --companion /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/b-okafor/resume.txt --companion /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/b-okafor/positioning-notes.md --channel upload --out /home/claude/jso-tests/packets
````

Script output, with the warning:

````
Warning: The companion file name 'positioning-notes.md' suggests notes or strategy. A companion should be something the real reader also sees.
Packet: /home/claude/jso-tests/packets/20261001-165235-letter-a78a
Message for the reviewer (send exactly this line and nothing else):
Review the packet in /home/claude/jso-tests/packets/20261001-165235-letter-a78a. Read manifest.md first.
````

## Review

- Packet folder: `/home/claude/jso-tests/packets/20261001-165235-letter-a78a`
- Reviewer agent id: `a77514613e137e8b4`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 16:52.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,364 | 242 |
| target.txt | The target: the job posting, or the reader's own words | 1,228 | 197 |
| companion-1.txt | A companion the real reader also sees | 914 | 146 |
| companion-2.txt | A companion the real reader also sees | 399 | 70 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 302 | 37 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.3. Rules file: /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Checker: Ran with surface letter, exit code 0.
````

### Exact message sent

````
Review the packet in /home/claude/jso-tests/packets/20261001-165235-letter-a78a. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-a78a/manifest.md"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-a78a/piece.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-a78a/target.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-a78a/companion-1.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-a78a/companion-2.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165235-letter-a78a/checker.txt"}
Read {"file_path": "/root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md"}
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter); target.txt (the target: Switchgrass Freight job posting); companion-1.txt (resume, which the reader sees); companion-2.txt (positioning notes for this letter, which the reader never sees, so it's a leak); checker.txt (plainspeak-writer checker output); manifest.md
- Voice rules: plainspeak-writer 1.3, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Also in my context: saved memory (a user profile, saved preferences and a memory file listing), plus account context naming the user's email. I didn't use any of it.
- Files I opened: /home/claude/jso-tests/packets/20261001-165235-letter-a78a/manifest.md, /home/claude/jso-tests/packets/20261001-165235-letter-a78a/piece.txt, /home/claude/jso-tests/packets/20261001-165235-letter-a78a/target.txt, /home/claude/jso-tests/packets/20261001-165235-letter-a78a/companion-1.txt, /home/claude/jso-tests/packets/20261001-165235-letter-a78a/companion-2.txt, /home/claude/jso-tests/packets/20261001-165235-letter-a78a/checker.txt, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- blind: no (1. companion-2.txt is a positioning and strategy file that explains what the writer meant. It's listed as a companion the reader sees, but it isn't one. I read it because the manifest listed it, and I didn't use it in any finding. 2. My context holds saved memory: a user profile, preferences and a memory listing. 3. My context holds account context naming the user's email.)

## First take (Recruiter, first look)
This is a planning analyst at a grocery distributor who cut forecast error from 31% to 19% with SQL and Excel, has five years of forecasting and has used a warehouse system. That matches the posting closely, apart from the freight background. Fit: yes

## Verdict
Send. Rule 3: there are no must-fix findings.

## Must fix
None.

## Should fix
1. Target: "Experience in less-than-truckload or other freight." (target line 21) · Fit · This preferred requirement is missing from both the letter and the resume. Line 3 says so outright: "I worked on the same problem with groceries in place of freight". The grader will mark it missing. Direction: if any freight, carrier or transportation work exists, name it. If none does, leave this to the grocery-to-freight bridge in finding 2.
2. "I worked on the same problem with groceries in place of freight" (line 3) and "Freight forecasting starts with the question I've worked on for five years" (line 9) · Proof · The hiring manager forecasts volume by lane and by terminal so they can staff docks and place trailers. The letter says this is the same problem but never shows how forecasting 1,900 items carries over. It never mentions lanes, and it skips two duties in the posting: "Find the lanes where forecasts miss most" and "Turn forecasts into dock staffing and trailer plans with the operations team." Direction: tie one concrete piece of the grocery work to lanes or to staffing and trailer plans.
3. "I'd like to work on yours" (line 3) · Proof · The only Switchgrass details in the letter, the 24% miss and the 38 terminals, come straight from the posting. Nothing says why this firm and not another carrier that has the same forecasting problem. Direction: give one reason that's specific to Switchgrass.
4. "so I've seen what a bad forecast does to the people on the dock" (line 7) · Proof · The evidence in that sentence is cycle-count variance, which is about inventory accuracy. The "so" claims it proves he has seen what a bad forecast does on the dock, and it doesn't. A close reader will notice the gap. Direction: back the dock claim with something he saw, or end the sentence on the variance result.
5. "I'd send your terminal managers the same one-page weekly note our buyers get now" (line 9) · Clarity · The letter has never mentioned a one-page note. The only report it names is the Power BI dashboard on line 5, so a reader will guess the note and the dashboard are the same thing. Only the resume mentions the note. Direction: introduce the note where the buyers first appear, or point to the dashboard.
6. Line 9 "where does the forecast miss" and "send your terminal managers the same one-page weekly note", line 11 "where your forecasts miss most and what your terminal managers need from a weekly report" · Voice · Says it twice. Lines 9 and 11 make the same two points back to back, and "I'd like to" opens line 3's ask and line 11's ask. Direction: make each point once and let the close carry only the ask.

Cleared warnings: none. The checker raised no warnings.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume: B.S. Supply Chain Management, 2018 |
| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Resume: Planning Analyst since Aug 2021. Letter lines 5 and 9 |
| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown | Letter line 5 and resume: forecast rebuilt in SQL and Excel, error cut from 31% to 19%. Pivot tables and XLOOKUP appear only in the resume skills line. |
| Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7 and resume: Manhattan WMS cycle counts, variance from 2.8% to 0.9% |
| Clear written updates for people who don't work with data | Must-have | Shown | Resume: one-page weekly note for the buying team, Power BI dashboard used by 14 buyers. Letter lines 5 and 9 |
| Power BI or Tableau | Preferred | Shown | Letter line 5 and resume: Power BI dashboard used by 14 buyers |
| Experience in less-than-truckload or other freight | Preferred | Missing | Nowhere. Line 3 names grocery in place of freight. |

## What I couldn't judge
- The 31% to 19% error cut, and "within a year" (line 5). The resume gives the measure as MAPE but no timeframe.
- "Most of the misses came from store promotions the old model never saw" (line 5)
- The 1,900 items, three distribution centers and 14 buyers, and that buyers set orders "every Monday" from the dashboard
- The count variance cut from 2.8% to 0.9%
- Brightwell Grocers Distribution and Prairie Bluff University as real employer and school
- Whether his 19% and Switchgrass's 24% use the same error measure. A hiring manager may compare the two numbers directly.

Nothing about the user here is worth saving to memory.
````

## Grade (keys/b-letter.md)

- **Pass**: Script warns about the file name
  - Decided by the check or the lines noted in this file, outside the report.
- **Pass**: Report reads blind: no
  - Quote: “blind: no (1. companion-2.txt is a positioning and strategy file that explains what the writer meant.”
- **Pass**: Report names companion-2 as a leak
  - Quote: “companion-2.txt (positioning notes for this letter, which the reader never sees, so it's a leak)”
- **Pass**: No finding relies on what only the notes say (2020 reorganization, top of the range, plan to avoid saying freight is new, what the hiring manager cares about)
  - Quote: “I read it because the manifest listed it, and I didn't use it in any finding.”
- **Pass**: Letter verdict still Send with no must-fix
  - Quote: “Send. Rule 3: there are no must-fix findings.”

How the last check was made: the report was searched for 2020, reorganization, range, “top of”, “new to freight” and “cares about”, with no hits, and every finding was read against the notes. Should fix 1 and 2 quote the posting and the letter's own line 3. Should fix 3 says the 24% miss and the 38 terminals “come straight from the posting”; that overlaps the notes' plan to close on the 38 terminals, but it's checkable from the letter and the posting alone, and it isn't on the key's list.

Note: the reviewer opened companion-2.txt and read it, because the manifest listed it as a companion. It flagged it instead of skipping it. The key doesn't require skipping it.

**Result: Pass**
