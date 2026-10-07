# Job Seeker Ops

Job Seeker Ops is a Claude plugin for job-search writing. It sits beside two tools that stay separate: plainspeak-writer, which writes in a plain human voice, and resume-ops, which builds resumes. Version 0.3 holds three pieces. Candidate positioning works out the case for a posting before anything gets written, cover letter writes the letter from that case, and submission review checks a finished piece before it goes out.

## Candidate positioning

Before a resume or a letter gets written, candidate positioning works out the case for one candidate and one posting and saves it in one positioning file. resume-ops 2.4.0 reads the file to decide which proof leads and where the summary points, and cover letter reads it for the reasoning behind the letter and keeps each letter's record in it. So the case gets settled once, from the evidence, rather than twice in two drafts.

It reads the posting and the resume being sent, plus anything else the person shares, such as a master resume, LinkedIn text, a career record, portfolio pages, past letters or notes. Then it:

1. Finds what the hiring team is buying, from the problem the posting describes rather than its list of duties.
2. Maps every requirement to the evidence that answers it, with the file and line, and names the gaps.
3. Looks up the firm for facts from the posting and the firm's other pages, never its home page.
4. Writes the hiring team's view after an imagined interview, and the case in four lines.
5. Ranks three to five proofs, each with its story and source, and lists the words the candidate can claim.
6. Shows the person the case once, with any conflict between sources or any choice between two readings as a question, and saves the file once they confirm it.

The gaps, the hiring team's concern and anything private stay in the file. They decide which proof leads, and nothing the person lacks goes on a page a reader sees.

A script, `check_positioning.py`, checks every file: the sections, a source for every row and proof, each quote against its file and line, whether a source changed since the person confirmed the file, and plainspeak-writer's voice check on the sentences a resume or letter will reuse.

## Cover letter

Cover letter writes one letter for one posting from three files: the positioning file, the posting and the resume that goes with the letter. The resume is the evidence, and the letter is the reasoning: why this firm, why this seat, why now, proved by two or three named results. The person's deeper record reaches the letter only through the positioning file, and with no positioning file the skill offers candidate positioning instead of working out a case of its own.

It:

1. Checks that the positioning file is confirmed and current, holds two firm facts, and agrees with the resume going with the letter on every figure the letter will use.
2. Maps the four movements (the frame, the proof, the fit and why now, and the invitation) before writing a sentence, and saves the map in the positioning file.
3. Drafts with plainspeak-writer, matching the person's own writing when they share some. A phrase plainspeak-writer blocks in that writing never comes back, and a sentence from it moves into the letter only with a fact the files still hold.
4. Checks every number, date and name in the letter against the three files by script, along with the length, the channel's rules and every phrase on the positioning file's keep-off list.
5. Has submission review's blind reviewer read the draft, twice at most, before the person sees it.
6. Hands over the letter with the results, and saves it as a Word file for an upload, the text for a text box, or the email itself, with its record in the positioning file. It never makes a PDF.

A tailored letter is worth the work. In one resume company's field test, applications with a letter tailored to the job drew 53% more callbacks than applications with no letter [C16]. Source IDs in square brackets point to `skills/cover-letter/references/sources.md`, where each one has its date, grade and link.

### The watermark

Current Claude models put an invisible watermark in the text they write. It's added at the model level, so it's there in Claude Code and Cowork as well as the Claude apps. It travels with copied text and can last through some editing, and detecting it in text is in private preview for eligible organizations [C24, C25]. A letter this skill drafts may have it. The skill says so when it hands over a letter, and it never tries to remove, hide or get around the mark.

The skill builds each letter for the person to finish. The facts come from their own files, and the hand-over points to the two sentences only they can write: the opener and the topic they'd like to talk about. In one study of a freelance platform, more time spent editing an AI-drafted letter went with a better chance of winning the job, though the study doesn't show the editing caused it [C15].

## Submission review

A reviewer reads a finished cover letter, resume, outreach note, referral blurb, LinkedIn About section or application answer the way its real reader will: a recruiter's ten-second first look, a hiring manager reading closely, and an AI grader checking the posting's requirements. It returns quoted findings and a verdict of Send, Fix first or Rethink.

The reviewer never saw how the piece was made. The conversation that wrote a letter knows the career record, the strategy and every draft, and that knowledge fills the gaps a real reader would stop at. So the review runs in a separate helper that sees only a packet of files.

### How the review stays blind

- A script builds the packet: the piece, the posting, any document the reader also sees (such as the resume sent with a letter), plainspeak-writer's checker output and a manifest. The script has no field for notes, and it leaves original file names out.
- The helper starts with one fixed line that names the packet folder. It checks that line word for word and marks the review "blind: no" if anything was added.
- The helper's only tool is Read. It opens the files the manifest names and can't search for others, and it can't edit anything.
- It skips project instruction files (CLAUDE.md), which helpers load by default.
- Its report opens with what it received and whether the review was blind.

**The second direction.** When the posting has a positioning file, the conversation checks the piece against that file after the report, under its own heading. It notes whether the reviewer's first take lands on what the case says the reader should believe, whether a must-fix finding falls on a gap or the concern, which proofs made it onto the page, and any phrase from the file's keep-off list that shows up. The reviewer never sees the file, so the review itself stays blind.

**One limit in Cowork.** Cowork gives every helper the account's saved memory, and no setting in the plugin can turn that off. If your saved memory holds your career history, a Cowork review sees it and says "blind: no." For a fully blind review, run it in Claude Code, such as the Code tab in the Claude desktop app, which doesn't load the Claude app's saved memory.

### What the report holds

1. What the reviewer received, and whether the review was blind.
2. A first take in the reader's voice, two sentences at most, ending on whether the writer fits.
3. The verdict, set by fixed rules.
4. Up to five must-fix and five should-fix findings. Each quotes the line, names the check and says what goes wrong for the reader. A finding can point toward a fix, but it never supplies new wording.
5. Each requirement in the posting, marked shown, claimed without proof, or missing.
6. What the reviewer couldn't judge, since it has no career record to check facts against.

A finding is must-fix when it's a HARD hit from plainspeak-writer's checker, a block from plainspeak-writer's rules found by reading, a risk to the application, a missing must-have requirement when the AI grader is reading, or a piece over a hard character limit. Risks include a gap named outright, an apology, an exit story, negative talk about an employer, and a title, date, company or figure that disagrees with the resume.

The verdict is Rethink when the first take sees no fit, when there are more than five must-fix findings, or when more than half the must-have requirements are missing. It's Fix first for one to five must-fix findings, and Send for none.

## Install

**Cowork and the Claude desktop app.**

1. Get `job-seeker-ops.zip` from the Releases page, or zip this folder yourself, leaving out `tests/`.
2. Open **Customize**, then **Plugins**, then **Add**, then **Upload plugin**, and choose the zip.
3. Start a new Cowork task. A plugin loads when a task starts.

Install it under Plugins, not Skills. A skill upload drops the reviewer, and the review then refuses to run. A plugin on your account also shows up in Claude Code at its next session start.

**Claude Code.** Run `claude --plugin-dir ./job-seeker-ops` to load it for one session. A marketplace listing comes with the first public release.

**What it needs.** Python 3.8 or newer runs the scripts. plainspeak-writer runs the voice checks; without it, the review marks voice as unchecked and runs everything else, and a positioning file's stamp says its voice check didn't run. Cover letter needs plainspeak-writer for the voice, and stops without it. resume-ops reads a positioning file from version 2.4.0 on, and an older resume-ops builds without it. Chat on claude.ai doesn't run plugin helpers, so the review needs Cowork or Claude Code.

## Use

Give Claude the posting and your resume, plus anything else you have, and ask for your case:

> Work out my case for this posting before I write anything.

> What should my resume and cover letter lead with for this job?

Then ask for the letter:

> Write my cover letter for this posting. I'm uploading it with the resume in this folder.

> I need a cover letter for the Ironwood job. Their form has a text box that takes 3,000 characters.

For a review, give Claude the finished piece and the posting:

> Review this cover letter against the posting before I send it.

> Is this LinkedIn About section ready for recruiters?

> Run a submission review on my resume for this job.

Claude asks once for anything missing, builds the packet, starts the reviewer and hands back its report unchanged. A second opinion is a new review with a new packet, never the same reviewer changing its mind. A writing skill that calls the review runs it twice at most per piece, then hands the open findings to the person.

## Files

```
job-seeker-ops/
├── .claude-plugin/plugin.json      name, version and description
├── agents/submission-reviewer.md   the reviewer's instructions
├── skills/candidate-positioning/
│   ├── SKILL.md                    the ten steps that build a positioning file
│   ├── references/format.md        the file's format, with a full example
│   ├── references/case.md          finding what the firm is buying, and the case
│   └── scripts/check_positioning.py  checks a positioning file
├── skills/cover-letter/
│   ├── SKILL.md                    the nine steps that write a letter
│   ├── references/letter.md        the letter's shape, the map, the channels, a full example
│   ├── references/checks.md        every check, what runs it, and the hard fails
│   ├── references/sources.md       the research behind the rules
│   ├── scripts/check_letter.py     checks a letter against the three files
│   └── scripts/build_letter.py     writes the Word file
├── skills/submission-review/
│   ├── SKILL.md                    the steps Claude follows to start a review
│   └── scripts/build_packet.py     builds the packet
├── tests/                          tests and test pieces, left out of the install zip
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Tests

- `python3 tests/unit/run_tests.py` runs every unit test: the packet script's, the positioning checker's, cover letter's two scripts and its sources, and the check that `plugin.json`, the changelog and a built package agree.
- `tests/RUN-TESTS.md` holds submission review's live tests: isolation, leaks, seeded flaws, repeat runs and the rest.
- `tests/RUN-TESTS-positioning.md` holds candidate positioning's live tests. Every test piece comes from made-up writers, and writer H applies to a real posting, which isn't stored here.
- `tests/RUN-TESTS-cover-letter.md` holds cover letter's live tests, with made-up writers too.

## Contributing

- Keep it general, with no personal details, clients or private work in any file.
- Build on what's here instead of replacing it.
- Log every change in `CHANGELOG.md`: what was added, changed or removed, and why.
- Run plainspeak-writer's checker on every file you change.
- Give every change to a shipped file a new version. Build the package from the release commit, so it matches the commit byte for byte: `git archive --format=zip --prefix=job-seeker-ops/ -o dist/job-seeker-ops.plugin HEAD .claude-plugin agents skills README.md CHANGELOG.md LICENSE`.
- The voice rules live in plainspeak-writer. This plugin keeps no copy of them.

## License

MIT. See `LICENSE`.
