# The blind review of writer E's resume, word for word

# Submission review

## What I received
- Message: the fixed line
- Packet files: manifest.md (the manifest), piece.txt (the piece: resume), target.txt (the target: Operations Supervisor posting, Ironwood Trail Supply Co.), checker.txt (plainspeak-writer checker output, surface resume, exit code 1)
- Voice rules: plainspeak-writer 1.4.1, C:\Users\<user>\AppData\Local\Packages\Claude_<id>\LocalCache\Roaming\Claude\local-agent-mode-sessions\skills-plugin\<id>\<id>\skills\plainspeak-writer\references\tells.md
- Also in my context: an account email; tool instructions from connected tool servers (docs, computer use, Figma) that say nothing about the person or the piece; environment details (working directory, platform). No saved memory, profile, preferences, project instructions, earlier conversation or git snapshot.
- Files I opened: C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261005-155944-resume-7f2c\manifest.md; C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261005-155944-resume-7f2c\piece.txt; C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261005-155944-resume-7f2c\target.txt; C:\Users\<user>\repos\tools\jso-tests\positioning\packets\20261005-155944-resume-7f2c\checker.txt; the tells.md path above
- blind: yes

## First take (Recruiter, first look)
This is a distribution center shift supervisor with 10 years at one company who opened a new cross-dock and took on-time shipping from 79% to 98% in five months. That's the exact problem in this posting, so I keep reading. Fit: yes

## Verdict
Fix first. Rule 2: two must-fix findings (one checker HARD rule, one missing must-have requirement with the AI grader reading).

## Must fix
1. "Jan 2022 – Present" (line 7), "May 2018 – Dec 2021" (line 13), "Jun 2016 – Apr 2018" (line 17) · Voice · The checker logs three HARD hits under R01, the rule against dashes. These are date ranges, but the rules only allow an en dash between two bare numbers. These dashes join a month and year to "Present" or to a month name, so they block. Direction: change the separator in all three date ranges to one the rules allow.
2. "OSHA 30-hour General Industry card." (target line 16) · Fit · The posting lists this under Requirements. The resume shows only "OSHA 10-Hour General Industry | 2021" (line 22), so the grader marks the requirement missing, and the 10-hour card may suggest she doesn't meet it. Direction: if she holds the 30-hour card or is enrolled, list it with its date. If not, this gap stays on the page.

## Should fix
1. "Bilingual in English and Spanish." (target line 22), "Lean or Six Sigma training." (target line 23) · Fit · Two of the three preferred items don't appear anywhere, so the grader scores them as missing. Direction: list either one only if she has it.
2. "Lead daily start-up meetings and monthly safety audits." (target line 10), "Report productivity and on-time numbers to the site manager every week." (target line 11), "cover call-outs" (target line 9) · Fit · The posting lists these duties, and the resume has no matching work. It doesn't mention safety, meetings, reporting to a manager or covering absences. A grader that scores against the duties finds nothing for them. Direction: name these tasks if she does them now.
3. "by August 2022" (line 8), "through 2023 and 2024" (line 11), "Cut mis-picks from 1.2% to 0.4%" (line 10) · Proof · The newest dated result is from 2024, and the mis-pick result has no date at all. The current role runs to the present, so a reader sees nothing from the last year and a half or more. Direction: date the mis-pick result and add a 2025 or 2026 figure.
4. "Tumbleweed Home Goods, Reno, NV" (line 6), "Opened the Fernley, NV cross-dock in March 2022" (line 8), "in a 400,000-square-foot distribution center" (line 9) · Clarity · The heading says Reno, the first line under the role is about a cross-dock in Fernley, and the next is about an unnamed 400,000-square-foot distribution center. An outsider can't tell whether these are one building or two, or where she supervises today. Direction: name each building and say where she works now.
5. "Opened a cross-dock in Fernley, NV and brought it up to speed in five months, lifting on-time shipping from 79% to 98%." (line 4) against "Opened the Fernley, NV cross-dock in March 2022. ... brought on-time shipping from 79% to 98% by August 2022." (line 8) · Voice · The summary repeats line 8 almost word for word. "Moved up" also appears twice (lines 4 and 18). The top of the page, which is what the recruiter reads, spends its space on one result told twice. Direction: give the summary a second match to the posting that line 8 doesn't already make.

Cleared warning: V01, list of three (whole piece). Both flagged phrases are names, not lists. "Fernley, NV" (line 4) is a place, and "Forklift Operator, sit-down and reach truck" (line 23) is a certification. The real three-item lists in lines 8 and 18 are specific and each item does work.

## Requirements
| Requirement | Must-have or preferred | Status | Where it shows |
|---|---|---|---|
| Three or more years supervising warehouse or distribution associates | Must-have | Shown | Line 7 (Shift Supervisor, Jan 2022 to present), line 9 (35 associates), line 15 (team of 12 as lead) |
| Experience with a warehouse management system | Must-have | Shown | Lines 9, 10, 14, 25 (Manhattan WMS) |
| OSHA 30-hour General Industry card | Must-have | Missing | Line 22 shows only the 10-hour card |
| Forklift certification, or able to earn it in the first 30 days | Must-have | Shown | Line 23 (2017) |
| High school diploma or equivalent | Must-have | Shown | Line 20 |
| Experience opening or ramping up a new building | Preferred | Shown | Lines 4 and 8 (Fernley cross-dock, 79% to 98%) |
| Bilingual in English and Spanish | Preferred | Missing | None |
| Lean or Six Sigma training | Preferred | Missing | None. The pack-out second scan (line 10) is process work, not training |

## What I couldn't judge
- Whether she holds the OSHA 30-hour card or is working toward it.
- Her role in "Opened the Fernley, NV cross-dock": a shift supervisor opening a site, and how much of the 79% to 98% gain was her work and how much was the site team's. A hiring manager will ask.
- The 1.2% to 0.4% mis-pick figures: the time period and how they were measured.
- The 99.6% inventory accuracy for 2023 and 2024, and the 400,000-square-foot and 35-associate figures.
- Whether the 2017 forklift certification is still current, since a reader may expect a recent evaluation.
- The two years between the 2014 diploma and the June 2016 start, which a reader may ask about.
