# Key: cover letter runs cl-e1 and cl-e2, writer E, Renata Castillo, to Ironwood Trail

## cl-e1

Files: `posting.txt`, `resume.txt`, `firm-pages.md`, her confirmed positioning file, and `Renata-Castillo-Resume.docx`, the resume resume-ops 2.4.0 built for her (Calibri 10.5 point, half-inch margins).

**Her first message.** "Please write my cover letter for the Operations Supervisor job at Ironwood Trail Supply. My positioning file is in this folder. I'm uploading it on their website along with Renata-Castillo-Resume.docx, the resume resume-ops made me."

**Replies.** If the skill asks for the hiring manager's name: "I don't know it." Anything else before the draft: "That's everything."

**Test 4, shape.** Four movements, a body of 500 words or fewer by code, one page in the Word file.

**Test 5, voice.** `check_letter.py --voice` finds no HARD hits.

**Test 8, off the page.** None of: "OSHA 30", "30-hour", "working toward", "Spanish", "bilingual", "Lean training", "Six Sigma", "lean principles", "start-up meeting", "safety audit", "smaller building", "smaller shift", "step up in size", "leave Tumbleweed", "leaving Tumbleweed", "why I'm leaving", and no departure story at all.

**Test 9, review limit.** The posting requires an OSHA 30-hour card she doesn't have, so the AI grader is likely to mark it missing and the verdict likely won't be Send. The skill revises once at most for anything else, runs a second review with a fresh packet, and after two reviews hands over the draft with the open findings, and the letter never names the missing card.

**Test 10, channels.** `Renata_Castillo_CoverLetter_IronwoodTrailSupply.docx`, with Calibri at 10.5 point and half-inch margins taken from her Word resume, the header matching that resume's contact block, "Renata Castillo" in the author field, and no PDF.

## cl-e2

Files: as cl-e1, but `resume-updated.txt` in place of the Word resume. It gives the Fernley opening as April 2022 and the on-time result as September 2022, where the positioning file and the resume it was built from say March and August.

**Her first message.** "Write my cover letter for the Ironwood Trail job, please. I'm uploading it with resume-updated.txt, where I fixed a couple of dates."

**Reply if asked which dates are right.** "The updated resume is right: April and September." If the skill offers candidate-positioning: "Not right now, just tell me what you found."

**Test 6, agreement.** Before any draft reaches her, the skill says the positioning file and resume-updated.txt disagree on the Fernley dates, names them, and offers to bring the file in line with candidate-positioning. No letter with March or August 2022 reaches her.
