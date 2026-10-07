## Claude Code run on 0.2.1

- Date: 2026-10-06
- Product: Claude Code 2.1.288, from the `AI_AGENT` environment variable, in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- Installed in the app: job-seeker-ops 0.2.1 as a plugin, and resume-ops 2.4.0 and plainspeak-writer 1.5 as uploaded skills. The plugin's `build_packet.py` reports 0.2.1 and `check_positioning.py` reports 0.2.0, and each is the same file as this repository's copy, byte for byte. Python 3.12.10.
- Voice rules in every packet: the installed plainspeak-writer 1.5, which keeps the full check in `references/full-check.md`. The packet script didn't find it on its own, so each packet was built again with `--voice-dir` pointing at it, as submission-review's SKILL.md says.
- Working folder: this repository, on `main`. The session opened in the folder above it, which isn't a git repository, and moved into the repository before any reviewer started, so every reviewer had the git snapshot.
- Evidence: the five `-claude-code-0.2.1.md` files in `tests/evidence/`, and `positioning-installed-claude-code-0.2.1.md` beside them. The positioning run and the resume build used `..\jso-tests\positioning\runs\e-installed\`, outside the repository.

| Test | Result | Reason |
|---|---|---|
| 1. Isolation from the conversation | Pass | The reply says "I don't know any of the three", and Adebayo, Denver and Copperfinch appear nowhere in the report or either reply. |
| 2. Saved memory, with the git snapshot | Pass | The first live review under 0.1.3's rule for the snapshot. The reviewer named the git snapshot, quoted no branch, user name, file name or commit title, kept it apart from a profile and wrote `blind: yes`. |
| 7. Seeded flaws | Pass | Fix first. Must-fix: the dash, "wasn't just", Q-Ladder, the 2017 date, the gap. Should-fix: the opener, "known across the hospital", "keep the room calm". No replacement wording. |
| 11. Voice source, with the full check in its own file | Pass with `--voice-dir` | The manifest's "Full check" line names the installed `full-check.md`, and the test 7 reviewer opened the five packet files, `tells.md` and `full-check.md`, and nothing else. On its own the script found no plainspeak-writer, and the manifest read "Voice rules: not found". Unit tests: 22 of 22 OK. |
| Positioning 1. The file's shape, writer E | Pass | `check_positioning.py --sources --current` passes with all 33 quotes found, and so do `--for resume-ops` and `--for cover-letter`. resume-ops 2.4.0 reads the file as "use it". |
| Positioning 2. No invention | Pass | The OSHA 30-hour card is R4, "gap, owned by the role", kept off. Spanish and Lean or Six Sigma are gaps too. |
| Positioning 3. What the firm is buying | Pass | Line 1 aims at getting Sparks from 82% toward 97% on time, and P1 is the Fernley opening, 79% to 98% by August 2022. |
| Positioning 4. Firm facts | Pass | Three facts link to the news and careers pages with a checked date, and none of the home page's facts made it in: no "since 1987", "42 stores" or "free returns". |
| Positioning 7. One confirmation | Pass | One message at step 2, one confirmation at step 9, then the closing message. |
| The installed skill in the positioning run | Pass | The helper's first call loaded `job-seeker-ops:candidate-positioning`, and every run of `check_positioning.py` used the installed copy. No call touched this repository. |
| 16. The second direction | Pass | resume-ops 2.4.0 showed the seventh Level Set line, the POSITIONING line, "positioning PASS" and the review offer. The review read `blind: yes`, the file stayed out of the packet, and the skill's check against it ran 24 seconds after the report. |

11 of 11 passed. Test 11 passed only with `--voice-dir`, because the packet script can't find plainspeak-writer in this app on its own.

### Worth a look

- `build_packet.py` 0.2.1 doesn't find plainspeak-writer when it's uploaded to the desktop app as a skill. Its `default_roots()` searches `~/.claude/skills`, `~/.claude/plugins` and `.claude/skills` in the working folder, and the app keeps uploaded skills in `%APPDATA%\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\`. `check_positioning.py` in the same plugin searches that folder and found the same copy on its own. Every packet here needed `--voice-dir`, and without it a review runs with voice unchecked. The unit tests cover a standalone copy, a plugin and `~/.claude/skills/synced`, and not this layout.
- Test 2 needs the session in the repository. Opened in the folder above it, the session's helpers got only the account email, so a throwaway helper confirmed the git snapshot before any reviewer started. RUN-TESTS.md could say to open the session in the repository and to check for the snapshot first.
- The app builds each helper's git snapshot when the helper starts. The test 16 reviewer's snapshot listed the five evidence files this session had written by then, one of them named `positioning-installed-claude-code-0.2.1.md`. The reviewer listed them only as "changed files", quoted none, and judged that none names the piece, the candidate or the target, so the review stayed `blind: yes`. That's a closer call than a clean status, since the piece was built from a positioning file. Writing the evidence after the reviews would keep the status clean.
- The test 1 reviewer answered each follow-up in a few lines. After its first reply, the harness asked it to hand its report back, and it sent the short answer again, with a line saying the full review had gone earlier.
- resume-ops still writes a date range as "Jan 2022 – Present", and plainspeak-writer 1.5 still blocks the dash under R01, so the review gave the resume a must-fix for it, as in 0.2.0.
- The positioning helper wrote one working file, `reused.txt`, to this session's scratch folder to run the voice checker by hand, and listed the folder above its run folder once. It opened nothing outside its folder, the skill and plainspeak-writer, and it made no web lookups.
- LibreOffice still isn't on the test computer, so the resume-ops helper couldn't run its render and widow check, and said so. It opened its own plain-text copy in the app's built-in browser to measure line widths instead.

### Not run in this session

- Tests 3 to 6, 8 to 10 and 12, and test 11's packet without voice rules for writer C. This round asked for tests 1, 2, 7, 11 and 16.
- Positioning tests 5, 6 and 8 to 13 through the installed skill. The resume half of test 6 held in test 16's build.
