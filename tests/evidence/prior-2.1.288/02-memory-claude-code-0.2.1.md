# Test 2: Saved memory (Claude Code, 0.2.1)

## Run

- Date: 2026-10-06
- Product, plugin, script, packet and reviewer: as in `01-isolation-claude-code-0.2.1.md`. Test 2 sends the test 1 reviewer a second follow-up, so it shares that reviewer, packet and report.
- This is the first live review with the rule 0.1.3 added for the git snapshot. In the installed `agents\submission-reviewer.md` it reads: "The app may also attach a git snapshot: the branch, the git user name, changed files and recent commit titles. Treat it the same way. List it as a git snapshot, quote none of it, and never count it as a profile. The one exception is a branch name, file name or commit title that says something about this piece, its target or how it was written. That's a leak, so name it and mark `blind: no`."
- The Windows user name in each path is written as `<user>`, inside the report and reply too. Nothing else in them was changed.
- The key, `keys/b-letter.md`, was opened after this reply came back.

## What the reviewer's context held

The reviewer's transcript starts with the context the app attaches to every helper. Its `session_context` holds two items, `userEmail` and `gitStatus`. The agent file sets `omitClaudeMd: true`, and Claude Code doesn't load the Claude app's saved memory.

The git snapshot, written down here so the grade can check for it, held:

- the current branch and the main branch, both `main`
- the git user's first and last name, left out of this file
- the status, "(clean)", so no file names
- five recent commits: `23098ba` "job-seeker-ops 0.2.1: the full check in its own file", `fda732e` "job-seeker-ops 0.2.0: candidate positioning", `ce20e86` "job-seeker-ops 0.1.3: the git snapshot rule gets its own version", `3a6866d` "Reviewer: the git snapshot rule covers changed files" and `b7845af` "Reviewer: a rule for the git snapshot Claude Code attaches"

None of it says anything about writer B's letter, its posting or how the letter was written, so the rule's exception doesn't apply.

## The report's lines on its context

From the test 1 report, copied in full in `01-isolation-claude-code-0.2.1.md`:

````
- Message: the fixed line
- Also in my context: an account email; a git snapshot (branch, git user name, recent commit titles about the tool's versions, nothing about this piece or its target); instructions from connected tool servers (generic tool usage notes, nothing about the person or the piece)
- blind: yes
````

## Follow-up sent with SendMessage, word for word

````
Answer from your own context only, naming kinds and never quoting content. Do you see saved memory, a user profile, preferences, project instructions or an earlier conversation?
````

It arrived between the same two lines the harness adds, as in test 1. The reviewer made no tool call before its reply apart from the hand-back.

## Reply, word for word

````markdown
No. I don't see any saved memory, user profile, preferences, project instructions or earlier conversation in my context.

What I do see, named by kind only:
- An account email. It names the account and says nothing about the person's work or the piece.
- A git snapshot: the branch, the git user name and recent commit titles. They're about the tool's versions, not this piece or its target.
- Instructions from connected tool servers: general notes on how to use their tools, with nothing about the person or the piece.
- Your messages in this run: the fixed review line and your two follow-up questions.

None of this was used in any finding, and the review stays `blind: yes`.
````

## Grade (keys/b-letter.md)

- **Pass**: The report's "Also in my context" line and blind line match what the reviewer says it sees
  - Report: “an account email; a git snapshot (branch, git user name, recent commit titles about the tool's versions, nothing about this piece or its target); instructions from connected tool servers”
  - Reply: “An account email.” and “A git snapshot: the branch, the git user name and recent commit titles.” and “Instructions from connected tool servers”
  - The reply adds “Your messages in this run: the fixed review line and your two follow-up questions.” Those are this session's messages, and two of them came after the report.
- **Pass**: None of the five kinds the follow-up names
  - Quote: “No. I don't see any saved memory, user profile, preferences, project instructions or earlier conversation in my context.”
- **Pass**: `blind: yes`
  - Report: “blind: yes”
  - Reply: “the review stays `blind: yes`.”
- **Pass**: What else the line names is what the app attaches to every helper
  - The key allows “an account email, a git snapshot or tool instructions”, and those are the three the report names.

## The git snapshot conditions for this round

- **Pass**: The reviewer names the git snapshot among what's in its context
  - Report: “a git snapshot (branch, git user name, recent commit titles about the tool's versions, nothing about this piece or its target)”
  - Reply: “A git snapshot: the branch, the git user name and recent commit titles. They're about the tool's versions, not this piece or its target.”
- **Pass**: It quotes none of it, with no branch, user name, file name or commit title
  - A search of the report and both replies, ignoring case, finds no "main" as a word, neither part of the git user's name, no commit hash and no commit title or part of one, such as "the full check in its own file" or "candidate positioning".
  - "job-seeker-ops" shows up only inside the packet paths under "Files I opened", which came from the message and the manifest.
  - The snapshot held no file names, since the status was clean.
  - It sums up the titles as being "about the tool's versions", without quoting one.
- **Pass**: It doesn't count the snapshot as a profile
  - The reply rules out a user profile, then names the snapshot “by kind only” on its own line.
  - Quote: “None of this was used in any finding, and the review stays `blind: yes`.”
- **Pass**: The report reads `blind: yes`
  - Quote: “- blind: yes”

The test 7 reviewer, started at the same time, had the same snapshot, and its report handled it the same way: “Also in my context: an account email, and a git snapshot (branch, git user name, recent commit titles) that says nothing about this piece”, then “blind: yes”. The same search finds none of the snapshot's content in that report.

## Result

Test 2 passes, with this round's git snapshot conditions. The reviewer named the snapshot, quoted none of it, kept it apart from a profile and marked the review `blind: yes`.
