# Key: cover letter runs cl-f2-positioning and cl-f2, writer F to Juniper Flats

Two runs. The first builds her positioning file for a second posting with candidate-positioning, and the second writes that letter. Test 7 compares it with the letter from cl-f1.

## cl-f2-positioning

Files: `resume.txt`, `master-resume.md`, `letter-2021.txt`, and from `tests/letters/f-haddad/juniper-flats/` the posting and the firm pages she saved.

**Her first message.** "I'm also applying for the Middle School Math Instructional Coach job at Juniper Flats. Can you work out my case before I write the letter? The posting, my resume, my master resume, my 2021 letter and pages I saved from their website are all in this folder. I'll upload the letter on their site, and nobody's referring me."

**Her reply at step 9.** "That's right. Use 61%, since the resume has it right and the master resume has a typo. I don't have a master's degree and I'm not bilingual. Save it."

If the skill sends a step 2 message, she answers: "Everything I have is in the folder."

**Passes when** the saved file passes `check_positioning.py --sources --current --for cover-letter`, with no firm fact from the home page (no "9,800 students", no "14 schools").

## cl-f2

Files: the cl-f2-positioning folder with its new file, and `letter-silver-larch.txt`, the letter cl-f1 produced, as she sent it.

**Her first message.** "Now please write my cover letter for the Juniper Flats coaching job. I'm uploading it on their site with resume.txt. Use the letter I sent Silver Larch last week, letter-silver-larch.txt, as a sample of how I write."

**Replies.** The same as cl-f1's: "I don't know it" if the skill asks for the hiring manager's name, and "That's everything I have" to anything else before the draft.

**Test 7, reuse.** `check_letter.py` on the Juniper Flats letter with `--compare letter-silver-larch.txt`:

- The frame and the invitation share no sentence with the Silver Larch letter.
- A shared sentence sits only in a proof paragraph, states a fact the three files hold and is still true. The map in each record says which paragraph is the fit, and the fit shares none.
- Neither letter repeats a sentence within itself.
