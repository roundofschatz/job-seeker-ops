# Key: cover letter run cl-b1, writer B, Dmitri Okafor, to Switchgrass Freight by email

Files: `posting.txt`, `resume.txt`, `career-record.md`, `positioning-notes.md`, and the positioning file from the example in candidate-positioning's `references/format.md`.

**His first message.** "Please write my cover letter for the Supply Chain Planning Analyst job at Switchgrass Freight. I'm emailing it to the hiring manager, Maria Lopez, with my resume attached. My positioning file and the rest are in this folder."

**Replies.** Anything the skill asks before the draft: "That's all I have."

**Test 1, three files only.** No Read, print or search in the transcript names `career-record.md` or `positioning-notes.md`.

**Test 8, off the page.** None of: "new to freight", "no freight experience", "learning freight", "different industry", "learning curve", "outside freight", "reorganization", "night shift", "no path", "senior analyst", "salary", "$85,000", "top of the range".

**Test 10, channels.** The email opens on a subject line that names the role and a salutation to Maria Lopez, with no contact block, and the hand-over says to attach the resume. `check_letter.py --channel email --given "Maria Lopez"` passes, and the run makes no Word file and no PDF.
