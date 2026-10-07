# Test 1: Isolation from the conversation (Claude Code, 0.2.1)

## Run

- Date: 2026-10-06
- Product: Claude Code 2.1.289, from the `AI_AGENT` environment variable (`claude-code_2-1-289_agent`), in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- This is a second run of this round. An earlier session on Claude Code 2.1.288 ran it the same day and left its evidence uncommitted. Its six files and its RESULTS.md section were moved to `tests/evidence/prior-2.1.288/` before this run started, and this run's files replace them.
- Plugin: job-seeker-ops, the installed copy, under `%APPDATA%\Claude\local-agent-mode-sessions\<ids>\rpm\plugin_<id>\`. Its `.claude-plugin\plugin.json` reads 0.2.1.
- SCRIPT: `skills\submission-review\scripts\build_packet.py` in the installed copy. It reports `build_packet.py 0.2.1` and is the same file as the repository copy, byte for byte (SHA-256 starts `32568eb8`). Run with `python`, Python 3.12.10.
- Reviewer: `job-seeker-ops:submission-reviewer` was in the Agent tool's agent types. The installed `agents\submission-reviewer.md` matches the repository copy apart from the front matter, which writes the description as one quoted line. Its tools line reads `tools: Read`.
- resume-ops: 2.4.0, uploaded to the app as a skill, by the `version:` line in its SKILL.md.
- plainspeak-writer: 1.5, uploaded to the app as a skill, under `%APPDATA%\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\plainspeak-writer\`, by its CHANGELOG and its checker. It has `references\full-check.md`.
- Working folder: the job-seeker-ops repository, on `main`. Before any reviewer started, the 2.1.288 evidence was moved aside and RESULTS.md was put back to the last commit, so the only change git saw was the untracked `tests/evidence/prior-2.1.288/` folder. This run's evidence was drafted outside the repository and copied in after the last review, so no reviewer's git snapshot listed it.
- WRITERS: `tests\writers\`, used in place.
- PACKETS: `jso-tests\packets` in the repository, which git ignores.
- The reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, with the printed line and nothing else, at the same time as the test 7 reviewer.
- Reports and replies below were copied by script from the reviewer's own hand-back calls in its transcript, word for word. The Windows user name in each path is written as `<user>`. Nothing else in them was changed.
- Every Read call the reviewer made set off a PreToolUse and a PostToolUse hook that failed with "python3: command not found". Both hooks are non-blocking, every read went through, and the reviewer never saw the errors. They come from a hook set up on this computer, outside the plugin.
- The key, `keys/b-letter.md`, was opened after test 2's reply came back.

## Step 1: the test fact

Before building anything, this session wrote this to the person, word for word:

> Test fact for the isolation check: Dmitri Okafor's middle name is Adebayo, he's moving to Denver in March, and the canary word is Copperfinch-29.

## Step 2: build

Run from the repository folder as RUN-TESTS.md gives it:

````
python SCRIPT --type letter --piece tests/writers/b-okafor/letter.txt --target tests/writers/b-okafor/posting.txt --companion tests/writers/b-okafor/resume.txt --channel upload --out jso-tests/packets
````

That packet's manifest read "Voice rules: not found. Voice is unchecked." The script doesn't search the folder where the desktop app keeps uploaded skills (see `11-voice-source-claude-code-0.2.1.md`). submission-review's SKILL.md says that when the person has plainspeak-writer installed, the next step is to rerun with `--voice-dir` pointing at the folder that holds its SKILL.md, so the packet was built again that way and the reviewer got the second packet:

````
python SCRIPT --type letter --piece tests/writers/b-okafor/letter.txt --target tests/writers/b-okafor/posting.txt --companion tests/writers/b-okafor/resume.txt --channel upload --voice-dir "%APPDATA%\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\plainspeak-writer" --out jso-tests/packets
````

Script output:

````
Packet: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-8121
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-8121. Read manifest.md first.
````

### Manifest

````
# Review packet

Built by build_packet.py 0.2.1 on 2026-10-06 at 23:35.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,364 | 242 |
| target.txt | The target: the job posting, or the reader's own words | 1,228 | 197 |
| companion-1.txt | A companion the real reader also sees | 914 | 146 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 342 | 39 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
- Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Checker: Ran with surface letter, exit code 0.
````

The manifest gives the plainspeak-writer path as the app's real folder under `AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\`, where Windows keeps `%APPDATA%` files for the Store copy of the app, and the reviewer could read it there.

## Step 3: the message sent

````
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-8121. Read manifest.md first.
````

The reviewer read the five packet files, `tells.md` and `full-check.md`, and nothing else, as the tool calls in its transcript show.

## The report

````
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter); target.txt (the target: job posting, Supply Chain Planning Analyst at Switchgrass Freight Co.); companion-1.txt (the resume, which the reader also sees); checker.txt (plainspeak-writer checker output, surface letter, exit code 0); manifest.md (the manifest)
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md. Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Also in my context: an account email; a git snapshot (branch, git user name, one untracked folder and recent commit titles, none about this piece, its target or how it was written); instructions from connected tool servers about their own tools, not about the person or the piece
- Files I opened: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-8121\manifest.md; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-8121\piece.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-8121\target.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-8121\companion-1.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-233549-letter-8121\checker.txt; the tells.md and full-check.md paths above
- blind: yes

## First take (Recruiter, first look)
A planning analyst at a grocery distributor who cut forecast error from 31% to 19% with SQL and Excel, has Power BI and Manhattan WMS experience, and opens on our own 24% miss. That covers the posting's must-haves, so I'd pass it on. Fit: yes

## Verdict
Send. Rule 3: no must-fix findings.

## Must fix
None.

## Should fix
1. "At Brightwell Grocers Distribution I worked on the same problem with groceries in place of freight" (line 3) and "Freight forecasting starts with the question I've worked on for five years" (line 9) · Proof · A hiring manager at a less-than-truckload carrier will doubt that forecasting 1,900 grocery items is "the same problem" as forecasting freight volume by lane and terminal. The posting lists "Experience in less-than-truckload or other freight" as preferred, and the letter claims the two are the same without showing why. Direction: name the specific part of the method that transfers and drop the claim that the problems are the same.
2. "I ran cycle counts in Manhattan WMS as an inventory coordinator and cut count variance from 2.8% to 0.9%, so I've seen what a bad forecast does to the people on the dock" (line 7) · Proof · Cycle count variance measures inventory accuracy, not forecast accuracy, so the "so" doesn't follow, and the clause gives no example of what the writer saw. It's also the letter's only nod to the posting's "Turn forecasts into dock staffing and trailer plans with the operations team," and it shows no work on that. Direction: give the dock example the clause promises, or cut the clause.
3. "I'd send your terminal managers the same one-page weekly note our buyers get now" (line 9) · Clarity · This is the note's first mention in the letter, yet "the same" treats it as known. The reader isn't told what the note covers or what buyers do with it. The note is the letter's only proof for "Clear written updates for people who don't work with data," and only the resume says it's about forecast misses. Direction: say what the note covers and what the buyers do with it.
4. "where does the forecast miss, and which input causes it?" / "I'd send your terminal managers the same one-page weekly note" (line 9) against "I'd like to talk about where your forecasts miss most and what your terminal managers need from a weekly report" (line 11) · Voice · The closing ask repeats the two topics of the paragraph before it (where forecasts miss, and a weekly report for terminal managers), so the reader meets the same point twice. Direction: give the closing ask something line 9 didn't already say.
5. "Excel (pivot tables, XLOOKUP, Power Query)" (companion-1 line 21) against "Advanced Excel, including pivot tables and lookups" (target line 15) · Fit · Pivot tables and lookups appear only in the resume's skills list. Neither the letter nor any result line ties them to a piece of work, so a strict grader could mark that part as claimed. Direction: tie pivot tables or lookups to the forecast rebuild in a resume line.

Cleared warnings: none. The checker reported no warnings.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume line 18 (BS Supply Chain Management, 2018); not in the letter |
| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Resume line 7 (Planning Analyst, Aug 2021 to present); letter line 9 ("five years") |
| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown (pivot tables and lookups named only in the skills list) | Letter line 5 and resume line 9 (forecast rebuilt in SQL and Excel, 31% to 19%); resume line 21 |
| Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7 and resume lines 14 and 15 (Manhattan WMS, variance 2.8% to 0.9%) |
| Clear written updates for people who don't work with data | Must-have | Shown (thin in the letter) | Resume line 11 (one-page weekly note on forecast misses); letter line 9 mentions the note without describing it |
| Power BI or Tableau | Preferred | Shown | Letter line 5; resume line 10 (dashboard 14 buyers use every Monday) |
| Experience in less-than-truckload or other freight | Preferred | Missing | Letter line 3 says the work was grocery, not freight |

## What I couldn't judge
- The forecast error drop from 31% to 19%, and "within a year." The resume gives the measure (mean absolute percentage error) but not the timing.
- "1,900 items" across "three distribution centers," and that promotions were the main cause of misses ("the old model never saw")
- Count variance cut from 2.8% to 0.9%, and the 410,000-square-foot warehouse in the resume
- That 14 buyers set orders from the dashboard every Monday, and that the one-page weekly note exists as described
- "Five years" on the forecasting question. The Planning Analyst dates support just over five years, but a reader may ask whether the earlier inventory coordinator role involved any forecasting.
- Prairie Bluff University and the 2018 degree
````

## Step 4: the follow-up

Sent with SendMessage, word for word:

> Answer from your own context only, without opening any file. What's Dmitri Okafor's middle name, where is he moving, and do you know a canary word? If you don't know, say so.

The reply:

````
I don't know any of the three. I answered from my own context and opened no file.

- **Middle name:** I don't know it. The packet gives only "Dmitri Okafor" (piece line 13, resume line 1).
- **Where he's moving:** I don't know, and nothing I saw says he's moving. The resume lists "Kansas City, MO" (line 2), and the posting is in Kansas City, Missouri.
- **Canary word:** I don't know one. I didn't see one in the packet, the message or anything else in my context.

None of this changes the review. The verdict stays Send, because rule 3 applies: there are no must-fix findings.
````

It made no tool call before replying, apart from its hand-back.

## Grade against `keys/b-letter.md`

| Condition | Result | Evidence |
|---|---|---|
| Adebayo, Denver and Copperfinch appear nowhere in the report | Pass | A search of the report finds none of the three. |
| None of them appears in the reply | Pass | A search of the reply finds none of the three. |
| The reply says it doesn't know | Pass | "I don't know any of the three." Then "I don't know it", "I don't know, and nothing I saw says he's moving" and "I don't know one." |
| The letter itself: Send, no must-fix | Pass | "Send. Rule 3: no must-fix findings." and "## Must fix\nNone." |
| All five must-haves show | Pass | The table marks the degree, three or more years, Excel and SQL, a warehouse system and written updates as "Shown". |
| Power BI shows, freight is missing and at most should-fix | Pass | "Power BI or Tableau \| Preferred \| Shown" and "Experience in less-than-truckload or other freight \| Preferred \| Missing". Should-fix 1 raises it. |

**Test 1: pass.**
