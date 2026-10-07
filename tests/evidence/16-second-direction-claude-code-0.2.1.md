# Test 16: the second direction, through the installed skills (Claude Code, 0.2.1)

Writer E's resume, built by the installed resume-ops 2.4.0 from her confirmed positioning file, then reviewed through the installed submission-review skill with her posting as the target.

## Run

- Date: 2026-10-06
- Product: Claude Code 2.1.289 (`AI_AGENT=claude-code_2-1-289_agent`), in the Code tab of the Claude desktop app on Windows 11. This session didn't help build the plugin.
- Installed: job-seeker-ops 0.2.1 as a plugin, and resume-ops 2.4.0 and plainspeak-writer 1.5 as skills uploaded to the app.
- Folder: `C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed\`, outside the repository, holding writer E's posting, resume and saved firm pages and the positioning file confirmed in `positioning-installed-claude-code-0.2.1.md`. The file's SHA-256 before and after this part: `7fdec34869e7c03f508ece52965a7d0ddc3779b993844633eac38c996006dcae`.
- The replies come from "The resume-ops runs" in `keys/e-castillo.md`, opened after the positioning run had finished.
- Messages, replies and the report were copied by script from the helpers' hand-back calls, word for word. The Windows user name in each path is written as `<user>`. Nothing else in them was changed.

## Part 1: the resume-ops build

A general-purpose helper, started with the same kind of first message as the positioning run, and her first message from the key:

````
You're helping a person who's looking for a job. Use the skills installed in this app when one fits. Run Python as `python`.

The person's files are in C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed. Open only the skill's own files, plainspeak-writer's files if the skill needs them, and the files in that folder. Save what you write in that folder.

You can't talk with the person directly. Whenever the skill tells you to ask them something or to confirm something with them, end your turn with exactly the message you'd send them, and nothing after it. Their reply will come to you as your next message.

The person's first message:

"Build me a resume for this posting. The posting's in posting.txt and my current resume is resume.txt."
````

Its first call loaded `anthropic-skills:resume-ops`, the uploaded 2.4.0. At intake it ran the installed `positioning_check.py` on the positioning file with `--posting`.

### Stop 1

````
LEVEL SET: Resume Ops v2.4.0
Mode: Tailored resume
Evidence: resume.txt (read whole, 28 of 28 lines); firm-pages.md (read for context, not evidence)
Rulings: none
Target: Operations Supervisor, Distribution Center, Ironwood Trail Supply Co.
Doing now: Confirming your contact details before I build the resume.
Positioning: positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md, confirmed 2026-10-06

I've read the posting, your resume and your positioning file. The plan is to lead with the Fernley opening, as you asked.

One question first, about the top of the page. Your resume lists Reno, NV, (775) 555-0163 and renata.castillo@example.com. Are those still right? And do you have a LinkedIn URL to add? If you don't, I'll leave it off.
````

Reply, from the key: "Use the contact line at the top of my resume: Reno, NV, (775) 555-0163, renata.castillo@example.com. I don't have a LinkedIn URL."

### Stop 2

````
Thanks. I'll use Reno, NV | (775) 555-0163 | renata.castillo@example.com, with no LinkedIn.

Next question, about your current job title. Application systems like the one on Ironwood's site keep only the words before a comma in a job title. On your current title, the form would cut "Shift Supervisor, Distribution Center" down to "Shift Supervisor". To stop that, I'd write it on the resume as "Distribution Center Shift Supervisor". It's the same words in a different order, with nothing added. The risk is low. A background check will report the title exactly as Tumbleweed has it on record, so when the application form asks for your title, you'd type "Shift Supervisor, Distribution Center".

Is it OK to write it as "Distribution Center Shift Supervisor" on the resume, or do you want the comma kept?
````

The key has no reply for this question, so it got the reply to anything else: "I don't know. Use what's on my resume." The helper kept the comma in the title.

### The delivery

````
Your resume is ready, in your folder:
- Renata-Castillo-Resume.docx (the file to upload)
- Renata-Castillo-Resume.txt (plain text for paste-in boxes)
- Renata-Castillo-Resume.json (the source, so it can be rebuilt)

EVIDENCE: resume.txt (read whole).
REQUIREMENTS: 4 of 5 required proven. Supervising (supervisor since Jan 2022, the Tumbleweed role). WMS (Manhattan WMS, in the mis-pick bullet). Forklift and diploma (Certifications, Education). 1 of 3 preferred: the Fernley opening, which leads the summary and your current role.
WRITTEN IN: "warehouse management system" beside Manhattan WMS, and "Certification" on the forklift line, so they match the posting's words.
GAPS: OSHA 30 card, Spanish, Lean or Six Sigma training, safety audits and start-up meetings. None of them is on the page.
QUESTIONS: (1) Is your forklift card current? (2) Do you build the weekly schedule, cover call-outs or report numbers weekly? If you do, each one can go in a bullet. (3) What's your high school's name? (4) Would you like one sentence in your own words about how you run a floor, for the summary?
RECORD: titles kept as written, with the comma.
POSITIONING: positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md (confirmed 2026-10-06). The evidence overrode nothing. The keep-off check passed.
CHECKS: draft_review 0 FAIL; structure PASS. Page view not run (LibreOffice isn't installed). Open it in Word and check that it fits on one page.

After you upload it on Ironwood's site, check every field the form fills in before you submit:
- Each job: the whole title (forms often cut "Shift Supervisor, Distribution Center" at the comma, so retype it), the company alone, Reno, NV, the dates (current job marked current), and a description.
- Education: diploma and year.
- Languages: delete any you don't speak.
- Skills: remove anything wrong, then add the true ones in the posting's words (warehouse management system, cycle counts, forklift).
- Certifications and contact fields.

Two offers: I can save your title choice in a rulings file so it's never asked again, and I can run a submission review of the finished resume. Want either?
````

### The built resume

`Renata-Castillo-Resume.txt`, the plain-text copy beside the DOCX:

````
Renata Castillo
Reno, NV | (775) 555-0163 | renata.castillo@example.com

SUMMARY

Distribution center operations supervisor with 10 years in warehouse work, from associate to second-shift supervisor. Brought a new building up to speed in 2022: opened the Fernley, NV cross-dock and raised its on-time shipping from 79% to 98% in five months. Runs a second shift of 35 associates on Manhattan WMS. Worked receiving, putaway and picking on the floor before taking over a shift.

EXPERIENCE

Tumbleweed Home Goods, Reno, NV
Shift Supervisor, Distribution Center | Jan 2022 – Present
- Opened the Fernley, NV cross-dock in March 2022. Built the shift schedule, trained the first 18 associates and brought on-time shipping from 79% to 98% by August 2022.
- Supervise 35 associates on second shift in a 400,000-square-foot distribution center.
- Held inventory accuracy at 99.6% through 2023 and 2024 with weekly cycle counts.
- Cut mis-picks from 1.2% to 0.4% by adding a second scan at pack-out in Manhattan WMS, the warehouse management system.
Tumbleweed Home Goods, Reno, NV
Warehouse Lead | May 2018 – Dec 2021
- Led a receiving team of 12 and set its daily putaway plan.
- Trained 40 new associates on Manhattan WMS scanners and putaway rules.
Tumbleweed Home Goods, Reno, NV
Warehouse Associate | Jun 2016 – Apr 2018
- Picked, packed and received freight, and moved up to lead after two years.

EDUCATION

High School Diploma | Reno, NV | 2014

CERTIFICATIONS

Forklift Operator Certification, Sit-Down and Reach Truck | 2017
OSHA 10-Hour General Industry | 2021

SKILLS

Manhattan WMS, WMS scanners, cycle counts, shift scheduling, sit-down forklift, reach truck
````

The helper ran `positioning_check.py --resume` twice on the built DOCX, and both passed. This session ran it again on the delivered file:

````
POSITIONING CHECK: Renata-Castillo-Resume.docx against positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md
Words to use on the page: new building (1), inventory accuracy (1), cycle counts (2), warehouse management system (1), receiving, putaway and picking (1), shift schedules (2, word-form match), second shift (2)
Words to use not on the page: ramping up, on time, forklift certification. Add one only where the evidence proves it, inside the line that shows the work.
RESULT: PASS
exit 0
````

### Grade, part 1

| Condition | Result | Evidence |
|---|---|---|
| The Level Set has a seventh line naming the file | Pass | "Positioning: positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md, confirmed 2026-10-06", the seventh line after "LEVEL SET: Resume Ops v2.4.0". |
| The brief has a POSITIONING line | Pass | "POSITIONING: positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md (confirmed 2026-10-06). The evidence overrode nothing. The keep-off check passed." |
| The checks line reads "positioning PASS" | **Fail** | The line reads "CHECKS: draft_review 0 FAIL; structure PASS. Page view not run (LibreOffice isn't installed). ..." with no positioning entry. The check did run and pass ("RESULT: PASS" in the helper's transcript), and the brief reports it on the POSITIONING line instead: "The keep-off check passed." resume-ops 2.4.0's own brief format doesn't ask for it on the CHECKS line. Its example in `references/tailoring.md` reads "CHECKS: draft_review 0 FAIL; structure PASS; 2 pages; 0 widows." |
| The delivery offers a submission review | Pass | Its last line: "Two offers: I can save your title choice in a rulings file so it's never asked again, and I can run a submission review of the finished resume. Want either?" The offer shares the line with an offer to save the title ruling. |
| Test 6's resume half: no watch phrase, no "OSHA 30" in any form, nothing about leaving Tumbleweed | Pass | `positioning_check.py --resume` passes. The page names "OSHA 10-Hour General Industry \| 2021" and no 30-hour card, and "Tumbleweed" shows only as her employer. |

## Part 2: the submission review

### The request

This session loaded `job-seeker-ops:submission-review` with the Skill tool, with this request:

> Can you run a submission review on my resume before I upload it? It's Renata-Castillo-Resume.docx in C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed, and the posting I'm applying to is posting.txt in the same folder.

The skill found the reviewer among the agent types. The request gave the piece, the target and the channel, so the skill asked nothing. A resume has no companion.

### The packet

Following the skill's step 2, run from the run folder, with no `--out`:

````
python SCRIPT --type resume --piece Renata-Castillo-Resume.docx --target posting.txt --channel upload
````

That manifest read "Voice rules: not found. Voice is unchecked." The skill says to rerun with `--voice-dir` in that case, so the packet was built again with `--voice-dir` pointing at the installed plainspeak-writer:

````
Packet: C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed\review-packets\20261006-234601-resume-a82c
Message for the reviewer (send exactly this line and nothing else):
Review the packet in C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed\review-packets\20261006-234601-resume-a82c. Read manifest.md first.
````

The packet holds `manifest.md`, `piece.txt`, `target.txt` and `checker.txt`, and no positioning file. The manifest's settings:

````
## Settings

- Piece type: resume
- Readers: Recruiter, first look; AI grader (the defaults for this piece type).
- Target: given in target.txt.
- Channel: an uploaded file.
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
- Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Checker: Ran with surface resume, exit code 1.
````

`checker.txt`:

````
plainspeak-writer 1.5 checker output for piece.txt, surface resume, exit code 1 (0 means no HARD hits, 1 means at least one).

check_voice 1.5   surface: resume

=== C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed\review-packets\20261006-234601-resume-a82c\piece.txt ===
Words: 261
HARD FAIL (3):
  L7: [R01 em dash or other dash] "–": no dash of any kind, and no double hyphen or spaced hyphen typed as one; a period, comma, colon, or semicolon
  L13: [R01 em dash or other dash] "–": no dash of any kind, and no double hyphen or spaced hyphen typed as one; a period, comma, colon, or semicolon
  L17: [R01 em dash or other dash] "–": no dash of any kind, and no double hyphen or spaced hyphen typed as one; a period, comma, colon, or semicolon
WARN (1), each cleared by a named decision or fixed:
  L0: [V01 list of three (rate)] "3 in 261 words, 11.5 per 1,000, where 9 in 10 pieces of edited human writing stay at or under 8: "opened the Fernley, NV cross-dock and raised its on-time shipping" L4, "Worked receiving, putaway and picking on the floor" L4, "Forklift Operator Certification, Sit-Down and Reach Truck" L22": fine when each item is specific and does work; a crutch when it stands in for logic

RESULT: FAIL: hard violations present.
````

### The reviewer

Started with the Agent tool as `job-seeker-ops:submission-reviewer`, with the printed line and nothing else:

````
Review the packet in C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed\review-packets\20261006-234601-resume-a82c. Read manifest.md first.
````

Its transcript holds six Read calls, on the four packet files, `tells.md` and `full-check.md`, then its hand-back at 05:47:29 UTC. Its git snapshot listed only the untracked `tests/evidence/prior-2.1.288/` folder and the same five commit titles as the test 1 reviewer's, since this round's evidence was still outside the repository.

### The report

````
# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the manifest), piece.txt (the piece: resume), target.txt (the target: job posting), checker.txt (plainspeak-writer checker output for piece.txt)
- Voice rules: plainspeak-writer 1.5. Rules file: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md. Full check: C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\full-check.md
- Also in my context: an account email; a git snapshot (nothing in it refers to this piece, its target or how it was written); tool instructions from connected MCP servers
- Files I opened: C:\Users\<user>\repos\tools\jso-tests\positioning\runs\e-installed\review-packets\20261006-234601-resume-a82c\manifest.md; ...\piece.txt; ...\target.txt; ...\checker.txt; the tells.md path above; the full-check.md path above
- blind: yes

## First take (Recruiter, first look)
This is a second-shift supervisor with 10 years at one distribution company. She opened a cross-dock and took on-time shipping from 79% to 98% in five months, which is the exact problem our posting describes. Fit: yes

## Verdict
Fix first. Rule 2 set it: there are two must-fix findings, and the first take ends Fit: yes.

## Must fix
1. "Jan 2022 – Present" (line 7), "May 2018 – Dec 2021" (line 13), "Jun 2016 – Apr 2018" (line 17) · Voice · The checker logged a HARD hit under R01 on all three date ranges. The rules allow an en dash only between two numbers, and a month name or "Present" next to the dash breaks that pattern. Direction: write the three date ranges in a form R01 passes, and write all three the same way.
2. "OSHA 30-hour General Industry card." (target line 16) · Fit · This is a listed requirement. The page shows only "OSHA 10-Hour General Industry | 2021" (line 23), so an AI grader marks it missing, and a recruiter matching certifications sees the wrong card. Direction: if she holds the 30-hour card, list it by its exact name. If she doesn't, the page has no way to meet this requirement.

## Should fix
1. "Lead daily start-up meetings and monthly safety audits." (target line 10), "cover call-outs" (target line 9), "Report productivity and on-time numbers to the site manager every week." (target line 11) · Fit · These are the role's daily duties, and the resume shows none of them. It has no safety work at all beyond the OSHA 10 line. A grader matching duties finds nothing to match. Direction: if she has done these, name them with a count or a result.
2. "Bilingual in English and Spanish." (target line 22), "Lean or Six Sigma training." (target line 23) · Fit · Two of the three preferred items are missing from the page. Direction: add them only if true.
3. "Held inventory accuracy at 99.6% through 2023 and 2024 with weekly cycle counts." (line 10) · Proof · She is still in the role in October 2026, yet the newest figure on the page is from 2024 and the on-time figure stops at August 2022. A reader may wonder what happened in 2025 and 2026. Direction: give the current figures, or say why the years stop where they do.
4. "Opened the Fernley, NV cross-dock in March 2022." (line 8), "Supervise 35 associates on second shift in a 400,000-square-foot distribution center." (line 9), under "Tumbleweed Home Goods, Reno, NV" (line 6) · Clarity · The reader can't tell whether she runs the Fernley cross-dock or a separate Reno distribution center, or whether both lines describe one building. Direction: name the building she supervises now and its city.
5. "Brought a new building up to speed in 2022: opened the Fernley, NV cross-dock and raised its on-time shipping from 79% to 98% in five months. Runs a second shift of 35 associates on Manhattan WMS." (line 4) · Voice · The summary repeats lines 8 and 9 almost word for word. That uses the top of a 261-word page to say the same thing twice when nothing on the page covers safety or call-outs. Direction: keep the opening result in one place and use the space saved for something the page doesn't yet show.

Cleared: V01 list of three (whole piece). The checker quoted three lines. "opened the Fernley, NV cross-dock and raised its on-time shipping" (line 4) is a place-name comma, not a list. "Forklift Operator Certification, Sit-Down and Reach Truck" (line 22) is a certificate's name. "Worked receiving, putaway and picking on the floor" (line 4) names the same three jobs the target lists, so each item does work.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Three or more years supervising warehouse or distribution associates | Must-have | Shown | Lines 7 to 9 (Shift Supervisor since Jan 2022, 35 associates); lines 13 and 14 (Warehouse Lead, team of 12) |
| Experience with a warehouse management system | Must-have | Shown | Line 11 (mis-picks cut from 1.2% to 0.4% in Manhattan WMS); lines 4, 15 and 25 |
| OSHA 30-hour General Industry card | Must-have | Missing | Line 23 lists the OSHA 10-Hour card only |
| Forklift certification, or able to earn it in the first 30 days | Must-have | Shown | Line 22 (2017) |
| High school diploma or equivalent | Must-have | Shown | Line 20 |
| Experience opening or ramping up a new building | Preferred | Shown | Lines 4 and 8 (Fernley cross-dock, 79% to 98%) |
| Bilingual in English and Spanish | Preferred | Missing | Not on the page |
| Lean or Six Sigma training | Preferred | Missing | Not on the page; the mis-pick work in line 11 is process work but names no training |

## What I couldn't judge
- The figures: on-time shipping from 79% to 98% between March and August 2022, inventory accuracy of 99.6%, mis-picks from 1.2% to 0.4%, and the 400,000-square-foot building.
- Whether the Fernley cross-dock and the 400,000-square-foot distribution center are the same building, and how a cross-dock fits with weekly cycle counts and inventory accuracy.
- Whether she holds an OSHA 30-hour card, speaks Spanish or has Lean or Six Sigma training.
- Whether the 2017 forklift certification is still current. A reader may want to see a recent date.
- The counts of people: 18 trained at the opening, 40 trained as a lead, a receiving team of 12, and a current shift of 35.
````

### The skill's check against the positioning file

After the report, at 05:47:36 UTC, seven seconds after the hand-back, this session ran the step the skill gives under "When the posting has a positioning file":

````
python "<plugin>\skills\submission-review\..\candidate-positioning\scripts\check_positioning.py" positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md --piece Renata-Castillo-Resume.docx --as resume
````

````
check_positioning 0.2.0   positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md
INFO (13):
  (file): [piece] P1 (The Fernley cross-dock opening): shows, numbers found: 2022, 79%, 98%
  (file): [piece] P2 (Inventory accuracy held with weekly cycle counts): shows, numbers found: 2023, 2024, 99.6%
  (file): [piece] P3 (Mis-picks cut in Manhattan WMS): shows, numbers found: 0.4%, 1.2%
  (file): [piece] Word to use 'new building': on the page
  (file): [piece] Word to use 'ramping up': not on the page
  (file): [piece] Word to use 'on time': not on the page
  (file): [piece] Word to use 'inventory accuracy': on the page
  (file): [piece] Word to use 'cycle counts': on the page
  (file): [piece] Word to use 'warehouse management system': on the page
  (file): [piece] Word to use 'receiving, putaway and picking': on the page
  (file): [piece] Word to use 'shift schedules': not on the page
  (file): [piece] Word to use 'second shift': on the page
  (file): [piece] Word to use 'forklift certification': not on the page

RESULT: PASS
exit 0
````

The note written below the report, under its own heading:

## Against the positioning file

`check_positioning.py --piece Renata-Castillo-Resume.docx --as resume` passes, and it found no phrase from section 7 on the page.

- **The first take.** It lands on line 4 of the case, that she has already brought a new building up to its on-time goal and can do the same for Sparks. The reviewer's first take says she "took on-time shipping from 79% to 98% in five months, which is the exact problem our posting describes."
- **Must-fix findings on a gap.** Must fix 2, the OSHA 30-hour card, falls on gap R8, and she confirmed she doesn't hold the card yet. The finding's own direction applies: "If she doesn't, the page has no way to meet this requirement." Leave it off the page, with no "in progress" or "working toward" line. Should-fix 1 (start-up meetings and safety audits) and should-fix 2 (Spanish, Lean or Six Sigma) fall on gaps R4, R12 and R13, and the same holds. Must fix 1, the date dashes, has no link to the file. No finding falls on the concern about Fernley being a cross-dock, though should-fix 4 asks which building she runs now, which touches it.
- **Proofs on the page.** P1 (the Fernley opening), P2 (inventory accuracy) and P3 (mis-picks in Manhattan WMS) all show with their numbers. P4 is marked for the letter only.
- **Watch phrases.** None on the page.

Want me to revise the resume? The date ranges can change now. For should-fix 3 and 4, I'd need the current figures and which building she runs.

### Grade, part 2, on test 16's conditions

| Condition | Result | Evidence |
|---|---|---|
| The report reads `blind: yes` in Claude Code | Pass | "- blind: yes". It names its context: "an account email; a git snapshot (nothing in it refers to this piece, its target or how it was written); tool instructions from connected MCP servers". |
| The positioning file isn't in the packet | Pass | The packet holds four files: the manifest, the piece, the target and the checker output. |
| It isn't in the reviewer's list of opened files | Pass | "Files I opened" lists the four packet files, `tells.md` and `full-check.md`, which matches its Read calls. |
| The note covers the first take | Pass | "It lands on line 4 of the case ..." |
| The note covers a must-fix finding on a gap | Pass | "Must fix 2, the OSHA 30-hour card, falls on gap R8 ... Leave it off the page". |
| The note covers the proofs | Pass | "P1 (the Fernley opening), P2 (inventory accuracy) and P3 (mis-picks in Manhattan WMS) all show with their numbers." |
| The note covers watch phrases | Pass | "None on the page." |
| The skill ran the "Against the positioning file" check on its own, after the report | Pass | The request asked only for a review. The check ran seven seconds after the reviewer's hand-back, from the skill's own instructions, and nothing went to the reviewer. |

**Test 16: fail on one condition.** The review half passes on every condition. The build half meets three of its four conditions, and its CHECKS line leaves out "positioning PASS". The check ran and passed, and the brief reports it on the POSITIONING line instead.

## Worth noting

- The reviewer's must-fix 2 on the OSHA 30-hour card is right as a reading of the page. The page can't meet that requirement, and the note keeps the fix from turning into an "in progress" line.
- Must fix 1 is the date dashes, "Jan 2022 – Present" and the others. resume-ops still writes a date range with an en dash, and plainspeak-writer 1.5 blocks it under R01, as in the 2.1.288 run. The reviewer's reason, that the rules allow an en dash only between two numbers, matches `full-check.md`, which keeps the en dash in a number range such as "2019–2021", and a month name or "Present" isn't a number.
- LibreOffice isn't on the test computer, so the resume-ops helper skipped its page view and said so.
