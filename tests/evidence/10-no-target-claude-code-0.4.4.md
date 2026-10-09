# Test 10: No target (Claude Code, job-seeker-ops 0.4.4)

## Run
- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app, Windows 11 Pro. `claude --version` on this computer's PATH reports 2.1.295.
- Plugin: job-seeker-ops 0.4.4, installed on the account, in `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>`. Packet script: build_packet.py 0.4.0. Voice rules: the plugin's own plainspeak-writer 1.7.1 (check_voice 1.7.1).
- Python: `python`, 3.12.10.
- SCRIPT: `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\submission-review\scripts\build_packet.py`. WRITERS: `C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers`. PACKETS: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets`.
- Session: a fresh helper session in the Code tab that didn't build the plugin. Every reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, never a fork or a general-purpose helper.
- Packet: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215734-letter-a6f7`
- Reviewer agent ID: a575d0d388a28e692.
- Key: `tests/keys/c-letter.md`, opened after this report came back.

## Following the skill
1. Loaded `job-seeker-ops:submission-review` with the Skill tool for the request "Run a submission review on C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers\c-abernathy\letter.txt."
2. Checked the Agent tool's agent types: `job-seeker-ops:submission-reviewer` is there, so the skill goes on to Step 1.
3. Step 1 says to ask once, in one message, for whatever's missing. The piece was given; the posting was missing; companions and channel are optional. This session asked once, in this message, and asked nothing more afterward:

```text
Do you have the job posting this letter is for, or the reader's own words for what they want? If there's a resume or anything else the reader sees with the letter, send that too, and tell me where the letter goes: an upload, a text box with its character limit, or an email body. If there's no posting, I'll go on without one, and the reviewer will read it as a general reader for a cover letter would.
```

4. Nobody was there to answer. As RUN-TESTS says, the run went on as if the answer had been "There isn't one. Review it without a posting."
5. Step 2, built the packet:

`python SCRIPT --type letter --piece WRITERS\c-abernathy\letter.txt --out PACKETS`

```text
Voice rules from: \\?\C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\plainspeak-writer
Packet: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215734-letter-a6f7
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215734-letter-a6f7. Read manifest.md first.
```

6. Step 3, started the reviewer with the printed line and nothing else, and waited for the report.
7. Step 4, the hand-back: the report goes to the person as it came back, below. It reads `blind: yes`, so no explanation line is needed. After it, the skill offers to revise the piece.

## Manifest
```text
# Review packet

Built by build_packet.py 0.4.0 on 2026-10-08 at 21:57.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,025 | 174 |
| voice-rules.md | plainspeak-writer 1.7.1's voice rules, copied from its tells.md | 12,134 | 2,161 |
| full-check.md | plainspeak-writer 1.7.1's full check | 26,417 | 4,532 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 789 | 125 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: none given. Review against a general reader for this type of piece.
- Channel: not given.
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md
- Full check: full-check.md
- Checker: Ran with surface letter, exit code 0.
```

## Message sent
```text
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215734-letter-a6f7. Read manifest.md first.
```

## Report, word for word
```text
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the manifest), piece.txt (the piece, a cover letter), voice-rules.md (voice rules), full-check.md (the full check), checker.txt (checker output for piece.txt)
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md and full-check.md
- Also in my context: an account email
- Files I opened: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215734-letter-a6f7\manifest.md, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215734-letter-a6f7\piece.txt, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215734-letter-a6f7\checker.txt, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215734-letter-a6f7\voice-rules.md, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215734-letter-a6f7\full-check.md
- blind: yes

## First take (Recruiter, first look)
This is a high school chemistry teacher who has built 26 online lab modules in Articulate Rise and wants to move into course design, and the numbers (1,100 students, 58% to 71%) show up in the first ten seconds. With no target to compare against, the background fits a general course-design opening. Fit: yes

## Verdict
Send. Rule 3 set it: there are no must-fix findings.

## Must fix
None.

## Should fix
1. "I'd like to build courses with your design team." (line 3) and "talk about the courses you're building next." (line 9) · Proof · Copperleaf Learning shows up only in the greeting. These two lines could go to any course company unchanged, so the hiring manager never finds out why this firm and not another one. Direction: name something Copperleaf builds or serves and tie it to the lab work.
2. "Last year 1,100 students across six schools used them, and the share of students passing our stoichiometry unit rose from 58% to 71%." (line 5) · Proof · The sentence implies the modules caused the rise. A close reader will ask what the 58% is measured against (which year, which schools) and whether anything else changed. Direction: state the baseline the two figures compare.
3. "I'm best at finding where students get lost. I sit in the back of other teachers' classes, note the moment students stop asking questions, and rebuild that step of the lesson." (line 7) · Proof · The letter calls this its strongest skill, and the method is clear, but no rebuilt lesson or result follows. The claim stops at the process. Direction: name one step that was rebuilt and what changed afterward.
4. "I'd like to build courses with your design team." (line 3) · Clarity · The letter never names a role or posting, so a recruiter sorting letters has to guess which opening this is for. Direction: name the role.
5. "the share of students passing our stoichiometry unit" (line 5) and "the stoichiometry module" (line 9) · Clarity · Outside chemistry, a recruiter may not know the word. The number still lands, but the reader can't tell what skill the module teaches. Direction: give a few plain words on what the unit covers.
6. "I'd like to build courses" (line 3) and "I'd like to show you" (line 9) · Voice · the same opener used twice in a 174-word letter, and 7 of 10 sentences start with "I".

Cleared warning: V01 list of three (whole piece). "a two-minute video, a practice set and a quiz that checks the one idea the lab teaches" (line 5) names specific items that each do work. "through six after-school workshops and a step-by-step guide I wrote" (line 7) has two items, not three. With one real hit, the piece is under the two-hit minimum.

## Requirements
None. No target was given, so this check was skipped, and the review used a general reader for a cover letter to a course design team.

| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|

## What I couldn't judge
- Larkhollow High School and the unnamed district: a reader may want to know where these are and check them.
- "nine years" teaching and "the last four" building online labs.
- "26 hands-on labs" turned into modules "in 2022".
- "1,100 students across six schools" last year.
- The pass rate moving "from 58% to 71%", and whether the modules caused it.
- "trained 40 teachers" through "six after-school workshops" and a guide she wrote.
- Whether Copperleaf Learning has an open role in course design, and what it asks for.
- Whether the stoichiometry module is ready to show, since the letter offers it.
```

## Files the reviewer opened, from its transcript
```text
agent a575d0d388a28e692: 6 tool call(s)
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215734-letter-a6f7\\manifest.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215734-letter-a6f7\\piece.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215734-letter-a6f7\\checker.txt'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215734-letter-a6f7\\voice-rules.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215734-letter-a6f7\\full-check.md'
```

## Grade against keys/c-letter.md
- **The manifest says no target was given.** Pass. "- Target: none given. Review against a general reader for this type of piece."
- **The report uses a general reader for a cover letter, skips the requirement check, and writes "None." or a note under Requirements.** Pass. "None. No target was given, so this check was skipped, and the review used a general reader for a cover letter to a course design team."
- **The skill asked for the posting once and no more.** Pass. One question, quoted above, and no second ask. This session both followed the skill and grades it, so this condition rests on this session's own transcript.
- **Verdict: Send.** Pass. "Send. Rule 3 set it: there are no must-fix findings."
- **The checker's list-of-three warning is listed or cleared with a reason.** Pass. plainspeak-writer 1.7.1 gives one V01 warning for the whole piece, and the report clears it: "Cleared warning: V01 list of three (whole piece). ... With one real hit, the piece is under the two-hit minimum."

## Result
Pass.
