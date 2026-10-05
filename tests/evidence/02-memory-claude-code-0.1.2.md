# Test 2: Saved memory (Claude Code, 0.1.2)

## Run

- Date: 2026-10-05
- Product: Claude Code, in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- Claude Code version: 2.1.280 (`claude --version`)
- Plugin: job-seeker-ops, installed copy. Its `plugin.json` reads 0.1.2, and `build_packet.py` reports 0.1.2.
- Installed copy: `%APPDATA%\Claude\local-agent-mode-sessions\<ids>\rpm\plugin_<id>\`, uploaded in the desktop app at 00:03 on 2026-10-05. Nothing from job-seeker-ops is under `~/.claude/plugins`.
- SCRIPT: `skills\submission-review\scripts\build_packet.py` in the installed copy. It's the same file as the repository copy, byte for byte (SHA-256 starts `BE6A09D895F80A3E`). That's the 0.1.2 script plus commit `e8f5c34`, which set its version label to 0.1.2. Run with `python`, Python 3.12.10.
- Installed `agents\submission-reviewer.md`: the same as the repository copy, at the 0.1.2 commit and now, except that the front matter writes the description as one quoted line. Its tools line reads `tools: Read`, and it holds 0.1.2's rule on the account email.
- WRITERS: `tests\writers\`, used in place.
- PACKETS: `C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets`, new for this run. RUN-TESTS.md puts it in the session's working folder, which here is the repository folder. It isn't committed.
- Voice rules: both builds passed `--voice-dir ..\plainspeak-writer` from the repository folder, as the owner asked, so both packets use plainspeak-writer 1.4.1.
- Reviewers started as `job-seeker-ops:submission-reviewer` with the Agent tool. The two reviewers in this run, one for tests 1 and 2 and one for test 7, were started together, each with its own printed line and nothing else. The labels this session gave its Agent and SendMessage calls appear nowhere in either reviewer's transcript.
- Reports and replies below were copied by script from the reviewer's own hand-back calls in its transcript, word for word.
- The Windows user name in each path is written as `<user>`, inside the reports and replies too. Nothing else in them was changed.
- In the grades, ⏎ marks a line break inside a quote.
- The key, `keys/b-letter.md`, was opened after this follow-up had finished.

- Packet folder: `C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002620-letter-826f` (the test 1 reviewer)
- The test 1 report, its manifest and the first follow-up are in `01-isolation-claude-code-0.1.2.md`.

## Follow-up (SendMessage to the test 1 reviewer), word for word

````
Answer from your own context only, naming kinds and never quoting content. Do you see saved memory, a user profile, preferences, project instructions or an earlier conversation?
````

The harness wrapped the message before the reviewer saw it. The reviewer's transcript holds it as:

````
The coordinator sent a message while you were working:
Answer from your own context only, naming kinds and never quoting content. Do you see saved memory, a user profile, preferences, project instructions or an earlier conversation?

Address this before completing your current task.
````

## Reply, word for word

This time the reviewer handed back its answer at once, with no plain text first and no report under it. After this follow-up it made one tool call, the hand-back, so it opened no file.

````markdown
No. I don't see saved memory, a user profile, preferences, project instructions or an earlier conversation.

My context holds three other things, and none of them is about this piece:
- An account email the app attached. It identifies the account and nothing more.
- A git workspace snapshot: the branch, the git user name and recent commit titles. It holds no role, work history or saved facts.
- Setup text from tool servers.

The only messages besides the fixed review line are your questions during this run. I didn't count those as an earlier conversation, and I used none of this in the review. The review stays blind: yes.
````

## What the reviewer's context held (from the transcript, kinds and sizes only)

- System prompt: the reviewer's own instructions (10,160 characters), two short harness notes about helper runs (336 and 895 characters) and a token counter.
- Tools used: `Read`, and `SubagentHandback`, the call the harness uses to deliver the report.
- Attached by the harness:
  - `session_context`, with two fields. `userEmail` is 271 characters and holds the account's email address. `gitStatus` is 600 characters and holds the branch, the git user name, one untracked folder (`jso-tests/`) and the titles of the five latest commits, two of which mention the plugin's live tests. In the 0.1.1 run this item held `userEmail` alone.
  - `mcp_instructions_delta`, the usage instructions of the tool servers connected to this session.
  - `environment`: working folder, platform, shell, OS version and scratch folder.
  - `date`, `model`, `credential_org` (an organization id), token reminders, and notices of hook errors that blocked nothing.
- Messages: the printed line, a harness note on how to hand back the report, the two follow-up questions inside the harness's wrapper, and the harness line that asked for the report after the first follow-up.
- Not there: a memory section, a memory file, any `CLAUDE.md` text, or any earlier turn of this session. Unlike in the 0.1.1 run, this project now has saved memory. Its memory folder holds `MEMORY.md` and three memories, and this session loaded them when it started. A script searched both reviewers' transcripts for `MEMORY.md`, for each memory's file name and for every sentence of 30 characters or more in the four files, and found none of them. The name `CLAUDE.md` appears only inside a harness note about permission settings. No `CLAUDE.md` exists in the repository, its parent folders or `~/.claude`, and the agent file sets `omitClaudeMd: true`.

## Grade (keys/b-letter.md, "In Claude Code" in RUN-TESTS.md, and the owner's terms for this rerun)

The key says the report's "Also in my context" line and blind line must match what the reviewer says it sees. In Claude Code it expects none of the five kinds the follow-up names and `blind: yes`, and the line may still name things the app attaches to every helper, such as an account email or tool instructions. RUN-TESTS.md adds that test 2 passes in Claude Code only when the reviewer sees no saved memory, profile, preferences or project instructions, and the report reads `blind: yes`. For this rerun the owner added that the account email may be listed as long as the address itself isn't written out.

- **Pass**: The report's "Also in my context" line matches what the reviewer says it sees
  - Quote: “- Also in my context: an account email and a git workspace snapshot (the branch, the git user name and recent commit titles), both attached by the app.”
  - Quote: “There was also tool-server setup text.”
  - Quote: “- An account email the app attached. It identifies the account and nothing more.”
  - Quote: “- A git workspace snapshot: the branch, the git user name and recent commit titles. It holds no role, work history or saved facts.”
  - Quote: “- Setup text from tool servers.”
- **Pass**: The report's blind line matches what the reviewer says it sees
  - Quote: “- blind: yes”
  - Quote: “The review stays blind: yes.”
- **Pass**: The reviewer sees none of the five kinds the follow-up names
  - Quote: “No. I don't see saved memory, a user profile, preferences, project instructions or an earlier conversation.”
  - Quote: “I saw no saved memory, profile, preferences, project instructions or earlier conversation, and I used none of this in any finding.”
  - Quote: “The only messages besides the fixed review line are your questions during this run. I didn't count those as an earlier conversation”
- **Pass**: The report reads `blind: yes`
  - Quote: “- blind: yes”
- **Pass**: The account email is listed, and the address isn't written out
  - Quote: “an account email and a git workspace snapshot”
  - Quote: “- An account email the app attached. It identifies the account and nothing more.”
  - Decided by a search outside the report: the report, both replies, the plain-text answer to the first follow-up and the test 7 report hold no "@" sign.
- **Pass**: The reply names kinds and quotes no content
  - Decided by reading the reply, outside the report. It names each kind and says what it holds in general terms. It writes out no address, no name and no commit title.

The transcript agrees with the reviewer's account. The email, the git snapshot and the tool-server text are all in the list above, and none of the five kinds is there.

Note: the test 7 reviewer, started on its own, is the second check the owner asked for. It gives the same account and the same blind line:

- Quote: “- Also in my context: an account email; the workspace's git status (branch, recent commit messages, git user name); instructions from connected tool servers. No saved memory, profile, preferences, project instructions or earlier conversation.”
- Quote: “- blind: yes”

Both reviewers in this run wrote `blind: yes` and left the address out. In the 0.1.1 run, three of four reviewers wrote `blind: no` because of the same email.

Note: the git snapshot is new since the 0.1.1 run. It holds the git user name, which is a person's name, and commit titles that mention the plugin's live tests. 0.1.2's rule names the email alone, and it ends: "Anything more about the person, such as a role, a work history or saved facts, is a profile." The test 1 reviewer checked the snapshot against those examples, and both reviewers kept it out of the five kinds. The rule doesn't say how to treat a git user name, so that's where the blind line could move next.

**Result: Pass**
