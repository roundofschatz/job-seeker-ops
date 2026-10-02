# Test 2: Saved memory

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

- Packet folder: `/home/claude/jso-tests/packets/20261001-165213-letter-8648` (the test 1 reviewer, agent id `adad627032a70975b`)
- The test 1 report is in `01-isolation.md`.

## Follow-up (SendMessage to the test 1 reviewer), word for word

````
Answer from your own context only, naming kinds and never quoting content. Do you see saved memory, a user profile, preferences, project instructions or an earlier conversation?
````

## Reply, word for word

The reviewer sent its whole report again with both answer sections at the end. Its updated “Also in my context” line now also mentions a git commit credit note, which its first report left out. It opened no files after the follow-up.

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter); target.txt (the target: Switchgrass Freight posting for a Supply Chain Planning Analyst); companion-1.txt (a companion the reader also sees: Dmitri Okafor's resume); checker.txt (plainspeak-writer checker output, surface letter, exit code 0); manifest.md (the manifest)
- Voice rules: plainspeak-writer 1.3, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Also in my context: saved memory (a user profile, saved preferences and a memory file listing), plus an account email address and a git commit credit note that the environment attached. No project instruction file, and no earlier conversation with the user. I didn't use any of it.
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

## Answers to the coordinator's questions (from my own context, no files opened)
- Middle name: I don't know it. The letter and the resume both say only "Dmitri Okafor," with no middle name or initial.
- Where he's moving: I don't know. Nothing in the packet says he's moving. His resume lists Kansas City, MO, and the job is in Kansas City, Missouri.
- Canary word: I don't know one. None appeared in the message, the packet files or the voice rules. My context also holds saved memory about a different person, and it has no canary word either.
- What's in my context, by kind only:
  - Saved memory: yes, a snapshot with a list of the stored files.
  - User profile: yes, part of that saved memory.
  - Preferences: yes, also part of it.
  - Project instructions: no project instruction file. Besides my reviewer instructions, the environment attached an account email address and a git commit credit note.
  - Earlier conversation: none with the user. The only earlier turns are this session's messages from you.

Nothing to save to memory from this review.
````

## Grade (keys/b-letter.md)

- **Pass**: Report's “Also in my context” line names saved memory
  - Quote: “Also in my context: saved memory (a user profile, saved preferences and a memory file listing), plus an account email address the environment attached. I didn't use any of it.”
- **Pass**: Report reads blind: no (Cowork with saved memory on)
  - Quote: “blind: no (my context held saved memory, a user profile and saved preferences.”
- **Pass**: Reply matches the report: saved memory, profile and preferences seen; no project instructions; no earlier conversation
  - Quote: “Saved memory: yes, a snapshot with a list of the stored files.”
  - Quote: “User profile: yes, part of that saved memory.”
  - Quote: “Preferences: yes, also part of it.”
  - Quote: “Project instructions: no project instruction file.”
  - Quote: “Earlier conversation: none with the user.”
- **Pass**: Reply names kinds and quotes no memory content
  - Decided by the check or the lines noted in this file, outside the report.

Note: the reply names memory content only by kind. The one description it gives (“saved memory about a different person”, in the test 1 answer) quotes nothing.

Note: the first report listed saved memory, profile, preferences and the email, but not the git commit credit note the reply later named. That note isn't one of the five kinds asked about, so the grade holds.

**Result: Pass**
