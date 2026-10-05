# Positioning test 6: off the page

Spec: "The gap and the concern never show up in a resume or letter built from the file."

The resume half ran here. The letter half waits for cover-letter, whose spec repeats this test.

- Run e-resume, on October 5, 2026: a fresh helper followed resume-ops 2.4.0 from its repository to build writer E's resume, with her confirmed positioning file from run e1 beside her posting and resume. Files: `positioning-runs/e-resume/`.
- The file's keep-off list holds four gaps (the OSHA 30-hour card, Spanish, Lean or Six Sigma training, and start-up meetings with safety audits), the concern about the size of the building she opened, and why she's leaving Tumbleweed. Each has phrases to watch for.

## The finished resume

- resume-ops's `positioning_check.py --resume` read "RESULT: PASS", with no keep-off phrase on the page.
- job-seeker-ops's `check_positioning.py --piece --as resume` found no watch phrase on the page, and found all five proofs.
- A search of the text for each gap and the concern found one certification line, "OSHA 10-Hour General Industry | 2021", as on her resume. Nothing names the 30-hour card, Spanish, Lean, safety audits or start-up meetings, compares the cross-dock's size with Ironwood's, or says why she's leaving.
- The summary leads where the case points: "Opened a cross-dock in Fernley, NV and brought it up to speed in five months, lifting on-time shipping from 79% to 98%."

## How the build used the file

The Level Set had a seventh line naming the file and its confirmed date. The brief added "POSITIONING: positioning-ironwood-trail-supply-operations-supervisor-distribution-center.md (confirmed 2026-10-05); the evidence overrode nothing", the checks line read "positioning PASS", and the delivery ended with an offer of a submission review. Test 16 ran that review.

The same build with no positioning file, in `positioning-runs/e-resume-nofile/`, had a six-line Level Set, no POSITIONING line and no review offer, as in 2.3.0.

## Result

Pass for the resume. The letter half runs in cover-letter's build.
