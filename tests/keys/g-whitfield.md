# Key: Writer G, Graham Whitfield (positioning tests 1, 4 and 7)

Files: `posting.txt`, `resume.txt` and `linkedin.md`. The run has no web access.

**His first message.** "I'd like to go for this Calder Basin job. The posting, my resume and my LinkedIn text are in the folder. Can you work out my case before I write anything?"

**His reply to the step 2 message.** "Two things I found on their site: their board approved a ten-year, $600 million capital plan in May 2026 (https://www.calderbasinwater.example/board/capital-plan-2026), and all of their sewer lining so far has been done by outside contractors (https://www.calderbasinwater.example/projects/sewer-lining). I'm open to either program. I'll apply on their site. A former colleague, Dana Ruiz, works in their engineering group and said she'd pass my name along."

**His reply at step 9.** "Go with your recommendation. The rest looks right. Save it."

**Test 7, an ambiguous case.** The posting names two programs and says the role will fit the person, and the evidence supports both: nine state revolving fund projects taken to bid on schedule, and the trenchless program he started. The step 9 message asks which case to lead with, names both, recommends one and gives a reason. The case fails if the skill picks one without asking, or merges the two without asking.

**Test 4, no web access.** The step 2 message asks for two or more facts about the firm, each with where it came from. The saved file holds both facts he gave, sourced to his answer or his links, with checked dates. The run uses no web tool.

**Test 1, the file's shape.** `check_positioning.py` passes with `--sources --current`.

**Also.** The reader line names Dana Ruiz as a warm referral who said she'd pass his name along.
