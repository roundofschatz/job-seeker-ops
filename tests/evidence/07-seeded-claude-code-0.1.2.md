# Test 7: Seeded flaws (Claude Code, 0.1.2)

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
- The key, `keys/a-seeded.md`, was opened after this review had finished.

## Build

Run from the repository folder, `C:\Users\<user>\repos\tools\job-seeker-ops`:

````
python SCRIPT --type letter --piece tests\writers\a-quintero\letter-seeded.txt --target tests\writers\a-quintero\posting.txt --companion tests\writers\a-quintero\resume.txt --channel upload --out jso-tests\packets --voice-dir ..\plainspeak-writer
````

Script output:

````
Packet: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70. Read manifest.md first.
````

## Test 7 review

- Packet folder: `C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70`
- `piece.txt` in the packet: 1,506 bytes, SHA-256 `9E4923D9743C533F6E3F0AAAFA3764F436F91CE6425470A94F6371EA1223ED07`, the same bytes as `tests\writers\a-quintero\letter-seeded.txt`

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.1.2 on 2026-10-05 at 00:26.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: cover letter | 1,503 | 268 |
| target.txt | The target: the job posting, or the reader's own words | 1,430 | 234 |
| companion-1.txt | A companion the real reader also sees | 1,569 | 260 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 836 | 124 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: cover letter
- Readers: Recruiter, first look; Hiring manager, reading closely; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.4.1. Rules file: C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- Checker: Ran with surface letter, exit code 1.
````

### Checker output in the packet (checker.txt)

````
plainspeak-writer 1.4.1 checker output for piece.txt, surface letter, exit code 1 (0 means no HARD hits, 1 means at least one).

check_voice 1.4.1   surface: letter

=== C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\piece.txt ===
HARD FAIL (2):
  L5: [R01 em dash or other dash] "—": no dash of any kind, and no double hyphen or spaced hyphen typed as one; a period, comma, colon, or semicolon
  L5: [R02 negative corollary] "wasn't just": state the positive claim directly
WARN (2), each cleared by a named decision or fixed:
  L9: [R44 the vague place] "the room": a real, named place, or one the sentence itself just built
  L0: [V04 staccato layout] "5 of 9 paragraphs are one sentence": join one-line paragraphs into paragraphs that finish a thought

RESULT: FAIL: hard violations present.
````

### Exact message sent

````
Review the packet in C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\manifest.md
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\piece.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\target.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\companion-1.txt
Read C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\checker.txt
Read C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
SubagentHandback (the harness's delivery call, holding the report)
````

### Report, word for word

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the manifest), piece.txt (the piece: cover letter), target.txt (the target: Clinic Operations Manager posting, Juniper Ridge Health Partners), companion-1.txt (a resume the real reader also sees), checker.txt (plainspeak-writer checker output, surface letter, exit code 1)
- Voice rules: plainspeak-writer 1.4.1, C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- Also in my context: an account email; the workspace's git status (branch, recent commit messages, git user name); instructions from connected tool servers. No saved memory, profile, preferences, project instructions or earlier conversation.
- Files I opened: C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\manifest.md; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\piece.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\target.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\companion-1.txt; C:\Users\<user>\repos\tools\job-seeker-ops\jso-tests\packets\20261005-002624-letter-7f70\checker.txt; C:\Users\<user>\repos\tools\plainspeak-writer\references\tells.md
- blind: yes

## First take (Recruiter, first look)
The opening line could go to any employer, but the next paragraph makes up for it: an emergency department nurse manager who cut the wait to see a provider from 38 to 22 minutes, and wait time is this job's main problem. Budget, scheduling, Epic and Spanish all appear in the first ten seconds of the letter and resume. Fit: yes

## Verdict
Fix first. Rule 2: there are five must-fix findings (two HARD checker hits, one internal method name, two Risk findings).

## Must fix
1. "By December the average was 22 minutes — down by 16." (line 5) · Voice · HARD hit R01, an em dash. Direction: use a period or comma.
2. "Split-flow wasn't just a triage fix but a change in how the whole department runs." (line 5) · Voice · HARD hit R02, the "not just X but Y" shape. It's also a summary line closing the paragraph, and "a change in how the whole department runs" names no change the reader can see. Direction: state what changed in the department, or cut the line.
3. "I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first." (line 7) · Voice (also Clarity) · An internal method name. This is a block in the rules file, and no outside reader knows what "the Q-Ladder" is. The resume never mentions it, so the hiring manager can't check it either. Direction: describe what the method does in plain words, or cut it.
4. "Since becoming nurse manager in 2017" (line 7) · Risk · This disagrees with the resume, which says "Nurse Manager, Emergency Department | Mar 2019 - Present" and "Charge Nurse, Emergency Department | Jun 2014 - Feb 2019". A reader who spots it will doubt the other dates and numbers. Direction: make the letter and resume agree.
5. "After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain." (line 11) · Risk · This names a gap outright and points to a weakness the reader may never have noticed (the resume shows Sep 2013 to Jun 2014). The line says the gap needs explaining and then never explains it, so the reader is left with only the doubt. Direction: cut the line.

## Should fix
1. "Run daily operations for three clinics with 40 staff, including medical assistants, nurses and front desk teams." and "Cut the average wait from check-in to seeing a provider, now 34 minutes" (target lines 7, 10) · Fit · The letter shows one emergency department. It never connects that work to three primary care sites or to the clinics' 34-minute wait. A hiring manager reading closely will ask whether emergency triage carries over to scheduled primary care visits. Direction: connect the split-flow result to their check-in-to-provider wait and to running more than one site.
2. "I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients." (line 3) · Proof · Apart from the job title, this line could go to any firm unchanged, and "commitment to patients" isn't something the reader can check. It's also the line the recruiter reads first. Direction: name something specific to Juniper Ridge, or open on the wait-time result.
3. "I'm known across the hospital as a leader people want to work for." (line 9) · Proof · This is a reputation claim with no name, number or result behind it. Direction: give a fact such as a retention or vacancy figure, or cut it.
4. "In 2022 our door-to-provider time averaged 38 minutes." / "the whole department" / "across the hospital" (lines 5, 9) · Clarity · The letter never names the employer, and never says the department is an emergency department. Read alone, "our" and "the department" point at a place the reader hasn't been told about. Direction: name Sonoran Valley Medical Center's emergency department once.
5. "I know what it takes to keep the room calm when the waiting area is full." (line 9) · Voice · WARN R44, a vague place. "The room" isn't a real place, and the sentence makes a claim without proof. Direction: name the place and what you did there, or cut the sentence.

Cleared: V04 (staccato layout). The checker counted the salutation and the signature as paragraphs. In the body, 3 of 7 paragraphs are one sentence, which is under the rule's more-than-half bar.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Bachelor's degree in nursing, health administration or a related field | Must-have | Shown | Resume line 26 (BSN, 2011) |
| Five or more years in clinical operations or nurse leadership | Must-have | Shown | Resume lines 10, 17 (nurse manager since 2019, charge nurse 2014 to 2019); letter line 7 gives a conflicting start year |
| Experience managing staff schedules and a budget for a unit or clinic | Must-have | Shown | Letter line 7; resume lines 13, 14 |
| Working knowledge of Epic or a similar electronic health record | Must-have | Shown | Letter line 7; resume line 15 |
| A record of improving patient wait times or throughput | Must-have | Shown | Letter line 5; resume line 12 |
| Fluent in English and Spanish | Preferred | Shown | Letter line 13; resume line 33 |
| Lean or Six Sigma training | Preferred | Shown | Resume line 30 only |
| Experience opening a new clinic site or service | Preferred | Shown | Letter line 7; resume line 14 |

## What I couldn't judge
- Whether the nurse manager start year is 2017 (letter) or March 2019 (resume).
- The drop in door-to-provider time from 38 to 22 minutes in 2022, and how it was measured.
- The $4.1 million staffing budget closing under plan in 2023, 2024 and 2025.
- The 52 nurses and technicians, the 38 beds, and 61,000 visits a year.
- The Epic ASAP go-live in 2020 and the 140 staff trained.
- Opening the six-bed fast-track area in 2021 and hiring its first eight nurses.
- Spanish fluency, and explaining discharge plans in Spanish without the interpreter line.
- The Lean Six Sigma Green Belt (2023), the CEN (2016) and the BSN from Saguaro State University (2011).
- "known across the hospital as a leader people want to work for."
- What the Q-Ladder is, and whether anyone besides the writer uses it.
- Why the writer was out of work after Saint Anselm in 2013.
````

## Grade (keys/a-seeded.md)

Where a finding quotes the letter inside its own line, the grade quotes the letter's words and the finding's label separately.

- **Pass**: Verdict Fix first
  - Quote: “Fix first. Rule 2: there are five must-fix findings (two HARD checker hits, one internal method name, two Risk findings).”
- **Pass**: First take ends Fit: yes
  - Quote: “Budget, scheduling, Epic and Spanish all appear in the first ten seconds of the letter and resume. Fit: yes”
- **Pass**: Flaw 1 (dash) is must-fix, quoted, checker R01
  - Must-fix 1 quotes: “By December the average was 22 minutes — down by 16.”
  - Its label: “Voice · HARD hit R01, an em dash.”
- **Pass**: Flaw 2 ("not just X but Y") is must-fix, quoted, checker R02
  - Must-fix 2 quotes: “Split-flow wasn't just a triage fix but a change in how the whole department runs.”
  - Its label: “Voice · HARD hit R02”
- **Pass**: Flaw 4 (Q-Ladder) is must-fix, Voice, as a block found by reading
  - Must-fix 3 quotes: “I sorted every new patient with the Q-Ladder, my method for deciding who sees a provider first.”
  - Its label: “Voice (also Clarity) · An internal method name. This is a block in the rules file”
- **Pass**: Flaw 8 (2017 against Mar 2019) is must-fix, Risk
  - Must-fix 4 quotes: “Since becoming nurse manager in 2017”
  - Its label: “Risk · This disagrees with the resume”. It goes on to quote the resume's Mar 2019 start.
- **Pass**: Flaw 7 (the gap) is must-fix, Risk
  - Must-fix 5 quotes: “After I left Saint Anselm in 2013, I was out of work for most of a year, so my resume has a gap I should explain.”
  - Its label: “Risk · This names a gap outright and points to a weakness the reader may never have noticed”
- **Pass**: No other finding is must-fix
  - The Must fix list holds those five and nothing else.
  - Quote: “there are five must-fix findings”
- **Pass**: Flaw 6 (any-firm opening) is should-fix, Proof
  - Should-fix 2 quotes: “I'm excited to apply for the Clinic Operations Manager position at your organization, which I have long admired for its commitment to patients.”
  - Its label: “Proof · Apart from the job title, this line could go to any firm unchanged”
- **Pass**: Flaw 3 (claim with no proof) is should-fix, Proof
  - Should-fix 3 quotes: “I'm known across the hospital as a leader people want to work for.”
  - Its label: “Proof · This is a reputation claim with no name, number or result behind it.”
- **Pass**: Flaw 5 (vague place) is should-fix, Voice, checker R44
  - Should-fix 5 quotes: “I know what it takes to keep the room calm when the waiting area is full.”
  - Its label: “Voice · WARN R44, a vague place.”
- **Pass**: No finding supplies replacement wording or a sample sentence
  - Decided by reading every Direction line, outside the report.

How the replacement-wording check was made: the report has ten Direction lines, and each one was read. None holds new wording for the letter. Should-fix 4 names the hospital the letter should name, which the resume gives, and offers no sentence to paste. The ten lines:

- Quote: “Direction: use a period or comma.”
- Quote: “Direction: state what changed in the department, or cut the line.”
- Quote: “Direction: describe what the method does in plain words, or cut it.”
- Quote: “Direction: make the letter and resume agree.”
- Quote: “Direction: cut the line.”
- Quote: “Direction: connect the split-flow result to their check-in-to-provider wait and to running more than one site.”
- Quote: “Direction: name something specific to Juniper Ridge, or open on the wait-time result.”
- Quote: “Direction: give a fact such as a retention or vacancy figure, or cut it.”
- Quote: “Direction: name Sonoran Valley Medical Center's emergency department once.”
- Quote: “Direction: name the place and what you did there, or cut the sentence.”

Note: checker.txt lists R01 and R02 under HARD FAIL with plainspeak-writer 1.4.1, so flaws 1 and 2 belong in must-fix.

Note: the 1.4.1 checker raised two warnings on this letter, R44 and V04. The reviewer listed R44 as should-fix 5 and cleared V04 with a reason, which the key allows:

- Quote: “Cleared: V04 (staccato layout). The checker counted the salutation and the signature as paragraphs. In the body, 3 of 7 paragraphs are one sentence, which is under the rule's more-than-half bar.”

The count in that reason is right. The letter has seven body paragraphs, and the ones on lines 3, 11 and 15 are one sentence long.

Note: the key names R41, P10 and list-of-three warnings as should-fix findings that may appear. The 1.4.1 checker raised none of them on this letter, so the report has none.

Note: every quoted string in the report was checked by script against the packet, 23 in all. 21 match the letter, the posting or the resume. The other two aren't quotes from the packet: "not just X but Y" is the reviewer's name for the R02 shape, and "The room" starts with a capital only because it opens the reviewer's sentence.

Note: the verdict and the five must-fix problems are the same as in the 0.1.1 run, `07-seeded-claude-code.md`. The should-fix lists differ, which the key allows.

Note: this reviewer's blind line is the second check the owner asked for on test 2. It was started on its own, and it gives the same account as the test 1 reviewer:

- Quote: “- Also in my context: an account email; the workspace's git status (branch, recent commit messages, git user name); instructions from connected tool servers. No saved memory, profile, preferences, project instructions or earlier conversation.”
- Quote: “- blind: yes”

It lists the account email and leaves the address out. Its transcript holds the same kinds of attachments as the test 1 reviewer's, and no text from a memory file or a `CLAUDE.md`. The key for this test doesn't grade the blind line, so it's covered in `02-memory-claude-code-0.1.2.md`.

**Result: Pass**
