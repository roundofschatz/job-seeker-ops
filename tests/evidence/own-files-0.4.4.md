# The plugin's own files, job-seeker-ops 0.4.4

Cover-letter test 14, candidate-positioning test 13 and submission-review test 15 check the same thing: every file passes plainspeak-writer's checker with no HARD hits apart from quoted examples, holds nothing personal, and has its change logged.

## The checker

plainspeak-writer 1.7.1's `check_voice.py`, the plugin's own copy, ran on the 17 files the package ships outside the two bundled copies, at tag v0.4.4. No file has a HARD hit.

The bundled copies of plainspeak-writer and resume-ops aren't checked here, since they're those tools' own files, each checked by its own release.

Warnings, by file:

- **Code:** `check_positioning.py`, `check_letter.py`, `build_letter.py` and `build_packet.py` draw U04 and V04 from `!=`, `#!` and their lines of code.
- **Lists of three, by rate:** `README.md`, `agents/submission-reviewer.md`, candidate-positioning's `SKILL.md`, `format.md` and submission-review's `SKILL.md`. These were cleared in earlier releases.
- **"What the X did" (V10, new in 1.7):** in files that 0.4.x didn't change.
  - `agents/submission-reviewer.md` has "what the writer meant" three times.
  - `case.md` has two.
  - cover-letter's `letter.md` has five, such as "what the writer did" and "what the letter will do".
  
  The three SKILL.md files lost theirs in 0.4.0. `letter.md` matters most, since the drafting learns from it, so it's the first to fix in the next version.
- **`CHANGELOG.md`:** warnings in earlier releases' entries, which stay as logged.

## Nothing personal

A search of every file at tag v0.4.4 for the computer's user name, the account email, the app's, the session's and the plugin's install IDs, and the old made-up names finds only the credit the owner asked for. That's the owner's name in `LICENSE`, the README's Author line, `plugin.json`, `marketplace.json`, the 0.4.1 changelog entry, and the bundled copies' own licenses and READMEs. The only other hits are made-up examples in resume-ops's `document.md`, such as `linkedin.com/in/handle`.

The evidence files these tests added hold none of those either. In them, the user name became `<user>` and the IDs became `<id>`.

## The changelog

`CHANGELOG.md` logs every file 0.4.0 to 0.4.4 changed and why.

## Result

Pass.
