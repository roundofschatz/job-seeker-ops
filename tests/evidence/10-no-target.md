# Test 10: No target

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

## How it ran

1. Loaded `job-seeker-ops:submission-review` with the Skill tool for the request “Run a submission review on WRITERS/c-abernathy/letter.txt.”
2. The skill checked for the reviewer (present), then asked once, in one message, for the missing posting and the optional companions and channel. The question, as asked (AskUserQuestion, options “No posting” and “I'll give a posting”):

````
Test 10 (the skill's question): To review c-abernathy/letter.txt, I need the job posting it answers, or the reader's own words for what they want. Optional: anything the reader also sees, like a resume, and where it goes (upload, a text box with a limit, or an email). Which posting should I use?
````

3. The owner was here and answered: “there is none”. The skill asked nothing more.
4. The skill built the packet with the script and started the reviewer with the printed line only:

````
python3 "/root/.claude/plugins/synced/<account>/job-seeker-ops/skills/submission-review/scripts/build_packet.py" --type letter --piece /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/c-abernathy/letter.txt --out /home/claude/jso-tests/packets
````

````
Packet: /home/claude/jso-tests/packets/20261001-170017-letter-f53b
Message for the reviewer (send exactly this line and nothing else):
Review the packet in /home/claude/jso-tests/packets/20261001-170017-letter-f53b. Read manifest.md first.
````

`--out PACKETS` was added so this packet sits with the others; the skill doesn't set a folder of its own.

## Review

- Packet folder: `/home/claude/jso-tests/packets/20261001-170017-letter-f53b`
- Reviewer agent id: `aacff7626dcccabe0`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 17:00.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,027 | 175 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 750 | 121 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: none given. Review against a general reader for this type of piece.
- Channel: not given.
- Voice rules: plainspeak-writer 1.3. Rules file: /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Checker: Ran with surface letter, exit code 0.
````

### Exact message sent

````
Review the packet in /home/claude/jso-tests/packets/20261001-170017-letter-f53b. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read {"file_path": "/home/claude/jso-tests/packets/20261001-170017-letter-f53b/manifest.md"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-170017-letter-f53b/piece.txt"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-170017-letter-f53b/checker.txt"}
Read {"file_path": "/root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md"}
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (packet index and settings); piece.txt (the piece: cover letter, 1,027 characters, 175 words); checker.txt (plainspeak-writer checker output for piece.txt, surface letter, exit code 0)
- Voice rules: plainspeak-writer 1.3, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- Also in my context: saved memory (a user profile, saved preferences and a listing of memory files) and account details (the user's email). I didn't quote or use any of it.
- Files I opened: /home/claude/jso-tests/packets/20261001-170017-letter-f53b/manifest.md, /home/claude/jso-tests/packets/20261001-170017-letter-f53b/piece.txt, /home/claude/jso-tests/packets/20261001-170017-letter-f53b/checker.txt, /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
- blind: no (my context held saved memory, a user profile and preferences, and account details. The message and the packet were clean, and no leaked files were found.)

## First take (Recruiter, first look)
This is a high school chemistry teacher with nine years in the classroom who has spent four years building her district's online labs in Articulate Rise, with a pass-rate gain to show for it. She reads as a credible teacher moving into course design, and I'd keep reading. Fit: yes

## Verdict
Send. Rule 3: the first take is Fit: yes and there are no must-fix findings.

## Must fix
None.

## Should fix
1. "I'd like to build courses with your design team." (line 3) and "talk about the courses you're building next." (line 9) · Proof · Copperleaf is named only in the greeting. Change that name and the letter could go to any course-design firm unchanged, so the hiring manager never learns why she picked this firm. Direction: name a course, audience or product Copperleaf builds and tie it to her work.
2. "I'd like to show you the stoichiometry module" (line 9) · Proof · The best proof in the letter is offered for later, but the reader has no way to see it now. A hiring manager has to reply before they can check the work. Direction: give a link to the module.
3. "the share of students passing our stoichiometry unit rose from 58% to 71%" (line 5) and "the stoichiometry module" (line 9) · Clarity · A recruiter who isn't a chemist may not know the word. It names the unit behind her headline number, so it matters more there than anywhere else. Direction: name the topic in plain words once, unless the role is science content.
4. "I'd like to build courses with your design team." (line 3) and "I'd like to show you the stoichiometry module" (line 9) · Voice · Both asks open on the same words. In a letter this short, the second one reads as an echo of the first. Direction: change the shape of one of the two sentences.

Cleared warnings: V01 at line 5 ("a two-minute video, a practice set and a quiz that checks the one idea the lab teaches") is cleared because each item is specific and describes what the module holds. V01 at line 7 ("six after-school workshops and a step-by-step guide I wrote") is cleared because each item is specific and counted, and it's two items, not a crutch list.

## Requirements
None. No target was given, so this check was skipped and the review used a general reader for a cover letter.

## What I couldn't judge
- Larkhollow High School, the nine years teaching and the four years building online labs.
- 26 labs converted in 2022, and 1,100 students across six schools last year.
- The pass-rate rise from 58% to 71%. A careful hiring manager will ask whether the modules caused it or whether something else changed in the same period. The letter puts the two facts side by side without saying how they're linked.
- 40 teachers trained through six workshops, and the guide she wrote.
- What role at Copperleaf Learning this letter is for. Without a target, I can't say whether a classroom background meets the posting's bar.

Nothing from this review needs saving to memory.
````

## Grade (keys/c-letter.md)

- **Pass**: The skill asked for the posting once and no more
  - Decided by the check or the lines noted in this file, outside the report.
- **Pass**: Manifest says no target was given
  - Decided by the check or the lines noted in this file, outside the report.
- **Pass**: Report says it used a general reader for a cover letter
  - Quote: “No target was given, so this check was skipped and the review used a general reader for a cover letter.”
- **Pass**: Requirement check skipped, “None.” under Requirements
  - Quote: “## Requirements ⏎ None.”
- **Pass**: Verdict Send (checker has only two list-of-three warnings)
  - Quote: “Send. Rule 3: the first take is Fit: yes and there are no must-fix findings.”

The manifest line that decides the second row: “Target: none given. Review against a general reader for this type of piece.”

The checker found two V01 list-of-three warnings and no HARD hits; the report cleared both with reasons.

Note: the same session ran the skill and graded it, so “asked once” rests on this session's own record. The question above is the only one it asked.

**Result: Pass**
