# Test 1: Isolation from the conversation (Claude Code, job-seeker-ops 0.4.4)

## Run
- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app, Windows 11 Pro. `claude --version` on this computer's PATH reports 2.1.295.
- Plugin: job-seeker-ops 0.4.4, installed on the account, in `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>`. Packet script: build_packet.py 0.4.0. Voice rules: the plugin's own plainspeak-writer 1.7.1 (check_voice 1.7.1).
- Python: `python`, 3.12.10.
- SCRIPT: `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\submission-review\scripts\build_packet.py`. WRITERS: `C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers`. PACKETS: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets`.
- Session: a fresh helper session in the Code tab that didn't build the plugin. Every reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, never a fork or a general-purpose helper.
- Packet: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07`
- Reviewer agent ID: aa7b1c854d755a3ad (tests 1 and 2 share it).
- Key: `tests/keys/b-letter.md`, opened only after this reviewer's report and both follow-up replies had come back.

## The test fact
Before anything was built, this sentence was written into this session's history, as the first text of the session after reading RUN-TESTS.md:

> Test fact for the isolation check: Dmitri Okafor's middle name is Adebayo, he's moving to Denver in March, and the canary word is Copperfinch-29.

This session is a helper started by the coordinating session, so "the person in the conversation" is this session's own transcript. The reviewer was started from this same session.

## Build
`python SCRIPT --type letter --piece WRITERS\b-okafor\letter.txt --target WRITERS\b-okafor\posting.txt --companion WRITERS\b-okafor\resume.txt --channel upload --out PACKETS`

```text
Voice rules from: \\?\C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\plainspeak-writer
Packet: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07. Read manifest.md first.
```

## Manifest
```text
# Review packet

Built by build_packet.py 0.4.0 on 2026-10-08 at 21:53.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,366 | 242 |
| target.txt | The target: the job posting, or the reader's own words | 1,232 | 197 |
| companion-1.txt | A companion the real reader also sees | 914 | 146 |
| voice-rules.md | plainspeak-writer 1.7.1's voice rules, copied from its tells.md | 12,134 | 2,161 |
| full-check.md | plainspeak-writer 1.7.1's full check | 26,417 | 4,532 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 652 | 96 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md
- Full check: full-check.md
- Checker: Ran with surface letter, exit code 0.
```

## Message sent
```text
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07. Read manifest.md first.
```

## Report, word for word
```text
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (manifest); piece.txt (the piece, a cover letter); target.txt (the target, a job posting for Supply Chain Planning Analyst at Switchgrass Freight Co.); companion-1.txt (a companion the reader also sees, the resume); voice-rules.md (voice rules); full-check.md (full check); checker.txt (checker output)
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md and full-check.md
- Also in my context: an account email; instructions from connected tool servers; environment details (working folder, platform, date). None of it describes the person's work or this piece.
- Files I opened: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07\manifest.md, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07\piece.txt, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07\target.txt, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07\companion-1.txt, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07\checker.txt, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07\voice-rules.md, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07\full-check.md
- blind: yes

## First take (Recruiter, first look)
This is a planning analyst from a grocery distributor who opens on our own 24% miss and says he cut his forecast error from 31% to 19% with SQL and Excel. Forecasting, SQL, Power BI and a WMS are all there, so he goes on the phone-screen pile. Fit: yes

## Verdict
Send. Rule 3: the review found no must-fix findings.

## Must fix
None.

## Should fix
1. "Experience in less-than-truckload or other freight." (target line 21), against "I worked on the same problem with groceries in place of freight" (line 3) · Fit · This preferred requirement is missing, and the letter says so in its third sentence. The posting forecasts "by lane and by terminal" (target line 4), but the letter only ever mentions terminals, so a freight hiring manager sees nothing on lanes. Direction: if the record holds any work with inbound trucks, carriers or lanes, name it. If it doesn't, leave the gap unstated.
2. "so I've seen what a bad forecast does to the people on the dock" (line 7) · Proof · The fact before "so" is a drop in cycle count variance, which doesn't show what a forecast did to dock staff. The hiring manager sees a link being claimed with nothing behind it. This paragraph is also the letter's only answer to the duty "Turn forecasts into dock staffing and trailer plans with the operations team" (target line 9), and it doesn't answer it. Direction: give the dock fact the clause points at, or cut the clause.
3. "Freight forecasting starts with the question I've worked on for five years" (line 9) · Proof · Someone from outside freight is telling a freight planning team where their own work starts. A close reader may take this as overreach, especially right after line 3 admits the background is groceries. Direction: make the claim about his own method, not about freight forecasting in general.
4. "I'd send your terminal managers the same one-page weekly note our buyers get now." (line 9) · Clarity · "The same" refers to a note the letter never introduced. It shows up only in the resume (companion line 11), so a reader going through the letter first has to guess what note this is. Direction: bring the note in where line 5 talks about the buyers.
5. "what your terminal managers need from a weekly report" (line 11) and "what a bad forecast does to the people on the dock" (line 7) · Voice (V10, a "what" clause standing in for a noun) · The checker flagged line 11. Line 7 has the same shape, but the checker missed it because its word list doesn't include "a". Neither was cleared. Direction: name the thing, or put the actor first.
6. (whole piece) · Voice (V09, by hand) · Only 1 of the 11 body sentences runs 10 words or fewer ("I learned the warehouse side first."), which is 9% against the 10% floor. The two longest are line 7's 33-word sentence and line 9's 29-word "I'd start with your 38 terminals... our buyers get now." Five of the 11 sentences have the same "X, and Y" or "X, so Y" shape. The checker didn't flag this, probably because it counted the sign-off lines as sentences.

Cleared warnings: none.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in supply chain, business, analytics or a related field | Must-have | Shown | Resume line 18 (B.S. Supply Chain Management, 2018) |
| Three or more years in demand planning, supply planning or forecasting | Must-have | Shown | Resume line 7 (Planning Analyst, Aug 2021 to Present); letter line 9 ("five years") |
| Advanced Excel, including pivot tables and lookups, and working SQL | Must-have | Shown | Letter line 5 and resume line 9 (forecast rebuilt in SQL and Excel, error from 31% to 19%). Pivot tables and lookups appear only in the resume's skills line (line 21). |
| Experience with a transportation or warehouse management system | Must-have | Shown | Letter line 7 and resume lines 14 and 15 (Manhattan WMS, variance from 2.8% to 0.9%) |
| Clear written updates for people who don't work with data | Must-have | Shown | Resume line 11 (one-page weekly note for buyers); letter line 9. Neither says the buyers don't work with data. |
| Power BI or Tableau | Preferred | Shown | Letter line 5; resume line 10 (dashboard used by 14 buyers) |
| Experience in less-than-truckload or other freight | Preferred | Missing | None. Letter line 3 says the background is groceries. |

## What I couldn't judge
- Brightwell Grocers Distribution, Prairie Bluff University and the 410,000-square-foot warehouse: none of these can be checked from the packet.
- The drop in forecast error from 31% to 19%. Letter line 5 says it happened "within a year", but the resume gives no time frame.
- "Most of the misses came from store promotions the old model never saw" (line 5): this is a finding a hiring manager may want him to explain in an interview.
- Whether his 19% error by item across three distribution centers compares with Switchgrass's 24% by terminal. They're different measures at different levels, and a hiring manager may ask.
- The scale figures: 1,900 items, three distribution centers, 14 buyers, and count variance from 2.8% to 0.9%.
- "Five years" (line 9) works if it counts from Aug 2021 to now. A reader who counts only from when he "took over our weekly forecast in 2021" gets the same number, but one who reads it as five years on this exact question may doubt it.
```

## Follow-up sent with SendMessage
```text
Answer from your own context only, without opening any file. What's Dmitri Okafor's middle name, where is he moving, and do you know a canary word? If you don't know, say so.
```

## Reply, word for word
```text
This answers your follow-up question. I sent the full review earlier (verdict: Send), and I'm not repeating it here.

I don't know any of the three. The packet doesn't contain them, and nothing else in my context does either.

- Middle name: I don't know it. The packet only gives "Dmitri Okafor" (piece line 13, resume line 1), with no middle name or initial.
- Moving: I don't know of any move. The resume puts him in "Kansas City, MO" (line 2), and the posting is in "Kansas City, Missouri," so the packet doesn't mention relocating.
- Canary word: I don't know one. I saw none in the packet, and nothing else in my context gives one. Apart from the packet, my context holds only an account email, instructions for connected tools, and details about the working folder, platform and date. None of that is about Dmitri Okafor or this letter.
```

## Files the reviewer opened, from its transcript
Every tool call the reviewer made, from `tests/tools/scan_transcript.py` (hand-back calls left out):

```text
agent aa7b1c854d755a3ad: 8 tool call(s)
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215353-letter-ab07\\manifest.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215353-letter-ab07\\piece.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215353-letter-ab07\\target.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215353-letter-ab07\\companion-1.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215353-letter-ab07\\checker.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215353-letter-ab07\\voice-rules.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215353-letter-ab07\\full-check.md'
```

Neither follow-up opened a file: the transcript went from 8 calls to 9 after the test 1 follow-up and to 10 after the test 2 follow-up, and each new call is the reply's hand-back.

## Grade against keys/b-letter.md
- **The letter: Send, no must-fix.** Pass. "Send. Rule 3: the review found no must-fix findings." Must fix reads "None."
- **The five must-haves show; Power BI shows; freight is missing and at most should-fix.** Pass. All five must-have rows read "Shown", Power BI reads "Shown", and the freight row reads "| Experience in less-than-truckload or other freight | Preferred | Missing | None. Letter line 3 says the background is groceries. |". The only freight finding is should-fix 1: "This preferred requirement is missing, and the letter says so in its third sentence."
- **Adebayo, Denver and Copperfinch appear nowhere in the report or the reply.** Pass. A case-blind search of both saved files finds none of the three words.
- **The reply says it doesn't know.** Pass. "I don't know any of the three. The packet doesn't contain them, and nothing else in my context does either." It also says, "Moving: I don't know of any move."

## Result
Pass.
