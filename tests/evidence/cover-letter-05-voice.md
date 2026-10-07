# Cover letter test 5: voice

Spec: "plainspeak-writer's checker finds no HARD hits on any letter."

`check_letter.py --voice` runs plainspeak-writer 1.6.2's `check_voice.py --surface letter` on each final letter. 1.6.2 is both the installed copy and the newest commit in its repository (577a985).

| Run | File checked | HARD | Warnings |
|---|---|---|---|
| cl-f1 | the Word file | 0 | 0 |
| cl-e1 | the Word file | 0 | 0 |
| cl-g1 | `letter.txt`, the text box form | 0 | 0 |
| cl-b1 | `cover-letter-switchgrass-freight.txt`, the email | 0 | 0 |
| cl-f2 | the text copy of the Word file | 0 | 0 |

The first check of cl-e1's Word file gave one warning, "V04 staccato layout", because the script handed the checker each header line as a paragraph of its own. That was the script's fault, not the letter's: the same letter as text gave none. `check_letter.py` now lays a Word file out the way its text form is written, with the contact block and the sign-off as blocks, and the warning is gone. The cl-f1 helper had cleared the same warning by reading, for the same reason.

## Result

Pass.
