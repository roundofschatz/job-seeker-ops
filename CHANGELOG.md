# Changelog

Every change to this plugin is logged here: what was added, changed or removed, and why. Nothing comes out without a line saying so. Newest first.

## 0.4.6 · The marketplace says which tool to install

The owner asked on October 9 why the marketplace lists resume-ops on its own when this plugin includes it. That's by design, so a person can take the whole set or one tool. But the listing didn't say that resume-ops and plainspeak-writer are already inside this plugin, and someone who installs both gets two resume skills or two writing skills, with Claude free to load either.

Changed:

- `.claude-plugin/marketplace.json`: each entry says who it's for. This plugin is "the full job-search set" with the other two included, "so install this one alone". resume-ops and plainspeak-writer each say they're "already included in job-seeker-ops, so skip this if you install that". The marketplace's own description says the same in one line. Nothing in the marketplace format lets one plugin block another, so the descriptions do the steering.
- `skills/plainspeak-writer/`: plainspeak-writer 1.7.2, copied from tag v1.7.2 (commit 8e51313). Its README now covers installing it as a plugin and says not to install it beside this plugin. No rule changed. Its marketplace entry moves to v1.7.2.
- README: the section on the bundled copies names plainspeak-writer 1.7.2.
- `.claude-plugin/plugin.json`: version 0.4.6.

resume-ops's READMEs already said to install it or this plugin, not both, so resume-ops doesn't change.

## 0.4.5 · Fixes from the live suites on 0.4.4

On October 8 every live suite ran on 0.4.4 as the desktop app installed it, and `tests/RESULTS.md` named four things to fix. The owner said yes to all four.

Changed:

- **Finding the positioning file shows no other file's text.** Cover letter's step 1 printed the first line of every `positioning-*.md` file to find the one for the posting. Writer B keeps notes in `positioning-notes.md`, so its heading reached the conversation and cover-letter test 1 failed in run cl-b1. `check_positioning.py` 0.4.5 adds `--list FOLDER`, which prints each file whose first line is a positioning heading and only counts any other file named the same way. Step 1 of cover-letter and of candidate-positioning now runs it, never opens a file it skips, and cover-letter's search for earlier voice samples uses the same list.
- **A count of years that a later role leaves open.** In positioning test 11, writer F's file counted about six years of teaching, her Math Teacher dates, and left her years as chair out, though her own proof showed her teaching her own classes in 2020. candidate-positioning now counts a later role's years only where a source shows the same work in them, cites that source, and otherwise counts the narrower span, says why, and asks at step 9 with the narrower count as the default. The key for test 11 accepts either result, and `RUN-TESTS-positioning.md` says so.
- **plainspeak-writer 1.7's "what the X did" warning.** Ten such phrases in files 0.4.0 didn't touch are reworded with the same meaning, such as "what the writer meant" to "the writer's intent":
  - five in cover-letter's `letter.md`, which the drafting learns from;
  - two in candidate-positioning's `case.md`;
  - three in the reviewer's instructions.
- **`tests/RUN-TESTS.md`.** Its title said "Live tests for job-seeker-ops 0.1.0". It now says what it tests, and its setup names the folder where the desktop app installs a plugin on the account from a marketplace.
- `plugin.json`: version 0.4.5.

Added:

- Three unit tests for `--list`: a notes file named `positioning-notes.md` is counted and none of it shown, a heading after a byte-order mark and a blank line still counts, and an empty or missing folder gets a plain answer.

Checked:

- The unit tests: 184 of 184 pass on Windows with Python 3.12.10, once the package is built from the release commit.
- Cover-letter run cl-b1 again, from this repository's working tree: step 1 used `--list`, and nothing from writer B's notes or career record reached the conversation, so test 1 passes.
- Writer F's positioning run again: her teaching counts through March 2021 from the sources that show it, and step 9 asked about the rest, so test 11 passes under its new key.
- plainspeak-writer 1.7.1's checker, the copy in `skills/`, on every file this version changes outside the two copies, with no HARD hits.

## 0.4.4 · The marketplace lives here, and plainspeak-writer 1.7.1

The owner chose on October 8 to move the shared marketplace into this repository. In resume-ops it made a loop: this plugin releases whenever plainspeak-writer or resume-ops does, to bring the new copy in, and each of those releases moved a tag in resume-ops's marketplace. That was a resume-ops release, which changed the copy of resume-ops this plugin holds and needed another release here. Here, the tag moves in the same release that brings the copy in, and changes flow one way, from the tools into this plugin. The same day, plainspeak-writer 1.7.1 credited its author by name, change 10 in the tools folder's change notes.

Added:

- `.claude-plugin/marketplace.json`: the marketplace `roundofschatz`, with the same three tools under the same names. This plugin comes from this repository (`"./"`), and resume-ops and plainspeak-writer come over HTTPS at the tags of the copies in `skills/`, v2.4.4 and v1.7.1. plainspeak-writer's entry states its version, since its repository has no plugin manifest.
- Two tests in `tests/unit/test_bundled.py`. One fails when the marketplace's tags or plainspeak-writer's version differ from the copies' records in `bundled.json`, so a sync can't leave the marketplace behind. The other fails when the README's section on the copies names another version.

Changed:

- `skills/plainspeak-writer/`: plainspeak-writer 1.7.1, copied from tag v1.7.1 (commit 9465a33). Its license names the author, its README has an Author section, and its checker's version line says 1.7.1. No rule changed.
- `skills/resume-ops/`: resume-ops 2.4.4, copied from tag v2.4.4 (commit b25d535). It drops its own marketplace file, and its READMEs point at this repository. No rule changed.
- README: Claude Code adds `roundofschatz/job-seeker-ops` as the marketplace, and a person who added `roundofschatz/resume-ops` before removes it first, since Claude keeps one marketplace for each name. The file list names the marketplace file and no longer gives the copies' versions, which had gone out of date there.
- `.claude-plugin/plugin.json`: version 0.4.4.

Checked:

- The unit tests: 181 of 181 pass on Windows with Python 3.12.10, once the package is built from the release commit. On 0.4.3 the marketplace test fails, since that version has no marketplace file.
- resume-ops's own tests at v2.4.4: 295 tests, 1 skipped, no failures. plainspeak-writer 1.7.1's checker gives the same reports as 1.7's, apart from its version line.
- plainspeak-writer 1.7.1's checker, the copy in `skills/`, on every file this version changes outside the two copies, with no HARD hits.

The owner asked on October 8 for the three tools to work on their own and together, through one marketplace. resume-ops's marketplace, `roundofschatz`, now lists plainspeak-writer and this plugin beside resume-ops, so one place installs the whole set or any tool alone.

Changed:

- `skills/resume-ops/`: resume-ops 2.4.3, copied from tag v2.4.3 (commit 2278afc). Its marketplace is the shared one, and its READMEs say what the marketplace lists and to install this plugin or the tools on their own, not both. No rule changed.
- README: Claude Code installs the plugin with `/plugin marketplace add roundofschatz/resume-ops` and `/plugin install job-seeker-ops@roundofschatz`, and the same marketplace installs either bundled tool on its own.
- `.claude-plugin/plugin.json`: version 0.4.3.

Removed:

- `.claude-plugin/marketplace.json`, added in 0.4.0. Two marketplaces that list the same plugin give a person two ways to install it twice. The shared marketplace points at this repository's release tags, starting with v0.4.3.

Checked:

- A copy of the shared marketplace, pointed at the tags then current, installed all three plugins in an empty Claude Code setup: plainspeak-writer 1.7 with its one skill, resume-ops with its one, and this plugin with five skills and its reviewer.
- On Windows, a plugin's files have to fit under the 260-character path limit once installed. This repository's longest path is 134 characters, and Claude Code's install folder in a typical user's home adds about 83.

## 0.4.2 · resume-ops 2.4.2, and a link beside the author's name

resume-ops 2.4.2 fixes how its PDF checks read the text `pdftotext` writes, and its repository now tags each release, so this version copies it in by tag. The owner also asked on October 8 for the same author credit in all three tools: the name and a LinkedIn link, with no job title or city.

Changed:

- `skills/resume-ops/`: resume-ops 2.4.2, copied from tag v2.4.2 (commit a61c493) with `tools/sync_bundled.py`. `widow_check.py` and `requirement_check.py` now ask `pdftotext` for UTF-8. The `pdftotext` that comes with Git for Windows wrote Latin-1, so the dates in a resume's role lines came back unmatched. That was the failing test 0.4.0 left for resume-ops to fix. The other changes are version numbers and resume-ops's changelog. `bundled.json` records the tag, the commit and each file's hash.
- resume-ops's history was rewritten on October 8 to take out a made-up company name that belonged to a real company, the rename this plugin made in 0.3.1. Its 2.4.0 is now commit f51607b, with the tag v2.4.0. The commit that 0.4.0's entry names, 23a6a5d, is gone from the public repository, and the files copied from it held no trace of the name.
- README: the Author section adds a LinkedIn link to the owner's name, and the section on the bundled copies names resume-ops 2.4.2.
- `.claude-plugin/plugin.json`: version 0.4.2.

Checked:

- The unit tests: 179 of 179 pass on Windows with Python 3.12.10, once the package is built from the release commit. `tools/sync_bundled.py --check` finds no problem with either copy.
- resume-ops's own tests at v2.4.2: 295 tests, 1 skipped, no failures.
- The pinned voice checker, plainspeak-writer 1.7 at tag v1.7, on every file this version changes outside the two copies, with no HARD hits.

## 0.4.1 · The owner credited by name

The owner asked on October 8 to be credited by name as the creator of this plugin, plainspeak-writer and resume-ops, and to keep the name out of everything the tools produce and out of every example. Until now this plugin named its author only by the GitHub account.

Changed:

- `LICENSE`: the copyright line names the owner, Ryan Schatzman, in place of "The job-seeker-ops contributors". MIT asks every copy of the code to keep that line, so the credit goes wherever the code goes. Who owns the work doesn't change.
- README: a new Author section with the owner's name.
- `.claude-plugin/plugin.json`: the author is the owner's name in place of the account name, and the version is 0.4.1. `marketplace.json` names the owner the same way. Both keep the link to the account.

Not changed:

- The name reaches nothing the skills produce. `build_letter.py` puts the letter writer's own name in a Word file's properties, from the sign-off or `--name`, and no example, rule or test uses the owner's name.
- The two bundled copies keep their own licenses. resume-ops's already names the owner. plainspeak-writer's still credits "The Plainspeak Writer contributors" until a release of its own changes it, and the next sync brings that in.

Outside this plugin:

- `plainspeak-change-notes.md` in the tools folder, change 10: the same license line and an Author section for plainspeak-writer, for its next release.

Checked:

- The unit tests: 179 of 179 pass on Windows with Python 3.12.10, once the package is built from the release commit.
- The pinned voice checker, plainspeak-writer 1.7 at tag v1.7, on every file this version changes, with no HARD hits.

## 0.4.0 · plainspeak-writer and resume-ops come with the plugin

The owner asked on October 7 for the whole toolset in one install, with plainspeak-writer and resume-ops still available on their own for a leaner setup. Until now, a person who installed only the plugin had no resume skill, and cover letter stopped at its first step for want of plainspeak-writer. The owner waited for plainspeak-writer 1.7, which holds the letter warnings their review of the first cover letters asked for, so the plugin starts with that voice.

Added:

- `skills/plainspeak-writer/`: plainspeak-writer 1.7, copied from tag v1.7 of its repository, commit f50d66c.
- `skills/resume-ops/`: resume-ops 2.4.0, copied from commit 23a6a5d of its repository, which has no release tags yet.
- Both copies leave out their tests, which stay in their own repositories, and plainspeak-writer's `.gitignore`. Nothing in them is edited here.
- `bundled.json`: for each copy, its repository, the tag or commit, its version and a hash for every file.
- `tools/sync_bundled.py`: copies one commit of either skill into `skills/` with git, and writes its record. It won't replace a folder the record doesn't list, and `--check` compares every copy with the record.
- `.claude-plugin/marketplace.json`, so Claude Code installs the plugin from this repository with `/plugin marketplace add roundofschatz/job-seeker-ops`. `claude plugin validate` passes it. Installed from this folder into an empty Claude Code setup, the plugin listed all five skills and the reviewer, and its scripts found the copy of plainspeak-writer installed with them.
- README: "plainspeak-writer and resume-ops", which says where the copies come from, why the plugin uses its own plainspeak-writer, and to keep one copy of each tool installed.

Changed:

- `check_positioning.py`, `check_letter.py` and `build_packet.py` 0.4.0 use the plugin's own plainspeak-writer, beside their skill in the plugin's skills folder, before any search. A copy installed elsewhere doesn't change that, so a person with both installed no longer gets stopped by the check for copies that differ. The search from 0.3.2 runs only when a skill was installed without the plugin, and `--voice-dir` still picks another copy.
- The SKILL.md files of cover-letter, candidate-positioning and submission-review point Claude at the plugin's copy, at `${CLAUDE_SKILL_DIR}/../plainspeak-writer/`, and cover-letter loads submission-review from beside it too.
- The unit tests that ran plainspeak-writer's real checker used a clone next to this repository and skipped without one. They now run the plugin's copy every time.
- `plugin.json` 0.4.0 says what comes with the plugin. The package leaves out `marketplace.json`, which only Claude Code's marketplace reads, so the build command in the README names `.claude-plugin/plugin.json`.
- README: the opening paragraph, the Claude Code install, what it needs, the file list, the tests and the rules for contributors.
- `tests/RUN-TESTS-cover-letter.md`: the helper loads the plugin's other skills from beside cover-letter, and test 17 checks that the run used the plugin's plainspeak-writer. `tests/RUN-TESTS.md` test 11 and the positioning tests' message say the same.
- Six instructions in the three SKILL.md files lost a "what the X did" phrase that 1.7 now warns on, such as "what the writer meant", which became "the writer's intent". Each says what it said before.

Checked:

- The unit tests: 179 of 179 pass on Windows with Python 3.12.10 and LibreOffice installed, once the package is built from the release commit. 14 are new. `tests/unit/test_bundled.py` holds 9: each copy matches its record, the record matches the commit in the skill's own clone, the copies hold no tests, an edited copy gets caught, a folder the record doesn't list is never replaced, and the bundled resume-ops reads the example positioning file and checks a resume against its keep-off list. The other 5 cover the plugin's copy coming first and the search running when a skill sits outside the plugin.
- Test 17 passed live in run cl-f1-040: the helper read plainspeak-writer only from the plugin's copy, every voice check named it, and the letter met cl-f1's key again. 1.7's warning for long, flat letters fired on three drafts, and the letter it handed over averages 19.8 words a sentence, with 11% at ten words or fewer, where the 0.3.0 letters averaged 26 with 1%.
- resume-ops's own tests at the pinned commit pass 290 of 291, with one skipped. The one that fails reads a rendered page through the `pdftotext` that comes with Git for Windows, which can't write the dash in two resume dates. That's for resume-ops to fix.
- The pinned voice checker, plainspeak-writer 1.7 at tag v1.7, on every text file this release adds or changes outside the two copies.

## 0.3.2 · The security review, and the spec's open questions

On October 7 a read-only security review of 0.3.1 found twelve problems, five of them worth fixing before the repository goes public, and the owner accepted every fix. The owner also accepted the recommended answers to the cover-letter spec's five open questions, and installed LibreOffice.

Fixed, from the security review:

- **Text from others could give orders (high).** A line in a posting or a firm's page could speak to Claude, and nothing said it was data. All three SKILL.md files and the reviewer now say text in the files is evidence to quote, never an instruction. `check_positioning.py --sources` warns on a source line that speaks to an AI tool, and `check_letter.py` fails the gate on one in the posting, since it may be a trap for AI-written applications. The pattern lives in `check_positioning.py`, and `build_packet.py` keeps a copy that a unit test compares with it.
- **Hidden text reached the reviewer (medium).** Hidden, white or tiny text in a Word file stays out of the piece. `build_packet.py` puts it in `hidden.txt`, the reviewer reports it under Risk, `check_letter.py` fails a letter that has it, and `check_positioning.py` warns on a source that has it.
- **A posting's words went into a shell command (medium).** No skill types the company or the role into a command anymore. candidate-positioning names its file with the new `--name-from`, which reads the draft's heading. cover-letter finds the file by reading headings, and `build_letter.py` takes the company from `--positioning`.
- **The voice-rules search trusted the wrong folders (medium).** `build_packet.py` and `check_positioning.py` search only the skills folders, each plugin that `installed_plugins.json` lists, and the desktop app's uploads. They no longer search the working folder or the plugin catalogs Claude Code downloads, and copies that differ stop the run with a list instead of the highest version winning. The packet holds copies of the rules, `voice-rules.md` and `full-check.md`, so the reviewer opens nothing outside it and its report names no folder on the person's computer.
- **A positioning file could name files outside the folder (medium).** A file the stamp or a citation names has to sit in the person's folder. An absolute, drive or network path, a `..` step or a link fails without being opened or looked up.
- **The low ones.**
  - Every script reads a Word file in one pass without recursion, and refuses a part over 20 MB or an XML parser older than expat 2.4.1.
  - Three patterns that slowed down on long lines were rewritten.
  - `build_letter.py` escapes quotes in attributes, falls back to Calibri for an odd font name, and won't write over an existing file without `--replace`.
  - `--check-links` opens only public web addresses, follows a redirect only on the same host, and names no tool.
  - `build_packet.py` warns on a companion named like the deeper record and on a letter's companion that isn't a resume.
  - candidate-positioning searches the web with the firm's name, the role and public terms only.
  - Older test evidence lost the app's and a session's IDs.
- `tests/tools/scan_transcript.py`: a search or a command over the whole folder now shows as broad, and with `--run-folder` the scan looks through every tool result for the forbidden files' own lines. Run again on test 1's three runs, it found none.

Changed, from the owner's answers to the spec's open questions:

- A letter's record says the watermark notice was given at hand-over: cover-letter's step 9 and section 9 of `format.md`.
- cover-letter uses the voice samples from the newest letter record again and says so, so the person names them once.
- Kept as they were: a Word file and text in Cowork, with a Claude Doc only when asked; no section headers; blurbs and outreach notes later.

Added:

- `check_letter.py` counts a Word file's pages with LibreOffice when it's installed, in its own empty profile so an open LibreOffice can't block it, and falls back to the estimate otherwise. `--no-render` skips it.
- Test 16, a posting that speaks to AI tools: `tests/keys/cl-inj.md`, `tests/letters/f-haddad/injected/`, the run in `stage_run.py`, and `tests/evidence/cover-letter-16-ai-addressed.md`.
- 28 unit tests for the fixes above, and one that renders a letter with LibreOffice when it's installed.
- Script versions: `check_positioning.py`, `check_letter.py`, `build_letter.py` and `build_packet.py` 0.3.2, and `plugin.json` 0.3.2.

Checked:

- The unit tests: 165 of 165 pass on Windows with Python 3.12.10 and LibreOffice installed, once the package is built from the release commit.
- Test 16 passed live in run cl-inj1, and test 15 still holds by its unit tests.
- The pinned voice checker, plainspeak-writer 1.6.2 at commit 577a985, on every text file this release touches.
- Released with a rewritten git history, which takes the old made-up name and the app and session IDs out of earlier commits.

## 0.3.1 · The owner's review, and a posting that rules out AI

The owner reviewed skill-creator's side-by-side page for 0.3.0 on October 7 and asked for a check on a posting's rules about AI, an end to the stock ask every test letter closed on, a README section on what the plugin won't do, and the open items from earlier runs closed before a public release. The voice constructs the review flagged belong to plainspeak-writer, so they went to its change notes instead of into this plugin.

Added:

- `skills/cover-letter/scripts/check_letter.py` 0.3.1, before drafting: it quotes any posting line about AI in application materials. It fails a line that rules them out, warns on one that asks for disclosure or for the applicant's own words, and notes one about the employer's own use. A line that names AI only as a skill or a product isn't listed.
- `check_letter.py`, on a letter: a warning when the ask opens on a stock phrase such as "I'd like to talk about", and with `--compare`, a warning when two letters' asks open with the same four words.
- `skills/cover-letter/SKILL.md` step 1, item 4, and call 10: when the posting rules out AI-written materials, the skill doesn't draft. It quotes the line, offers the person's case as notes and the fact checks on a letter they write, and drafts only if the person says the employer allows it. A line asking for disclosure gets a reminder at hand-over, and the record says what the posting said and what the person decided.
- `README.md`: "What it won't do", with the watermark.
- Test 15, a posting that rules out AI: the key `tests/keys/cl-ai.md`, the pieces in `tests/letters/f-haddad/no-ai/`, the run in `tests/tools/stage_run.py`, and `tests/evidence/cover-letter-15-no-ai.md`. Seven unit tests cover the posting's rules, the stock ask and two asks that open alike.

Changed:

- `skills/cover-letter/references/letter.md`: the invitation says to write the ask the way the writer would, starting from the named thing, and names the stock openers. The example letter's ask is now a direct question, and "which is the work I've done" became a sentence of its own. Every test letter had copied both from the example. Its body stays at 350 words.
- `skills/cover-letter/SKILL.md` step 6 and `references/checks.md`: the sentence list is about what a sentence names, not its length, so a short sentence that names its thing stays. The test letters averaged 26 words a sentence, with 1% at ten words or fewer, where human writing in the red team's sets averages about 20, with about a fifth at ten or fewer.
- `references/checks.md`: rows for the posting's rules on AI and for the ask, and a hard fail for drafting when the posting rules AI out.
- Made-up names that matched real ones. The name made up for writer B's employer belonged to a real freight company in the same metro area, and the tests gave it invented figures. It's now Switchgrass Freight Co. in every file, including the examples that ship in `format.md` and `letter.md`, with the example's stamp hashes worked out again. Writer C's school and two firms in the unit tests had near matches too, and became Larkhollow High School and Quillmoor. A web search found no organization by any of the new names.
- `tests/RUN-TESTS-positioning.md` test 6: how to read resume-ops 2.4.0's brief. Its POSITIONING line names the file, and its CHECKS line has no entry for the positioning check, so the test runs `positioning_check.py --resume` itself. That closes the open item from the 0.2.1 Claude Code run, whose grading asked for "positioning PASS" on the CHECKS line because one earlier run happened to write it there.
- `.claude-plugin/plugin.json`: version 0.3.1.

Outside this plugin:

- `plainspeak-change-notes.md` in the tools folder, changes 6 to 9: "what the [noun] [verb]", "that's the [thing]", "do what ours did" and sentences that run long and flat, each with counts from the red team's sets. plainspeak-writer's next build takes them up, so the letters' voice changes when it ships.

Checked:

- The unit tests: 136 of 136 pass on Windows with Python 3.12.10, once the package is built from the release commit.
- Test 15 passed live in run cl-ai1. Tests 1 to 14 weren't run again: the changes to the draft are the ask and the example, which the unit tests cover.
- plainspeak-writer 1.6.2's checker, pinned at commit 577a985, on every text file this release adds or changes.

## 0.3.0 · Cover letter

The third skill, built from the cover-letter spec. It writes one letter for one posting from three files, the positioning file, the posting and the resume that goes with the letter, in plainspeak-writer's voice. It checks every fact against those files by script, has submission-review's blind reviewer read the draft before the person sees it, and saves the letter in the channel's form, with its record in a ninth section of the positioning file.

Added:

- `skills/cover-letter/SKILL.md`: the nine steps, the calls, when to stop, and the hand-over with the watermark line.
- `skills/cover-letter/references/letter.md`: the four movements with their word budgets and where each takes its material from in the positioning file, the map, sentences from earlier writing, the three channel forms, and a full example letter from writer B, which the unit tests check against his files.
- `skills/cover-letter/references/checks.md`: every check and what runs it, the hard fails, the sentence list, the two swap tests, and what happens when the person edits.
- `skills/cover-letter/references/sources.md`: 25 sources, each checked again on October 7, 2026 from the 27 in the owner's own notes and the two pages on Anthropic's watermark, with its date, grade and link, and 9 more listed with the reason they're left out.
- `skills/cover-letter/scripts/check_letter.py` 0.3.0. Before drafting, it compares the proofs marked for the letter with the resume that goes with it and lists the sentences plainspeak-writer blocks in a voice sample. On a draft, it counts the body's words and the letter's characters, and checks the header against the resume, every number, date and name against the three files, a count of years, the keep-off phrases, restated resume lines, the firm and any referral in the first two sentences, the close, a channel's rules, and sentences shared with a sample or another letter. On a Word file, it checks the author field, the layout and the page. It reads the positioning file with `check_positioning.py`, so the format has one reader.
- `skills/cover-letter/scripts/build_letter.py` 0.3.0, which writes the Word file the way resume-ops writes a resume: every part Word writes, the writer's name as author, no program named in the properties, and the resume's font, size and margins. It never makes a PDF.
- `tests/unit/test_check_letter.py`, with 41 tests for both scripts, and `tests/unit/test_cover_letter_sources.py`, which checks that every cited source has a row and every row is cited where it says.
- `tests/RUN-TESTS-cover-letter.md`, the keys `tests/keys/cl-*.md`, the pieces in `tests/letters/` (copies of writers E, F and G's confirmed positioning files, writer E's Word resume, a resume with changed dates, a voice sample with blocked phrases, a second posting for writer F, and a file with one firm fact), and three tools for the live tests: `tests/tools/stage_run.py`, `scan_transcript.py` and `measure_page.py`.
- The evidence: `tests/evidence/cover-letter-01-three-files.md` to `cover-letter-14-own-files.md`, with the runs' letters, records and hand-backs in `tests/evidence/cover-letter-runs/`, and a cover-letter section in `tests/RESULTS.md`.

Changed:

- `skills/candidate-positioning/references/format.md`: the format of section 9, one record per letter with its labelled lines, its map, its checks and its text.
- `skills/candidate-positioning/scripts/check_positioning.py` 0.3.0. It checks each record in section 9, adds the records to `--json`, and writes its output as UTF-8, since a record's heading holds a middle dot that a Windows console wrote in its own code page.
- `skills/candidate-positioning/SKILL.md`: the file list names the section 9 check.
- `tests/unit/test_check_positioning.py`: the section 9 test now checks a full record, and five new tests cover a draft record, a finished record missing its parts, missing lines and map rows, the section's name, and a heading inside the letter's text.
- `README.md`: a cover letter section with the watermark, examples, the file list and the tests.
- `.claude-plugin/plugin.json`: version 0.3.0 and a description that names cover letter.

Where this build departs from the spec, and why. The owner approved each of these on October 7 before the build:

- **Voice samples never turn a rule off.** plainspeak-writer lets a user's own samples override a rule that blocks. Call 10 says a blocked phrase can't come back through a sample, so the skill tells plainspeak-writer, as part of the request, that samples set word choice and rhythm only.
- **Section 9's format lives in candidate-positioning's `format.md`,** the format's one home, and `check_positioning.py` checks it.
- **The gate compares the proofs with the resume going with the letter,** since it may not be the one the case was built from. That's how a changed date gets caught before drafting.
- **`check_positioning.py --current` hashes the deeper record** to prove the case is current. No text from it reaches the conversation, and the three-files test checks that nothing reads, prints or searches it.
- **A missing reviewer means the letter is recorded as not reviewed,** as submission-review tells a calling skill.
- **A bracket plainspeak-writer leaves** is the one thing the person fills, and the Word file waits for it. The gate asks up front for what the letter can't stand without, and `--given` lets a name the person gives in the session, like the hiring manager's, pass the name check.
- **Two scripts, not one:** the checks in `check_letter.py`, and the Word file in `build_letter.py`, the way resume-ops keeps its build apart.
- **`sources.md` gives where each source says it,** and quotes only the two open-licensed studies, to keep word-for-word quotes from copyrighted pages to a minimum.
- **A text resume has no font,** so the Word file uses Calibri 11 with one-inch margins and says so.
- **The page is estimated,** since neither Word nor LibreOffice is on the test computer. The tests measure each Word file line by line with the real font's widths.
- **A text box letter drops the contact block and the date,** as the email form does. The channel and the reader come from the positioning file when it has them.
- **Without plainspeak-writer the skill stops,** since it keeps no copy of the voice.
- **The research changed two things the spec says.** The Yale study holds as a preprint about one freelance platform, where keyword-tailored letters predicted callbacks about half as strongly after an AI tool arrived, and where editing time went with winning but wasn't shown to cause it. The watermark covers current Claude models, with older ones still being added, so the notice says a letter's text "may carry" the mark.

Fixed before release, from the live runs:

- Step 1 looked the positioning file up from the person's shorthand in run cl-n1. It now lists the `positioning-*.md` files and takes the company and the role from the posting.
- The watermark line in SKILL.md held its source ID inside the quote, and three hand-overs passed "[C24]" to the person. The ID now sits outside the line.
- `check_letter.py`: a comma now ends a name ("Fernley, Nevada"); a plural possessive and words like "Thank" at a sentence's start no longer read as names; a Word file's voice check reads the contact block and the sign-off as blocks, not one-line paragraphs; and a number counts as disagreeing with the resume when the resume the case was built from held it, while a number from a deeper record is only noted.

Checked:

- Every live test in `tests/RUN-TESTS-cover-letter.md` passed, 14 of 14, in runs on October 7 with made-up writers B, E, F and G. `tests/RESULTS.md` gives each result, and `tests/evidence/cover-letter-*.md` gives the evidence.
- skill-creator graded two of those runs against the same requests without the skill, on ten checks each. With the skill, both letters passed all ten, and without it they passed 3 and 2.
- The unit tests: 129 of 129 pass on Windows with Python 3.12.10, once the package is built from the release commit.
- plainspeak-writer 1.6.2's checker, pinned at commit 577a985, ran on every text file this release adds or changes. HARD hits are left only in quoted material, and `tests/evidence/cover-letter-14-own-files.md` lists them with each warning that was cleared.

## 0.2.3 · Home page facts and confirmed gaps

Two faults in `check_positioning.py` from the Claude Code run on 0.2.1, and three lines that plainspeak-writer 1.6 and the 0.2.2 install left out of date.

In that run, writer E's positioning file kept "now ships to all 42 stores" as a firm fact. The news page says it, and so does the home page, and the skill's step 3 drops any fact the home page states. The checker passed the file, since it looked only at the address a fact cites, and this one cited the news page. In the same run, the helper couldn't cite her confirmation in a gap row. `searched resume.txt; A2` failed because the checker read "A2" as a file missing from the stamp, and `A2; searched resume.txt` failed because a gap's source had to start with "searched".

Changed:

- `skills/candidate-positioning/scripts/check_positioning.py` 0.2.3. With `--sources`, when a firm pages file in the stamp holds the home page, found by its address, a fact that shares a number and the word after it with the home page fails ("42 stores", "2,400 shippers"), and so does a founding year ("since 1987"), whichever page the fact cites. A home page fact with no number, like "free returns", is still left to the skill's reading. A gap's source can name the answer that confirmed it, before or after what was searched, like `searched resume.txt; A2`. Anything else in a gap's source fails with a message that says what's allowed.
- `skills/candidate-positioning/references/format.md`: the map's Source column allows an answer ID on a gap, the firm facts paragraph says what the checker does with a saved home page, and the example's voice check names plainspeak-writer 1.6.2.
- `tests/keys/a-seeded.md`: the note on which plainspeak-writer lists R01 and R02 under HARD names 1.6.2, and says flaw 5 still warns under 1.6's narrower R44.
- `tests/RUN-TESTS.md`: setup step 3 names the folder where the Code tab installs an uploaded plugin, where 0.2.2 went.
- `tests/unit/test_check_positioning.py`: five tests, for a gap citing its answer in either order, a gap source holding something else, a home page fact, a home page that shares nothing, and what counts as a claim. Four of them fail on 0.2.2's script, and the fifth passes on both.
- `.claude-plugin/plugin.json`: version 0.2.3.

Checked:

- The unit tests pass on Windows with Python 3.12.10, with plainspeak-writer 1.6.2 beside the repository.
- Against every saved positioning run in `jso-tests/positioning/runs/`, the new script gives the same result as 0.2.2's on all but one: writer E's file from the 0.2.1 run, which now fails on "42 stores". The 2.1.288 run's file for the same writer, which kept the fact out, still passes.

## 0.2.2 · Voice rules uploaded to the desktop app

The packet script didn't find plainspeak-writer when it was uploaded to the Claude desktop app as a skill. The app keeps uploaded skills in its own folder, `local-agent-mode-sessions\skills-plugin\<ids>\skills\` under `%APPDATA%\Claude\` on Windows, and the script searched only `~/.claude/skills`, `~/.claude/plugins` and `.claude/skills` in the working folder. In both live runs of 0.2.1 in the Code tab, every packet came out "Voice rules: not found. Voice is unchecked." until it was built again with `--voice-dir`. candidate-positioning's `check_positioning.py` already searched the app's folder and found the same copy on its own.

Changed:

- `skills/submission-review/scripts/build_packet.py` 0.2.2. `default_roots()` adds the app's `local-agent-mode-sessions` folder: under `%APPDATA%\Claude\` on Windows, `~/Library/Application Support/Claude/` on a Mac and `~/.config/Claude/` on Linux, the same places `check_positioning.py` searches. Nothing else changed, and `--voice-dir` still wins when it's given.
- `tests/unit/test_build_packet.py`: three tests for the app's layout. Two of them, the search roots and a packet built with no `--voice-dir`, fail on 0.2.1's script.
- `tests/RUN-TESTS.md`: test 11's step 3 names the new layout among those the unit tests cover.
- `.claude-plugin/plugin.json`: version 0.2.2.

Checked:

- `test_build_packet.py`: 25 of 25 pass on Windows with Python 3.12.10.
- On the test computer, with plainspeak-writer 1.5 uploaded to the app, a packet for writer B's letter built with no `--voice-dir` named plainspeak-writer 1.5, its rules file and its full check, and the checker ran. The search took under a second.

Left for later:

- The package in `dist/` still holds 0.2.1 until it's built from the release commit.

## 0.2.1 · The full check in its own file

plainspeak-writer's 1.5 build moves the full check out of `references/tells.md` into `references/full-check.md`. The full check is the rule-by-rule list that says which rules block and which warn. 0.2.0's review packet named only `tells.md`, and the reviewer opens nothing the manifest doesn't name. So with 1.5 installed, the reviewer would have had no list of blocks to sort its own findings by, and no full check to run by hand when the checker can't run. This version works with both layouts.

Changed:

- `skills/submission-review/scripts/build_packet.py` 0.2.1. When plainspeak-writer has `references/full-check.md`, the manifest gets a "Full check" line naming it under the "Voice rules" line, and a checker that didn't run points the reviewer at that file. With 1.4.1, which keeps the full check in `tells.md`, the manifest is the same as before apart from the script's version. That version had stayed at 0.1.2 until now, since the script didn't change in 0.1.3 or 0.2.0. Three section comments that ended in "--" and two subtractions with a spaced minus are rewritten without them, because plainspeak-writer's checker reads code as prose and blocked each one under R01. They're older than this version, and the script works the same.
- `agents/submission-reviewer.md`: the reviewer opens the file on the manifest's "Full check" line as well as the rules file, and takes the list of blocks from the full check wherever it sits. The report's "Voice rules" line names each rules file it used.
- `tests/keys/b-letter.md`: test 5's list of opened files allows the full check file when the manifest names it.
- `tests/RUN-TESTS.md`: test 11 checks the "Full check" line, and that the reviewer opened that file, when plainspeak-writer 1.5 or later is installed.
- `tests/unit/test_build_packet.py`: three tests for the two layouts. The two for the new layout fail on 0.2.0's script.
- `.claude-plugin/plugin.json`: version 0.2.1.

Checked:

- The unit tests: 71 of 71 pass on Windows with Python 3.12.10, including the check that the package in `dist/` matches the repository.
- With the installed plainspeak-writer 1.4.1, a packet for writer B's letter came out the same as from 0.2.0's script, apart from the script's version and the packet folder's name. With the 1.5 build at commit `3396771`, the manifest named both files, and the checker ran.
- Every file this version changes passes plainspeak-writer 1.4.1's checker and the 1.5 build's with no HARD hits.

Left for later:

- A live review with the new instructions, which needs 0.2.1 installed. The fresh-session tests cover it.

## 0.2.0 · Candidate positioning

The second skill, built from the candidate-positioning spec. It works out the case for one candidate and one posting before anything gets written, and saves it as one positioning file. resume-ops reads the file from 2.4.0 on, and cover-letter will read it once it's built. Submission review gains a second direction that uses the same file.

Added:

- `skills/candidate-positioning/SKILL.md`, the ten steps, the rules and the commands. The skill asks the person at two points at most: one message at step 2 when something's missing, and one confirmation at step 9.
- `skills/candidate-positioning/references/format.md`, the positioning file's format, section by section, with a full example built on test writer B's files. It's the format's one home.
- `skills/candidate-positioning/references/case.md`, on finding what the firm is buying, the hiring team's view, the four lines, ranking the proofs and picking the phrases to watch for.
- `skills/candidate-positioning/scripts/check_positioning.py` 0.2.0. It checks a file's shape every time. Its options check each quote against its file and line, whether a source changed since the stamp, the sentences a file shares with a past letter, plainspeak-writer's voice check on the sentences other pieces reuse, what resume-ops or cover-letter needs, a finished piece against the file, and the firm facts' links. It also prints a JSON view and the file's name.
- `tests/unit/test_check_positioning.py`, 47 tests for the script; `tests/unit/test_version.py`, which checks that `plugin.json`, this file and the built package agree; and `tests/unit/run_tests.py`, which runs every unit test.
- Writers E to H in `tests/writers/` and their keys in `tests/keys/`. Writer H's posting is a real one, as the owner asked, so the link test reaches real pages. Its text stays on the test computer, out of the repository.
- `tests/RUN-TESTS-positioning.md`, with the spec's thirteen tests and how to run them; the `tests/evidence/positioning-*.md` files and `tests/evidence/positioning-runs/`; and a candidate-positioning section in `tests/RESULTS.md`.
- Test 16 in `tests/RUN-TESTS.md`, for the review's second direction, with its evidence in `tests/evidence/16-second-direction.md`.

Changed:

- `skills/submission-review/SKILL.md`: when the posting has a positioning file, the conversation checks the piece against it after the blind report, under its own heading. The owner asked for a review that works in both directions. The reviewer never sees the file, so the review itself stays blind, and `agents/submission-reviewer.md` is unchanged.
- `README.md`: a section on candidate positioning, the review's second direction, new examples, the file list and the tests.
- `.claude-plugin/plugin.json`: version 0.2.0, a description that names both skills, and the keyword "positioning".
- `tests/RUN-TESTS.md`: the Claude desktop app keeps an uploaded plugin under `%APPDATA%\Claude\local-agent-mode-sessions\` on Windows, not under `~/.claude/plugins`, so the setup step names both places.
- `tests/writers/README.md`: rows for writers E to H.

Fixed before release, from round one of the tests:

- Writer E's facts from her saved pages cited the saved file and line but not the page. A fact from a saved page now gives the page's address, with the saved file and line in brackets, and the checker warns when a fact from beyond the posting has no link.
- Writer H's posting has numbered headings and lines for other units, which no requirement row fits, so the checker warned on 15 of its lines. A "Not mapped" line under the map now lists such lines with the reason, and the checker warns only when the reason is missing.
- Writer H's first file said how often one of her certifications renews, which came from general knowledge, not from her files. SKILL.md now says an outside fact goes in the firm facts with its source, or to the person as a question. In round two the skill asked her.

Round two ran writers E and H again, and both passed.

Where this build departs from the spec, and why:

- **Past letters.** The spec says no sentence or structure moves from an old letter into the file. On October 5 the owner ruled that a sentence may move from one piece to another when it states the same proven fact and is still true, and that no sentence repeats word for word within one piece. The skill follows the ruling. `--against` lists every sentence the file shares with a past letter so each one gets checked, a fact that ages is still worked out from the dates, and the shape check fails a sentence the file says twice. The spec's test for past letters became a check that each shared sentence is still true.
- **Firm facts.** The owner ruled that facts come from the posting and the firm's other pages, that two is a floor, and that relevance decides how many. Each fact says why it matters to the case. Home-page facts stay out, since every applicant reads the home page.
- **Stops.** The spec has the skill stop once, at step 9, and also ask once at step 2. The skill asks at step 2 only when something's missing, puts the request for firm facts into that message when the session can't reach the web, and confirms once at step 9.
- **Reading a long file.** The spec reads a file whole under about 2,000 lines. The skill takes resume-ops's whole rule, about 2,000 lines or 150 KB, so a file of few but very long lines gets searched too.
- **The voice check** also covers the plain descriptions in section 6, since pages use them, and runs on the letter surface, since cover-letter reuses these sentences in letters.
- **The format adds four things** the spec doesn't name: a short SHA-256 for each source in the stamp, so a script can tell whether the file is current; IDs for the answers the person gives in the session; "Confirmed: not yet" for a saved draft; and "off" in the show-on column for a gap.
- **The letter half of "Off the page"** waits for cover-letter, whose spec repeats the test. The resume half ran on a resume built by resume-ops 2.4.0.

Checked:

- The spec's tests 1 to 13 pass, with their evidence in `tests/evidence/positioning-01-shape.md` to `positioning-13-own-files.md`. Test 4 passed in round two. Test 6 ran for the resume only.
- Test 16 passes. The reviewer stayed blind, and the check against the file sorted its two must-fix findings.
- The unit tests: 68 of 68 pass on Windows with Python 3.12.10, including the 19 submission-review tests and the check that the package in `dist/` matches the repository.
- Every file this version adds or changes passes plainspeak-writer 1.4.1's checker and the 1.5 build's with no HARD hits, apart from the quoted examples that `positioning-13-own-files.md` lists. No file holds anything personal to the owner.

Left for later:

- cover-letter, and with it section 9 of the format and the letter half of test 6.
- A fresh session with 0.2.0 installed, for submission-review test 2 with the git snapshot rule and for a positioning run through the installed plugin.
- plainspeak-writer 1.4.1 blocks the dash in a date range such as "Jan 2022 – Present", which resume-ops writes, so a review of a resume-ops resume gets a must-fix for it. The fix belongs in plainspeak-writer, and a change note for its next version asks for it.

## 0.1.3 · A rule for the git snapshot

A package rebuilt on October 5 carried these changes under the 0.1.2 number, so two different packages shared one version. This version gives the changes their own number. A changed file always gets a new version from here on.

Changed:

- `build_packet.py` reports its own version as 0.1.2, so a packet's manifest shows which script built it. The script changed in 0.1.2, but the 0.1.2 commit (`7d0de7e`) still called it 0.1.0. The copy uploaded to the desktop app on October 5 already had this fix, so it reports 0.1.2.
- The reviewer treats the git snapshot that Claude Code attaches to every helper (the branch, the git user name, changed files and recent commit titles) the way it treats the account email: it lists the snapshot, quotes none of it and never counts it as a profile. A branch name, file name or commit title about the piece, its target or how it was written counts as a leak. The 0.1.2 rerun showed the snapshot reaching every reviewer with no rule for it, and a commit title such as "soften the gap line" would tell a reviewer what the writer meant. File names count because the snapshot lists changed files, and a file name can say what the writer meant, which is why the manifest leaves them out.
- `tests/keys/b-letter.md`: test 2 names a git snapshot among the things the app attaches to every helper, next to the account email and tool instructions.
- `.gitignore` leaves out `jso-tests/`. RUN-TESTS.md has a session build its packets there, and in Claude Code that folder sits inside the repository, so the rerun's packets showed up as untracked files.

Added:

- `tests/evidence/01-isolation-claude-code-0.1.2.md`, `02-memory-claude-code-0.1.2.md` and `07-seeded-claude-code-0.1.2.md`, from a rerun of tests 1, 2 and 7 in Claude Code with 0.1.2 installed, and a "Claude Code rerun on 0.1.2" section in `tests/RESULTS.md`. All three passed. Test 2 passed this time because the reviewer saw none of the five kinds, listed the account email without the address and wrote `blind: yes`. The test 7 reviewer wrote the same blind line. The `-claude-code.md` files from the 0.1.1 run stay as they were. The Windows user name in each path is written as `<user>`, and no email address appears.

Checked:

- The three new evidence files, `tests/RESULTS.md` and this file pass plainspeak-writer 1.4.1's checker with no HARD hits.
- `agents/submission-reviewer.md` and `tests/keys/b-letter.md` pass the same checker with no HARD hits. The git snapshot rule hasn't run in a live review yet. Test 2 needs a new run with it installed.

## 0.1.2 · A fix from the Claude Code tests

Tests 1, 2, 7 and 14 ran in Claude Code on 0.1.1, in the Code tab of the Claude desktop app. Tests 1 and 7 passed, test 14 passed on its terms, and test 2 failed. The evidence is in the four `-claude-code.md` files in `tests/evidence/`, and the summary is under "Claude Code run" in `tests/RESULTS.md`. This change fixes what test 2 showed.

Changed:

- The reviewer is told that an account email alone isn't a user profile. It lists the email under "Also in my context" without the address and never counts it as a reason for `blind: no`. Anything more about the person is still a profile. In Claude Code the app attaches the account's email address to every helper, and the instructions didn't say how to treat it. Three of the run's four reviewers wrote `blind: no` for it and one wrote `blind: yes`, so test 2 failed on a review that saw no saved memory, preferences, project instructions or earlier conversation.
- `tests/keys/b-letter.md`: for test 2 in Claude Code, the key expects none of the five kinds the follow-up names, where it said "none". In Claude Code the "Also in my context" line still names the account email and the app's tool instructions, so it can't read "none". A strict reading of the old wording would have failed a review that reads `blind: yes`.
- `skills/submission-review/scripts/build_packet.py`: the packet's files are written as bytes. The script passed `newline` to `Path.write_text`, which Python takes only from 3.10 on, so it couldn't build a packet on 3.8 or 3.9, though the README says 3.8 or newer. On 3.12 the packet's files come out the same, byte for byte. On Python 3.8.20 and 3.9.25, 13 of the 19 tests failed before the change and all 19 pass after it.
- `tests/unit/test_build_packet.py`: the test piece is written as bytes, and the line-ending test checks the packet's copy as bytes. The piece was written in text mode, where Windows turns each `\n` into `\r\n`, so the file held `\r\r\n`. `build_packet.py` rightly turned that into a blank line, and the test failed on Windows while it passed on Linux, where the 0.1.1 run was recorded. The check also read the packet's copy in text mode, which turns `\r\n` back into `\n`, so a piece that held `\r\n` passed whether or not the script fixed it. The 19 tests pass on Windows with Python 3.12 and the 1.4 checker next to the repository.

Added:

- `tests/evidence/01-isolation-claude-code.md`, `02-memory-claude-code.md`, `07-seeded-claude-code.md` and `14-human-letters-claude-code.md`, from the Claude Code run, and a "Claude Code run" section in `tests/RESULTS.md`. The test 14 file gives counts only, and the reports and quotes stay in `tests/human/results/`, which git ignores. The Windows user name in each path is written as `<user>`, so nothing personal ships in the repository.

Checked:

- `agents/submission-reviewer.md` and this file pass plainspeak-writer 1.4's checker with no HARD hits.
- The new rule hasn't run in a live review yet. Test 2 needs a new run in a fresh Claude Code session with 0.1.2 installed.

## 0.1.1 · Fixes from the first live tests

Twelve live tests ran in Cowork on 0.1.0 and all twelve passed. The evidence is in `tests/evidence/` and the summary is in `tests/RESULTS.md`. These changes fix what the runs showed.

Changed:

- The reviewer writes "(whole piece)" in place of a line number when a checker hit is marked L0. One run showed "Line 0" with no direction, and plainspeak-writer 1.4 marks every rate warning L0, so this now comes up often.
- The reviewer numbers findings past the fifth on from 6. One report put all of them under a single number, which hid how many there were.
- The reviewer ends its report with "What I couldn't judge" and adds nothing after it. In Cowork, reports ended with a stray line about saved memory.
- "When the caller pushes back" is now "After the report", and a follow-up question gets a short answer instead of the whole report sent again. Every follow-up in the live tests got the full report back.
- `tests/keys/a-clean.md`, `a-seeded.md` and `c-letter.md`: a checker warning counts as met when the report lists it as should-fix or clears it with a reason. The reviewer's rules allow both, and test 6 cleared its warnings with sound reasons.
- `tests/keys/a-seeded.md`: the label for flaw 2 sits in quotation marks, so the checker reads it as a quoted example.
- `tests/RUN-TESTS.md`: test 14 says a PDF can lose its signature in its text layer, and adds an optional check of published letters by well-known writers, with counts only. The Claude Code run now includes the letters people wrote.
- `tests/evidence/` and `tests/RESULTS.md`: the computer's name, the account folder IDs and the owner's first name are replaced with plain stand-ins, so nothing personal ships in the repository.

Added:

- `tests/evidence/01-isolation.md` to `12-channel.md` and `tests/RESULTS.md`, from the live run.
- `tests/evidence/14-human-letters.md`, counts only. Two letters a person wrote got Fix first, every HARD finding was one the rules require, no quote was wrong, and the one false alarm came from the PDF's missing signature. The letters, the reports and the quotes stay in `tests/human/`, which git ignores.

Checked against plainspeak-writer 1.4:

- The 19 unit tests pass with the 1.4 checker next to the repository.
- The checker's HARD hits on the test pieces match the keys: R01 and R02 on the seeded letter, none on the others. 1.4 turns per-hit warnings into one rate warning per piece.

## 0.1.0 · Submission review

Added:

- `agents/submission-reviewer.md`, the reviewer. It reads a packet and nothing else, runs seven checks for up to three readers, and reports in a fixed shape under fixed verdict rules.
- `skills/submission-review/SKILL.md`, the skill that checks the reviewer is installed, collects the files, builds the packet, starts the reviewer by name and hands back its report.
- `skills/submission-review/scripts/build_packet.py`, which builds the packet. It turns Word files into text, finds plainspeak-writer, runs its checker and writes the manifest. It has no field for notes.
- `tests/unit/test_build_packet.py`, with 19 tests for the script.
- `tests/RUN-TESTS.md` and the test pieces, for the live tests with made-up writers.
- `README.md`, `LICENSE` (MIT), `.gitignore` and `.claude-plugin/plugin.json`.

Where this build departs from the spec, and why:

- Names: `submission-reviewer` for the reviewer and `submission-review` for the skill replace the spec's working names. The owner named them.
- The reviewer's only tool is Read, where the spec allowed read and search tools. The manifest names every path, so search adds nothing, and without search the reviewer can't find files outside the packet.
- The reviewer has no shell, and the skill runs the checker. Current docs say a plugin's helper can't hold its own permission rules or hooks, so no setting could limit a shell to one script. The spec named this fallback.
- The reviewer skips project instruction files (CLAUDE.md), which helpers load by default.
- The skill starts the reviewer by name with the Agent tool. It avoids the skill setting that runs a skill in its own context, which has an open bug where plugin skills run inside the main conversation (anthropics/claude-code issue 49559). It never starts a fork, which copies the conversation.
- Cowork is supported in 0.1, where the spec listed it for later. Current docs say Cowork loads plugin helpers, and the same files work in both products.
- The report says whether the reviewer saw saved memory. A test in Cowork showed that every helper gets the account's saved memory, whatever its tools, and the spec's isolation test only checked the conversation.
- The manifest leaves original file names out, because a file name can say what the writer meant.
- With no reviewer available, as in claude.ai chat or after an upload under Skills, the skill stops instead of sending the person to a fresh chat. Chat ignores plugin helpers, and a fresh chat still has saved memory.
- The skill asks once for a missing target. The reviewer can't ask the person anything, so with no target it reviews against a general reader and says so.
- Every block in plainspeak-writer's rules counts as must-fix, including the ones only a reader can catch, such as an internal method name. The spec named checker blocks only.
- One finding per problem: a rule that hits several lines is one finding that quotes each line. Otherwise one repeated punctuation habit could push a piece to Rethink.
- Requirement checks: a resume is judged alone, and any other piece sent with a resume is judged across both, because the AI grader sees both. Requirement findings count as must-fix only when the AI grader is one of the readers. Without this, every letter would have to repeat the resume to pass.
- The first take ends on `Fit: yes` or `Fit: no`, so the verdict rules run the same way every time.
- Findings past the fifth in a section are listed one line each, with a short quote, where the spec capped each section at five. A finding cut from the report can't be fixed or tested.
- A checker warning is a should-fix finding unless the reviewer clears it with a stated reason, the way plainspeak-writer's rules treat warnings. A dry run showed the reviewer doing this on its own, so the rule now says so.
