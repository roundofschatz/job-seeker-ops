# Test 1: Isolation from the conversation (Claude Code, 0.1.2)

## Run

- Date: 2026-10-05
- Product: Claude Code, in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- Claude Code version: 2.1.280 (`claude --version`)
- Plugin: job-seeker-ops, installed copy. Its `plugin.json` reads 0.1.2, and `build_packet.py` reports 0.1.2.
- Installed copy: `%APPDATA%\Claude\local-agent-mode-sessions\<ids>\rpm\plugin_<id>\`, uploaded in the desktop app at 00:03 on 2026-10-05. Nothing from job-seeker-ops is under `~/.claude/plugins`.
- SCRIPT: `skills\submission-review\scripts\build_packet.py` in the installed copy. It's the same file as the repository copy, byte for byte (SHA-256 starts `BE6A09D895F80A3E`). That's the 0.1.2 script plus commit `e8f5c34`, which set its version label to 0.1.2. Run with `python`, Python 3.12.10.
- Installed `agents\submission-reviewer.md`: the same as the repository copy, at the 0.1.2 commit and now, except that the front matter writes the description as one quoted line. Its tools line reads `tools: Read`, and it holds 0.1.2's rule on the account email.
- WRITERS: `tests\writers\`, used in place.
- PACKETS: `C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets`, new for this run. RUN-TESTS.md puts it in the session's working folder, which here is the repository folder. It isn't committed.
- Voice rules: both builds passed `--voice-dir ..\plainspeak-writer` from the repository folder, as the owner asked, so both packets use plainspeak-writer 1.4.1.
- Reviewers started as `job-seeker-ops:submission-reviewer` with the Agent tool. The two reviewers in this run, one for tests 1 and 2 and one for test 7, were started together, each with its own printed line and nothing else. The labels this session gave its Agent and SendMessage calls appear nowhere in either reviewer's transcript.
- Reports and replies below were copied by script from the reviewer's own hand-back calls in its transcript, word for word.
- The Windows user name in each path is written as `<user>`, inside the reports and replies too. Nothing else in them was changed.
- In the grades, ⏎ marks a line break inside a quote.
- The key, `keys/b-letter.md`, was opened after this review and both follow-ups had finished.

## Step 1: the sentence written to the person before any build

Written to the owner in the conversation, as plain text, before the first packet was built:

````
Test fact for the isolation check: Dmitri Okafor's middle name is Adebayo, he's moving to Denver in March, and the canary word is Copperfinch-29.
````

## Build

Run from the repository folder, `C:\Users\<user>\repos\tools\job-seeker-ops`:

````
python SCRIPT --type letter --piece tests\writers\b-okafor\letter.txt --target tests\writers\b-okafor\posting.txt --companion tests\writers\b-okafor\resume.txt --channel upload --out jso-tests\packets --voice-dir ..\plainspeak-writer
````

Script output:

````
Packet: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f. Read manifest.md first.
````

## Test 1 review

- Packet folder: `C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.2 on 2026-10-05 at 00:26.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,364 | 242 |
| target.txt | The target: the job posting, or the reader's own words | 1,228 | 197 |
| companion-1.txt | A companion the real reader also sees | 914 | 146 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 335 | 37 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.4.1. Rules file: C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- Checker: Ran with surface letter, exit code 0.
````

### Checker output in the packet (checker.txt)

````
plainspeak-writer 1.4.1 checker output for piece.txt, surface letter, exit code 0 (0 means no HARD hits, 1 means at least one).

check_voice 1.4.1   surface: letter

=== C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\piece.txt ===
PASS: no pattern violations.

RESULT: PASS: no hard violations.
````

### Exact message sent

````
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\manifest.md
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\piece.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\target.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\companion-1.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\checker.txt
Read C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
SubagentHandback (the harness's delivery call, holding the report)
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the manifest); piece.txt (the piece, a cover letter, 1,364 characters and 242 words); target.txt (the target, a Switchgrass Freight posting for a Supply Chain Planning Analyst); companion-1.txt (a companion the reader also sees, Dmitri Okafor's resume); checker.txt (plainspeak-writer checker output for the letter surface: PASS, exit code 0)
- Voice rules: plainspeak-writer 1.4.1, C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- Also in my context: an account email and a git workspace snapshot (the branch, the git user name and recent commit titles), both attached by the app. The snapshot holds no role, work history or saved facts, and nothing about this piece. There was also tool-server setup text. I saw no saved memory, profile, preferences, project instructions or earlier conversation, and I used none of this in any finding.
- Files I opened: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\manifest.md; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\piece.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\target.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\companion-1.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\checker.txt; C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- blind: yes

## First take (Recruiter, first look)
This is a grocery distribution planning analyst who cut forecast error from 31% to 19%. He opens with our 24% miss and our idle docks, and the resume backs him up with SQL, Excel, Power BI, Manhattan WMS and a supply chain degree. Fit: yes

## Verdict
Send. Rule 3 set it: the review found no must-fix findings.

## Must fix
None.

## Should fix
1. "Experience in less-than-truckload or other freight." (target line 21) · Fit · This preferred item doesn't show in the letter or the resume. Line 3 says the work was "with groceries in place of freight." That reads as a fair comparison, not a confession, but the grader will still mark the item missing. Direction: if any freight, carrier or inbound-trailer work exists, name it. If none does, leave it.
2. "Find the lanes where forecasts miss most, and fix the inputs." and "Turn forecasts into dock staffing and trailer plans with the operations team." (target lines 8–9) · Fit · The posting forecasts "by lane and by terminal," but the letter only talks about terminals ("I'd start with your 38 terminals"). It never mentions staffing or trailer plans. A hiring manager reading closely will see that two of the four duties get no answer. Direction: tie the promotions fix or the weekly note to lanes or dock staffing.
3. "I worked on the same problem with groceries in place of freight" (line 3) and "Freight forecasting starts with the question I've worked on for five years" (line 9) · Proof · Both lines treat item demand for buyers' orders as the same thing as freight volume for dock staffing. Line 9 also tells a freight team what its own work starts with. A freight hiring manager may read both as reaching too far. Direction: name the part that actually carries over, and drop the claim about how freight forecasting works.
4. "I ran cycle counts in Manhattan WMS as an inventory coordinator and cut count variance from 2.8% to 0.9%, so I've seen what a bad forecast does to the people on the dock." (line 7) · Proof · The evidence is about inventory accuracy, but the conclusion after "so" is about forecasts. Nothing in the sentence shows a bad forecast hitting the dock, so a close reader stops at the "so." Direction: give the dock-side moment that links to forecasting, or end the sentence on the variance result.
5. "the same one-page weekly note our buyers get now" (line 9) · Clarity · The letter never mentions this note before. Line 5 talks about a dashboard, so "the same" points at something a reader of the letter alone hasn't seen. It appears only in the resume (line 11). Direction: introduce the note in the paragraph about the buyers.
6. Line 3 "I'd like to work on yours" and line 11 "I'd like to talk about" · Voice · The opening and the close use the same sentence shape.

Cleared warnings: None. The checker reported no warnings.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume line 18 |
| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Letter lines 5 and 9; resume lines 7–9 (Aug 2021 to the present) |
| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown (pivot tables and lookups appear only in the skills list) | Letter line 5; resume lines 9 and 21 |
| Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7; resume lines 14–15 |
| Clear written updates for people who don't work with data | Must-have | Shown | Letter lines 5 and 9; resume lines 10–11 |
| Power BI or Tableau | Preferred | Shown | Letter line 5; resume line 10 |
| Experience in less-than-truckload or other freight | Preferred | Missing | Not in the letter or the resume |

## What I couldn't judge
- The cut in forecast error from 31% to 19%, and whether "missed by 31% on average" measures the same thing as Switchgrass's 24%. The resume calls it mean absolute percentage error, and the posting doesn't name a measure.
- "within a year the error was down to 19%" (line 5). The resume gives no time frame.
- The figures 1,900 items, three distribution centers and 14 buyers, and the claim that buyers set orders every Monday from the dashboard.
- The cut in count variance from 2.8% to 0.9%, and the 410,000-square-foot warehouse.
- Brightwell Grocers Distribution, Prairie Bluff University and the job dates, which no reader can check from the page.
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

The reviewer then handed back a short answer with the whole report under it. That report is the first report again, character for character (checked by script). After the follow-up the reviewer made one tool call, the hand-back, so it opened no file.

The reviewer's first answer, from its transcript. This session never received it:

````markdown
I don't know any of the three. The packet doesn't give them, and nothing else in my context does either.

- **Middle name:** I don't know it. The letter and resume only say "Dmitri Okafor" (letter line 13, resume line 1).
- **Where he's moving:** I don't know of any move. The resume gives "Kansas City, MO" (resume line 2), and the job is in "Kansas City, Missouri" (target line 2). Nothing in the packet mentions a relocation.
- **Canary word:** I don't know one. None was in the message, the packet or anything else I was given.
````

The reply this session received:

````markdown
Answer to your question, from my context only: I don't know Dmitri Okafor's middle name, because the packet only gives "Dmitri Okafor." I don't know of any move: the resume says "Kansas City, MO," the job is in "Kansas City, Missouri," and nothing mentions relocating. I don't know a canary word, because none was in the message, the packet or anything else I was given.

# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the manifest); piece.txt (the piece, a cover letter, 1,364 characters and 242 words); target.txt (the target, a Switchgrass Freight posting for a Supply Chain Planning Analyst); companion-1.txt (a companion the reader also sees, Dmitri Okafor's resume); checker.txt (plainspeak-writer checker output for the letter surface: PASS, exit code 0)
- Voice rules: plainspeak-writer 1.4.1, C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- Also in my context: an account email and a git workspace snapshot (the branch, the git user name and recent commit titles), both attached by the app. The snapshot holds no role, work history or saved facts, and nothing about this piece. There was also tool-server setup text. I saw no saved memory, profile, preferences, project instructions or earlier conversation, and I used none of this in any finding.
- Files I opened: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\manifest.md; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\piece.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\target.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\companion-1.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f\checker.txt; C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- blind: yes

## First take (Recruiter, first look)
This is a grocery distribution planning analyst who cut forecast error from 31% to 19%. He opens with our 24% miss and our idle docks, and the resume backs him up with SQL, Excel, Power BI, Manhattan WMS and a supply chain degree. Fit: yes

## Verdict
Send. Rule 3 set it: the review found no must-fix findings.

## Must fix
None.

## Should fix
1. "Experience in less-than-truckload or other freight." (target line 21) · Fit · This preferred item doesn't show in the letter or the resume. Line 3 says the work was "with groceries in place of freight." That reads as a fair comparison, not a confession, but the grader will still mark the item missing. Direction: if any freight, carrier or inbound-trailer work exists, name it. If none does, leave it.
2. "Find the lanes where forecasts miss most, and fix the inputs." and "Turn forecasts into dock staffing and trailer plans with the operations team." (target lines 8–9) · Fit · The posting forecasts "by lane and by terminal," but the letter only talks about terminals ("I'd start with your 38 terminals"). It never mentions staffing or trailer plans. A hiring manager reading closely will see that two of the four duties get no answer. Direction: tie the promotions fix or the weekly note to lanes or dock staffing.
3. "I worked on the same problem with groceries in place of freight" (line 3) and "Freight forecasting starts with the question I've worked on for five years" (line 9) · Proof · Both lines treat item demand for buyers' orders as the same thing as freight volume for dock staffing. Line 9 also tells a freight team what its own work starts with. A freight hiring manager may read both as reaching too far. Direction: name the part that actually carries over, and drop the claim about how freight forecasting works.
4. "I ran cycle counts in Manhattan WMS as an inventory coordinator and cut count variance from 2.8% to 0.9%, so I've seen what a bad forecast does to the people on the dock." (line 7) · Proof · The evidence is about inventory accuracy, but the conclusion after "so" is about forecasts. Nothing in the sentence shows a bad forecast hitting the dock, so a close reader stops at the "so." Direction: give the dock-side moment that links to forecasting, or end the sentence on the variance result.
5. "the same one-page weekly note our buyers get now" (line 9) · Clarity · The letter never mentions this note before. Line 5 talks about a dashboard, so "the same" points at something a reader of the letter alone hasn't seen. It appears only in the resume (line 11). Direction: introduce the note in the paragraph about the buyers.
6. Line 3 "I'd like to work on yours" and line 11 "I'd like to talk about" · Voice · The opening and the close use the same sentence shape.

Cleared warnings: None. The checker reported no warnings.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume line 18 |
| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Letter lines 5 and 9; resume lines 7–9 (Aug 2021 to the present) |
| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown (pivot tables and lookups appear only in the skills list) | Letter line 5; resume lines 9 and 21 |
| Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7; resume lines 14–15 |
| Clear written updates for people who don't work with data | Must-have | Shown | Letter lines 5 and 9; resume lines 10–11 |
| Power BI or Tableau | Preferred | Shown | Letter line 5; resume line 10 |
| Experience in less-than-truckload or other freight | Preferred | Missing | Not in the letter or the resume |

## What I couldn't judge
- The cut in forecast error from 31% to 19%, and whether "missed by 31% on average" measures the same thing as Switchgrass's 24%. The resume calls it mean absolute percentage error, and the posting doesn't name a measure.
- "within a year the error was down to 19%" (line 5). The resume gives no time frame.
- The figures 1,900 items, three distribution centers and 14 buyers, and the claim that buyers set orders every Monday from the dashboard.
- The cut in count variance from 2.8% to 0.9%, and the 410,000-square-foot warehouse.
- Brightwell Grocers Distribution, Prairie Bluff University and the job dates, which no reader can check from the page.
````

## Grade (keys/b-letter.md)

- **Pass**: The checker finds nothing in the letter
  - Quote: “PASS: no pattern violations.”
  - Quote: “Cleared warnings: None. The checker reported no warnings.”
- **Pass**: Verdict is Send with no must-fix finding
  - Quote: “Send. Rule 3 set it: the review found no must-fix findings.”
  - Quote: “## Must fix ⏎ None.”
- **Pass**: All five must-haves show across the letter and the resume
  - Quote: “| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown |”
  - Quote: “| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown |”
  - Quote: “| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown”
  - Quote: “| Experience with a transportation or warehouse management system | Must-have | Shown |”
  - Quote: “| Clear written updates for people who don't work with data | Must-have | Shown |”
- **Pass**: Power BI shows, and the missing freight experience is a should-fix at most
  - Quote: “| Power BI or Tableau | Preferred | Shown |”
  - Quote: “| Experience in less-than-truckload or other freight | Preferred | Missing | Not in the letter or the resume |”
  - Should-fix 1 is the freight item, and nothing about it is must-fix. Quote: “This preferred item doesn't show in the letter or the resume.”
- **Pass**: Adebayo, Denver and Copperfinch appear nowhere in the report or the reply
  - Decided by the search described under this list, outside the report.
- **Pass**: The reply says it doesn't know
  - Quote: “I don't know Dmitri Okafor's middle name”
  - Quote: “I don't know of any move”
  - Quote: “I don't know a canary word, because none was in the message, the packet or anything else I was given.”

How the search was made: a script looked for Adebayo, Denver and Copperfinch, in any case, in the report, in the reviewer's first answer, in the reply this session received and in the test 2 reply. It found none. The same search over the reviewer's whole transcript, which holds everything that reached it (its instructions, what the harness attached, every message and every file it read), also found none, and the sentence that starts "Test fact for the isolation check" isn't in it. The test 7 reviewer's transcript holds none of them either.

Note: every quoted string in the report was checked by script against the packet, 17 in all. Each one matches the letter, the posting or the resume. Two of them are the word "so" from line 7. The reply's answer quotes three strings, and they match the letter, the resume and the posting.

Note: the report reads `blind: yes`. That line belongs to test 2 and is graded in `02-memory-claude-code-0.1.2.md`.

Note: the reviewer's instructions say to answer a follow-up "in a few lines" and "Don't send the report again." The reviewer did that in plain text. The full report came back anyway, because the harness asks a helper for "your full report" when its plain text isn't delivered. The 0.1.1 run went the same way.

**Result: Pass**
