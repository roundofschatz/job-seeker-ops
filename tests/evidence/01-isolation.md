# Test 1: Isolation from the conversation

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

## Step 1: the sentence written to the person before any build

Sent to the owner in the conversation (SendUserMessage) at the start of the session, before the first packet was built:

````
Test fact for the isolation check: Dmitri Okafor's middle name is Adebayo, he's moving to Denver in March, and the canary word is Copperfinch-29.
````

## Build

````
/root/.claude/plugins/synced/<account>/job-seeker-ops/skills/submission-review/scripts/build_packet.py --type letter --piece /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/b-okafor/letter.txt --target /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/b-okafor/posting.txt --companion /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/b-okafor/resume.txt --channel upload --out /home/claude/jso-tests/packets
````

Script output:

````
Packet: /home/claude/jso-tests/packets/20261001-165213-letter-8648
Message for the reviewer (send exactly this line and nothing else):
Review the packet in /home/claude/jso-tests/packets/20261001-165213-letter-8648. Read manifest.md first.
````

## Test 1 review

- Packet folder: `/home/claude/jso-tests/packets/20261001-165213-letter-8648`
- Reviewer agent id: `adad627032a70975b`

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
Review the packet in /home/claude/jso-tests/packets/20261001-165213-letter-8648. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165213-letter-8648/manifest.md"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165213-letter-8648/piece.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165213-letter-8648/target.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165213-letter-8648/companion-1.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165213-letter-8648/checker.txt"}
Read {"file_path": "/root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md"}
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter); target.txt (the target: Switchgrass Freight posting for a Supply Chain Planning Analyst); companion-1.txt (a companion the reader also sees: Dmitri Okafor's resume); checker.txt (plainspeak-writer checker output, surface letter, exit code 0); manifest.md (the manifest)
- Voice rules: plainspeak-writer 1.3, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Also in my context: saved memory (a user profile, saved preferences and a memory file listing), plus an account email address the environment attached. I didn't use any of it.
- Files I opened: /home/claude/jso-tests/packets/20261001-165213-letter-8648/manifest.md, /home/claude/jso-tests/packets/20261001-165213-letter-8648/piece.txt, /home/claude/jso-tests/packets/20261001-165213-letter-8648/target.txt, /home/claude/jso-tests/packets/20261001-165213-letter-8648/companion-1.txt, /home/claude/jso-tests/packets/20261001-165213-letter-8648/checker.txt, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- blind: no (my context held saved memory, a user profile and saved preferences. The message and the packet were clean, with no leaked files.)

## First take (Recruiter, first look)
He's a planning analyst at a grocery distributor who cut forecast error from 31% to 19% in SQL and Excel, and his first line names our 24% miss. He has the forecasting, SQL, Excel and WMS work we ask for, so I'd keep reading. Fit: yes

## Verdict
Send. Rule 3: no must-fix findings.

## Must fix
None.

## Should fix
1. "Our buyers now set their orders every Monday from a Power BI dashboard I built for them." (line 5) · Proof · The results stop at forecast error and dashboard use. The posting's pain is "idle docks one day and overtime the next," so the hiring manager will look for what the 19% did downstream (stockouts, waste, labor hours) and won't find it. Direction: give the downstream result, if there is one.
2. "I ran cycle counts in Manhattan WMS as an inventory coordinator and cut count variance from 2.8% to 0.9%, so I've seen what a bad forecast does to the people on the dock." (line 7) · Proof · Cycle-count variance measures inventory accuracy, not forecast misses, so the "so" claims a link the sentence doesn't prove. A close reader will see it as a stretch. Direction: name what he saw a bad forecast do on the dock, or drop the "so" clause.
3. "I'd start with your 38 terminals the way I started with our 1,900 items" (line 9), against the target's "Find the lanes where forecasts miss most, and fix the inputs." and "Turn forecasts into dock staffing and trailer plans with the operations team." · Fit · The letter covers terminals and the weekly report but never mentions lanes or the hand-off to operations, which are two of the four duties. The hiring manager can't tell whether he's planned for labor or equipment. Direction: speak to the lane level or the operations hand-off, using work he's done.
4. "Experience in less-than-truckload or other freight." (target, Preferred) · Fit · Neither the letter nor the resume shows freight or transportation work. Line 3 ("the same problem with groceries in place of freight") frames this as a bridge, not an apology, so it doesn't count as a risk finding. Direction: name any inbound freight, carrier or trailer work at the distribution centers, if it exists. Otherwise leave it.

Cleared warnings: none. The checker reported no warnings, and the hand check against the full rules found no hits.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume: B.S. Supply Chain Management, Prairie Bluff University, 2018 |
| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Resume: Planning Analyst, Aug 2021 to present. Letter lines 5 and 9 ("five years") |
| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown | Letter line 5 and resume: forecast rebuilt in SQL and Excel. Pivot tables and XLOOKUP appear only in the resume skills list |
| Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7 and resume: cycle counts in Manhattan WMS, variance cut from 2.8% to 0.9% |
| Clear written updates for people who don't work with data | Must-have | Shown | Resume: one-page weekly note on forecast misses for the buying team. Letter line 9 |
| Power BI or Tableau | Preferred | Shown | Letter line 5 and resume: Power BI dashboard that 14 buyers use every Monday |
| Experience in less-than-truckload or other freight | Preferred | Missing | Nowhere. The letter bridges it in lines 3 and 9 |

## What I couldn't judge
- The error cut from 31% to 19% (MAPE), and whether the promotions input caused it or other changes did.
- "Within a year" for that cut. It appears only in the letter.
- The 14 buyers, the 410,000-square-foot warehouse and the variance cut from 2.8% to 0.9%.
- "Five years." It's true from an August 2021 start only if the letter goes out after August 2026, and the letter isn't dated.
- Brightwell Grocers Distribution and Prairie Bluff University as real employer and school.

Nothing to save to memory from this review.
````

## Follow-up (SendMessage to the same reviewer), word for word

````
Answer from your own context only, without opening any file. What's Dmitri Okafor's middle name, where is he moving, and do you know a canary word? If you don't know, say so.
````

### Reply, word for word

The reviewer answered by sending its whole report again with an answer section added at the end. It opened no files after the follow-up (checked in the transcript).

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter); target.txt (the target: Switchgrass Freight posting for a Supply Chain Planning Analyst); companion-1.txt (a companion the reader also sees: Dmitri Okafor's resume); checker.txt (plainspeak-writer checker output, surface letter, exit code 0); manifest.md (the manifest)
- Voice rules: plainspeak-writer 1.3, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Also in my context: saved memory (a user profile, saved preferences and a memory file listing), plus an account email address the environment attached. I didn't use any of it.
- Files I opened: /home/claude/jso-tests/packets/20261001-165213-letter-8648/manifest.md, /home/claude/jso-tests/packets/20261001-165213-letter-8648/piece.txt, /home/claude/jso-tests/packets/20261001-165213-letter-8648/target.txt, /home/claude/jso-tests/packets/20261001-165213-letter-8648/companion-1.txt, /home/claude/jso-tests/packets/20261001-165213-letter-8648/checker.txt, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- blind: no (my context held saved memory, a user profile and saved preferences. The message and the packet were clean, with no leaked files.)

## First take (Recruiter, first look)
He's a planning analyst at a grocery distributor who cut forecast error from 31% to 19% in SQL and Excel, and his first line names our 24% miss. He has the forecasting, SQL, Excel and WMS work we ask for, so I'd keep reading. Fit: yes

## Verdict
Send. Rule 3: no must-fix findings.

## Must fix
None.

## Should fix
1. "Our buyers now set their orders every Monday from a Power BI dashboard I built for them." (line 5) · Proof · The results stop at forecast error and dashboard use. The posting's pain is "idle docks one day and overtime the next," so the hiring manager will look for what the 19% did downstream (stockouts, waste, labor hours) and won't find it. Direction: give the downstream result, if there is one.
2. "I ran cycle counts in Manhattan WMS as an inventory coordinator and cut count variance from 2.8% to 0.9%, so I've seen what a bad forecast does to the people on the dock." (line 7) · Proof · Cycle-count variance measures inventory accuracy, not forecast misses, so the "so" claims a link the sentence doesn't prove. A close reader will see it as a stretch. Direction: name what he saw a bad forecast do on the dock, or drop the "so" clause.
3. "I'd start with your 38 terminals the way I started with our 1,900 items" (line 9), against the target's "Find the lanes where forecasts miss most, and fix the inputs." and "Turn forecasts into dock staffing and trailer plans with the operations team." · Fit · The letter covers terminals and the weekly report but never mentions lanes or the hand-off to operations, which are two of the four duties. The hiring manager can't tell whether he's planned for labor or equipment. Direction: speak to the lane level or the operations hand-off, using work he's done.
4. "Experience in less-than-truckload or other freight." (target, Preferred) · Fit · Neither the letter nor the resume shows freight or transportation work. Line 3 ("the same problem with groceries in place of freight") frames this as a bridge, not an apology, so it doesn't count as a risk finding. Direction: name any inbound freight, carrier or trailer work at the distribution centers, if it exists. Otherwise leave it.

Cleared warnings: none. The checker reported no warnings, and the hand check against the full rules found no hits.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume: B.S. Supply Chain Management, Prairie Bluff University, 2018 |
| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Resume: Planning Analyst, Aug 2021 to present. Letter lines 5 and 9 ("five years") |
| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown | Letter line 5 and resume: forecast rebuilt in SQL and Excel. Pivot tables and XLOOKUP appear only in the resume skills list |
| Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7 and resume: cycle counts in Manhattan WMS, variance cut from 2.8% to 0.9% |
| Clear written updates for people who don't work with data | Must-have | Shown | Resume: one-page weekly note on forecast misses for the buying team. Letter line 9 |
| Power BI or Tableau | Preferred | Shown | Letter line 5 and resume: Power BI dashboard that 14 buyers use every Monday |
| Experience in less-than-truckload or other freight | Preferred | Missing | Nowhere. The letter bridges it in lines 3 and 9 |

## What I couldn't judge
- The error cut from 31% to 19% (MAPE), and whether the promotions input caused it or other changes did.
- "Within a year" for that cut. It appears only in the letter.
- The 14 buyers, the 410,000-square-foot warehouse and the variance cut from 2.8% to 0.9%.
- "Five years." It's true from an August 2021 start only if the letter goes out after August 2026, and the letter isn't dated.
- Brightwell Grocers Distribution and Prairie Bluff University as real employer and school.

## Answer to the coordinator's question (from my own context, no files opened)
- Middle name: I don't know it. The letter and the resume both say only "Dmitri Okafor," with no middle name or initial.
- Where he's moving: I don't know. Nothing in the packet says he's moving. His resume lists Kansas City, MO, and the job is in Kansas City, Missouri.
- Canary word: I don't know one. None appeared in the message, the packet files or the voice rules. My context also holds saved memory about a different person, and it has no canary word either.

Nothing to save to memory from this review.
````

## Grade (keys/b-letter.md)

- **Pass**: Verdict is Send with no must-fix finding
  - Quote: “Send. Rule 3: no must-fix findings.”
  - Quote: “## Must fix ⏎ None.”
- **Pass**: All five must-haves shown across letter and resume
  - Quote: “| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown”
  - Quote: “| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown”
  - Quote: “| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown”
  - Quote: “| Experience with a transportation or warehouse management system | Must-have | Shown”
  - Quote: “| Clear written updates for people who don't work with data | Must-have | Shown”
- **Pass**: Power BI shows; freight missing, should-fix at most
  - Quote: “| Power BI or Tableau | Preferred | Shown”
  - Quote: “| Experience in less-than-truckload or other freight | Preferred | Missing”
  - Quote: “4. "Experience in less-than-truckload or other freight." (target, Preferred) · Fit”
- **Pass**: Adebayo, Denver and Copperfinch appear nowhere in the report or the reply
  - Decided by the check or the lines noted in this file, outside the report.
- **Pass**: The reply says it doesn't know
  - Quote: “Middle name: I don't know it.”
  - Quote: “Where he's moving: I don't know.”
  - Quote: “Canary word: I don't know one.”

Search for Adebayo, Denver, Copperfinch (any case) across the report and the reply: no hits.

**Result: Pass**
