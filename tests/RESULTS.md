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
