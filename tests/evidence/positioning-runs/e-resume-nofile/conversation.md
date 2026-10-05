# Run e-resume-nofile: the conversation, word for word

## The person

Build me a resume for this posting. The posting's in posting.txt and my current resume is resume.txt.

## The helper

```
LEVEL SET: Resume Ops v2.4.0
Mode: Tailored resume
Evidence: resume.txt (read whole)
Rulings: none
Target: Operations Supervisor, Distribution Center at Ironwood Trail Supply Co.
Doing now: Confirming your contact block before I map your resume to the posting.
```

Your resume's top line has Reno, NV, (775) 555-0163 and renata.castillo@example.com. Should those go on this resume too, and what LinkedIn URL should go with them?

## The person

Use the contact line at the top of my resume: Reno, NV, (775) 555-0163, renata.castillo@example.com. I don't have a LinkedIn URL.

Address this before completing your current task.

## The helper

Thanks, that contact line is set, with no LinkedIn.

Your resume proves four of the posting's five requirements. The fifth is the OSHA 30-hour General Industry card. Your resume lists the 10-hour card from 2021. Do you hold the 30-hour card?

## The person

I don't know. Use what's on my resume.

Address this before completing your current task.

## The helper

Got it. The resume will list the OSHA 10-hour card as yours does, and I'll name the 30-hour card as a gap in the brief.

The posting prefers someone who speaks English and Spanish. Do you speak Spanish, and how well?

## The person

I don't know. Use what's on my resume.

Address this before completing your current task.

## The helper

Your resume is built. It's one page, in the `out` folder inside your folder:
- `Renata-Castillo-Resume.docx` is the file to upload.
- `Renata-Castillo-Resume.txt` is the same resume in plain text, for boxes that only take pasted text.

Its source file, `Renata-Castillo-Resume.json`, stays in your folder so the resume can be rebuilt.

```
EVIDENCE: resume.txt (read whole) and today's answers.
REQUIREMENTS: 4 of 5 required proven: supervising and WMS (supervisor role), forklift, diploma. R3 OSHA 30-hour card: gap. 1 of 3 preferred: new-building ramp-up (Fernley bullet).
WRITTEN IN: none. Posting terms added inside true lines: operations supervisor, ramped up, warehouse management system, forklift certification.
GAPS: OSHA 30-hour card, Spanish, Lean or Six Sigma.
PROVISIONAL: none.
QUESTIONS: May I write your title "Distribution Center Shift Supervisor" so Workday keeps it whole? Same words, low background-check risk. One sentence, your words, on how you run a floor? Is the 2017 forklift certification current? Do you run start-up meetings, safety audits or productivity reports?
RECORD: no LinkedIn. Titles and dates as on resume.txt; type them exactly into forms.
SYSTEM: not named (no posting link). Post-upload review below.
CHECKS: draft_review 0 FAIL; structure PASS; LibreOffice render not run; approximate Calibri render: 1 page, 0 widows.
```

**Post-upload review.** This applies when the application fills its form from your file. If it doesn't fill a form, there's nothing to fix, and the file is the whole application.

For each of your three Tumbleweed Home Goods roles:
- **Title whole.** Forms like Workday keep only the words before a comma, so your supervisor title may come back as "Shift Supervisor". Type "Shift Supervisor, Distribution Center".
- **Company and place.** The company field should say Tumbleweed Home Goods with nothing stuck to it, and the location should be Reno, NV.
- **Dates.** The supervisor role should be marked current.
- **Description.** Each role should have one.

Then:
- **Education:** the resume doesn't name your high school, so type its name in the school field.
- **Languages:** delete any you don't speak.
- **Skills:** check this box every time. Remove anything wrong, then add "warehouse management system" and "forklift certification".
- **Certifications:** if the form has a place for them, add OSHA 10-Hour General Industry (2021) and the forklift certification (2017).
- **Contact fields:** check them. Leave Websites empty.
- **Screening questions:** answer slowly and exactly. If one asks about the OSHA 30-hour card, answer truthfully; the resume doesn't claim it.
- **Background-check form, if one comes later:** titles exactly as held, dates as on the resume.

If a company comes back blank, look at the last bullet of the job above it and move that bullet up.

**To save for next time:** with your yes, I'll write these two rulings to `rulings.md` in your folder, so later resumes don't ask again:

```
### 2026-10-05: Contact line
Ruling: Reno, NV | (775) 555-0163 | renata.castillo@example.com. No LinkedIn URL.
Kind: fact. Applies to: all resumes.

### 2026-10-05: OSHA 30-hour card and Spanish
Ruling: Neither is claimed. Asked about each, Renata said she didn't know and to use what's on her resume.
Kind: fact. Applies to: all resumes, until she says otherwise.
```

I can also keep a facts file with this build's numbers, so the next posting goes faster. Should I save the rulings, and start the facts file?
