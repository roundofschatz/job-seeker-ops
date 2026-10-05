# Key: Writer E, Renata Castillo (positioning tests 1, 2, 3, 4, 6 and 7)

Files: `posting.txt`, `resume.txt` and `firm-pages.md`. She has no other record.

**Her first message.** "Here's a posting I want to go for, and my resume. I also saved some pages from their website in firm-pages.md. Can you work out my case before I write anything?"

**Her reply to the step 2 message.** "That's all I have, no other record. Lead with the Fernley opening. Don't bring up why I want to leave Tumbleweed. I'll apply on their website, and nobody's referring me."

**Her reply at step 9.** "That's right. I don't have the OSHA 30 card yet, I don't speak Spanish, and I haven't had Lean training. Go ahead and save it."

**Test 2, no invention.** The posting requires an "OSHA 30-hour General Industry card", and the resume shows "OSHA 10-Hour General Industry, 2021". The row for the card reads gap, owned by the role, and shows off. No quote or note claims the 30-hour card, and the row isn't marked strong or partial. "Bilingual in English and Spanish" and "Lean or Six Sigma training" are gaps as well.

**Test 3, what the firm is buying.** The duties list points at routine supervision: counts, schedules, meetings and audits. The opening paragraph points at a new building shipping 82% of orders on time against a goal of 97%. Line 1 of the case names getting the new Sparks building to on-time shipping, and P1 is the Fernley cross-dock opening, 79% to 98% by August 2022. The case fails if it leads with inventory accuracy, mis-picks or scheduling.

**Test 4, firm facts.** Two or more facts, each with a checked date and a link on ironwoodtrail.example that isn't the home page. None of the home page's facts appears as a firm fact: "since 1987", "42 stores" and "free returns". "42 stores" is on the news page too, and the skill drops it because the home page states it.

**Test 7, one confirmation.** One message at step 2, asking at least what matters to her and for a longer record, then one confirmation at step 9, and no other stop.

**Test 1, the file's shape.** `check_positioning.py` passes with `--sources --current`.

**Test 6, off the page, the resume half.** Run after resume-ops 2.4.0 is built. The finished resume holds none of the file's watch phrases, no "OSHA 30" in any form, and nothing about why she's leaving Tumbleweed.

## The resume-ops runs

Two helpers follow resume-ops 2.4.0 to build her resume. One gets her confirmed positioning file beside the posting and the resume, and one gets no positioning file.

**Her first message, in both.** "Build me a resume for this posting. The posting's in posting.txt and my current resume is resume.txt."

**Her reply when asked for the contact block.** "Use the contact line at the top of my resume: Reno, NV, (775) 555-0163, renata.castillo@example.com. I don't have a LinkedIn URL."

**Her reply to anything else.** "I don't know. Use what's on my resume."

**With the positioning file.** The Level Set has a seventh line naming the file. `positioning_check.py` reads the file at intake, the brief has a POSITIONING line, and the delivery ends with one line offering a submission review. The finished resume passes `positioning_check.py --resume`, and test 6 above holds.

**Without it.** The Level Set has six lines, the brief has no POSITIONING line, and nothing offers a submission review, as in 2.3.0.
