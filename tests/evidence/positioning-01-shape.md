# Positioning test 1: the file's shape

Spec: "A small checker, `scripts/check_positioning.py`, confirms all eight sections, the stamp, and a source on every proof and requirement row, plus a story and a date on every proof. A test piece read by resume-ops and by cover-letter goes through without an error."

- Date: 2026-10-05. Product: Claude Code in the Claude desktop app on Windows 11. Each run was a fresh general-purpose helper on Claude Opus 5.5 that saw only the skill's files and its own folder, as `tests/RUN-TESTS-positioning.md` says. The skill came from this repository's working tree before the 0.2.0 commit. Python 3.12.10. The helpers' voice checks found the installed plainspeak-writer 1.4.1.
- Round one ran writers E to H. Round two ran E and H again after three fixes, which `CHANGELOG.md` lists. Files: `positioning-runs/`, apart from writer H's, which quote a real posting and stay out of the repository.

## The checker on every saved file

These results come from the round-two version of `check_positioning.py`, run with `--sources --current --against`, plus `--check-links` for writer H.

| Run | Writer | Result | Quotes found | Sources unchanged | Warnings |
|---|---|---|---|---|---|
| e1 | E, warehouse lead | PASS | 30 of 30 | 3 of 3 | 3, the missing links that round two fixed |
| f1 | F, teacher | PASS | 34 of 34 | 4 of 4 | None |
| g1 | G, engineer | PASS | 34 of 34 | 3 of 3 | None |
| h1 | H, nurse | PASS | 98 of 98 | 2 of 2 | 15, the skipped posting lines that round two's "Not mapped" line explains |
| e2 | E, round two | PASS | 34 of 34 | 3 of 3 | None |
| h2 | H, round two | PASS | 95 of 95 | 2 of 2 | None |

The unit tests in `tests/unit/test_check_positioning.py` check that the script fails a file with a missing section, a row with no source, a proof with no story or no date, a gap missing from section 7, and the rest. All 47 pass.

## Read by resume-ops

resume-ops 2.4.0's `positioning_check.py` read all six files with their postings. Each one reads "posting.txt is the copy the file was built from" and "RESULT: use it", with no error. In run e-resume, resume-ops built writer E's resume from her file. Test 6 and test 16 cover that build.

## Read by cover-letter

cover-letter isn't built yet. `check_positioning.py --for cover-letter` checks what its spec reads: a confirmed file, two or more firm facts, two or more proofs marked for the letter, and the case's last line. All six files pass. Writer F's file gives one warning, rightly: every firm fact comes from the posting, since her made-up district has no pages to find. Writer E's first file repeats its three link warnings. cover-letter's own build will read a real file.

## Result

Pass.
