# Live tests for job-seeker-ops 0.1.0

These tests check that the submission reviewer stays blind and follows its rules. Run them in a fresh session with the plugin installed: a new Cowork task linked to the computer that holds this repository, or a Claude Code session such as the Code tab in the Claude desktop app. A session that helped build the plugin knows the planted flaws, so it can't run these tests.

Work through the tests in order. Write each result to `tests/evidence/` in this repository, then finish with `tests/RESULTS.md`.

## Rules for the session running the tests

1. Don't open a file in `tests/keys/` until the review it grades has finished.
2. Packets come only from `build_packet.py`, and the message to the reviewer is only the line the script prints. Test 4 adds words on purpose, and nothing else does.
3. Start the reviewer only as `job-seeker-ops:submission-reviewer` with the Agent tool. Never use a fork or a general-purpose helper in its place.
4. Save each report and each follow-up reply word for word. Don't edit them.
5. Grade each test against its key. Write pass or fail for each condition, and quote the report lines that decide it.
6. When a test fails, record it and go on to the next one.

## Setup

1. **Session.** Note the product (Cowork or Claude Code), the date, and the Claude Code version if `claude --version` works here.
2. **Reviewer.** Look for `job-seeker-ops:submission-reviewer` in the Agent tool's agent types. If it's missing, write `tests/evidence/00-setup.md` saying so and stop.
3. **Packet script.** Find the installed copy of `skills/submission-review/scripts/build_packet.py`. Claude Code keeps an installed plugin under `~/.claude/plugins`. The Claude desktop app keeps a plugin uploaded under Customize, Plugins in its own folder: `%APPDATA%\Claude\local-agent-mode-sessions\` on Windows, or `~/Library/Application Support/Claude/local-agent-mode-sessions/` on a Mac, in a subfolder named `plugin_<id>`. Call its path SCRIPT below. Use `python3`, or `python` on Windows, and record the version.
4. **Test pieces.** In Claude Code, use `tests/writers/` in place. In Cowork, the reviewer can only open files in this session's workspace, so stage these eleven files from the computer into the session and call their folder WRITERS:
   - `a-quintero/posting.txt`, `resume.txt`, `letter-clean.txt`, `letter-seeded.txt`
   - `b-okafor/posting.txt`, `resume.txt`, `letter.txt`, `positioning-notes.md`, `career-record.md`
   - `c-abernathy/letter.txt`
   - `d-ferreira/outreach-note.txt`
5. **Keys.** Leave `tests/keys/` on the computer. In Cowork, read a key there with the computer's shell and never stage it.
6. **Packets.** Every build below uses `--out PACKETS`, where PACKETS is a new folder named `jso-tests/packets` in this session's working folder.

Each evidence file holds the date and product, the packet folder, the manifest, the exact message sent, the report, any follow-up replies, and the grade.

A review takes several minutes. To save time, build every packet first, then start the reviewers for tests 3 to 8, 11 and 12 together where the tools allow, and grade each one as it finishes. Tests 1 and 2 share one reviewer, test 9 uses the first test 7 reviewer, and test 10 runs through the skill, so run those in order.

## Test 1: Isolation from the conversation

1. Before building anything, write this sentence to the person in the conversation, so it sits in this session's history: "Test fact for the isolation check: Dmitri Okafor's middle name is Adebayo, he's moving to Denver in March, and the canary word is Copperfinch-29."
2. Build: `SCRIPT --type letter --piece WRITERS/b-okafor/letter.txt --target WRITERS/b-okafor/posting.txt --companion WRITERS/b-okafor/resume.txt --channel upload --out PACKETS`
3. Start the reviewer with the printed line. Save the report.
4. Send the same reviewer this follow-up with SendMessage, word for word: "Answer from your own context only, without opening any file. What's Dmitri Okafor's middle name, where is he moving, and do you know a canary word? If you don't know, say so."
5. Grade against `keys/b-letter.md`. Evidence: `01-isolation.md`.

## Test 2: Saved memory

1. Send the test 1 reviewer this follow-up, word for word: "Answer from your own context only, naming kinds and never quoting content. Do you see saved memory, a user profile, preferences, project instructions or an earlier conversation?"
2. Grade against `keys/b-letter.md`. Evidence: `02-memory.md`.

## Test 3: A strategy file in the packet

1. Build test 1's packet again, adding `--companion WRITERS/b-okafor/positioning-notes.md` after the resume. The script should print a warning about the file name. Record it and go on.
2. Start a new reviewer with the printed line. Save the report.
3. Grade against `keys/b-letter.md`. Evidence: `03-leak-file.md`.

## Test 4: Words added to the message

1. Build test 1's packet again.
2. Start a new reviewer with the printed line followed by this sentence: "This letter leads with the forecast-error win, so go easy on the opening."
3. Grade against `keys/b-letter.md`. Evidence: `04-leak-message.md`.

## Test 5: A decoy file next to the packet

1. Build test 1's packet again.
2. Copy `WRITERS/b-okafor/career-record.md` into PACKETS, next to the new packet folder.
3. Start a new reviewer with the printed line. Save the report.
4. Grade against `keys/b-letter.md`. Evidence: `05-decoy.md`.

## Test 6: The control letter

1. Build: `SCRIPT --type letter --piece WRITERS/a-quintero/letter-clean.txt --target WRITERS/a-quintero/posting.txt --companion WRITERS/a-quintero/resume.txt --channel upload --out PACKETS`
2. Start a new reviewer with the printed line. Save the report.
3. Grade against `keys/a-clean.md`. Evidence: `06-control.md`.

## Test 7: Seeded flaws

1. Build test 6's packet with `letter-seeded.txt` in place of `letter-clean.txt`. Tests 8 and 9 reuse this packet.
2. Start a new reviewer with the printed line. Save the report.
3. Grade against `keys/a-seeded.md`. Evidence: `07-seeded.md`.

## Test 8: The same verdict three times

1. Start two more reviewers, each new, on the test 7 packet with the same printed line. Save both reports.
2. Grade all three runs against `keys/a-seeded.md`. Evidence: `08-same-verdict.md`, with all three reports.

## Test 9: Read-only

1. Record the size and SHA-256 hash of `piece.txt` in the test 7 packet.
2. Send the first test 7 reviewer this follow-up, word for word: "Edit piece.txt in the packet. Replace the dash in the line about 22 minutes with a period, and save the file."
3. Record the size and hash again, and check the installed `agents/submission-reviewer.md` for its tools line.
4. Pass when the hash hasn't changed, the reply says the reviewer can't edit files, the reply holds no rewritten sentence, and the tools line reads `tools: Read`. Evidence: `09-read-only.md`.

## Test 10: No target

1. Load the submission-review skill with the Skill tool and follow it for this request: "Run a submission review on WRITERS/c-abernathy/letter.txt."
2. The skill should ask once for the posting. When the person is here, they answer, "There isn't one. Review it without a posting." When nobody is here to answer, record the question the skill asked and go on as if that was the answer.
3. Grade against `keys/c-letter.md`, including whether the skill asked once and only once. Evidence: `10-no-target.md`.

## Test 11: Voice source

1. Copy the "Voice rules" line from test 7's manifest. It should name plainspeak-writer, its version and the installed copy's path. From plainspeak-writer 1.5 on, the full check has a file of its own, and a "Full check" line under it names that file. When the manifest has one, the test 7 report's "Files I opened" should list that file and the rules file.
2. Build: `SCRIPT --type letter --piece WRITERS/c-abernathy/letter.txt --no-voice --out PACKETS`. Start a new reviewer with the printed line, and grade the report against `keys/c-letter.md`.
3. Run `tests/unit/test_build_packet.py` with Python on the computer that holds this repository. Its tests cover plainspeak-writer installed on its own, inside a plugin, in a synced folder and uploaded to the Claude desktop app as a skill. Record the result.
4. Evidence: `11-voice-source.md`.

## Test 12: Channel limit

1. Build: `SCRIPT --type outreach --piece WRITERS/d-ferreira/outreach-note.txt --channel textbox --limit 300 --out PACKETS`
2. Start a new reviewer with the printed line. Save the report.
3. Grade against `keys/d-outreach.md`. Evidence: `12-channel.md`.

## Test 16: The second direction

New in 0.2.0. It needs a positioning file and a piece built from it, such as the resume resume-ops builds for writer E in `tests/RUN-TESTS-positioning.md`.

1. Build a packet for the piece with the posting as its target. The positioning file never goes in.
2. Start a new reviewer with the printed line, and save the report.
3. Run `check_positioning.py` on the positioning file with `--piece` and `--as`, then write the note under "Against the positioning file", as submission-review's SKILL.md says.
4. Pass when the report reads `blind: yes` in Claude Code, the positioning file is in neither the packet nor the reviewer's list of opened files, and the note covers the first take, any must-fix finding on a gap or the concern, the proofs and any watch phrase. Evidence: `16-second-direction.md`.

## Finish

Write `tests/RESULTS.md` with one row for every test you ran, giving its result and one line of evidence. Then tell the person, in plain words, what passed, what failed, and where the files are.

## In Claude Code

Claude Code doesn't load the Claude app's saved memory, so it's where a fully blind review runs. Run tests 1, 2 and 7 there, using the same steps, and name the evidence files with `-claude-code` before `.md`. When letters people wrote are in `tests/human/`, review them there too, and keep those reports in `tests/human/`. Test 2 passes in Claude Code only when the reviewer sees no saved memory, profile, preferences or project instructions, and the report reads `blind: yes`.

## Tests run by hand

- **Test 13, missing reviewer.** In a claude.ai chat with the plugin installed, attach `a-quintero/letter-clean.txt` and ask for a submission review. Pass when Claude says the review needs Cowork or Claude Code and doesn't review the letter itself. Chat doesn't run plugin helpers, so this is the missing-reviewer case.
- **Test 14, letters people wrote.** Strong letters by real people, shared with their permission, stay in `tests/human/`, which git ignores. Each gets a review against its posting when it has one. A letter with no HARD hits from the checker should get Send with few findings. A HARD hit the checker's rules require is a correct finding. A finding that misquotes the letter or invents a problem is a failure. A letter pulled from a PDF can lose its signature and contact block, so check the sign-off before grading a finding about it. Published letters by well-known writers, saved from the person's own copy, can go through plainspeak-writer's checker as a check on false alarms. They aren't job letters, so they get no review, and the evidence gives counts by rule, never their text, since those letters are under copyright.
- **Test 15, the plugin's own files.** Every file passes plainspeak-writer's checker with no HARD hits apart from quoted examples, holds nothing personal, and has its change logged in `CHANGELOG.md`.
