# Key: Writer F, Nadia Haddad (positioning tests 1, 5, 7, 8, 9, 10, 11 and 12)

Files: `posting.txt`, `resume.txt` (the resume being sent), `master-resume.md` (last updated November 2, 2025) and `letter-2021.txt` (dated March 2, 2021, to another district).

**Her first message.** "I'm going for the Math Curriculum Coordinator job at Silver Larch. Everything's in this folder: the posting, the resume I'm sending, my master resume, and a cover letter I wrote in 2021 for a coaching job. Can you work out my case before I write the letter? I want to lead with my students' results. I'll upload through their job portal, and nobody's referring me."

**Her reply at step 9.** "That's right. Use 61%, since the resume has it right and the master resume has a typo. I don't have a master's degree and I'm not bilingual. Save it."

Nothing is missing, so the skill needs no step 2 message. If it sends one, she answers: "Everything I have is in the folder."

**Test 8, deeper proof.** Summer Bridge Math is in the proof bank: 120 incoming 6th graders in 2023, and 52% passing the first fall benchmark against 38% of students who didn't attend. It has a story from the master resume, its file and line, the date 2025-11-02, "On the resume being sent: no", and a mark of letter or both.

**Test 9, gap search.** "Experience leading professional development for teachers" isn't a gap. Its row is strong or partial and cites the master resume's line on monthly professional development for 18 teachers. "Experience with a curriculum adoption" isn't a gap either, since the master resume puts her on the 2020 adoption committee.

**Test 10, conflict.** The step 9 message raises 61% on the resume against 63% in the master resume, and says the resume's 61% stands unless she says otherwise. The saved file uses 61% wherever it gives the figure as hers.

**Test 11, aging facts.** The row for "Five or more years teaching middle school math" gives 13 years, worked out from August 2013 to October 2026. The letter's "eight years" never appears as her current experience.

**Test 12, past letters.** `--against letter-2021.txt` lists every sentence the file shares with the letter, and each one is still true. None holds the letter's "eight years" or "for the last two".

**Test 7, one confirmation.** No step 2 message, or one at most, then one confirmation at step 9.

**Test 1, the file's shape.** `check_positioning.py` passes with `--sources --current --against`.

**Test 5, reuse.** After the file is saved, a new helper gets her first message again. It finds the file, runs `--current`, reuses it without rebuilding, and stops. The file's SHA-256 doesn't change.
