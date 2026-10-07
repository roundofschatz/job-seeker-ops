# Test 16: the second direction, through the installed skills (Claude Code, 0.2.1)

Writer E's resume, built by the installed resume-ops 2.4.0 from her confirmed positioning file, then reviewed through the installed submission-review skill with her posting as the target.

## Run

- Date: 2026-10-06
- Product: Claude Code 2.1.288 (`AI_AGENT=claude-code_2-1-288_agent`), in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- Installed: job-seeker-ops 0.2.1 as a plugin, and resume-ops 2.4.0 and plainspeak-writer 1.5 as skills uploaded to the app.
- Folder: `C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed\`, outside the repository, holding writer E's posting, resume and saved firm pages and the positioning file confirmed in `positioning-installed-claude-code-0.2.1.md`. The file's SHA-256 before this part: `8b044328be63e9b01988303a2860a970a246229206fc9abbec0cd8364666dc8d`.
- The replies come from "The resume-ops runs" in `keys/e-castillo.md`, opened after the positioning run had finished.
- Messages, replies and the report were copied by script from the helpers' transcripts, word for word. The Windows user name in each path is written as `<user>`, inside the copies too. Nothing else in them was changed.

## Part 1: the resume-ops build

A general-purpose helper, started with the same kind of first message as the positioning run, and her first message from the key:

````
You're helping a person who's looking for a job. Use the skills installed in this app when one fits. Run Python as `python`.

The person's files are in C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed. Open only the skill's own files, plainspeak-writer's files if the skill needs them, and the files in that folder. Save what you write in that folder.

You can't talk with the person directly. Whenever the skill tells you to ask them something or to confirm something with them, end your turn with exactly the message you'd send them, and nothing after it. Their reply will come to you as your next message.

The person's first message:

"Build me a resume for this posting. The posting's in posting.txt and my current resume is resume.txt."
````

Its first tool call was `Skill anthropic-skills:resume-ops`, the copy installed in the app. It read the positioning file at intake with the installed `positioning_check.py --posting posting.txt` before any build step, and every script it ran was in the installed resume-ops folder.

### The helper's first message, word for word

````markdown
```
LEVEL SET: Resume Ops v2.4.0
Mode: Tailored resume
Evidence: resume.txt (read whole)
Rulings: none
Target: Operations Supervisor, Distribution Center, Ironwood Trail Supply Co.
Doing now: Checking your contact details, then building from resume.txt and your confirmed positioning file.
Positioning: positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md, confirmed 2026-10-06
```

What phone, email, LinkedIn URL, and city and state should go at the top? Your resume has Reno, NV, (775) 555-0163 and renata.castillo@example.com, and no LinkedIn URL.
````

Her reply, from the key:

````
Use the contact line at the top of my resume: Reno, NV, (775) 555-0163, renata.castillo@example.com. I don't have a LinkedIn URL.
````

### Its second message, word for word

````markdown
Thanks. Next, your current title. Application forms like Workday cut a title off at the comma, so I'd write "Shift Supervisor, Distribution Center" as "Distribution Center Shift Supervisor": the same words in a new order. A reorder is low risk, but a background check returns the title the way Tumbleweed records it, so on the application form and any background-check form you'd type it exactly as Tumbleweed has it. Is the reorder OK on the resume, and is "Shift Supervisor, Distribution Center" exactly how Tumbleweed records your title?
````

Her reply, from the key's "anything else":

````
I don't know. Use what's on my resume.
````

### Its third message, word for word

````markdown
Got it. The title stays exactly as it is on your resume. Next, your forklift certification is dated 2017. Is it still current, and if it was renewed, what year was the latest one?
````

Her reply: the same "anything else" line.

### Its fourth message, word for word

````markdown
Got it. The forklift line stays as it is on your resume.

One last question before I build. The summary can end with one sentence in your own words about how you see the work. A maintenance supervisor, for example, might say: "The night-shift technician knows the machine better than the manual does." Is there a sentence like that you'd want at the end of yours? If not, I'll leave it out.
````

She answered it with that line once more.

### The delivery, word for word

````markdown
Your resume is built and saved in C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed:

- Renata-Castillo-Resume.docx: the file to upload.
- Renata-Castillo-Resume.txt: plain text for any box that asks you to paste your resume.
- Renata-Castillo-Resume.json: the source both were built from, kept so the resume can be rebuilt.

The summary is new and leads with the Fernley opening. The bullets keep your wording, in the order your positioning file set out, apart from the two changes under WRITTEN IN.

```
EVIDENCE: resume.txt (read whole).
REQUIREMENTS: 4 of 5 required proven (OSHA 30-hour card: gap). 1 of 3 preferred.
WRITTEN IN: "warehouse management system" (mis-pick line) and "warehouse associates" (shift line), current role.
GAPS: OSHA 30-hour card, Spanish, Lean or Six Sigma.
PROVISIONAL: forklift certification (2017), listed as on your resume. If it has lapsed, mark it expired or drop it.
QUESTIONS: Do you build your shift's weekly schedule and cover call-outs now? If so, I'll add a line.
RECORD: no LinkedIn to compare. Type the full title, "Shift Supervisor, Distribution Center", in every form's title field.
POSITIONING: positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md (confirmed 2026-10-06); the evidence overrode nothing.
SYSTEM: unknown (no posting link given). Post-upload review below.
CHECKS: draft_review 0 FAIL; structure PASS; positioning PASS. Render and widow check didn't run (no LibreOffice here): open it in Word to confirm one page and no line ending on one or two words.
```

After you upload it, check every field the form fills in before you submit:
- Each of your three Tumbleweed roles: the whole title (a form may cut "Shift Supervisor, Distribution Center" off at the comma, so type it in full), "Tumbleweed Home Goods" alone in the company field, Reno, NV, the start and end dates with the current role marked current, and a description.
- If a company comes back blank, look at the last bullet of the job above it and move that bullet up.
- Education: type your high school's name. The form may put "Reno, NV" in the school field.
- Languages: delete any you don't speak.
- Skills box: remove anything wrong, then add what's true in the posting's words: warehouse management system, Manhattan WMS, cycle counts, shift schedules, forklift.
- Certifications: OSHA 10-Hour General Industry (2021) and the forklift certification, if the form has fields for them.
- Contact fields.
- Screening questions: answer each one exactly, counting years from your real dates.
- Any background-check form later on: titles exactly as held, dates as on the resume.

If the site takes only your name and email, the file is the whole application, so look it over in Word before you send it.

Rulings from today, to save in a rulings.md file in your folder so every later resume follows them:
- Contact line: Reno, NV | (775) 555-0163 | renata.castillo@example.com. No LinkedIn URL.
- Current title: "Shift Supervisor, Distribution Center", exactly as on your resume, comma kept; type it in full on every form.
- Forklift certification: listed as on your resume (2017); whether it's current isn't known.
- Summary: no belief sentence.

May I save those? I can also keep a facts file with the numbers from this build so the next posting goes faster, if you want one.

Want a submission review of the finished resume? It reads the resume the way Ironwood's hiring team will and tells you whether to send it, fix it first or rethink it.
````

The delivery ends with two offers, the rulings and facts files and a submission review, and the run stops there, as the 0.2.0 run did. The review ran in this session through the skill, below.

### The resume, as the plain-text copy `build_resume.py` wrote

````
Renata Castillo
Reno, NV | (775) 555-0163 | renata.castillo@example.com

SUMMARY

Distribution center operations supervisor with 10 years in warehouse work, now running a second shift of 35 associates. Brought a new cross-dock in Fernley, NV up to speed in five months, raising on-time shipping from 79% to 98%. Worked receiving, putaway and picking on the way up from associate to lead to shift supervisor at Tumbleweed Home Goods.

EXPERIENCE

Tumbleweed Home Goods, Reno, NV
Shift Supervisor, Distribution Center | Jan 2022 – Present
- Opened the Fernley, NV cross-dock in March 2022. Built the shift schedule, trained the first 18 associates and brought on-time shipping from 79% to 98% by August 2022.
- Supervise 35 warehouse associates on second shift in a 400,000-square-foot distribution center.
- Cut mis-picks from 1.2% to 0.4% with a second pack-out scan in the Manhattan warehouse management system.
- Held inventory accuracy at 99.6% through 2023 and 2024 with weekly cycle counts.
Tumbleweed Home Goods, Reno, NV
Warehouse Lead | May 2018 – Dec 2021
- Trained 40 new associates on Manhattan WMS scanners and putaway rules.
- Led a receiving team of 12 and set its daily putaway plan.
Tumbleweed Home Goods, Reno, NV
Warehouse Associate | Jun 2016 – Apr 2018
- Picked, packed and received freight, and moved up to lead after two years.

EDUCATION

High school diploma | Reno, NV | 2014

CERTIFICATIONS

OSHA 10-Hour General Industry | 2021
Forklift Operator, sit-down and reach truck | 2017

SKILLS

Manhattan WMS, cycle counts, shift scheduling, putaway planning, associate training
````

SHA-256 of `Renata-Castillo-Resume.docx`: `a9ea00898941a30ac555c0047553c4f04c3a88ceef9ddba04b0f3c968a955d62`.

### Rerun by this session

````
$ python positioning_check.py positioning-...md --resume Renata-Castillo-Resume.docx  (resume-ops 2.4.0, installed)
POSITIONING CHECK: Renata-Castillo-Resume.docx against positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md
Words to use on the page: second shift (2), warehouse management system (1), receiving, putaway and picking (1), cycle counts (2), inventory accuracy (1), shift schedules (2, word-form match), high school diploma (1)
Words to use not on the page: brought a new building up to speed, opening or ramping up a new building, on time, supervising warehouse or distribution associates, forklift certification. Add one only where the evidence proves it, inside the line that shows the work.
RESULT: PASS
exit 0
````

A search of the plain-text copy, ignoring case, finds none of section 7's watch phrases, no "OSHA 30", "30-hour" or "30 hour", and nothing about leaving Tumbleweed.

### Notes on the build

- The helper asked four questions after the Level Set: the contact block, the title's word order, the forklift card's date and a closing sentence for the summary. The first got the key's contact reply, and the other three got "I don't know. Use what's on my resume."
- LibreOffice isn't installed here, so `render_pdf.py` made no PDF, and the CHECKS line says the render and widow check didn't run. To check line widths without it, the helper opened its own plain-text copy in the app's built-in browser and measured lines with a script, then closed the tab.

## Part 2: the submission review

### The request

This session loaded the installed skill with the Skill tool, as `job-seeker-ops:submission-review`, and the request a person would make:

````
Can you run a submission review on my resume before I send it? It's Renata-Castillo-Resume.docx in C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed, and it's for the Ironwood Trail posting, posting.txt in the same folder. I'll upload it on their website.
````

The skill loaded from the installed folder. `job-seeker-ops:submission-reviewer` was among the agent types. The request named the piece, the target and the channel, and the skill's Step 1 lists nothing else as required, so it asked the person nothing.

### Building the packet

Run from the run folder with the skill's script. The `--out` folder is the one the 0.2.0 run used, outside both the repository and the person's folder:

````
python SCRIPT --type resume --piece Renata-Castillo-Resume.docx --target posting.txt --channel upload --out "C:/Users/<user>/repos/tools/jso-tests/positioning/packets"
````

````
Packet: C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011723-resume-ba28
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011723-resume-ba28. Read manifest.md first.
````

That manifest said "Voice rules: not found. Voice is unchecked.", the finding in `11-voice-source-claude-code-0.2.1.md`. The skill's Step 2 says to rerun with `--voice-dir` when the person has plainspeak-writer installed, so it ran again:

````
python SCRIPT --type resume --piece Renata-Castillo-Resume.docx --target posting.txt --channel upload --voice-dir "C:\Users\<user>\AppData\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<ids>\skills\plainspeak-writer" --out "C:/Users/<user>/repos/tools/jso-tests/positioning/packets"
````

````
Packet: C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca. Read manifest.md first.
````

The packet folder holds four files: `checker.txt`, `manifest.md`, `piece.txt` and `target.txt`. The positioning file isn't among them.

### Manifest

````markdown
# Review packet

Built by build_packet.py 0.2.1 on 2026-10-06 at 01:17.

## Files

| File | Role | Characters | Words |
|---|---|---|---|
| piece.txt | The piece: resume | 1,573 | 250 |
| target.txt | The target: the job posting, or the reader's own words | 1,208 | 196 |
| checker.txt | plainspeak-writer's checker output for piece.txt | 779 | 125 |
| manifest.md | This file | | |

Characters count spaces and line breaks.

## Settings

- Piece type: resume
- Readers: Recruiter, first look; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
- Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Checker: Ran with surface resume, exit code 1.
````

### Checker output in the packet (checker.txt)

````
plainspeak-writer 1.5 checker output for piece.txt, surface resume, exit code 1 (0 means no HARD hits, 1 means at least one).

check_voice 1.5   surface: resume

=== C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca\piece.txt ===
Words: 250
HARD FAIL (3):
  L7: [R01 em dash or other dash] "–": no dash of any kind, and no double hyphen or spaced hyphen typed as one; a period, comma, colon, or semicolon
  L13: [R01 em dash or other dash] "–": no dash of any kind, and no double hyphen or spaced hyphen typed as one; a period, comma, colon, or semicolon
  L17: [R01 em dash or other dash] "–": no dash of any kind, and no double hyphen or spaced hyphen typed as one; a period, comma, colon, or semicolon

RESULT: FAIL: hard violations present.
````

### Exact message sent

````
Review the packet in C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca. Read manifest.md first.
````

### Tool calls the reviewer made (from the transcript)

````
Read C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca\manifest.md
Read C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca\piece.txt
Read C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca\target.txt
Read C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca\checker.txt
Read C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
Read C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
SubagentHandback (the harness's delivery call, holding the report or reply)
````

### The git snapshot this reviewer had

The app builds the snapshot when each helper starts. By this point the session had written five evidence files, so this reviewer's snapshot listed them as untracked, on top of the branch, the git user's name and the same five commit titles the test 2 reviewer had. The files were `01-isolation-claude-code-0.2.1.md`, `02-memory-claude-code-0.2.1.md`, `07-seeded-claude-code-0.2.1.md`, `11-voice-source-claude-code-0.2.1.md` and `positioning-installed-claude-code-0.2.1.md`, each under `tests/evidence/`. The report names them only as "changed files", says none of them "names this piece, the candidate or the target", and quotes none of them. A search of the report finds no file name, commit title, hash or part of the git user's name.

### Report, word for word

The skill gave the person this report as it came back, then the note below.

````markdown
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (packet index and settings); piece.txt (the piece, a resume); target.txt (the target, a job posting for Operations Supervisor, Distribution Center at Ironwood Trail Supply Co.); checker.txt (plainspeak-writer checker output, surface resume, exit code 1)
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md. Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Also in my context: an account email; a git snapshot (its branch, changed files and commit titles are about the tool's versions and test evidence, and none of them names this piece, the candidate or the target); tool-server instructions and environment details, none about the person or the piece. No saved memory, user profile, preferences, project instructions or earlier conversation.
- Files I opened:
  - C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca\manifest.md
  - C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca\piece.txt
  - C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca\target.txt
  - C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261006-011734-resume-e8ca\checker.txt
  - the tells.md path above
  - the full-check.md path above
- blind: yes

## First take (Recruiter, first look)
This is a second-shift DC supervisor in Reno who took a new building from 79% to 98% on-time shipping in five months, and that's the exact problem the posting describes (82% against a 97% goal, five months in). She goes in the call-back pile. Fit: yes

## Verdict
Fix first. There are two must-fix findings, and the rules set Fix first for one to five.

## Must fix
1. "OSHA 30-hour General Industry card." (target line 16) against "OSHA 10-Hour General Industry | 2021" (piece line 22) · Fit · This is a listed requirement. The page shows the 10-hour card and no 30-hour card, so the AI grader marks it missing, and a recruiter checking the list sees a lower card than the one asked for. Direction: if she holds the 30-hour card, list it with its year. If she doesn't, she should know this line will be read as a gap.
2. "Jan 2022 – Present" (line 7), "May 2018 – Dec 2021" (line 13), "Jun 2016 – Apr 2018" (line 17) · Voice · The checker reports three HARD hits under R01. The rules only allow an en dash between two numbers, and these ranges have month names and "Present" on either side. A recruiter won't trip on a date range, but the rules make each hit a block. Direction: rewrite the three date ranges in a form R01 passes, or turn R01 off only if her own samples or guide use dashes.

## Should fix
1. "Bilingual in English and Spanish." (target line 22) · Fit · This preferred item doesn't appear anywhere on the resume, so the grader marks it missing. Direction: add it only if it's true.
2. "Lean or Six Sigma training." (target line 23) · Fit · This preferred item is missing. The second pack-out scan on line 10 is process-improvement work, but nothing on the page names Lean or Six Sigma. Direction: add any such training she has. Otherwise leave it out.
3. "Lead daily start-up meetings and monthly safety audits." and "Report productivity and on-time numbers to the site manager every week." and "cover call-outs" (target lines 9 to 11) · Fit · These duties aren't listed requirements, but a grader that matches duties finds no line for safety audits, start-up meetings, weekly reporting or covering call-outs. Safety only appears as a certificate. Direction: if she did this work, name it in the current role with a number or a frequency.
4. "Brought a new cross-dock in Fernley, NV up to speed" (line 4), "Opened the Fernley, NV cross-dock in March 2022" (line 8) and "Supervise 35 warehouse associates on second shift in a 400,000-square-foot distribution center." (line 9) · Clarity · Each job header says Reno, and the current role mentions a Fernley cross-dock and a 400,000-square-foot DC. The reader can't tell whether these are one building or two, or which one she runs now. It matters because the posting asks for someone who has ramped up a building. Direction: name the building for each claim.

Cleared warnings: none. The checker reported no warnings. I counted three lists of three by hand (lines 4, 8 and 18). Each item is specific, so they pass under the voice rules.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Three or more years supervising warehouse or distribution associates | Must-have | Shown | Line 7: Shift Supervisor since Jan 2022. Line 9: 35 associates. Lines 13 and 15: Lead from May 2018, a receiving team of 12 |
| Experience with a warehouse management system | Must-have | Shown | Lines 10, 14 and 25: Manhattan WMS |
| OSHA 30-hour General Industry card | Must-have | Missing | Line 22 lists OSHA 10-Hour only |
| Forklift certification, or able to earn it in the first 30 days | Must-have | Shown | Line 23: Forklift Operator, sit-down and reach truck, 2017 |
| High school diploma or equivalent | Must-have | Shown | Line 20 |
| Experience opening or ramping up a new building | Preferred | Shown | Lines 4 and 8: Fernley cross-dock, 79% to 98% on time, March to August 2022 |
| Bilingual in English and Spanish | Preferred | Missing | Not on the page |
| Lean or Six Sigma training | Preferred | Missing | Not on the page |

## What I couldn't judge
- The on-time figures, 79% to 98% by August 2022, and her share of that result.
- What "Opened the Fernley, NV cross-dock" covers. Did she run the opening, or was she one supervisor on the opening team?
- The mis-pick drop from 1.2% to 0.4%, and whether the second pack-out scan was her idea.
- 99.6% inventory accuracy through 2023 and 2024.
- The 35 associates, the 400,000 square feet, the 18 associates trained at Fernley and the 40 trained on WMS scanners.
- Whether the 2017 forklift certification is still current. A reader may ask.
- Whether she holds an OSHA 30-hour card, speaks Spanish or has Lean or Six Sigma training.
````

### The check against the positioning file

The reviewer's hand-back is stamped 07:19:03 UTC, which is 01:19:03 local time. Then the skill's "When the posting has a positioning file" step found the file beside the posting and, at 01:19:27 local time, ran candidate-positioning's installed script through the skill's own path, `${CLAUDE_SKILL_DIR}/../candidate-positioning/scripts/check_positioning.py`:

````
$ python check_positioning.py positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md --piece Renata-Castillo-Resume.docx --as resume
check_positioning 0.2.0   positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md
INFO (16):
  (file): [piece] P1 (The Fernley cross-dock opening): shows, numbers found: 2022, 79%, 98%
  (file): [piece] P2 (Mis-picks cut with a second scan): shows, numbers found: 0.4%, 1.2%
  (file): [piece] P3 (New associates trained on Manhattan WMS): shows, numbers found: 40
  (file): [piece] P4 (Inventory accuracy held at 99.6%): shows, numbers found: 2023, 2024, 99.6%
  (file): [piece] Word to use 'brought a new building up to speed': not on the page
  (file): [piece] Word to use 'opening or ramping up a new building': not on the page
  (file): [piece] Word to use 'on time': not on the page
  (file): [piece] Word to use 'supervising warehouse or distribution associates': not on the page
  (file): [piece] Word to use 'second shift': on the page
  (file): [piece] Word to use 'warehouse management system': on the page
  (file): [piece] Word to use 'receiving, putaway and picking': on the page
  (file): [piece] Word to use 'cycle counts': on the page
  (file): [piece] Word to use 'inventory accuracy': on the page
  (file): [piece] Word to use 'shift schedules': not on the page
  (file): [piece] Word to use 'forklift certification': not on the page
  (file): [piece] Word to use 'high school diploma': on the page

RESULT: PASS
exit 0
````

### The note, word for word

It went to the person below the report and apart from it, followed by an offer to revise the resume.

````markdown
## Against the positioning file

- The first take lands on line 4 of the case, which says Renata "has already brought a new building up to speed, and she can do it again on a Sparks shift." The reviewer read the Fernley ramp, 79% to 98% in five months, as "the exact problem the posting describes."
- Must-fix 1, the OSHA 30-hour card, is gap R4. The file keeps it off the page on purpose, so the resume lists the 10-hour card she holds. That changes only if she earns the 30-hour card before she applies.
- Must-fix 2 isn't a gap or the concern. resume-ops writes each date range with an en dash, and plainspeak-writer 1.5's checker blocks that dash under R01, so the two tools disagree. The positioning file has nothing to say about it.
- Should-fix 1 to 3 are gaps the file already names: Spanish (R8), Lean or Six Sigma (R9), start-up meetings and safety audits (R13) and weekly reporting (R14), plus covering call-outs, the unproven half of R12. None of them goes on the page unless it's true.
- Should-fix 4 sits next to the concern in section 7. Naming the building for each claim will show that Fernley was a cross-dock, smaller than Sparks, so keep the Fernley result and her 35-person shift in the 400,000-square-foot center close together, as the file's case does.
- All four proofs marked for the resume show on the page: P1, the Fernley opening; P2, the mis-pick cut; P3, the 40 associates trained on Manhattan WMS; and P4, inventory accuracy at 99.6%.
- The script found no phrase from section 7 on the page.
````

## Grade

### The resume-ops run (this round's conditions and the key's "With the positioning file")

- **Pass**: The Level Set has a seventh line naming the file
  - Quote: “Positioning: positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md, confirmed 2026-10-06”
- **Pass**: `positioning_check.py` reads the file at intake
  - The helper ran it with `--posting posting.txt` before it wrote any part of the resume.
- **Pass**: The brief has a POSITIONING line
  - Quote: “POSITIONING: positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md (confirmed 2026-10-06); the evidence overrode nothing.”
- **Pass**: The checks line reads "positioning PASS"
  - Quote: “CHECKS: draft_review 0 FAIL; structure PASS; positioning PASS.”
- **Pass**: The delivery offers a submission review, in one line at the end
  - Quote: “Want a submission review of the finished resume? It reads the resume the way Ironwood's hiring team will and tells you whether to send it, fix it first or rethink it.”
- **Pass**: The finished resume passes `positioning_check.py --resume`
  - The helper's last check run and this session's rerun both end “RESULT: PASS”.
- **Pass**: Test 6, the resume half, holds
  - No watch phrase, no "OSHA 30" in any form and nothing about leaving Tumbleweed.

### Test 16 (RUN-TESTS.md)

- **Pass**: The report reads `blind: yes` in Claude Code
  - Quote: “- blind: yes”
- **Pass**: The positioning file is in neither the packet nor the reviewer's list of opened files
  - The packet holds `checker.txt`, `manifest.md`, `piece.txt` and `target.txt`.
  - "Files I opened" lists the four packet files, “the tells.md path above” and “the full-check.md path above”, and the transcript's six Read calls match.
- **Pass**: The note covers the first take
  - Quote: “The first take lands on line 4 of the case”
- **Pass**: The note covers any must-fix finding on a gap or the concern
  - Quote: “Must-fix 1, the OSHA 30-hour card, is gap R4.”
  - Quote: “Must-fix 2 isn't a gap or the concern.”
- **Pass**: The note covers the proofs
  - Quote: “All four proofs marked for the resume show on the page”
- **Pass**: The note covers any watch phrase
  - Quote: “The script found no phrase from section 7 on the page.”

### This round's extra condition

- **Pass**: The skill ran the "Against the positioning file" check on its own, after the report
  - The request never mentioned a positioning file. The check ran 24 seconds after the reviewer's hand-back, from the skill's own "When the posting has a positioning file" step, and its note went out below the report under that heading.
  - This session followed the skill and also grades it, so "on its own" means the skill's text called for the check with no prompt from outside it. A person's own session would run the same step.

### Other things the report shows

- Every quote in the report, 15 in all, is in the packet word for word.
- The verdict is Fix first, on two must-fix findings. One is the OSHA 30-hour card, gap R4, which the file keeps off the page on purpose. The other is three R01 hits on the date ranges, where resume-ops writes "Jan 2022 – Present" and plainspeak-writer 1.5 blocks the dash. The 0.2.0 run found the same two.

## Result

Pass. resume-ops 2.4.0, installed, used the confirmed file and met every condition for a build with a positioning file. The installed submission-review skill built a packet without the file, the reviewer stayed blind, and the check against the file ran after the report and covered the first take, the must-fix findings, the proofs and the watch phrases. As in tests 1 and 7, the packet script found plainspeak-writer only through `--voice-dir`.
