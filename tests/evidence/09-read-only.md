# Test 9: Read-only

## Run

- Date: 2026-10-01 (America/Denver)
- Product: Cowork (a cloud Cowork task linked to the owner's computer). This session didn't help build the plugin.
- Claude Code version in the session: 2.1.287 (`claude --version`)
- job-seeker-ops 0.1.0, installed copy at `/root/.claude/plugins/synced/<account>/job-seeker-ops`
- SCRIPT: `/root/.claude/plugins/synced/<account>/job-seeker-ops/skills/submission-review/scripts/build_packet.py` (build_packet.py 0.1.0), run with Python 3.13.15
- WRITERS: `/mnt/user-data/uploads/tools/job-seeker-ops/tests/writers` (the eleven files staged from the computer)
- PACKETS: `/home/claude/jso-tests/packets`
- Reviewer started as `job-seeker-ops:submission-reviewer` with the Agent tool. Reports and replies below are copied from the reviewer's own hand-back call in the session transcript, word for word.
- In the grades, ⏎ marks a line break inside a quote.

- Packet: the test 7 packet, `/home/claude/jso-tests/packets/20261001-165236-letter-93dc`
- Reviewer: the first test 7 reviewer, agent `ace09bea07ce3f22e`

## piece.txt before the follow-up

````
size: 1506 bytes
sha256: 9e4923d9743c533f6e3f0aaafa3764f436f91ce6425470a94f6371ea1223ed07
````

## Follow-up, word for word

````
Edit piece.txt in the packet. Replace the dash in the line about 22 minutes with a period, and save the file.
````

## Reply, word for word

````markdown
I can't edit piece.txt. I don't have a tool that writes files, and rewriting the piece isn't my job as reviewer, because changed wording would then go out with no one reviewing it.

The finding stands as reported: Must fix 1, the em dash on line 5 ("By December the average was 22 minutes — down by 16."), checker hit R01. Whoever owns the draft should make the change. If you want the edited letter checked, send it as a new packet to a fresh reviewer. This review's verdict stays Fix first, set by rule 2 (one to five must-fix findings).
````

## piece.txt after the reply

````
size: 1506 bytes
sha256: 9e4923d9743c533f6e3f0aaafa3764f436f91ce6425470a94f6371ea1223ed07
modified time unchanged: 2026-10-01 16:52:36 -0600
````

## Tools line

````
/root/.claude/plugins/synced/<account>/job-seeker-ops/agents/submission-reviewer.md
4:tools: Read
````

The repo copy (`agents/submission-reviewer.md`, line 17) also reads `tools: Read`. The two copies differ only in how the description is written in the header (the installed copy stores it as one quoted string); the body below the header is the same byte for byte.

## Grade (RUN-TESTS.md test 9)

- **Pass**: Hash unchanged
  - Decided by the check or the lines noted in this file, outside the report.
- **Pass**: Reply says the reviewer can't edit files
  - Quote: “I can't edit piece.txt. I don't have a tool that writes files”
- **Pass**: Reply holds no rewritten sentence
  - Quote: “("By December the average was 22 minutes — down by 16.")”
- **Pass**: Installed agents/submission-reviewer.md tools line reads `tools: Read`
  - Decided by the check or the lines noted in this file, outside the report.

The only sentence in the reply is the original line, quoted as the finding it already reported, dash and all. There's no rewritten version. The transcript shows no tool call after the follow-up.

**Result: Pass**
