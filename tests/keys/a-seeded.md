# Key: Writer A, seeded letter (tests 7 and 8)

Packet: `a-quintero/letter-seeded.txt` with the posting and the resume as target and companion, channel upload. The letter is the clean letter with eight flaws planted, one of each kind the spec names.

| # | Planted flaw | Words to look for | Expected check | Expected class |
|---|---|---|---|---|
| 1 | A dash used for drama | "22 minutes — down by 16" | Voice, checker R01 | Must fix while the checker lists R01 under HARD |
| 2 | "Not just X but Y" | "wasn't just a triage fix but" | Voice, checker R02 | Must fix while the checker lists R02 under HARD |
| 3 | A claim with no proof | "known across the hospital as a leader people want to work for" | Proof | Should fix |
| 4 | A coined internal name | "Q-Ladder" | Voice, as a block found by reading (internal method names); Clarity may name it too | Must fix |
| 5 | A vague place | "keep the room calm" | Voice, checker R44 warning | Should fix |
| 6 | An opening that could go to any firm | "I'm excited to apply for the Clinic Operations Manager position at your organization" | Proof | Should fix |
| 7 | A line that names a gap | "I was out of work for most of a year" | Risk | Must fix |
| 8 | A date that disagrees with the resume | "Since becoming nurse manager in 2017" (the resume says Mar 2019) | Risk | Must fix |

**Test 7 passes when:**

- The verdict is Fix first and the first take ends `Fit: yes`.
- Flaws 1, 2, 4, 7 and 8 are must-fix, each quoting the planted words, and no other finding is must-fix.
- Flaws 3, 5 and 6 each appear as should-fix, in full or in a one-line entry past the fifth.
- No finding supplies replacement wording or a sample sentence.

If a newer checker moves R01 or R02 from HARD to WARN, that flaw moves to should-fix and the verdict stays Fix first.

Other should-fix findings are fine, such as R41 on "I have long admired," P10 on "just" in the same line as flaw 2, list-of-three warnings, and the one-sentence-paragraph warning. Any of those warnings may also be cleared with a reason on the "Cleared warnings" line. plainspeak-writer 1.4 still lists R01 and R02 under HARD, so flaws 1 and 2 stay must-fix.

**Test 8 passes when** all three runs give the same verdict and their must-fix lists name the same problems: the same quoted words under the same checks. The order and wording of the explanations can differ, and so can the should-fix lists.
