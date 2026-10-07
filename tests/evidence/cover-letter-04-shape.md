# Cover letter test 4: shape

Spec: "Four movements, a body of 500 words or fewer by code, and one page in the Word file."

Five letters from runs on October 7, 2026. The words are `check_letter.py`'s count of the body, between the salutation and the sign-off. The movements are the rows of each letter's map in section 9 of its positioning file, which `check_positioning.py` checks: Frame, Proof, Fit and why now, Invitation, Referral and Off the page.

| Run | Channel | Body words | Paragraphs | Map rows | Page |
|---|---|---|---|---|---|
| cl-f1 | upload | 382 | 5 | 6 of 6 | 0.72 measured, 0.78 estimated |
| cl-e1 | upload | 352 | 5 | 6 of 6 | 0.55 measured, 0.57 estimated |
| cl-g1 | text box | 355 | 5 | 6 of 6 | no Word file |
| cl-b1 | email | 350 | 5 | 6 of 6 | no Word file |
| cl-f2 | upload | 371 | 5 | 6 of 6 | 0.72 measured, 0.76 estimated |

Every body sits inside the 350 to 450 target and under the 500 cap. Each letter opens on the posting's measure or the firm's problem, gives two to five proofs in the middle, uses two or more firm facts, and ends on line 4 of its case followed by one named topic.

**The page.** Neither Word nor LibreOffice is on the test computer, so no file was rendered. `tests/tools/measure_page.py` wraps each paragraph with the real font's character widths from `calibri.ttf` and adds each paragraph's spacing and the font's line height. `check_letter.py`'s estimate came out at or above the measurement on all three files, so it leans the safe way. cl-e1's file has its resume's half-inch margins and 10.5 point type, which is why it fills less of the page.

## Result

Pass.
