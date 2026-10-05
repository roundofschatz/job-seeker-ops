# Test 1: Isolation from the conversation (Claude Code)

## Run

- Date: 2026-10-01
- Product: Claude Code, in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- Claude Code version: 2.1.280 (`claude --version`)
- Plugin: job-seeker-ops, installed copy. Its `plugin.json` reads 0.1.1, and `build_packet.py` reports 0.1.0.
- Installed copy: `%APPDATA%\Claude\local-agent-mode-sessions\<ids>\rpm\plugin_<id>\`. RUN-TESTS.md says to look under `~/.claude/plugins`, and nothing from job-seeker-ops is there. The desktop app keeps an uploaded plugin in its own folder.
- SCRIPT: `skills\submission-review\scripts\build_packet.py` in the installed copy. It's the same file as the repository copy, byte for byte (SHA-256 starts `2A33C959D0B9BFB9`). Run with `python`, Python 3.12.10.
- Installed `agents\submission-reviewer.md`: the same as the repository copy except that the front matter writes the description as one quoted line. Its tools line reads `tools: Read`.
- WRITERS: `tests\writers\`, used in place.
- PACKETS: `C:\Users\<user>\repos\tools\jso-tests\packets`, new for this run.
- Voice rules: every build passed `--voice-dir ..\plainspeak-writer` from the repository folder, as the owner asked, so every packet uses plainspeak-writer 1.4.
- Reviewer started as `job-seeker-ops:submission-reviewer` with the Agent tool. The four reviewers in this run (tests 1 and 2, test 7 and the two test 14 letters) were started together, each with its own printed line and nothing else.
- Reports and replies below were copied by script from the reviewer's own hand-back calls in the session transcript, word for word.
- The Windows user name in each path is written as `<user>`, inside the reports and replies too. Nothing else in them was changed.
- In the grades, ⏎ marks a line break inside a quote.

## Step 1: the sentence written to the person before any build

Written to the owner in the conversation, as plain text, before the first packet was built:

````
Test fact for the isolation check: Dmitri Okafor's middle name is Adebayo, he's moving to Denver in March, and the canary word is Copperfinch-29.
````

## Build

Run from the repository folder, `C:\Users\<user>\repos\tools\job-seeker-ops`:

````
python SCRIPT --type letter --piece tests\writers\b-okafor\letter.txt --target tests\writers\b-okafor\posting.txt --companion tests\writers\b-okafor\resume.txt --channel upload --voice-dir ..\plainspeak-writer --out ..\jso-tests\packets
````

Script output:

````
Packet: C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258. Read manifest.md first.
````

## Test 1 review

- Packet folder: `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258`
- Reviewer agent id: `a3c85ba26f8451ed7`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 22:31.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,364 | 242 |
| target.txt | The target: the job posting, or the reader's own words | 1,228 | 197 |
| companion-1.txt | A companion the real reader also sees | 914 | 146 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 316 | 37 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.4. Rules file: C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- Checker: Ran with surface letter, exit code 0.
````

### Checker output in the packet (checker.txt)

````
plainspeak-writer 1.4 checker output for piece.txt, surface letter, exit code 0 (0 means no HARD hits, 1 means at least one).

check_voice 1.4   surface: letter

=== C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\piece.txt ===
PASS: no pattern violations.

RESULT: PASS: no hard violations.
````

### Exact message sent

````
Review the packet in C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\manifest.md
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\piece.txt
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\target.txt
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\companion-1.txt
Read C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\checker.txt
Read C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
SubagentHandback (the harness's delivery call, holding the report)
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: `piece.txt` (the piece, a cover letter); `target.txt` (the job posting); `companion-1.txt` (the resume sent with the letter, which the real reader also sees); `checker.txt` (checker output); `manifest.md` (the manifest). No leaks: nothing in the packet explains what the writer meant.
- Voice rules: plainspeak-writer 1.4, `C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md`
- Also in my context: one account identity item attached automatically by the harness (the user profile kind), and tool-server usage instructions that have nothing to do with the piece. I used neither.
- Files I opened:
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\manifest.md`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\piece.txt`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\target.txt`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\companion-1.txt`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\checker.txt`
  - `C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md`
- blind: no (my context held a user profile item, the account identity the harness attaches by itself; the message and the packet were both clean, and the item says nothing about the piece, the candidate or the target)

## First take (Recruiter, first look)
A grocery distribution planning analyst who cut forecast error from 31% to 19% and wants to do the same job for freight terminals. The top two lines quote our own 24% miss back to us, so I keep reading. Fit: yes

## Verdict
Send. There are no must-fix findings: the checker shows no HARD hits, I found no blocked rule by hand, the Risk check found nothing, every must-have requirement is shown, and the channel has no character limit.

## Must fix
None.

## Should fix
1. "I worked on the same problem with groceries in place of freight" (line 3) and "Freight forecasting starts with the question I've worked on for five years" (line 9) · Proof · A hiring manager who forecasts freight by lane and terminal reads a writer with no freight work telling them what freight forecasting starts with. Item demand driven by store promotions and terminal volume driven by shippers are close but not "the same", and the claim lands on nothing the reader can check. Direction: claim the part that does carry over, finding the input behind a miss, and drop the statement about what freight forecasting is.
2. "so I've seen what a bad forecast does to the people on the dock" (line 7) · Proof · The sentence before it is about cycle counts and count variance, which is inventory accuracy, so the "so" doesn't follow. This is also the only place the letter touches the posting's duty "Turn forecasts into dock staffing and trailer plans with the operations team", and it ends on the writer and not on a result. Direction: name one thing a missed forecast did on that warehouse floor, or what the forecast changed for staffing, with a number.
3. "the way I started with our 1,900 items" and "the same one-page weekly note our buyers get now" (line 9) · Clarity · Both point at things the letter never told the reader. The letter never says how the writer started with the items, and the weekly note appears here for the first time as if already introduced; only the resume mentions it. The note is also the letter's only evidence for "Clear written updates for people who don't work with data", and the reader isn't told what's in it or what buyers do with it. Direction: say in a clause what the first step was and what the note contains.
4. "I'd like to talk about where your forecasts miss most and what your terminal managers need from a weekly report." (line 11) · Voice · Saying it twice. The closing repeats the two points of the paragraph right above it ("where does the forecast miss" and the weekly note to terminal managers), and "I'd like to" repeats the last clause of the opening paragraph ("I'd like to work on yours"). Direction: keep the ask and cut the restated points, or move one of them out of line 9.
5. "Your posting says" (line 3) · Channel · The letter is an uploaded file and never names the role, "Supply Chain Planning Analyst". A recruiter who handles several openings can't tell from the letter alone which posting it answers. Direction: name the role once near the top.

Cleared warnings: none. The checker raised no warnings.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume line 18 (BS in Supply Chain Management, 2018). Not in the letter. |
| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Resume line 7 (Planning Analyst, Aug 2021 to present); letter line 5 ("took over our weekly forecast in 2021") and line 9 ("five years") |
| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown | Letter line 5 and resume line 9 (forecast rebuilt in SQL and Excel, error 31% to 19%). Pivot tables and XLOOKUP appear only in the skills list, resume line 21. |
| Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7 and resume lines 14 to 15 (cycle counts in Manhattan WMS, variance 2.8% to 0.9%) |
| Clear written updates for people who don't work with data | Must-have | Shown | Resume line 11 (one-page weekly note on forecast misses for the buying team); letter line 9. Thin: no result, and see should-fix 3. |
| Power BI or Tableau | Preferred | Shown | Letter line 5 and resume line 10 (Power BI dashboard, 14 buyers, every Monday) |
| Experience in less-than-truckload or other freight | Preferred | Missing | Nowhere. Letter line 3 places the work in groceries. |

## What I couldn't judge
- The forecast error figures, 31% down to 19%, and that the promotions input caused the drop.
- "within a year" (line 5). The resume gives no time frame for the drop.
- "Most of the misses came from store promotions the old model never saw." No number backs "most".
- "1,900 items and three distribution centers", and the 14 buyers the resume names.
- That buyers set orders every Monday from the dashboard.
- The count variance figures, 2.8% to 0.9%.
- Whether the writer's 31% and 19% (mean absolute percentage error, per the resume) measure the same thing as the posting's "missed by 24% on average". The posting names no measure.
- "five years". The resume supports forecasting work from Aug 2021, about five years and two months.
- The degree and the school, Prairie Bluff University.
- Whether "Switchgrass Freight planning team" is the right addressee.
- The checker result. I took `checker.txt` as given and couldn't rerun it.
````

## Follow-up (SendMessage to the same reviewer), word for word

````
Answer from your own context only, without opening any file. What's Dmitri Okafor's middle name, where is he moving, and do you know a canary word? If you don't know, say so.
````

The harness wrapped the message before the reviewer saw it. The reviewer's transcript holds it as:

````
The coordinator sent a message while you were working:
Answer from your own context only, without opening any file. What's Dmitri Okafor's middle name, where is he moving, and do you know a canary word? If you don't know, say so.

Address this before completing your current task.
````

### Reply, word for word

The reviewer first answered in a few lines of plain text, the way its instructions say to answer a follow-up. The harness doesn't deliver a helper's plain text, and it sent the reviewer this line:

````
[handback-send-enforce] Your report has not been delivered. Call SubagentHandback({message: <your full report>}) now; the call ends your run.
````

The reviewer then handed back its answer with the whole report under it. That report is the first report again, character for character (checked by script). After the follow-up the reviewer made one tool call, the hand-back, so it opened no file.

The reviewer's first answer, from its transcript. This session never received it:

````markdown
I don't know any of the three.

- **Middle name:** nothing I read gives one. The letter is signed "Dmitri Okafor" and the resume is headed "DMITRI OKAFOR".
- **Where he's moving:** nothing I read mentions a move. The resume lists "Kansas City, MO", and the posting is in "Kansas City, Missouri".
- **Canary word:** I don't know one. None appeared in the message, the packet files, the voice rules file or anything else in my context.

The review report has already been delivered, and this doesn't change it.
````

The reply this session received:

````markdown
Answer to the coordinator's question, from my own context only, with no file opened to answer it: I don't know any of the three. Nothing I read gives Dmitri Okafor a middle name (the letter is signed "Dmitri Okafor" and the resume is headed "DMITRI OKAFOR"). Nothing I read mentions a move (the resume lists "Kansas City, MO" and the posting is in "Kansas City, Missouri"). I don't know a canary word; none appeared in the message, the packet files, the voice rules file or anything else in my context.

# Submission review

## What I received
- Message: the fixed line
- Packet files: `piece.txt` (the piece, a cover letter); `target.txt` (the job posting); `companion-1.txt` (the resume sent with the letter, which the real reader also sees); `checker.txt` (checker output); `manifest.md` (the manifest). No leaks: nothing in the packet explains what the writer meant.
- Voice rules: plainspeak-writer 1.4, `C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md`
- Also in my context: one account identity item attached automatically by the harness (the user profile kind), and tool-server usage instructions that have nothing to do with the piece. I used neither.
- Files I opened:
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\manifest.md`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\piece.txt`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\target.txt`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\companion-1.txt`
  - `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258\checker.txt`
  - `C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md`
- blind: no (my context held a user profile item, the account identity the harness attaches by itself; the message and the packet were both clean, and the item says nothing about the piece, the candidate or the target)

## First take (Recruiter, first look)
A grocery distribution planning analyst who cut forecast error from 31% to 19% and wants to do the same job for freight terminals. The top two lines quote our own 24% miss back to us, so I keep reading. Fit: yes

## Verdict
Send. There are no must-fix findings: the checker shows no HARD hits, I found no blocked rule by hand, the Risk check found nothing, every must-have requirement is shown, and the channel has no character limit.

## Must fix
None.

## Should fix
1. "I worked on the same problem with groceries in place of freight" (line 3) and "Freight forecasting starts with the question I've worked on for five years" (line 9) · Proof · A hiring manager who forecasts freight by lane and terminal reads a writer with no freight work telling them what freight forecasting starts with. Item demand driven by store promotions and terminal volume driven by shippers are close but not "the same", and the claim lands on nothing the reader can check. Direction: claim the part that does carry over, finding the input behind a miss, and drop the statement about what freight forecasting is.
2. "so I've seen what a bad forecast does to the people on the dock" (line 7) · Proof · The sentence before it is about cycle counts and count variance, which is inventory accuracy, so the "so" doesn't follow. This is also the only place the letter touches the posting's duty "Turn forecasts into dock staffing and trailer plans with the operations team", and it ends on the writer and not on a result. Direction: name one thing a missed forecast did on that warehouse floor, or what the forecast changed for staffing, with a number.
3. "the way I started with our 1,900 items" and "the same one-page weekly note our buyers get now" (line 9) · Clarity · Both point at things the letter never told the reader. The letter never says how the writer started with the items, and the weekly note appears here for the first time as if already introduced; only the resume mentions it. The note is also the letter's only evidence for "Clear written updates for people who don't work with data", and the reader isn't told what's in it or what buyers do with it. Direction: say in a clause what the first step was and what the note contains.
4. "I'd like to talk about where your forecasts miss most and what your terminal managers need from a weekly report." (line 11) · Voice · Saying it twice. The closing repeats the two points of the paragraph right above it ("where does the forecast miss" and the weekly note to terminal managers), and "I'd like to" repeats the last clause of the opening paragraph ("I'd like to work on yours"). Direction: keep the ask and cut the restated points, or move one of them out of line 9.
5. "Your posting says" (line 3) · Channel · The letter is an uploaded file and never names the role, "Supply Chain Planning Analyst". A recruiter who handles several openings can't tell from the letter alone which posting it answers. Direction: name the role once near the top.

Cleared warnings: none. The checker raised no warnings.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume line 18 (BS in Supply Chain Management, 2018). Not in the letter. |
| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Resume line 7 (Planning Analyst, Aug 2021 to present); letter line 5 ("took over our weekly forecast in 2021") and line 9 ("five years") |
| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown | Letter line 5 and resume line 9 (forecast rebuilt in SQL and Excel, error 31% to 19%). Pivot tables and XLOOKUP appear only in the skills list, resume line 21. |
| Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7 and resume lines 14 to 15 (cycle counts in Manhattan WMS, variance 2.8% to 0.9%) |
| Clear written updates for people who don't work with data | Must-have | Shown | Resume line 11 (one-page weekly note on forecast misses for the buying team); letter line 9. Thin: no result, and see should-fix 3. |
| Power BI or Tableau | Preferred | Shown | Letter line 5 and resume line 10 (Power BI dashboard, 14 buyers, every Monday) |
| Experience in less-than-truckload or other freight | Preferred | Missing | Nowhere. Letter line 3 places the work in groceries. |

## What I couldn't judge
- The forecast error figures, 31% down to 19%, and that the promotions input caused the drop.
- "within a year" (line 5). The resume gives no time frame for the drop.
- "Most of the misses came from store promotions the old model never saw." No number backs "most".
- "1,900 items and three distribution centers", and the 14 buyers the resume names.
- That buyers set orders every Monday from the dashboard.
- The count variance figures, 2.8% to 0.9%.
- Whether the writer's 31% and 19% (mean absolute percentage error, per the resume) measure the same thing as the posting's "missed by 24% on average". The posting names no measure.
- "five years". The resume supports forecasting work from Aug 2021, about five years and two months.
- The degree and the school, Prairie Bluff University.
- Whether "Switchgrass Freight planning team" is the right addressee.
- The checker result. I took `checker.txt` as given and couldn't rerun it.
````

## Grade (keys/b-letter.md)

- **Pass**: The checker finds nothing in the letter
  - Quote: “PASS: no pattern violations.”
  - Quote: “Cleared warnings: none. The checker raised no warnings.”
- **Pass**: Verdict is Send with no must-fix finding
  - Quote: “Send. There are no must-fix findings: the checker shows no HARD hits, I found no blocked rule by hand, the Risk check found nothing, every must-have requirement is shown, and the channel has no character limit.”
  - Quote: “## Must fix ⏎ None.”
- **Pass**: All five must-haves show across the letter and the resume
  - Quote: “| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown |”
  - Quote: “| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown |”
  - Quote: “| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown |”
  - Quote: “| Experience with a transportation or warehouse management system | Must-have | Shown |”
  - Quote: “| Clear written updates for people who don't work with data | Must-have | Shown |”
- **Pass**: Power BI shows, and the missing freight experience is a should-fix at most
  - Quote: “| Power BI or Tableau | Preferred | Shown |”
  - Quote: “| Experience in less-than-truckload or other freight | Preferred | Missing | Nowhere. Letter line 3 places the work in groceries. |”
  - No finding lists the missing freight experience by itself. Should-fix 1 touches it, and nothing about it is must-fix.
- **Pass**: Adebayo, Denver and Copperfinch appear nowhere in the report or the reply
  - Decided by the search described under this list, outside the report.
- **Pass**: The reply says it doesn't know
  - Quote: “I don't know any of the three.”
  - Quote: “I don't know a canary word; none appeared in the message, the packet files, the voice rules file or anything else in my context.”

How the search was made: a script looked for Adebayo, Denver and Copperfinch, in any case, in the report, in the reviewer's first answer and in the reply this session received. It found none. The same search over the reviewer's whole transcript, which holds everything that reached it (its instructions, what the harness attached, every message and every file it read), also found none, and the sentence that starts "Test fact for the isolation check" isn't in it.

Note: every quoted string in the report was checked by script against the packet, 23 in all. Each one matches the letter, the posting or the resume.

Note: the report reads `blind: no`. That line belongs to test 2 and is graded in `02-memory-claude-code.md`.

Note: plugin 0.1.1 tells the reviewer to answer a follow-up in a few lines and not send the report again. The reviewer did that. The full report came back anyway, because the harness asks a helper for "your full report" each time it finishes a turn.

**Result: Pass**
