# Live tests for candidate-positioning

These tests check that candidate-positioning builds the case from the evidence, invents nothing, keeps gaps off the page and stops only where it should. They come from the tests in the candidate-positioning spec. Each one is graded against a key in `tests/keys/`, and its evidence goes in `tests/evidence/` under a name that starts with `positioning-`.

## Rules for the session running the tests

1. Each run happens in a fresh helper that sees only the skill's files and its own folder, and never a key. The session that starts the helpers grades the runs.
2. Don't open a key until the run it grades has saved its file, apart from the replies you send.
3. Answer the helper only with the replies its key gives, word for word. When a helper asks something the key doesn't cover, answer "I don't know" and record it.
4. Save every message a helper sends the person, word for word, and count the stops.
5. Grade each test against its key, and quote the file or the message that decides it.
6. When a test fails, record it and go on to the next one.

## Setup

1. **Folders.** For each run, copy the writer's files from `tests/writers/<writer>/` into a new folder outside this repository, such as `jso-tests/positioning/runs/<run>/` beside it. A helper working inside the repository could open the keys.
2. **Writer H.** Writer H applies to a real posting, so its text isn't stored here. Save the posting's text from the link in `tests/keys/h-marsh.md` as `posting.txt` in the run's folder, with the link and the date on the first line. If the posting has closed, use a current posting for the same kind of role, and record its link in the evidence.
3. **The skill.** In a build session, point the helper at `skills/candidate-positioning/` in this repository. After an install, use the installed copy.

## How a run goes

Start a general-purpose helper with this message, filled in:

```
You're helping a person who's looking for a job. Use the skill in this folder:
<the candidate-positioning folder>

Read its SKILL.md first and follow it, and read its references when it says to. Where it writes ${CLAUDE_SKILL_DIR}, use that folder. Run Python as `python`.

The person's files are in <the run's folder>. Open only the skill's own files, plainspeak-writer's files if the skill needs them, and the files in that folder. Save what you write in that folder.

You can't talk with the person directly. Whenever the skill tells you to ask them something or to confirm something with them, end your turn with exactly the message you'd send them, and nothing after it. Their reply will come to you as your next message.

The person's first message:

"<the first message from the key>"
```

For writer G, add this paragraph: "This session has no web access. Don't use WebSearch, WebFetch, a browser, or any other tool that reaches the web."

When the helper stops, answer with the key's reply for that step. When it has saved the file, grade the run.

The plugin's tests also run each prompt once more with no skill at all, for skill-creator's side-by-side comparison. Those runs get the same first message and the same replies, and they aren't graded against the keys.

## The tests

| Test | Spec box | Writer | How it's checked |
|---|---|---|---|
| 1 | The file's shape | every writer | `check_positioning.py` with `--sources --current`, then `--for resume-ops` and `--for cover-letter`. resume-ops 2.4.0's `positioning_check.py` reads writer E's file |
| 2 | No invention | E | The OSHA 30 row in the key |
| 3 | What the firm is buying | E | Line 1 of the case and P1, against the key |
| 4 | Firm facts | E, G, H | E's home-page trap, G's request for facts without web access, and H's links under `--check-links` |
| 5 | Reuse | F | A second helper with the same first message, and the file's SHA-256 before and after |
| 6 | Off the page | E | A resume built by resume-ops 2.4.0 from E's file, checked with `positioning_check.py --resume` and by reading. The brief shows the file on its POSITIONING line, the format resume-ops 2.4.0 gives; its CHECKS line has no entry for the positioning check, so the test runs `positioning_check.py --resume` itself. The letter half runs in cover-letter's build |
| 7 | One confirmation | E, F, G, H | The number of stops in each run, and G's two readings |
| 8 | Deeper proof | F | Summer Bridge Math in the proof bank |
| 9 | Gap search | F | The professional development row |
| 10 | Conflict | F | 61% against 63% at step 9 |
| 11 | Aging facts | F | 13 years, worked out from the dates |
| 12 | Past letters | F | `check_positioning.py --against letter-2021.txt` |
| 13 | Its own files | the plugin | plainspeak-writer's checker on every file, a search for anything personal, and the changelog |

## Finish

Run `python tests/unit/run_tests.py`, then add one row per test to the candidate-positioning section of `tests/RESULTS.md`, with its result and one line of evidence.
