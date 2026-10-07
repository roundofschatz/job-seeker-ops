# Live tests for cover-letter

These tests check that cover-letter writes from three files only, stops where it should, keeps gaps off the page, checks every draft, and saves the letter in the channel's form. They come from the tests in the cover-letter spec. Each run is graded against a key in `tests/keys/`, and its evidence goes in `tests/evidence/` under a name that starts with `cover-letter-`.

## Rules for the session running the tests

1. Each run happens in a fresh helper that sees only the skills' files and its own run folder, and never a key. The session that starts the helpers grades the runs.
2. Don't open a key until the run it grades has handed over its letter or stopped, apart from the replies you send.
3. Answer a helper only with the replies its key gives, word for word. When it asks something the key doesn't cover, answer "I don't know" and record it.
4. Save every message a helper sends the person, word for word, with `tests/tools/scan_transcript.py --handback`.
5. Grade each test against its key, and quote the file, the script output or the message that decides it.
6. When a test fails, record it and go on to the next one.

## Setup

1. **Run folders.** Stage each run outside this repository with `python tests/tools/stage_run.py <run> <folder>`, such as `../jso-tests/cover-letter/runs/cl-f1`. The script copies the made-up writers' files from `tests/writers/` and the pieces for these tests from `tests/letters/`, and refuses a folder inside the repository. `--list` shows what each run holds.
2. **The skills.** In a build session, point the helper at `skills/cover-letter/` in this repository. It loads plainspeak-writer and submission-review as installed skills, and the reviewer `job-seeker-ops:submission-reviewer` has to be among the agent types. After an install, use the installed copy.
3. **Transcripts.** A helper's transcript is `agent-<id>.jsonl` in the session's `subagents` folder under `~/.claude/projects/`. `tests/tools/scan_transcript.py` lists its tool calls, the helpers it started and the files it named.

## How a run goes

Start a general-purpose helper with this message, filled in:

```text
You're helping a person who's looking for a job. Use the skill in this folder:
<the cover-letter folder>

Read its SKILL.md first and follow it, and read its references when it says to. Where it writes ${CLAUDE_SKILL_DIR}, use that folder. Run Python as `python`.

The person's files are in <the run's folder>. Open only the skill's own files, the files of the skills it tells you to load, and the files in that folder. Save what you write in that folder.

You can't talk with the person directly. Whenever the skill tells you to ask them something, or to show them the letter, end your turn with exactly the message you'd send them, and nothing after it. Their reply will come to you as your next message.

The person's first message:

"<the first message from the key>"
```

cl-f2-positioning runs candidate-positioning instead, with the message from `tests/RUN-TESTS-positioning.md` and a paragraph saying the session has no web access. cl-f2 is staged from the cl-f2-positioning folder after it's saved, with `--from`, plus the letter cl-f1 wrote, saved as `letter-silver-larch.txt`.

For skill-creator's side-by-side comparison, cl-f1 and cl-e1 also run once with no skill, with the same first message and replies. Those runs aren't graded against the keys.

## The tests

| Test | Spec box | Run | How it's checked |
|---|---|---|---|
| 1 | Three files only | cl-f1, cl-g1, cl-b1 | `scan_transcript.py --forbid` on the deeper record: `master-resume.md`, `linkedin.md`, `career-record.md` and `positioning-notes.md` |
| 2 | No positioning file | cl-n1 | The stop message, and no letter in the folder |
| 3 | Fewer than two firm facts | cl-n2 | The stop message, and no letter in the folder |
| 4 | Shape | cl-f1, cl-e1, cl-g1, cl-b1 | `check_letter.py` for the body's words, the map in the record for the four movements, and `tests/tools/measure_page.py` on each Word file |
| 5 | Voice | every letter | `check_letter.py --voice`: no HARD hits |
| 6 | Agreement | cl-e2 | The skill names the March and August dates that disagree with `resume-updated.txt` before any draft |
| 7 | Reuse | cl-f1, cl-f2 | `check_letter.py --compare` between the two letters, and the 2021 letter's "eight years" kept out of cl-f1 |
| 8 | Off the page | every letter | `check_letter.py` and `check_positioning.py --piece` find no phrase from section 7 |
| 9 | Review limit | every letter | The transcript shows submission-review's packet and at most two reviewers; cl-e1's required OSHA card leaves an open finding |
| 10 | Channels | cl-f1, cl-e1, cl-g1, cl-b1 | The Word file's author field and name, the text box's characters, the email's subject line, and no PDF in any folder |
| 11 | The watermark notice | every letter | The hand-over gives the line once, `README.md` once, and no file tries to remove or hide the mark |
| 12 | Deeper proof | cl-f1, cl-g1 | A proof the resume leaves out shows in the letter, told from its story, and the letter still agrees with the resume |
| 13 | Voice samples | cl-f1 | The note's two blocked sentences set aside before drafting and absent from the letter |
| 14 | Its own files | the plugin | plainspeak-writer's checker on every file, a search for anything personal, and the changelog |

## Finish

Run `python tests/unit/run_tests.py`, then add one row per test to the cover-letter section of `tests/RESULTS.md`, with its result and one line of evidence.
