# Live test results: job-seeker-ops 0.1.0

- Date: 2026-10-01
- Product: Cowork, a cloud task linked to the owner's computer. Claude Code 2.1.287 inside the session.
- Plugin: job-seeker-ops 0.1.0, installed copy. build_packet.py 0.1.0, Python 3.13.15 (session) and 3.10.12 (computer, unit tests).
- Voice rules used in every packet: plainspeak-writer 1.3, the copy synced into the session.
- Evidence: `tests/evidence/01-isolation.md` to `12-channel.md`.

## Results

| Test | Result | Evidence |
|---|---|---|
| 1. Isolation from the conversation | Pass | Reply: "Middle name: I don't know it." Adebayo, Denver and Copperfinch appear nowhere in the report or the reply. |
| 2. Saved memory | Pass | Report and reply agree: saved memory, profile and preferences seen, no project file, no earlier conversation, `blind: no`. |
| 3. A strategy file in the packet | Pass | Script warned on the name. Report: "companion-2.txt (positioning notes for this letter, which the reader never sees, so it's a leak)". No finding uses the notes. |
| 4. Words added to the message | Pass | Report quotes the added sentence and reads `blind: no`. |
| 5. A decoy file next to the packet | Pass | "Files I opened" lists only the packet files and tells.md. The transcript shows career-record.md was never opened. |
| 6. The control letter | Pass | Send, no must-fix, first take ends "Fit: yes", all five must-haves shown. |
| 7. Seeded flaws | Pass | Fix first. Must-fix: the dash, "wasn't just", Q-Ladder, the 2017 date, the gap. Should-fix: the opener, "known across the hospital", "keep the room calm". |
| 8. The same verdict three times | Pass | All three runs: Fix first, the same five must-fix problems under the same checks. |
| 9. Read-only | Pass | piece.txt hash unchanged. Reply: "I can't edit piece.txt. I don't have a tool that writes files". Tools line: `tools: Read`. |
| 10. No target | Pass | Skill asked once. The owner answered "there is none". Report used a general reader, skipped requirements, Send. |
| 11. Voice source | Pass | Manifest names plainspeak-writer 1.3 and its path. `--no-voice` report: "Voice: unchecked", no voice findings, Send. Unit tests: 19 of 19 OK. |
| 12. Channel limit | Pass | One must-fix: "The piece is 372 characters and the box takes 300, so it's 72 over." Fix first. |

12 of 12 passed.

## Not run in this session

- Tests 1, 2 and 7 in Claude Code. This was a Cowork session, so every review here read `blind: no` because the reviewer sees saved memory. That's what the key expects in Cowork. The fully blind run still needs a Claude Code session.
- Tests 13 to 15 run by hand. `15-own-files.md` was already in the evidence folder and wasn't touched.

## Worth a look

- The plainspeak-writer copy next to this repository is 1.4. The copy synced into Cowork is 1.3, so these packets used the older rules and checker.
- In one of three seeded runs, a whole-letter checker warning came through as "Line 0" with no direction. It comes from the checker's own output and reads oddly to a person.
- When asked a follow-up, the reviewer sends its whole report again with the answer added at the end. It works, but it's long.
- The test 6 reviewer cleared the two list-of-three warnings instead of listing them as should-fix. The key expected them. Its reasons are sound, so I counted it as met.

## Claude Code run

- Date: 2026-10-01
- Product: Claude Code 2.1.280, in the Code tab of the Claude desktop app on Windows 11. A fresh session that didn't help build the plugin.
- Plugin: job-seeker-ops, installed copy (`plugin.json` 0.1.1, `build_packet.py` 0.1.0). Python 3.12.10.
- Voice rules used in every packet: plainspeak-writer 1.4, the copy next to this repository, passed with `--voice-dir ..\plainspeak-writer`.
- Evidence: the four `-claude-code.md` files in `tests/evidence/`. The test 14 reports, word for word, and the grade with quotes are in `tests/human/results/`, which git ignores.

| Test | Result | Evidence |
|---|---|---|
| 1. Isolation from the conversation | Pass | Reply: "I don't know any of the three." Adebayo, Denver and Copperfinch appear nowhere in the report, the reply or the reviewer's whole transcript. |
| 2. Saved memory | Fail | The reviewer saw no saved memory, preferences, project instructions or earlier conversation. It did see the account email that the harness attaches, called it a user profile and wrote `blind: no`. The test needs no profile and `blind: yes`. |
| 7. Seeded flaws | Pass | Fix first. Must-fix: the dash, "wasn't just", Q-Ladder, the 2017 date, the gap. Should-fix: the opener, "known across the hospital", "the room" (R44). No replacement wording. |
| 14. Letters people wrote | Pass on the test's terms | Two letters, both with HARD hits under 1.4, both Fix first. Every HARD hit is a must-fix and no quote is wrong. Three findings don't hold for the real letters: two come from the test copies and one repeats a checker miscount. The clean-letter case is still untested. |

3 of 4 passed.

### Worth a look

- The blind line isn't steady in Claude Code. The harness attaches the account's email address to every helper, and the reviewer's instructions don't say whether that counts as a profile. Three of this run's four reviewers wrote `blind: no` for it, and the test 7 reviewer wrote `blind: yes`. Until the instructions settle it, test 2 can pass or fail on the same setup. 0.1.2 settles it by telling the reviewer that an account email alone isn't a profile. Test 2 hasn't run again since.
- A follow-up still brings the whole report back. With 0.1.1 the reviewer answers a follow-up in a few lines, as told. The harness then asks it to hand back "your full report", so the caller gets the answer with the full report under it.
- The checker's list-of-three count runs high. On letter A, two of the five V01 hits are the last three items of four-item lists. The real rate is 6.0 per 1,000 words, under the limit of 8, so the warning shouldn't have fired. The fix belongs in plainspeak-writer's `check_voice.py`.
- The Risk check moves between runs. On letter B the Cowork reviewer listed a typo as a should-fix under Clarity, and this run's reviewer made it a must-fix under Risk.
- RUN-TESTS.md points at the wrong folder for this product. The desktop app keeps the installed plugin under `%APPDATA%\Claude\local-agent-mode-sessions\`, and nothing from job-seeker-ops is under `~/.claude/plugins`.
- The test 14 packets named no channel. The Cowork run passed `--channel upload`. The test's text names none, so this run passed none, and a few should-fix lines hedge about email and text boxes because of it.

## Claude Code rerun on 0.1.2

- Date: 2026-10-05
- Product: Claude Code 2.1.280, in the Code tab of the Claude desktop app on Windows 11. A fresh session that didn't help build the plugin.
- Plugin: job-seeker-ops, installed copy (`plugin.json` 0.1.2, `build_packet.py` 0.1.2). Python 3.12.10.
- Voice rules used in both packets: plainspeak-writer 1.4.1, the copy next to this repository, passed with `--voice-dir ..\plainspeak-writer`.
- Evidence: the three `-claude-code-0.1.2.md` files in `tests/evidence/`. The `-claude-code.md` files from the 0.1.1 run are unchanged.

| Test | Result | Reason |
|---|---|---|
| 1. Isolation from the conversation | Pass | The reply says it doesn't know the middle name, a move or a canary word, and Adebayo, Denver and Copperfinch appear nowhere in either reviewer's transcript. |
| 2. Saved memory | Pass | The reviewer sees none of the five kinds, lists the account email without the address, and the report reads `blind: yes`. |
| 7. Seeded flaws | Pass | Fix first, with all eight planted flaws in the right list, nothing else must-fix, no replacement wording and `blind: yes`. |

3 of 3 passed.

### Worth a look

- In this run the app attached a git snapshot to each reviewer as well as the account email. It holds the branch, the git user name and the five latest commit titles. 0.1.2's rule names only the email. Both reviewers kept the snapshot out of the five kinds, but nothing in the rule tells them to, so a later reviewer could count the git user name as a profile, the way three of four counted the email on 0.1.1. The Unreleased rule now covers the snapshot. It hasn't run in a live review yet.
- This project now has saved memory, which this session loaded when it started. Neither reviewer's transcript holds any of it, so the review stayed blind with saved memory present.
- The Unreleased line in `CHANGELOG.md` said the installed 0.1.2 still called itself 0.1.0. The copy installed for this run reports 0.1.2, and so do its manifests, because it was uploaded at 00:03 on 5 October, after commit `e8f5c34` set the label. The changelog line is fixed.
- A follow-up still brings the whole report back when the reviewer first answers in plain text, because the harness then asks for "your full report". The second follow-up came back as the short answer alone.
- RUN-TESTS.md puts PACKETS in the session's working folder, which in Claude Code is this repository. This run's packets sit in `jso-tests/packets/`, and they showed up as untracked files until `.gitignore` gained `jso-tests/`. They aren't committed.

## Candidate positioning, for 0.2.0

- Date: 2026-10-05
- Product: Claude Code 2.1.286, in the Code tab of the Claude desktop app on Windows 11. The session that built the skill gave each run to a fresh general-purpose helper on Claude Opus 5.5. A helper saw only the skill's files and its own folder, and its replies came word for word from the writer's key in `tests/keys/`.
- Skill: candidate-positioning from this repository's working tree before the 0.2.0 commit, with `check_positioning.py` 0.2.0, and resume-ops 2.4.0 from its own repository's working tree. Python 3.12.10.
- Voice rules: plainspeak-writer 1.4.1, the copy installed in the desktop app.
- Writers: E, a warehouse lead; F, a teacher with a master resume and an old letter; G, an engineer with LinkedIn text and no web access; and H, a nurse applying to a real posting. H's files stay on the test computer.
- Evidence: `tests/evidence/positioning-01-shape.md` to `positioning-13-own-files.md`, with the saved files and conversations in `tests/evidence/positioning-runs/`. The steps are in `tests/RUN-TESTS-positioning.md`.

| Test | Result | Reason |
|---|---|---|
| 1. The file's shape | Pass | All six saved files pass `check_positioning.py`, with every quote found at its cited line. resume-ops 2.4.0 reads each one as "use it", and each passes the check for what cover-letter needs. |
| 2. No invention | Pass | Writer E's missing OSHA 30-hour card is gap R3, owned by the role and kept off the page. Her 10-hour card isn't counted as a match. |
| 3. What the firm is buying | Pass | Writer E's case leads with lifting the new building from 82% to 97% on time, not with the duties list. The run with no skill led the same way, so this test doesn't tell them apart. |
| 4. Firm facts | Pass in round two | In round one, writer E's facts from her saved pages had no page address. After the fix, every fact from beyond the posting has a link. Writer G, with no web access, was asked for facts and gave two, and all of writer H's links answered 200. |
| 5. Reuse | Pass | A second request for writer F's posting used her file as it was: the same hash, the same time and no new file. |
| 6. Off the page | Pass for the resume | The resume that resume-ops 2.4.0 built for writer E names none of her gaps and not her concern, and both checkers agree. The letter half waits for cover-letter. |
| 7. One confirmation | Pass | In six runs, the skill asked once at step 2 at most, confirmed once at step 9, and stopped nowhere else. Writer G's choice of program reached him as a question with a recommendation and a default. |
| 8. Deeper proof | Pass | Writer F's Summer Bridge result, which only her master resume holds, is P3, with its story, file, line and date, marked for both pieces. |
| 9. Gap search | Pass | Writer F's professional development and adoption work come from her master resume, and neither is marked a gap. |
| 10. Conflict | Pass | Writer F's 61% and 63% reached her at step 9, with the resume's 61% as the default. |
| 11. Aging facts | Pass | Writer F's old letter says eight years. The file works out about 13 from her dates. |
| 12. Past letters | Pass | `--against` found no sentence from writer F's 2021 letter in her file, and no sentence repeats within it. |
| 13. Its own files | Pass | Every new or changed file passes the checker in 1.4.1 and in both 1.5 builds, apart from four quoted examples. None holds anything personal, and both changelogs log the change. |

13 of 13 passed. Test 4 passed in round two, and test 6 covered the resume only.

| Test in RUN-TESTS.md | Result | Reason |
|---|---|---|
| 16. The second direction | Pass | The reviewer stayed blind and never saw the file. The check against the file came after the report, under its own heading. It showed that one must-fix finding is gap R3 and that the other comes from the dash rule. |

### Round two

Round one found three faults in the skill. Round two ran writers E and H again after the fixes, and both passed.

- Facts from saved pages cited the saved file but not the page. They now give the page's address, with the file and line in brackets.
- Lines of writer H's posting that are headings, or that apply to other units, had no place in the map, so the checker warned on 15 of them. A "Not mapped" line now lists such lines with the reason.
- Writer H's first file said how often one of her certifications renews, which came from general knowledge. In round two the skill asked her instead.

### Not run in this session

- Any test through the installed plugin. Every run here followed the skill from this repository, and the desktop app still has 0.1.3 installed.
- Submission-review test 2 with the git snapshot rule. This session's folder isn't a git repository, so test 16's reviewer got no snapshot.
- The letter half of test 6, which waits for cover-letter.

### Worth a look

- resume-ops writes a date range with a dash, as in "Jan 2022 – Present", and plainspeak-writer 1.4.1 blocks the dash, so a review of a resume-ops resume gets a must-fix for it. The owner ruled that a range outside prose may keep its dash, and the checker doesn't follow that ruling yet.
- skill-creator's benchmark for round one: 98% of the graded checks passed with the skill, against 36% for the same prompts with no skill. Without the skill, one run advised listing the OSHA 30-hour card as in progress, two saved a case with no confirmation, and one came back with new questions three times.
- A first build took 14 to 25 minutes of helper time, and a reuse took under three.
- LibreOffice isn't on the test computer, so neither resume-ops build could run its real render and widow check, and both said so.

## Claude Code run on 0.2.1

- Date: 2026-10-06
- Product: Claude Code 2.1.289, from the `AI_AGENT` environment variable, in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- Installed in the app: job-seeker-ops 0.2.1 as a plugin, and resume-ops 2.4.0 and plainspeak-writer 1.5 as uploaded skills. The plugin's `build_packet.py` and `check_positioning.py` are the same files as this repository's copies, byte for byte. Python 3.12.10.
- An earlier session ran this round on Claude Code 2.1.288 the same day and left its evidence uncommitted. That evidence and its section of this file were moved to `tests/evidence/prior-2.1.288/` before this run, and its run folder was renamed `e-installed-prior-2.1.288`.
- Voice rules in every packet: the installed plainspeak-writer 1.5, which keeps the full check in `references/full-check.md`. The packet script didn't find it on its own, so each packet was built again with `--voice-dir` pointing at it, as submission-review's SKILL.md says.
- Working folder: this repository, on `main`. This run's evidence was drafted outside the repository and copied in after the last review, so every reviewer's git snapshot showed only the `prior-2.1.288` folder and five commit titles.
- Evidence: the six `-claude-code-0.2.1.md` files in `tests/evidence/`. The positioning run and the resume build used `..\jso-tests\positioning\runs\e-installed\`, outside the repository.

| Test | Result | Reason |
|---|---|---|
| 1. Isolation from the conversation | Pass | The reply says "I don't know any of the three", and Adebayo, Denver and Copperfinch appear nowhere in the report or either reply. Send, with no must-fix finding. |
| 2. Saved memory, with the git snapshot | Pass | The reviewer named "a git snapshot (branch, git user name, one untracked folder and recent commit titles ...)", quoted no branch, user name, file name or commit title, kept it apart from a profile and wrote `blind: yes`. |
| 7. Seeded flaws | Pass | Fix first. Must-fix: Q-Ladder, the dash, "wasn't just", the 2017 date, the gap, and nothing else. Should-fix: the opener, "known across the hospital", "keep the room calm". No replacement wording. |
| 11. Voice source, with the full check in its own file | Pass with `--voice-dir` | The manifest's "Full check" line names the installed `full-check.md`, and the test 7 reviewer opened the five packet files, `tells.md` and `full-check.md`, and nothing else. Without `--voice-dir` the manifest read "Voice rules: not found". Unit tests: 22 of 22 OK. |
| Positioning 1. The file's shape, writer E | Pass | `check_positioning.py --sources --current` passes with 30 quotes found, and so do `--for resume-ops` and `--for cover-letter`. resume-ops 2.4.0 reads the file as "use it". |
| Positioning 2. No invention | Pass | The OSHA 30-hour card is R8, "gap, owned by the role", kept off. Spanish and Lean or Six Sigma are gaps too. |
| Positioning 3. What the firm is buying | Pass | Line 1 aims at bringing Sparks up to its on-time goal, and P1 is the Fernley opening, 79% to 98% by August 2022. |
| Positioning 4. Firm facts | **Fail** | Three facts link to the news and careers pages with a checked date, but F2 keeps "now ships to all 42 stores", a fact the home page states, which the skill's step 3 says to drop. No "since 1987" or "free returns". |
| Positioning 7. One confirmation | Pass | One message at step 2, one confirmation at step 9, then the closing message. |
| The installed skill in the positioning run | Pass | The helper's first call loaded `job-seeker-ops:candidate-positioning`, and every run of `check_positioning.py` used the installed copy. No call touched this repository. |
| 16. The second direction | **Fail**, on one condition | resume-ops 2.4.0 showed the seventh Level Set line, the POSITIONING line and the review offer, but its CHECKS line has no "positioning PASS". The check ran and passed, and the brief reports it on the POSITIONING line. The review passed every condition: `blind: yes`, the file in neither the packet nor the opened list, and the skill's check against it ran seven seconds after the report. |

9 of 11 passed. Test 11 passed only with `--voice-dir`.

### Worth a look

- Positioning test 4: the skill's rule to drop any fact the home page states didn't hold when the news page states the same fact. `check_positioning.py` can't catch it, since its home page check reads only a fact's source link. The 2.1.288 run kept "42 stores" out, so the miss doesn't happen every time.
- Test 16's CHECKS line: resume-ops 2.4.0's brief format doesn't name the positioning check on the CHECKS line, and its example line in `references/tailoring.md` has no place for it. Either the test's condition or resume-ops's format needs to change so they agree.
- `build_packet.py` 0.2.1 still doesn't find plainspeak-writer when it's uploaded to the desktop app as a skill. Its `default_roots()` searches `~/.claude/skills`, `~/.claude/plugins` and `.claude/skills` in the working folder. The app keeps uploaded skills in `%APPDATA%\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\`. `check_positioning.py` in the same plugin searches that folder and found plainspeak-writer on its own. Without `--voice-dir`, a review runs with voice unchecked. Fixed in 0.2.2, which searches the app's folder too.
- `check_positioning.py` won't take a confirmed answer as the source of a gap row. `searched resume.txt; A2` fails because it reads "A2" as a file missing from the stamp, and `A2; searched resume.txt` fails because a gap's source must start with "searched". The helper moved the A2 citations into the section 7 bullets.
- The positioning helper's closing hand-back put notes for this session ahead of its message to the person, though its first message asked for the message alone.
- resume-ops still writes date ranges as "Jan 2022 – Present", and plainspeak-writer 1.5 blocks the dash under R01, so the review gave the resume a must-fix for it, as in the 2.1.288 run.
- On this computer, every Read call by a reviewer set off a PreToolUse and a PostToolUse hook that failed with "python3: command not found". The hooks don't block, so every read went through. They come from a hook set up on this computer, outside the plugin.
- LibreOffice still isn't on the test computer, so the resume-ops helper skipped its page view and said so.

### Not run in this session

- Tests 3 to 6, 8 to 10 and 12, and test 11's packet without voice rules for writer C. This round asked for tests 1, 2, 7, 11 and 16.
- Positioning tests 5, 6 and 8 to 13 through the installed skill. The resume half of test 6 held in test 16's build.

## Claude Code rerun of test 11 on 0.2.2

- Date: 2026-10-07
- Product: Claude Code 2.1.289 in the Code tab of the Claude desktop app on Windows 11, with job-seeker-ops 0.2.2 uploaded to the app and plainspeak-writer 1.5 uploaded as a skill. The Code tab installed the plugin under `~/.claude/plugins/marketplaces/local-desktop-app-uploads/`.
- Evidence: `tests/evidence/11-voice-source-claude-code-0.2.2.md`.

| Test | Result | Reason |
|---|---|---|
| 11. Voice source, with no `--voice-dir` | Pass | Built exactly as RUN-TESTS.md gives it, the manifest names plainspeak-writer 1.5, its rules file and its full check. The reviewer opened the five packet files, `tells.md` and `full-check.md`, and nothing else, and its report meets `keys/a-seeded.md`. Unit tests: 25 of 25 OK. |
