# Test 16: the second direction

New in 0.2.0. When the posting has a positioning file, the conversation checks the finished piece against that file after the blind report, under its own heading, and the reviewer never sees the file.

- Date: 2026-10-05. Product: Claude Code in the Claude desktop app on Windows 11.
- The piece: the resume resume-ops 2.4.0 built for writer E from her confirmed positioning file. The resume, the file and the build's conversation are in `positioning-runs/e-resume/`.
- The packet: built by `build_packet.py` 0.1.2 from this repository, with `--type resume`, the posting as the target and `--channel upload`. Its voice rules came from the installed plainspeak-writer 1.4.1. The positioning file isn't in it.
- The reviewer: the installed `job-seeker-ops:submission-reviewer`, started with the printed line and nothing else. Its instructions are the same in 0.1.3 and 0.2.0.

## The blind report

It's word for word in `positioning-runs/e-resume/review.md`. In short:

- "blind: yes". The reviewer saw an account email, tool instructions and environment details, and no saved memory, profile, project instructions, earlier conversation or git snapshot. It opened the four packet files and the rules file, nothing else.
- First take: "This is a distribution center shift supervisor with 10 years at one company who opened a new cross-dock and took on-time shipping from 79% to 98% in five months. That's the exact problem in this posting, so I keep reading. Fit: yes"
- Verdict: Fix first, on two must-fix findings. The checker blocks the three date ranges under R01, and the posting's required OSHA 30-hour card is missing.

## Against the positioning file

`check_positioning.py --piece out/Renata-Castillo-Resume.docx --as resume` found no watch phrase on the page and found all five proofs there. The note written from it and the report:

**Against the positioning file**

- The first take lands on line 4 of the case: "Renata has brought a new building up to speed before, and she can do it again for a shift at Sparks."
- Must-fix 2, the OSHA 30-hour card, is gap R3. The file keeps it off the page, so the resume leads with Fernley. Earning the card before applying is her call, and if she does, the file and the resume can both change.
- Must-fix 1 isn't a gap. resume-ops writes a date range as "Jan 2022 – Present", and plainspeak-writer 1.4.1 blocks that dash. The fix belongs in plainspeak-writer's next version.
- P1 to P5 all show on the page, and no phrase from section 7 does.

## Result

Pass. The reviewer stayed blind, and the second direction sorted the two must-fix findings: one is a known gap the person can act on, and one comes from two tools that disagree about dates.
