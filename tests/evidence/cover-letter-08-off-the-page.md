# Cover letter test 8: off the page

Spec: "The gap and the concern from the positioning file never appear."

Two checks on each final letter: `check_letter.py`, which fails any phrase from section 7 on the page, and `check_positioning.py --piece --as letter`, submission-review's second direction. Both found no phrase in any letter. Then each letter was read for the gap and the concern in other words.

| Run | Section 7 holds | On the page |
|---|---|---|
| cl-f1 | No master's degree, not bilingual, no reporting to district leaders; the concern that she hasn't led an adoption across four schools; the Hollyhock application | None of them. The adoption is answered by the 2020 committee and the Basalt Creek sessions, without naming what she hasn't done |
| cl-e1 | No OSHA 30-hour card, no Spanish, no Lean or Six Sigma, no start-up meetings or safety audits; the concern that Fernley was smaller; why she's leaving | None of them. The size concern is answered by the shift of 35 and her years on every floor. No departure story |
| cl-g1 | No board reporting; the concern that his lining work dates from 2017 to 2020 | None of them. The lining work stands on the specifications the utility still uses |
| cl-b1 | No freight work; the concern that he planned grocery demand; the 2020 reorganization, his reason for looking and pay | None of them. The freight concern is answered by his warehouse years, in a paragraph of their own |

The reviews tested this too. cl-e1's reviewers both raised the missing OSHA card as must-fix, and the skill kept it open rather than name it (test 9). cl-b1's reviewer raised freight as should-fix, and the skill left it open "on purpose. Freight is the gap your positioning file keeps off every page".

**Without the skill.** The same request for writer E with no skill kept every gap off the page too, but used a home-page fact, "all 42 of your stores", which her file had kept out, and `check_letter.py` failed it.

## Result

Pass.
