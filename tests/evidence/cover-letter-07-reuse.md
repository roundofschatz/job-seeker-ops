# Cover letter test 7: reuse

Spec: "Two letters for one writer to two firms, checked by the shared-sentence script: a sentence they share states the same proven fact from the three files and is still true, and the frame, fit and invitation share none. A sentence from an earlier letter whose fact runs on time, such as "for eight years" written three years ago, doesn't move unchanged. No sentence repeats within either letter."

Two runs for writer F on October 7, 2026. In cl-f2-positioning, candidate-positioning built her case for a second posting, Middle School Math Instructional Coach at Juniper Flats School District. The file passes `check_positioning.py --sources --current --for cover-letter`, with no fact from the district's home page. In cl-f2, she asked for that letter and gave cl-f1's Silver Larch letter as her sample: "Use the letter I sent Silver Larch last week, letter-silver-larch.txt, as a sample of how I write."

**The shared-sentence script.** `check_letter.py` ran on the Juniper Flats letter with `--compare letter-silver-larch.txt`, and on the Silver Larch letter with `--compare` set to the Juniper Flats one, each against its own positioning file. Both found 0 shared sentences and passed, and neither letter repeats a sentence within itself.

**The closest pairs.** No sentence moved word for word. The two nearest pairs, by difflib's similarity ratio, are both proofs:

| Ratio | Silver Larch | Juniper Flats | Juniper Flats map row |
|---|---|---|---|
| 0.75 | "From 2022 to 2024 I ran a monthly session for 18 math teachers from three Basalt Creek middle schools, on how to read unit test results and plan reteach lessons from them." | "From 2022 to 2024 I also led monthly professional development for 18 math teachers from three middle schools in the Basalt Creek School District, on how to read unit test results and plan reteach lessons from them." | Proof, P2 |
| 0.70 | "When I mentored four Columbia Plateau University student teachers, the part I liked best was helping a new teacher see which lessons were working, and that's the coaching I'd bring to your new teachers' classrooms." | "Before I became chair, I mentored four of Columbia Plateau University's student teachers, and I liked helping a new teacher see which lessons were working more than any other part of it." | Proof, P3 |

Each states a fact from a story in the Juniper Flats file, and each fact is still true. The sessions ran from 2022 to 2024, and the mentoring ended before 2019. The Silver Larch sentence about the student teachers ends on what she'd bring to Silver Larch, and the Juniper Flats one leaves that part out.

**Frame, fit and invitation.** The record's map puts the frame in paragraph 1, the fit in paragraph 4 and the invitation in paragraph 5. Each is built on Juniper Flats' own facts: the board's August report that 7th grade scores fell for a second year (F3), seven of the 11 new math teachers in their first year (F1), and the 34 new teachers with a coach for each new math teacher all year (F2). The nearest fit sentence, "I'd run the monthly session for all of your middle school math teachers the way I ran the Basalt Creek sessions," scores 0.61 against her Silver Larch plan to train that district's 30 math teachers on a new curriculum, and names a different job. Line 4 and the ask differ too:

- Silver Larch: "I'd like to talk about the common unit assessments I'd build to go with your new math curriculum."
- Juniper Flats: "I'd like to talk about the 7th grade math scores your board heard about in August, and what your new teachers' common unit assessments would need to show them."

**Facts that run on time.** Neither letter has "eight years", "for the last two" or "five years now", the counts in cl-f1's samples (test 13). In the Juniper Flats letter, "have chaired its math department since then" stays true while she holds the job, and every other time it gives is a closed span or a year. Three things from the Silver Larch letter stayed out because this file doesn't hold them, as the record's "Off the page" row says: the 2023 summer program, the 2020 textbook committee, and regrouping every three weeks.

**The rest of the run.**

- plainspeak-writer 1.6.2 finds 0 HARD hits and 0 warnings.
- The body is 371 words in five paragraphs.
- The Word file is `Nadia_Haddad_CoverLetter_JuniperFlatsSchoolDistrict.docx`, with "Nadia Haddad" as author. It measures 0.72 of a page against the script's estimate of 0.76.
- One blind review said Send, so no second ran. The skill took five of its ten should-fix findings and gave the reason for leaving each of the others open.
- The hand-over gives the watermark line once, without "[C24]" (test 11).
- The scan finds no call that names `master-resume.md` or `letter-2021.txt`, though both were in her folder.

The hand-back, letter, record and scan are in `cover-letter-runs/cl-f2/`.

## Result

Pass.
