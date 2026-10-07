# Cover letter test 12: deeper proof

Spec: "A proof the positioning file marks for the letter that isn't on the resume shows up in the letter, built from its story, and the letter still agrees with the resume on every title, date and figure."

**cl-f1, writer F.** Her file marks P2, P3 and P4 for both pieces, and none is on `resume.txt`. All three are in the letter, told from their stories:

- P2: "From 2022 to 2024 I ran a monthly session for 18 math teachers from three Basalt Creek middle schools, on how to read unit test results and plan reteach lessons from them."
- P3: the four-week summer program for 120 incoming 6th graders in 2023, and "That fall 52% of them passed the district's first math benchmark".
- P4: the 2020 textbook review committee and the two finalists she piloted.

`check_letter.py` reports each of those numbers as coming from the proof's deeper record, and fails nothing. The letter gives her result as 61%, the resume's figure, never the master resume's 63%. Her title, Math Department Chair since 2019, matches the resume.

**cl-g1, writer G.** His P1 is on the resume, but its story draws on his LinkedIn text, which the resume leaves out. The letter gives all three of those details through the positioning file: "the utility still uses the specifications I wrote for cured-in-place pipe lining", "I also ran the resident meetings before each street was lined", and "each mile of lined pipe drew about a quarter of the complaints that a mile of open-trench work did". The helper never opened `linkedin.md` (test 1). The figures match the resume: 14 miles, about 40% of the cost, nine projects, $31 million.

## Result

Pass.
