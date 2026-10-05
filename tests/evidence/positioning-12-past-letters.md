# Positioning test 12: past letters

Spec, as the owner ruled on October 5: a sentence may move from a past letter into the file when it states the same proven fact and is still true, and no sentence repeats word for word within the file. The spec's first version let no sentence move at all, and `CHANGELOG.md` records the change.

- Run f1, writer F, with her 2021 letter in the stamp as a past letter. Files: `positioning-runs/f1/`.

## The check

`check_positioning.py --against` read the letter and reported: "letter-2021.txt: 0 sentence(s) shared with this file." The shape check, which fails any sentence the file says twice, passed.

The skill used the letter as a fact source and put its facts in new words. P1 cites `letter-2021.txt L7` for when she began moving the department to common unit tests, and P5 cites `L9` for what she liked about mentoring. The letter's out-of-date "eight years" and "for the last two" appear nowhere.

## Result

Pass.
