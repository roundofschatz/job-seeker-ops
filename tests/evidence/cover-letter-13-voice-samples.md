# Cover letter test 13: voice samples

Spec: "A sample with a blocked phrase gets flagged before drafting, and that sentence never shows up in the letter. Any sentence the letter shares with a sample, found by the shared-sentence script, states a fact the three files hold and is still true."

Run cl-f1. Writer F picked two samples: her 2021 letter to another district, and `note-to-families.txt`, a May 2024 note from `tests/letters/f-haddad/` with two phrases plainspeak-writer blocks and a count of years that has since gone stale.

**Before drafting.** At its 14th tool call, before it loaded plainspeak-writer, the helper ran `check_letter.py --sample` on both. The 2021 letter blocked nothing. The note had two sentences set aside: the one with the dash ("Our 8th graders' math results are in" followed by a dash) and "That growth is not just a number, but a sign of what our teachers built together." Its one message before the draft says so: "note-to-families.txt: 2 sentences set aside, so they won't go into the letter." It also lists the stale lines it would keep out: the 2021 letter's "eight years", the note's "five years now", and the 2021 letter's invitation, written for another district.

**In the letter.** Neither blocked sentence is in it, and neither are "eight years", "for the last two" or "five years now". `check_letter.py` with both samples on the final Word file finds no sentence shared word for word and no stale count of years.

One sentence comes close to the 2021 letter's mentoring line, rewritten for this posting: "When I mentored four Columbia Plateau University student teachers, the part I liked best was helping a new teacher see which lessons were working". Its fact is in the file's P5 story and still true.

## Result

Pass.
