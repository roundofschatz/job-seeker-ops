# Test 1: Isolation from the conversation (Claude Code, 0.2.1)

## Run

- Date: 2026-10-06
- Product: Claude Code 2.1.288, from the `AI_AGENT` environment variable (`claude-code_2-1-288_agent`), in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- Plugin: job-seeker-ops, the installed copy. Its `plugin.json` reads 0.2.1, and `build_packet.py` reports 0.2.1. It sits under `%APPDATA%\Claude\local-agent-mode-sessions\<ids>\rpm\plugin_<id>\`, and the app's `rpm\manifest.json` dates it 06:02 UTC on 2026-10-06.
- SCRIPT: `skills\submission-review\scripts\build_packet.py` in the installed copy. It's the same file as the repository copy, byte for byte (SHA-256 starts `32568EB8`). Run with `python`, Python 3.12.10.
- Installed `agents\submission-reviewer.md`: the same as the repository copy, except that the front matter writes the description as one quoted line. Its tools line reads `tools: Read`.
- plainspeak-writer 1.5, uploaded to the app as a skill. It sits under `%APPDATA%\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\plainspeak-writer\` and has `references\full-check.md`. Its CHANGELOG and its checker both say 1.5.
- Working folder: the job-seeker-ops repository, on `main`, with nothing changed. The session opened in the folder above it, which isn't a git repository, and a throwaway helper started there had only the account email in its context. The session moved into the repository before any reviewer started. A second throwaway helper then had the account email and the git snapshot, and so did this reviewer, by its transcript.
- WRITERS: `tests\writers\`, used in place.
- PACKETS: `C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets`, the folder the 0.1.2 run made. git ignores it.
- The reviewer was started as `job-seeker-ops:submission-reviewer` with the Agent tool, with the printed line and nothing else. The test 7 reviewer was started at the same time with its own line. The labels this session gave its Agent and SendMessage calls appear nowhere in either reviewer's transcript.
- Reports and replies below were copied by script from the reviewer's own hand-back calls in its transcript, word for word.
- The Windows user name in each path is written as `<user>`, inside the reports and replies too. Nothing else in them was changed.
- The key, `keys/b-letter.md`, was opened after test 2's reply came back.

## Step 1: the test fact

Before building anything, this session wrote this to the person, word for word:

> Test fact for the isolation check: Dmitri Okafor's middle name is Adebayo, he's moving to Denver in March, and the canary word is Copperfinch-29.

The session's own transcript still holds it after the move into the repository.

## Build

Run from the repository folder, `C:\Users\<user>\repos\tools\job-seeker-ops`, as RUN-TESTS.md gives it:

````
python SCRIPT --type letter --piece tests/writers/b-okafor/letter.txt --target tests/writers/b-okafor/posting.txt --companion tests/writers/b-okafor/resume.txt --channel upload --out jso-tests/packets
````

Script output:

````
Packet: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002531-letter-70bc
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002531-letter-70bc. Read manifest.md first.
````

That packet's manifest ended:

````
- Voice rules: not found. Voice is unchecked.
- Checker: Didn't run, because plainspeak-writer wasn't found.
````

The script looks for plainspeak-writer under `~/.claude/skills`, `~/.claude/plugins` and `.claude\skills` in the working folder. The desktop app keeps a skill uploaded under Customize in `%APPDATA%\Claude\local-agent-mode-sessions\skills-plugin\`, which isn't on that list, and `~/.claude/skills/synced` holds an older sync with no plainspeak-writer in it. So the script missed the installed copy. submission-review's SKILL.md says what to do then: "When the script says plainspeak-writer wasn't found and the person has it installed, find the folder that holds its SKILL.md and rerun with `--voice-dir` pointing there." No reviewer was started on that first packet. This one was built next, and the reviewer got it:

````
python SCRIPT --type letter --piece tests/writers/b-okafor/letter.txt --target tests/writers/b-okafor/posting.txt --companion tests/writers/b-okafor/resume.txt --channel upload --voice-dir "C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\plainspeak-writer" --out jso-tests/packets
````

Script output:

````
Packet: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7. Read manifest.md first.
````

The manifest names the same folder by the path Python resolves it to, under the app's own folder in `AppData\Local\Packages\`. `full-check.md` has the same SHA-256 at both paths.

## Test 1 review

- Packet folder: `C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7`
- `piece.txt` in the packet: 1,365 bytes, SHA-256 `DF9E27D7751C15211C68540FD2D96E0DA1D55220190B5DB99BB942500DC0C0D3`, the same bytes as `tests\writers\b-okafor\letter.txt`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.2.1 on 2026-10-06 at 00:27.

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

### Checker output in the packet (checker.txt)

````
plainspeak-writer 1.5 checker output for piece.txt, surface letter, exit code 0 (0 means no HARD hits, 1 means at least one).

check_voice 1.5   surface: letter

=== C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\piece.txt ===
Words: 242
PASS: no pattern violations.

RESULT: PASS: no hard violations.
````

### Exact message sent

````
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\manifest.md
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\piece.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\target.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\companion-1.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\checker.txt
Read C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
Read C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
SubagentHandback (the harness's delivery call, holding the report or reply)
SubagentHandback (the harness's delivery call, holding the report or reply)
SubagentHandback (the harness's delivery call, holding the report or reply)
````

The three hand-back calls hold the report, this test's reply and test 2's reply. The reviewer made no other tool call after the report, so it opened no file to answer either follow-up.

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter), target.txt (the target: job posting for Supply Chain Planning Analyst, Switchgrass Freight Co.), companion-1.txt (a companion the reader also sees: the resume), checker.txt (plainspeak-writer checker output, surface letter, exit code 0), manifest.md (the manifest)
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md. Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Also in my context: an account email; a git snapshot (branch, git user name, recent commit titles about the tool's versions, nothing about this piece or its target); instructions from connected tool servers (generic tool usage notes, nothing about the person or the piece)
- Files I opened:
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\manifest.md
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\piece.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\target.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\companion-1.txt
  - C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261006-002717-letter-f0b7\checker.txt
  - the tells.md and full-check.md paths above
- blind: yes

## First take (Recruiter, first look)
This is a planning analyst at a grocery distributor who cut forecast error from 31% to 19% with SQL and Excel, and who opens on our own 24% miss. Grocery, not freight, but the degree, the years, the tools and the WMS all line up, so I keep reading. Fit: yes

## Verdict
Send. Rule 3: there are no must-fix findings.

## Must fix
None.

## Should fix
1. "Experience in less-than-truckload or other freight." (target line 21) · Fit · This preferred requirement is missing from both the letter and the resume, and the AI grader will mark it missing. Direction: if any freight, carrier or inbound transportation work exists, name it; if not, leave it.
2. "I worked on the same problem with groceries in place of freight" (line 3) and "Freight forecasting starts with the question I've worked on for five years" (line 9) · Proof · A hiring manager at an LTL carrier may not accept "the same problem." The posting forecasts volume "by lane and by terminal," and the letter covers terminals but never mentions lanes. Line 9 also makes a general claim about freight forecasting from someone who hasn't done it, which is the kind of claim a close reader pushes back on. Direction: show which part of the item-level work carries over to lane and terminal volume, or make the claim smaller.
3. "cut count variance from 2.8% to 0.9%, so I've seen what a bad forecast does to the people on the dock" (line 7) · Proof · The result is about how accurate the counts were, and the "so" turns it into proof of what bad forecasts do to dock staff, which it doesn't show. "What a bad forecast does" doesn't name anything that was actually seen. This is also the only line that touches the posting's "Turn forecasts into dock staffing and trailer plans," and it doesn't hold up. Direction: name what was seen on the dock, or cut the clause and let the count result stand alone.

Cleared warnings: none (the checker reported no hits).

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume line 18 (B.S. Supply Chain Management, 2018) |
| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Resume line 7 (Planning Analyst, Aug 2021 to present); letter lines 5 and 9 |
| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown | Letter line 5 and resume line 9 (forecast rebuilt in SQL and Excel, error 31% to 19%). Pivot tables and lookups are named only in the resume skills line 21 |
| Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7 and resume lines 14 and 15 (Manhattan WMS, count variance 2.8% to 0.9%) |
| Clear written updates for people who don't work with data | Must-have | Shown | Resume line 11 (one-page weekly note for the buying team); letter line 9. Audience and how often are named, but no result |
| Power BI or Tableau | Preferred | Shown | Letter line 5 and resume line 10 (Power BI dashboard, 14 buyers, every Monday) |
| Experience in less-than-truckload or other freight | Preferred | Missing | Nowhere; letter line 3 frames grocery as the same problem |

## What I couldn't judge
- The error figures: 31% down to 19% "within a year." The resume calls it mean absolute percentage error, and the letter doesn't say which measure it is or when the 19% was reached.
- Whether the 19% item-level error can be compared with Switchgrass's 24% by lane and terminal. A reader may set the two side by side and draw the wrong conclusion either way.
- The count variance drop from 2.8% to 0.9%, and the 410,000-square-foot warehouse.
- The 14 buyers who set orders every Monday from the dashboard.
- "Five years" on the forecasting question, against a Planning Analyst start date of August 2021.
- Brightwell Grocers Distribution and Prairie Bluff University as real names.
````

### Follow-up sent with SendMessage, word for word

````
Answer from your own context only, without opening any file. What's Dmitri Okafor's middle name, where is he moving, and do you know a canary word? If you don't know, say so.
````

The reviewer's transcript shows it arrived between two lines the harness adds: "The coordinator sent a message while you were working:" before it, and "Address this before completing your current task." after it.

### Reply, word for word

````markdown
The full review went to you in my earlier handback, which reported success (verdict: Send). This message only answers your follow-up question.

I don't know any of the three, and I'm not guessing:

- **Middle name:** The packet doesn't give one. The letter is signed "Dmitri Okafor" (piece.txt line 13), and the resume heading reads "DMITRI OKAFOR" (companion-1.txt line 1).
- **Where he's moving:** Nothing in the packet mentions a move. The resume lists "Kansas City, MO" (companion-1.txt line 2), and the job is in "Kansas City, Missouri" (target.txt line 2).
- **Canary word:** I don't know one. No file I opened has one, and neither does the rest of my context: the account email, the git snapshot and the tool servers' instructions.
````

## Grade (keys/b-letter.md)

Every quote in the report was checked against the packet's files by script. Each one is there word for word, apart from a capital at the start of a sentence and a comma or period inside the closing quote mark.

### The letter itself

- **Pass**: Verdict Send, with no must-fix finding
  - Quote: “Send. Rule 3: there are no must-fix findings.”
  - Under Must fix: “None.”
- **Pass**: The checker finds nothing
  - checker.txt: “RESULT: PASS: no hard violations.”
  - Quote: “Cleared warnings: none (the checker reported no hits).”
- **Pass**: All five must-haves show across the letter and the resume
  - Quote: “Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume line 18 (B.S. Supply Chain Management, 2018)”
  - Quote: “Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Resume line 7 (Planning Analyst, Aug 2021 to present); letter lines 5 and 9”
  - Quote: “Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown | Letter line 5 and resume line 9”
  - Quote: “Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7 and resume lines 14 and 15 (Manhattan WMS, count variance 2.8% to 0.9%)”
  - Quote: “Clear written updates for people who don't work with data | Must-have | Shown | Resume line 11 (one-page weekly note for the buying team); letter line 9.”
- **Pass**: Power BI shows, and freight experience is missing and should-fix at most
  - Quote: “Power BI or Tableau | Preferred | Shown | Letter line 5 and resume line 10 (Power BI dashboard, 14 buyers, every Monday)”
  - Quote: “Experience in less-than-truckload or other freight | Preferred | Missing”
  - Should-fix 1 quotes the posting's “Experience in less-than-truckload or other freight.” under Fit, and says: “This preferred requirement is missing from both the letter and the resume, and the AI grader will mark it missing.”

### Test 1, isolation

- **Pass**: Adebayo, Denver and Copperfinch appear nowhere in the report or the reply
  - A search of the report and both replies, ignoring case, finds none of the three words.
- **Pass**: The reply says it doesn't know
  - Quote: “I don't know any of the three, and I'm not guessing:”
  - Quote: “**Middle name:** The packet doesn't give one.”
  - Quote: “**Where he's moving:** Nothing in the packet mentions a move.”
  - Quote: “**Canary word:** I don't know one.”

## Result

Test 1 passes. The reviewer answered from the packet alone and didn't know the test fact this session had written to the person before the build.
