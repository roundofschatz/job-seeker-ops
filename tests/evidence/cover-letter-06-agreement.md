# Cover letter test 6: agreement

Spec: "A resume whose date differs from the positioning file gets caught before the person sees the draft."

Run cl-e2, October 7, 2026: writer E's confirmed positioning file, built from her `resume.txt`, with `resume-updated.txt` going with the letter. The updated resume gives the Fernley opening as April 2022 and the on-time result as September 2022, where the file and the old resume say March and August. Her message: "Write my cover letter for the Ironwood Trail job, please. I'm uploading it with resume-updated.txt, where I fixed a couple of dates."

The gate's `check_letter.py --positioning FILE --resume resume-updated.txt` failed: P1's story gives Mar 2022 and Aug 2022, which the resume the case was built from held and the resume going with the letter doesn't. The helper stopped before step 2. Its message, in `cover-letter-runs/cl-e2/handback.md`:

- opens "I can't start the letter yet because your positioning file and resume-updated.txt don't agree on two dates";
- names both, "the file says March 2022 and resume-updated.txt says April 2022" and the August and September pair;
- says the letter has to use the updated resume's dates and the file has to match it first;
- offers candidate-positioning to bring the file in line.

No draft was written and none reached her.

The unit test `test_a_resume_that_disagrees_with_a_proof_is_caught_before_drafting` covers the same case with a figure, writer B's 19% against a resume that says 21%.

## Result

Pass.
