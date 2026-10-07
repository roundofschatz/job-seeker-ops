# Cover letter test 2: no positioning file

Spec: "The skill stops and offers candidate-positioning."

Run cl-n1, October 7, 2026: writer F's posting, resume, master resume and 2021 letter, with no positioning file. Her first message: "Write my cover letter for the Math Curriculum Coordinator job at Silver Larch. Everything's in this folder."

The helper made four tool calls: it read SKILL.md, listed the skill's folder and hers, and ran `check_positioning.py --name`, then stopped. Its message, in `cover-letter-runs/cl-n1/handback.md`, opens "I can't write this letter yet. It needs a positioning file first", says what the file holds, and offers candidate-positioning: "Do you want me to start?"

It wrote no file, opened neither the master resume nor the 2021 letter, and worked out no case.

## A fix this run led to

It looked the file up as `positioning-silver-larch-math-curriculum-coordinator.md`, a name built from her shorthand rather than from the posting's own words ("Silver Larch School District", "Math Curriculum Coordinator, Grades 6 to 8"). With no file in the folder the stop was right, but the same guess would miss a file that exists. Step 1 now lists the `positioning-*.md` files first and takes the company and the role from the posting's first lines, and every later run found its file.

## Result

Pass.
