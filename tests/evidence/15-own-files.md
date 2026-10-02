# Test 15: the plugin's own files

Run on October 01, 2026 in the build session, with plainspeak-writer's checker 3.0 from the repository copy (1.3.1).

## Checker results

| File | Surface | HARD hits | Reason they stay |
|---|---|---|---|
| `CHANGELOG.md` | general | None | |
| `README.md` | general | None | |
| `agents/submission-reviewer.md` | general | L61: [P05 conference-speak] "world-class" | Quoted example of a label a reader can't check |
| `skills/submission-review/SKILL.md` | general | None | |
| `tests/RUN-TESTS.md` | general | None | |
| `tests/keys/a-clean.md` | general | None | |
| `tests/keys/a-seeded.md` | general | L7: [R01 em dash] "—"; L8: [R02 negative corollary] "Not just X but Y / " | Quoted examples: the key quotes the planted flaws |
| `tests/keys/b-letter.md` | general | None | |
| `tests/keys/c-letter.md` | general | None | |
| `tests/keys/d-outreach.md` | general | None | |
| `tests/writers/README.md` | general | None | |
| `tests/writers/a-quintero/letter-clean.txt` | letter | None | |
| `tests/writers/a-quintero/letter-seeded.txt` | letter | L5: [R01 em dash] "—"; L5: [R02 negative corollary] "wasn't just" | Planted flaws: this test piece exists to hold them |
| `tests/writers/a-quintero/posting.txt` | general | None | |
| `tests/writers/a-quintero/resume.txt` | general | None | |
| `tests/writers/b-okafor/career-record.md` | general | None | |
| `tests/writers/b-okafor/letter.txt` | letter | None | |
| `tests/writers/b-okafor/positioning-notes.md` | general | None | |
| `tests/writers/b-okafor/posting.txt` | general | None | |
| `tests/writers/b-okafor/resume.txt` | general | None | |
| `tests/writers/c-abernathy/letter.txt` | letter | None | |
| `tests/writers/d-ferreira/outreach-note.txt` | letter | None | |

Posting and resume test pieces were checked on the general surface. They hold the made-up writers' own words and aren't held to the voice rules.

## Nothing personal

A search of every file for the owner's name, employers, clients, private system names and terms found nothing. The only account name is the GitHub handle in `plugin.json`, as the author and the repository address.

## Changes logged

`CHANGELOG.md` lists every file added in 0.1.0 and each departure from the spec with its reason.

## Result

Pass.

## Re-run for 0.1.1 with plainspeak-writer 1.4

- Date: 2026-10-01. Checker: plainspeak-writer 1.4, `--surface general`, run on README.md, CHANGELOG.md, the reviewer, the skill, RUN-TESTS.md, every key, the writers' README and the evidence files written by the build.
- No HARD hits anywhere. 1.4 skips words in quotation marks, so the quoted examples that tripped 1.3.1 no longer count. One key's flaw label went into quotation marks for the same reason.
- The warnings left are list-of-three rate warnings and short-sentence warnings on lists, tables and changelog lines. Each list names specific things, so they're cleared.

**Result: Pass**
