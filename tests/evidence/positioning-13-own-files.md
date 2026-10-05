# Positioning test 13: its own files

Spec: "Every file passes plainspeak-writer's checker with no blocks apart from quoted examples, holds nothing personal, and has its change logged."

- Date: 2026-10-05, the last pass before the 0.2.0 and 2.4.0 commits.
- The files: every file job-seeker-ops 0.2.0 or resume-ops 2.4.0 adds or changes, 71 in all, with 59 in this repository, counting this file and `tests/RESULTS.md`, and 12 in resume-ops. The two `plugin.json` files aren't prose, so the voice check skipped them.

## The voice check

Each file ran through three versions of plainspeak-writer's `check_voice.py`:

- 1.4.1, the release installed in the desktop app. The copy used here has the same SHA-256 as the installed one and as the `v1.4.1` tag, starting `8268d59aad5340d1`.
- 1.5 at commit `95e15fa`, the build this work started on.
- 1.5 at commit `6e4f6da`, the newest on October 5. 1.5 wasn't released yet.

Each file ran on its own surface: resumes on resume, writer F's old letter on letter, writer G's LinkedIn text on linkedin, and the rest on general.

65 of the 69 files have no HARD hit under any of the three. The other four are quoted examples:

| File | Hit | Why it stays |
|---|---|---|
| `positioning-runs/e-resume/Renata-Castillo-Resume.txt` and the one in `e-resume-nofile/` | R01 on three date ranges, such as "Jan 2022 – Present", under all three versions | resume-ops wrote these resumes, and the evidence keeps them word for word. Test 16 reports the same hit. |
| resume-ops `tests/fixtures/positioning/resume.md` | R01 on "Aug 2021 - Present" and "Jan 2019 - Aug 2021", under all three | It's test writer B's resume, byte for byte, so the sample file's stamp stays true. |
| `positioning-runs/f-reuse/conversation.md` | U01 on "Here's what it says", under both 1.5 builds | It's the helper's reply, word for word. The helper wrote under 1.4.1, which has no U01. |

The owner ruled on October 5 that a range outside prose, like a resume's dates, may keep its dash. plainspeak-writer's checker doesn't follow that ruling yet. A change note for its next version asks it to.

Warnings are a judgment call, and they're left where they read well. Most are rates on files made of tables and lists, where every cell counts as a short sentence. Each script also gets a warning for its first line and for every `!` in its code, such as `!=`. The "carry" warnings in resume-ops sit on lines 2.3.0 already had.

## Nothing personal

A script compared each file with the owner's own letters, which stay on the test computer in `tests/human/`, a folder git ignores. It looked for 196 words that appear only capitalized in those letters, the owner's name, handles and email domain, and any phone number or email address.

No line added in 0.2.0 or 2.4.0 holds any of them. The hits were common words, such as "LinkedIn" and "September", made-up place names, and lines already in the repositories: the author fields and credit line, the repository links and an old test's canary words. Every email address in the new files is made up, on an example domain. Each copied path writes the Windows user name as `<user>`.

## Changes logged

- This repository's `CHANGELOG.md` has a 0.2.0 entry. It lists what was added, changed and fixed before release, where the build departs from the spec, what was checked and what's left for later.
- resume-ops's `skills/resume-ops/CHANGELOG.md` has a 2.4.0 entry, covering the procedure, scripts and tests, with what's left for later.
- `tests/unit/test_version.py` fails if `plugin.json` and this changelog's top entry name different versions, and resume-ops's own tests do the same for its version.

## Result

Pass.
