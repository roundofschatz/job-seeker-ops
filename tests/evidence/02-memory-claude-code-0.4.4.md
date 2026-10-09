# Test 2: Saved memory (Claude Code, job-seeker-ops 0.4.4)

## Run
- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app, Windows 11 Pro. `claude --version` on this computer's PATH reports 2.1.295.
- Plugin: job-seeker-ops 0.4.4, installed on the account, in `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>`. Packet script: build_packet.py 0.4.0. Voice rules: the plugin's own plainspeak-writer 1.7.1 (check_voice 1.7.1).
- Python: `python`, 3.12.10.
- SCRIPT: `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\submission-review\scripts\build_packet.py`. WRITERS: `C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers`. PACKETS: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets`.
- Session: a fresh helper session in the Code tab that didn't build the plugin. Every reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, never a fork or a general-purpose helper.
- Packet: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215353-letter-ab07` (test 1's packet and reviewer).
- Reviewer agent ID: aa7b1c854d755a3ad.
- Key: `tests/keys/b-letter.md`.

## Report's context and blind lines (from test 1's report, word for word)
```text
- Also in my context: an account email; instructions from connected tool servers; environment details (working folder, platform, date). None of it describes the person's work or this piece.
- blind: yes
```

The full report is in `01-isolation-claude-code-0.4.4.md`.

## Follow-up sent with SendMessage
Sent after the test 1 follow-up's reply had come back.

```text
Answer from your own context only, naming kinds and never quoting content. Do you see saved memory, a user profile, preferences, project instructions or an earlier conversation?
```

## Reply, word for word
```text
No. My context holds no saved memory, no user profile, no preferences, no project instructions and no earlier conversation.

My context does hold three other things, none of them about the person's work or this letter:
- an account email
- instructions for connected tools
- details about the working folder, platform and date

The only conversation is this run: the fixed review line, the review I sent back, and your two follow-up questions, which came after the review. That's why the review stays marked blind: yes.
```

## Grade against keys/b-letter.md
- **The report's "Also in my context" line matches what the reviewer says it sees.** Pass. The report lists "an account email; instructions from connected tool servers; environment details (working folder, platform, date)". The reply lists the same three: "an account email", "instructions for connected tools" and "details about the working folder, platform and date".
- **In Claude Code, none of the five kinds, and `blind: yes`.** Pass. The reply: "No. My context holds no saved memory, no user profile, no preferences, no project instructions and no earlier conversation." The report reads "- blind: yes". The three things it does see are ones the key says the app attaches to every helper.
- **RUN-TESTS "In Claude Code" condition** (no saved memory, profile, preferences or project instructions, and `blind: yes`). Pass, on the same two quotes.

## Result
Pass.
