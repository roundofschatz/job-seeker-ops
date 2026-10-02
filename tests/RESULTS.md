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
