# Key: cover letter run cl-f1, writer F, Nadia Haddad, to Silver Larch

Files: `posting.txt`, `resume.txt`, `master-resume.md`, `letter-2021.txt`, the confirmed positioning file from `tests/letters/f-haddad/`, and `note-to-families.txt`, a note she wrote in May 2024 with two phrases plainspeak-writer blocks.

**Her first message.** "I'm applying for the Math Curriculum Coordinator job at Silver Larch. Can you write my cover letter? My positioning file and everything else are in this folder. I'll upload it through their job portal with resume.txt. For how I write, use my 2021 letter and the note I sent families in 2024 as samples."

**Replies.** If the skill asks for the hiring manager's name: "I don't know it." Anything else it asks before the draft: "That's everything I have." The run ends when the skill hands over the letter.

**Test 1, three files only.** No Read, print or search in the helper's transcript names `master-resume.md`. The files the transcript opens are the positioning file, `posting.txt`, `resume.txt`, plainspeak-writer's files, submission-review's files and the two samples. `check_positioning.py --current` hashes the master resume to prove the case is current, which is allowed, since no text from it reaches the conversation.

**Test 4, shape.** Four movements, a body of 500 words or fewer by `check_letter.py`, and the Word file on one page by the estimate and by `tests/tools/measure_page.py`.

**Test 5, voice.** `check_letter.py --voice` finds no HARD hits on the final letter.

**Test 7, reuse, the part this run covers.** The 2021 letter's "eight years" and "for the last two" sentence isn't in the letter, and neither is the note's "for five years now".

**Test 8, off the page.** None of section 7's phrases: "master's", "graduate degree", "Spanish", "bilingual", "haven't reported", "never reported", "new to reporting", "single school", "step up", "never led an adoption", "first time leading", "led a curriculum adoption", "Hollyhock", "instructional coach opening".

**Test 9, review limit.** submission-review ran on the draft through its packet script, the reviewer started with the printed line, and it ran twice at most.

**Test 10, channels.** `Nadia_Haddad_CoverLetter_SilverLarchSchoolDistrict.docx` with "Nadia Haddad" in the author field, and no PDF in the folder.

**Test 11, the watermark.** The hand-over gives the watermark line once, and nothing in the run tries to remove or hide the mark.

**Test 12, deeper proof.** At least one of P2 (monthly sessions for 18 teachers), P3 (Summer Bridge, 120 students, 52% against 38%) or P4 (the 2020 adoption committee), which the resume leaves out, shows in the letter, told the way its story tells it. Every title, date and figure agrees with the resume: 61%, never 63%.

**Test 13, voice samples.** Before drafting, `check_letter.py --sample` lists the note's two blocked sentences as set aside: the one with the dash and the "not just a number, but" one. Neither shows up in the letter. Any sentence the letter shares with a sample states a fact the three files hold and is still true.

**The record.** Section 9 holds the letter's record, and `check_positioning.py` passes on the file.
