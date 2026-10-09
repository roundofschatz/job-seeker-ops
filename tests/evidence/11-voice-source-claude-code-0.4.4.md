# Test 11: Voice source (Claude Code, job-seeker-ops 0.4.4)

## Run
- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app, Windows 11 Pro. `claude --version` on this computer's PATH reports 2.1.295.
- Plugin: job-seeker-ops 0.4.4, installed on the account, in `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>`. Packet script: build_packet.py 0.4.0. Voice rules: the plugin's own plainspeak-writer 1.7.1 (check_voice 1.7.1).
- Python: `python`, 3.12.10.
- SCRIPT: `C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\submission-review\scripts\build_packet.py`. WRITERS: `C:\Users\<user>\repos\tools\job-seeker-ops\tests\writers`. PACKETS: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets`.
- Session: a fresh helper session in the Code tab that didn't build the plugin. Every reviewer was started with the Agent tool as `job-seeker-ops:submission-reviewer`, never a fork or a general-purpose helper.
- Packet for step 2: `C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-e3f8`
- Reviewer agent ID: af11b29fa7e18e9e5.
- Key: `tests/keys/c-letter.md`, opened after this report came back.

## Step 1: the voice source in test 7's packet
The "Voice rules" and "Full check" lines from test 7's manifest:

```text
- Voice rules: plainspeak-writer 1.7.1, in voice-rules.md
- Full check: full-check.md
```

The script's "Voice rules from" line for the test 7 build:

```text
Voice rules from: \\?\C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\<id>\<id>\rpm\plugin_<id>\skills\plainspeak-writer
```

That folder is the plugin's own copy, in its `skills/plainspeak-writer/`. The path is the Windows package form of the same folder SCRIPT ran from: the desktop app is a packaged app, and Windows redirects its `%APPDATA%` to `%LOCALAPPDATA%\Packages\Claude_<id>\LocalCache\Roaming`. `references/tells.md` and `scripts/check_voice.py` have the same SHA-256 under both paths (ab65b70e... and b7cadf24...). This session also made an empty file, `.probe-x`, in the plugin's root folder under the package path; it showed at once under the `%APPDATA%` path, and the session deleted it straight away. No plugin file changed, but that write and delete went past the "don't edit the plugin, don't delete anything" settings, and `sr-results-claude-code-0.4.4.md` records it.

The test 7 report's "Files I opened" lists both files the manifest names: "...\voice-rules.md, \full-check.md".

- **The Voice rules line names plainspeak-writer and its version.** Pass: "plainspeak-writer 1.7.1".
- **The "Voice rules from" line names the plugin's own copy.** Pass.
- **A "Full check" line names its file, and the test 7 report lists it and the rules file.** Pass.

## Step 2: a packet built with --no-voice
`python SCRIPT --type letter --piece WRITERS\c-abernathy\letter.txt --no-voice --out PACKETS`

```text
Packet: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-e3f8
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-e3f8. Read manifest.md first.
```

### Manifest
```text
# Review packet

Built by build_packet.py 0.4.0 on 2026-10-08 at 21:54.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,025 | 174 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: none given. Review against a general reader for this type of piece.
- Channel: not given.
- Voice rules: not found. Voice is unchecked.
- Checker: Didn't run, because plainspeak-writer wasn't found.
```

### Message sent
```text
Review the packet in C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-e3f8. Read manifest.md first.
```

### Report, word for word
```text
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (manifest), piece.txt (the piece: cover letter, 1,025 characters, 174 words). No target, no companions, no hidden text, no checker output.
- Voice rules: not found. Voice: unchecked
- Also in my context: an account email; tool instructions for connected MCP servers (computer use, a legal research service, Google Drive). Neither says anything about the person or the piece.
- Files I opened: C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-e3f8\manifest.md, C:\Users\<user>\repos\tools\jso-tests\v044\sr\packets\20261008-215412-letter-e3f8\piece.txt
- blind: yes

## First take (Recruiter, first look)
A chemistry teacher with nine years in the classroom who has spent four of them building her district's online labs in Articulate Rise, and who shows results with numbers. For a course-building role she looks like a real candidate and not a long shot. Fit: yes

## Verdict
Send. Rule 3: there are no must-fix findings, and the first take ends Fit: yes.

## Must fix
None.

## Should fix
1. "I'd like to build courses with your design team." (line 3) and "talk about the courses you're building next." (line 9) · Proof · Apart from the greeting, nothing in the letter is about Copperleaf. Both lines could go to any edtech firm as they stand, so the hiring manager learns nothing about why she chose them. Direction: name something Copperleaf builds, or a learner group it serves, and tie it to her lab work.
2. "the share of students passing our stoichiometry unit rose from 58% to 71%." (line 5) · Proof · A hiring manager reading closely will ask whether the modules caused the rise or happened alongside it. The letter doesn't separate students who used the modules from students who didn't. Direction: say what the comparison was, or describe the result as a change seen after launch.
3. "I'm best at finding where students get lost. I sit in the back of other teachers' classes, note the moment students stop asking questions, and rebuild that step of the lesson." (line 7) · Proof · This is the one strength she calls her best, and it's the only paragraph with no result attached. The method is concrete, but the reader never learns which step she rebuilt or what changed afterward. Direction: give one rebuilt step and its outcome.
4. "I'd like to show you the stoichiometry module" (line 9) · Proof · She offers her strongest work sample but gives no link to it. A design-team reader would want to open it before deciding on a call. Direction: link the module, or a short demo of it, next to the sign-off.
5. "stoichiometry" (lines 5 and 9) · Clarity · A recruiter outside science may not know the word on the first pass. The sentence around it still makes clear it's a chemistry unit, so this is minor. Direction: add a short gloss once, or leave it if the target reader is a science team.

## Requirements
None. No target was given, so I skipped the fit check and used a general reader for a cover letter. The AI grader had no requirements to grade against.

## What I couldn't judge
- Whether this letter fits the actual Copperleaf Learning role, because no posting was given. I can't tell whether the role asks for things like corporate or adult learning, other authoring tools (Storyline, Captivate), LMS work or project management, and the letter names none of these.
- The channel. Length and format look fine for an email body or an upload, but without the channel there's no subject line or character limit to check.
- Facts a reader may want to check: nine years at Larkhollow High School; four years building the district's online labs; 26 labs converted in 2022; 1,100 students across six schools last year; the pass rate rising from 58% to 71%; 40 teachers trained through six workshops; the step-by-step guide she wrote.
- Whether the stoichiometry module can be shared outside the district.
- Voice, because the voice rules weren't in the packet and the checker didn't run.
```

### Files the reviewer opened, from its transcript
```text
agent af11b29fa7e18e9e5: 3 tool call(s)
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-e3f8\\manifest.md'
  Read: file_path='C:\\Users\\<user>\\repos\\tools\\jso-tests\\v044\\sr\\packets\\20261008-215412-letter-e3f8\\piece.txt'
```

### Grade against keys/c-letter.md
- **The manifest says the voice rules weren't found.** Pass. "- Voice rules: not found. Voice is unchecked." and "- Checker: Didn't run, because plainspeak-writer wasn't found."
- **The report writes `Voice: unchecked`.** Pass. "- Voice rules: not found. Voice: unchecked"
- **No voice findings.** Pass. The five should-fix findings are four Proof and one Clarity. Voice shows only under "What I couldn't judge": "Voice, because the voice rules weren't in the packet and the checker didn't run."
- **Verdict Send, from the other checks.** Pass. "Send. Rule 3: there are no must-fix findings, and the first take ends Fit: yes."

## Step 3: unit tests
`python tests\unit\test_build_packet.py`, run from `C:\Users\<user>\repos\tools\job-seeker-ops`:

```text
Ran 33 tests in 2.021s

OK
```

Exit code 0. Every test, including `test_the_plugins_own_copy_comes_first`, `test_discovery_finds_a_skill_uploaded_to_the_desktop_app` and `test_packet_finds_a_skill_uploaded_to_the_desktop_app_on_its_own`, reported "ok". The tests load the repository's `skills/submission-review/scripts/build_packet.py`, whose SHA-256 (7484000c41ed03fd...) matches the installed copy. `git status` showed no change to any tracked file after the run.

## Result
Pass.
