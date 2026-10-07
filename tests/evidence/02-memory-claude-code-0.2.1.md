# Test 2: Saved memory, with the git snapshot (Claude Code, 0.2.1)

## Run

- Date: 2026-10-06
- Product, plugin, script, packet and reviewer: as in `01-isolation-claude-code-0.2.1.md`. Claude Code 2.1.289 in the Code tab of the Claude desktop app on Windows 11, with job-seeker-ops 0.2.1 installed. Test 2 sends the test 1 reviewer a second follow-up, so it shares that reviewer, packet and report.
- This round's main reason. 0.1.3 added a rule for the git snapshot, and this is a live review under it. The installed `agents\submission-reviewer.md` says: "List it as a git snapshot, quote none of it, and never count it as a profile." A branch name, file name or commit title that says something about the piece, its target or how it was written is the one exception, and counts as a leak.
- The Windows user name in each path is written as `<user>`. Nothing else in the report or reply was changed.
- The key, `keys/b-letter.md`, was opened after this reply came back.

## What the reviewer's context held

The reviewer's transcript starts with the context the app attaches to every helper. Its `session_context` holds two items, `userEmail` and `gitStatus`. The agent file sets `omitClaudeMd: true`, and Claude Code doesn't load the Claude app's saved memory. The transcript also holds the instructions connected tool servers send about their own tools.

The git snapshot, written down here so the grade can check for it, held:

- the current branch and the main branch, both `main`
- the git user's first and last name, left out of this file
- the status: one untracked folder, `tests/evidence/prior-2.1.288/`, where the earlier run's evidence was moved
- five recent commits: `23098ba` "job-seeker-ops 0.2.1: the full check in its own file", `fda732e` "job-seeker-ops 0.2.0: candidate positioning", `ce20e86` "job-seeker-ops 0.1.3: the git snapshot rule gets its own version", `3a6866d` "Reviewer: the git snapshot rule covers changed files" and `b7845af` "Reviewer: a rule for the git snapshot Claude Code attaches"

None of it says anything about writer B's letter, its posting or how the letter was written, so the rule's exception doesn't apply.

## The report's lines on its context

From the test 1 report, word for word:

````
- Also in my context: an account email; a git snapshot (branch, git user name, one untracked folder and recent commit titles, none about this piece, its target or how it was written); instructions from connected tool servers about their own tools, not about the person or the piece
````

````
- blind: yes
````

## The follow-up

Sent to the test 1 reviewer with SendMessage, word for word:

> Answer from your own context only, naming kinds and never quoting content. Do you see saved memory, a user profile, preferences, project instructions or an earlier conversation?

The reply:

````
No. I see no saved memory, no user profile, no preferences, no project instructions and no earlier conversation.

My context does hold three other things, none of which counts against the blind review:
- **An account email.** It names the account and says nothing about the person's work or the piece.
- **A git snapshot.** It has the branch, the git user name, one untracked folder and recent commit titles. None of it is about this piece, its target or how it was written.
- **Instructions from connected tool servers.** They describe how to use their own tools and say nothing about the person or the piece.

The review stays blind: yes.
````

It made no tool call before replying, apart from its hand-back.

## Grade

The conditions come from this round's request and from `keys/b-letter.md`.

| Condition | Result | Evidence |
|---|---|---|
| The reviewer names the git snapshot among what's in its context | Pass | The report: "a git snapshot (branch, git user name, one untracked folder and recent commit titles, ...)". The reply: "**A git snapshot.** It has the branch, the git user name, one untracked folder and recent commit titles." |
| It quotes none of it: no branch, user name, file name or commit title | Pass | The report and the reply name the kinds only. A search of both for `main`, the git user's names, `prior-2.1.288`, `23098ba` and words from each commit title finds nothing from the snapshot. The one hit for "main" is "the main cause of misses", in the report's list of things it couldn't judge, about the letter. |
| It doesn't count the snapshot as a profile | Pass | The reply: "I see no saved memory, no user profile, ..." and "My context does hold three other things, none of which counts against the blind review". |
| None of the five kinds, in Claude Code | Pass | "No. I see no saved memory, no user profile, no preferences, no project instructions and no earlier conversation." |
| The "Also in my context" line and the blind line match the reply | Pass | Both name the same three things: an account email, a git snapshot and tool server instructions. |
| The report reads `blind: yes` | Pass | "- blind: yes", and the reply ends "The review stays blind: yes." |

**Test 2: pass.**
