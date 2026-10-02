# Test 11: Voice source

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

## Step 1: the Voice rules line from test 7's manifest

````
- Voice rules: plainspeak-writer 1.3. Rules file: /root/.claude/skills/synced/<account>/plainspeak-writer/references/tells.md
````

It names plainspeak-writer, version 1.3, and the installed copy's path.

Note: the plainspeak-writer copy that sits next to this repository on the computer is version 1.4 (its CHANGELOG starts at “1.4 · The check reads like a reader”). The copy synced into this Cowork session is 1.3. So every packet in this run used the 1.3 rules and checker. Worth syncing the newer version.

## Step 2: build with --no-voice

````
/root/.claude/plugins/synced/<account>/job-seeker-ops/skills/submission-review/scripts/build_packet.py --type letter --piece /mnt/user-data/uploads/tools/job-seeker-ops/tests/writers/c-abernathy/letter.txt --no-voice --out /home/claude/jso-tests/packets
````

Script output:

````
Packet: /home/claude/jso-tests/packets/20261001-165236-letter-1c29
Message for the reviewer (send exactly this line and nothing else):
Review the packet in /home/claude/jso-tests/packets/20261001-165236-letter-1c29. Read manifest.md first.
````

## Review (built with --no-voice)

- Packet folder: `/home/claude/jso-tests/packets/20261001-165236-letter-1c29`
- Reviewer agent id: `a50069b4d737f07ec`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.0 on 2026-10-01 at 16:52.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,027 | 175 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: none given. Review against a general reader for this type of piece.
- Channel: not given.
- Voice rules: not found. Voice is unchecked.
- Checker: Didn't run, because plainspeak-writer wasn't found.
````

### Exact message sent

````
Review the packet in /home/claude/jso-tests/packets/20261001-165236-letter-1c29. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-1c29/manifest.md"}
Read {"file_path": "/home/claude/jso-tests/packets/20261001-165236-letter-1c29/piece.txt"}
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: piece.txt (the piece: cover letter, 1,027 characters, 175 words); manifest.md (the manifest)
- Voice rules: not found (the manifest gives no path)
- Also in my context: saved memory, a user profile, user preferences, a memory file listing, and account details (the user's email). I didn't use any of it.
- Files I opened: /home/claude/jso-tests/packets/20261001-165236-letter-1c29/manifest.md, /home/claude/jso-tests/packets/20261001-165236-letter-1c29/piece.txt
- blind: no (saved memory, a user profile, preferences and account details were in my context)

## First take (Recruiter, first look)
A high school chemistry teacher with nine years in the classroom who has spent four years building online labs in Articulate Rise, and who now wants to design courses. The second paragraph gives a tool, a count and a result, so I'd keep reading. Fit: yes

## Verdict
Send. Rule 3: there are no must-fix findings.

## Must fix
None.

## Should fix
1. "I'd like to build courses with your design team." (line 3) and "talk about the courses you're building next." (line 9) · Proof · The firm shows up only in the greeting. Swap the name and these lines could go to any course design firm, so the hiring manager never learns why Copperleaf. Direction: name one Copperleaf course, audience or product and tie it to the stoichiometry work.
2. "I'm best at finding where students get lost." and "I've also trained 40 teachers in my district to build their own modules" (line 7) · Proof · Both claims stop at the activity. The first describes a method but gives no change it produced. The second gives a headcount but no outcome, such as how many modules those teachers went on to build or use. Direction: give one result for each claim.
3. "the share of students passing our stoichiometry unit rose from 58% to 71%" (line 5) and "the stoichiometry module" (line 9) · Clarity · A recruiter without a chemistry background may not know the word. The letter's best number sits on a term they can't place. Direction: add a few plain words on what the unit covers, or let the number stand without the term.

Cleared warnings: none (the checker didn't run).

## Requirements
No target was given, so I skipped the fit check and reviewed against a general reader for a cover letter.

| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| None. | | | |

## Voice
Voice: unchecked. The manifest says the voice rules weren't found and the checker didn't run.

## Channel
No channel or character limit was given, so I couldn't check length against one. At 175 words the letter is short. The first two lines say who she is and what she wants, which works if the letter is read on a phone.

## Risk
None. The letter names no gap, apology or exit story. No companion documents came with it, so there was nothing to cross-check.

## What I couldn't judge
- Larkhollow High School, the nine years and the four years of building online labs.
- 26 labs converted in 2022, and whether that work was done in Articulate Rise.
- 1,100 students across six schools last year.
- The pass rate going from 58% to 71%, and whether the modules caused the rise or something else did, such as a curriculum change or a different group of students. A hiring manager would likely ask.
- 40 teachers trained, six workshops, and the guide she wrote.
- What Copperleaf Learning builds and who its design team serves.

Nothing from this review needs saving to memory.
````

## Step 3: unit tests

Run on the computer that holds the repository (the Cowork shell on the owner's computer, Python 3.10.12), with bytecode writing turned off so no file in the repo changed:

````
PYTHONDONTWRITEBYTECODE=1 python3 -B tests/unit/test_build_packet.py -v
````

Output:

````
test_checker_exit_code_recorded (__main__.BuildPacketTests) ... ok
test_discovery_finds_each_layout_and_picks_newest (__main__.BuildPacketTests) ... ok
test_discovery_skips_a_folder_with_another_skill_name (__main__.BuildPacketTests) ... ok
test_docx_text_and_header_note (__main__.BuildPacketTests) ... ok
test_empty_piece_refused (__main__.BuildPacketTests) ... ok
test_limit_over_and_under (__main__.BuildPacketTests) ... ok
test_message_line_is_exact (__main__.BuildPacketTests) ... ok
test_missing_piece_refused (__main__.BuildPacketTests) ... ok
test_no_field_for_notes (__main__.BuildPacketTests) ... ok
test_no_target_says_general_reader (__main__.BuildPacketTests) ... ok
test_no_voice_marks_voice_unchecked (__main__.BuildPacketTests) ... ok
test_original_file_names_left_out (__main__.BuildPacketTests) ... ok
test_pdf_refused (__main__.BuildPacketTests) ... ok
test_readers_validated (__main__.BuildPacketTests) ... ok
test_real_checker_when_available (__main__.BuildPacketTests) ... ok
test_strategy_name_warns (__main__.BuildPacketTests) ... ok
test_text_piece_copied_with_line_endings_fixed (__main__.BuildPacketTests) ... ok
test_unknown_surface_falls_back_to_general (__main__.BuildPacketTests) ... ok
test_voice_dir_runs_checker_with_mapped_surface (__main__.BuildPacketTests) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.297s

OK
exit=0
````

The last test used the real plainspeak-writer next to the repository and ran (not skipped). A file list with sizes and times taken before and after the run matched, so the run changed nothing in the repo.

## Grade (keys/c-letter.md, test 11 part, plus RUN-TESTS.md steps 1 and 3)

- **Pass**: Test 7's “Voice rules” line names plainspeak-writer, its version and the installed path
  - Decided by the check or the lines noted in this file, outside the report.
- **Pass**: --no-voice manifest says the voice rules weren't found
  - Decided by the check or the lines noted in this file, outside the report.
- **Pass**: Report writes Voice: unchecked
  - Quote: “Voice: unchecked. The manifest says the voice rules weren't found and the checker didn't run.”
- **Pass**: No voice findings
  - Quote: “· Proof ·”
  - Quote: “· Clarity ·”
- **Pass**: Verdict comes from the other checks: Send
  - Quote: “Send. Rule 3: there are no must-fix findings.”
- **Pass (19 of 19)**: Unit tests pass on the computer
  - Decided by the check or the lines noted in this file, outside the report.

The manifest lines that decide the second row: “Voice rules: not found. Voice is unchecked.” and “Checker: Didn't run, because plainspeak-writer wasn't found.” The report's three should-fix findings are two Proof and one Clarity.

**Result: Pass**
