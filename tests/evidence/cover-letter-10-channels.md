# Cover letter test 10: channels

Spec: "A text box letter fits its limit, an email letter has a subject line, and the Word file names the writer as author. No PDF anywhere."

| Run | Channel | What came out | Checked by |
|---|---|---|---|
| cl-f1 | upload | `Nadia_Haddad_CoverLetter_SilverLarchSchoolDistrict.docx` and a text copy, with "Nadia Haddad" as author, the twelve parts Word writes and no Application line. It has one column and no table, text box, header or footer. Her resume is text, so the build used Calibri 11 with one-inch margins | `check_letter.py` on the Word file |
| cl-e1 | upload | `Renata_Castillo_CoverLetter_IronwoodTrailSupply.docx` and a text copy, with "Renata Castillo" as author and Calibri at 10.5 point with half-inch margins, taken from her Word resume. The header matches that resume's contact block | `check_letter.py` with `--resume Renata-Castillo-Resume.docx`, and the file's own styles |
| cl-g1 | text box, 3,000 characters | `letter.txt`, 1,986 characters counted the way the packet counts them, from the salutation down, with straight quotes and no bold or bullets | `check_letter.py --channel textbox --limit 3000` |
| cl-b1 | email | `cover-letter-switchgrass-freight.txt`, first line "Subject: Supply Chain Planning Analyst application", "Dear Maria Lopez," with no contact block. The hand-over ends "Remember to attach your resume when you send it to Maria Lopez." | `check_letter.py --channel email --given "Maria Lopez"` |

No run folder holds a PDF.

**Without the skill.** The same request for writer F saved only a text file and offered "If the portal wants Word or PDF, I can make one." The request for writer E made a Word file whose properties say it was made in "Microsoft Macintosh Word", a program it wasn't made in.

## Result

Pass.
