# Candidate positioning live tests: Claude Code, job-seeker-ops 0.4.4

Every test in `tests/RUN-TESTS-positioning.md`, run on the build that went public.

## The setup

- Date: 2026-10-08.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app on Windows 11. Python 3.12.10.
- The skill: the installed copy of job-seeker-ops 0.4.4, the same as for the cover-letter tests. resume-ops is the plugin's own copy, 2.4.4.
- Runs, each in a fresh general-purpose helper with its folder in `..\jso-tests\v044\pos\`:
  - e1, f1, g1 and h1 build writer E's, F's, G's and H's files;
  - f-reuse sends writer F's first message again in her folder;
  - e-resume and e-resume-nofile build writer E's resume with and without her file.
- What the helpers were told: the protocol's message, plus one line for E, F and H to use WebSearch and WebFetch only, never a browser. G's message says the session has no web access.
- Writer H: the posting text saved on October 5 from https://careers.sharp.com/job/oceanside/clinical-nurse-educator-operating-room-sharp-tri-city-full-time/1031/100098116784, which still answered 200 on October 8. Her files stay on this computer.
- Copies: `tests/evidence/positioning-runs/v044/` holds the hand-backs, scans, saved files and resumes for every run but H's.

## Results

| Test | Result | Evidence |
|---|---|---|
| 1. The file's shape | Pass | The five files these tests saved pass `check_positioning.py --sources --current`, `--for resume-ops` and `--for cover-letter`: writers E, F, G and H, and writer F's Juniper Flats file from cl-f2-positioning. Writer F's passes with `--against` too. The plugin's resume-ops reads each one as "use it". |
| 2. No invention | Pass | Writer E's OSHA 30-hour card is R9, "gap, owned by the role", shown off, with her 10-hour card named as a different card. Spanish (R13) and Lean or Six Sigma (R14) are gaps too. |
| 3. What the firm is buying | Pass | Line 1 of writer E's case is a supervisor who can take Sparks "from 82% on time to its 97% goal". P1 is the Fernley cross-dock opening. |
| 4. Firm facts | Pass | Writer E: five facts from the posting and her saved pages, each with a non-home page on ironwoodtrail.example and a checked date, and "the home page's store count, founding year and free returns" left out. Writer G: the step 2 message asked for two facts with their sources, the file holds both with his links and the date, and the run made no web call. Writer H: five facts from Sharp's pages, each with a checked date, all five links answer 200 under `--check-links`, and none is a home page. |
| 5. Reuse | Pass | f-reuse found writer F's file, ran `--current`, kept it and stopped. The file's SHA-256 and time didn't change, and no new file appeared. |
| 6. Off the page | Pass for the resume | The resume the plugin's resume-ops built from writer E's file passes `positioning_check.py --resume`. It names none of her gaps, and nothing about leaving Tumbleweed. With the file, the Level Set names it, the brief has a POSITIONING line, and the delivery offers a submission review. Without it, none of the three appears. |
| 7. One confirmation | Pass | Writer E stopped twice, at step 2 and step 9. Writer F stopped once, at step 9. Writers G and H stopped twice each. Writer G's choice between the two programs reached him at step 9 as one question with a recommendation and a reason. |
| 8. Deeper proof | Pass | Summer Bridge Math is P3, with its story, master-resume.md L13 (2025-11-02), "On the resume being sent: no" and "Use on: both". |
| 9. Gap search | Pass | Leading professional development (R3, R9) and the curriculum adoption (R13) are strong, from the master resume. |
| 10. Conflict | Pass | The step 9 message asked "61% or 63%?" with the resume's 61% as the default. The saved file gives 61%, and names 63% only as the master resume's typo. |
| 11. Aging facts | Fail, as the key is written | The row for five or more years of teaching gives "About six years as a classroom math teacher", August 2013 to June 2019, and leaves her years as chair out because "the resume doesn't say how many classes she teaches as chair". The key expects 13 years, August 2013 to October 2026. The 2021 letter's "eight years" isn't used. |
| 12. Past letters | Pass | `--against letter-2021.txt` finds no shared sentence. |
| 13. Its own files | Pass | See `own-files-0.4.4.md`. |

12 of 13 passed.

## On test 11

The file is careful rather than wrong. It works the years out from the dates and keeps her chair years apart, since the resume doesn't say she taught then. Her own P4 says she piloted textbooks "in her own classes" in 2020, though, so the file's evidence answers the question it left open. In the same session, cl-f2-positioning asked her outright whether she kept teaching as chair, and kept the narrower count when she didn't say. Either the skill asks that question whenever a role change leaves the count open, or the key accepts the narrower count when the file says why. That's the owner's call.

## Worth a look

- Writer E's firm website didn't load and a web search found nothing, so her facts come from the pages she saved on October 4. The file says so.
- resume-ops asks its intake questions one at a time, such as whether to reorder her title, so writer E's resume runs stopped more often than candidate positioning does. That's resume-ops's own design, and no positioning test counts those stops.
