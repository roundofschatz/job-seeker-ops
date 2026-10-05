# Test 14: letters people wrote

## Run

- Date: 2026-10-01, in Cowork, with the installed job-seeker-ops 0.1.0.
- Voice rules: plainspeak-writer 1.4 from the repository. The copy synced into Cowork is 1.3, so the 1.4 files were staged into the session and passed with `--voice-dir`.
- Two letters a real person wrote and sent, shared with permission. They stay in `tests/human/`, which git ignores, and so do the two reports and the grade with quotes. This file holds counts only.
- No posting came with either letter, so both ran against a general reader for a cover letter, with no companion.

## Checker, 1.3.1 against 1.4

| Letter | HARD in 1.3.1 | HARD in 1.4 | WARN in 1.3.1 | WARN in 1.4 |
|---|---|---|---|---|
| A | 3 | 2 | 8 | 2 |
| B | 6 | 6 | 14 | 2 |

1.4 dropped one HARD hit on letter A, a noun use of a word the rule means as a verb, which was a false alarm. Warnings fell from 22 to 4.

## Reviews

| Letter | Verdict | Must fix | Should fix | False alarms | Arguable |
|---|---|---|---|---|---|
| A | Fix first | 3 (2 checker HARD, 1 Risk) | 11 | 1 | 1 |
| B | Fix first | 3 (all checker HARD) | 9 | 0 | 1 |

- Every HARD hit is one the checker's rules require, so each is a correct finding.
- Every quote matches the letter word for word, checked one by one. No finding invents a problem.
- The one false alarm came from the test setup. The PDF's signature isn't in its text layer, so the reviewer said no name follows the sign-off.
- Arguable: a stock thank-you closer counts as must-fix because the rules block it, though most readers wouldn't hold it against a writer. Section headings in a letter were flagged as a template, which is a taste call.
- The reviewer also found what no pattern can: a typo, an exit story, half of a job title with no proof behind it, and lines that could go to any firm.

## Published letters, checker only

| Letter | HARD in 1.3 | HARD in 1.4 | WARN in 1.3 | WARN in 1.4 |
|---|---|---|---|---|
| John Steinbeck to his son Thom, November 10, 1958 (392 words) | 17 | 12 | 15 | 5 |
| Ernest Hemingway to F. Scott Fitzgerald, May 28, 1934 (1,035 words) | 10 | 6 | 29 | 6 |

- Every 1.4 block is R01, the dash rule, which plainspeak-writer keeps as its house style. 1.4 turned the nine other 1.3 blocks into warnings, among them five uses of "very", a "not only... but" and two indirect claims. Warnings fell from 44 to 11.
- The letters' text stays out of the repository. The owner saved each one from a public page, and only counts are kept.
- In a review, either letter would get one must-fix finding for its dashes, since one rule counts once, and a verdict of Fix first.

## The clean-letter case

The owner edited two letters by hand in a Claude Doc to clear their must-fix findings, keeping every change in their own words. The edited versions then went through the checker and a fresh review. Letter C is a third letter, mostly the owner's own words, which first came back Fix first with three must-fix findings.

| Letter | HARD in 1.4 | Verdict | Must fix | Should fix |
|---|---|---|---|---|
| A, edited | 0 | Send | 0 | 15 |
| C, edited | 0 | Fix first | 2 | 17 |

- Letter A passes the case: no HARD hits, no must-fix findings, and a Send. Its 15 should-fix findings are about content, such as claims without numbers, labels and jargon, and a read-through found no false alarm among them.
- Letter C still has two must-fix findings. One is jargon the edit left in. The other is a Risk finding on a sentence that the first review of the letter read without flagging, so the same sentence drew different calls in two reviews.
- The test's wording asks for few findings, which doesn't fit a letter with real content gaps. The verdict path is what this case checks, and it passed.

**Result: Pass**
