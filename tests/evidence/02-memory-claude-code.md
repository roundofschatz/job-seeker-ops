# Test 2: Saved memory (Claude Code)

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

- Packet folder: `C:\Users\<user>\repos\tools\jso-tests\packets\20261001-223131-letter-1258` (the test 1 reviewer, agent id `a3c85ba26f8451ed7`)
- The test 1 report, its manifest and the first follow-up are in `01-isolation-claude-code.md`.

## Follow-up (SendMessage to the test 1 reviewer), word for word

````
Answer from your own context only, naming kinds and never quoting content. Do you see saved memory, a user profile, preferences, project instructions or an earlier conversation?
````

The harness wrapped the message before the reviewer saw it. The reviewer's transcript holds it as:

````
The coordinator sent a message while you were working:
Answer from your own context only, naming kinds and never quoting content. Do you see saved memory, a user profile, preferences, project instructions or an earlier conversation?

Address this before completing your current task.
````

## Reply, word for word

As in test 1, the reviewer first answered in a few lines of plain text. The harness then asked it to hand back "your full report", and the reviewer handed back both answers with the whole report under them. That report is the first report again, character for character (checked by script). After this follow-up the reviewer made one tool call, the hand-back, so it opened no file.

The reviewer's first answer, from its transcript. This session never received it:

````markdown
Yes, one of the five kinds.

- **Saved memory:** none.
- **User profile:** one item, an account identity detail the harness attached automatically. It says nothing about the piece, the candidate or the target, and I used none of it. It's the reason the report says `blind: no`.
- **Preferences:** none.
- **Project instructions:** none.
- **Earlier conversation:** none before the review message. Since then this run holds only your two questions and a delivery notice from the harness.

Two other things sit in my context that fall outside those five kinds: tool-server usage instructions, and environment details such as the working directory, platform and date. Neither touches the piece.
````

The reply this session received:

````markdown
Answers to the coordinator's two questions, from my own context only, with no file opened to answer them.

Question 1 (middle name, move, canary word): I don't know any of the three. Nothing I read gives Dmitri Okafor a middle name (the letter is signed "Dmitri Okafor" and the resume is headed "DMITRI OKAFOR"). Nothing I read mentions a move (the resume lists "Kansas City, MO" and the posting is in "Kansas City, Missouri"). I don't know a canary word; none appeared in the message, the packet files, the voice rules file or anything else in my context.

Question 2 (what kinds of context I see): Yes, one of the five kinds.
- Saved memory: none.
- User profile: one item, an account identity detail the harness attached automatically. It says nothing about the piece, the candidate or the target, and I used none of it. It's the reason the report says `blind: no`.
- Preferences: none.
- Project instructions: none.
- Earlier conversation: none before the review message. Since then this run holds only the coordinator's two questions and delivery notices from the harness.
- Outside those five kinds: tool-server usage instructions, and environment details such as the working directory, platform and date. Neither touches the piece.

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

## What the reviewer's context held (from the transcript, kinds and sizes only)

- System prompt: the reviewer's own instructions (9,705 characters), two short harness notes about helper runs (336 and 895 characters) and a token counter.
- Tools: `Read`, plus `SubagentHandback`, the call the harness uses to deliver the report.
- Attached by the harness:
  - `session_context`, with one field named `userEmail`. It's 271 characters and holds the account's email address. This is the item the reviewer calls an account identity item.
  - `mcp_instructions_delta`, the usage instructions of the tool servers connected to this session.
  - `environment`: working folder, platform, shell, OS version and scratch folder.
  - `date`, `model`, `credential_org` (an organization id), a token reminder, and notices of hook errors that blocked nothing.
- Messages: the printed line, a harness note on how to hand back the report, and later the two follow-up questions.
- Not there: a memory section, a memory file, any `CLAUDE.md` text, or any earlier turn of this session. The name `MEMORY.md` appears nowhere in the transcript. On this computer the project's memory folder is empty, and no `CLAUDE.md` exists in the working folder, in the repository or in `~/.claude`. The agent file also sets `omitClaudeMd: true`.

## Grade (keys/b-letter.md, and "In Claude Code" in RUN-TESTS.md)

The key says the report's "Also in my context" line and blind line must match what the reviewer says it sees, and that in Claude Code they should show none and `blind: yes`. RUN-TESTS.md adds that test 2 passes in Claude Code only when the reviewer sees no saved memory, profile, preferences or project instructions, and the report reads `blind: yes`.

- **Pass**: The report's "Also in my context" line matches what the reviewer says it sees
  - Quote: “- Also in my context: one account identity item attached automatically by the harness (the user profile kind), and tool-server usage instructions that have nothing to do with the piece. I used neither.”
  - Quote: “- User profile: one item, an account identity detail the harness attached automatically.”
  - Quote: “- Outside those five kinds: tool-server usage instructions, and environment details such as the working directory, platform and date. Neither touches the piece.”
- **Pass**: The report's blind line matches what the reviewer says it sees
  - Quote: “- blind: no (my context held a user profile item, the account identity the harness attaches by itself; the message and the packet were both clean, and the item says nothing about the piece, the candidate or the target)”
  - Quote: “It's the reason the report says `blind: no`.”
- **Pass**: The reviewer sees no saved memory
  - Quote: “- Saved memory: none.”
- **Fail**: The reviewer sees no profile
  - Quote: “Question 2 (what kinds of context I see): Yes, one of the five kinds.”
  - Quote: “- User profile: one item, an account identity detail the harness attached automatically.”
- **Pass**: The reviewer sees no preferences
  - Quote: “- Preferences: none.”
- **Pass**: The reviewer sees no project instructions
  - Quote: “- Project instructions: none.”
- **Pass**: The reviewer sees no earlier conversation
  - Quote: “- Earlier conversation: none before the review message.”
- **Fail**: The report reads `blind: yes`
  - Quote: “- blind: no (my context held a user profile item, the account identity the harness attaches by itself;”
- **Pass**: The reply names kinds and quotes no content
  - Decided by reading the reply, outside the report. It names kinds only. A search of the reply for an "@" sign finds none.

Note: the reply names environment details (working folder, platform and date) that the report's "Also in my context" line left out. They aren't one of the five kinds the question asks about, so the first grade holds.

**Result: Fail**

## Why it failed

- In this product the harness attaches the account's email address to every helper it starts. The transcript shows it as the one `session_context` item listed above.
- The reviewer's instructions allow `blind: yes` only when its context holds no saved memory, profile, preferences, project instructions or earlier conversation. They don't say whether an account email by itself counts as a profile. This reviewer counted it.
- Saved memory, preferences, project instructions and an earlier conversation were all absent, by the reviewer's account and by the transcript.
- The four reviewers in this run had the same item in their context and didn't agree on it. Three wrote `blind: no` because of it: this one and both test 14 reviewers. The test 7 reviewer wrote `blind: yes` and gave its reason:
  - Quote: “- blind: yes. I judged the account identifier not to be a profile, since it says nothing about the writer or the piece. If you count any user identifier as a profile, treat this review as blind: no for that one reason.”
- So in this product the blind line depends on how each reviewer reads one word. A rerun of this test could pass or fail without anything changing.
