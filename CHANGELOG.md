# Changelog

Every change to this plugin is logged here: what was added, changed or removed, and why. Nothing comes out without a line saying so. Newest first.

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
