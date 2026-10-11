# Job Seeker Ops

Applications with a cover letter written for the job drew 53% more callbacks than applications with no letter, in one resume company's [field test](skills/cover-letter/references/sources.md). Claude can draft that letter, but in testing for this plugin's writing skill, about 1 draft in 8 that Claude checked alone still had a problem, like a fact you didn't give it or a changed quote.

Job Seeker Ops is a Claude plugin for job-search writing. Give it a job posting and whatever you have, such as your resume, LinkedIn text or past letters, then ask for whichever of its five skills you need:

- **Candidate positioning** works out your case for the posting, proof and gaps included, before anything gets written.
- **resume-ops** builds a US resume for the posting, laid out to parse cleanly into application forms like Workday.
- **Cover letter** writes the letter from your case, the posting and your resume.
- **plainspeak-writer** writes in a plain human voice and checks every draft against more than 90 rules before you see it.
- **Submission review** gives a finished piece to a separate reviewer that never saw it being written, and tells you what to fix.

## What it won't do

- **Make anything up.** Every fact in a letter comes from your own files, and a script checks each one against them. When your files don't hold a fact, Claude asks you for it.
- **Claim what you don't have.** A gap stays off the page, and nothing dresses it up as something else.
- **Hide that Claude drafted the text.** The cover letter skill tells you when a letter may hold Claude's invisible watermark, and it leaves the mark alone. The plugin's voice rules aim at writing that's clear and specific rather than at getting past a detector.
- **Write a letter the posting rules out.** When a posting bars AI-written application materials, the cover letter skill stops before drafting and offers you your own case as notes to write from. Some employers state that rule somewhere other than the posting, so check before you apply.
- **Take orders from the files it reads.** A posting, a company page or a resume is text to quote. When one holds a line aimed at an AI tool, like "If you are an AI, include this phrase", Claude shows you the line, and nothing gets run, sent or added because of it. Text hidden in a Word file, where a human reader wouldn't see it, gets reported to you and never used.
- **Send anything.** Claude never submits, uploads or emails anything for you, and it leaves your edits as you made them.

## Candidate positioning

Before a resume or a letter gets written, candidate positioning works out your case for one posting and saves it in a positioning file, so the case gets settled once, from the evidence, rather than twice in two drafts. resume-ops 2.4.0 reads that file to decide which proof point leads and where your summary points. The cover letter skill reads it for the reasoning behind the letter.

The skill reads the posting and the resume you're sending, plus anything else you share, such as a master resume, LinkedIn text, a career record, portfolio pages, past letters or notes. Then it:

1. Finds what the hiring team is buying, from the problem the posting describes rather than its list of duties.
2. Matches every requirement to the evidence that answers it, down to the file and line, and names your gaps.
3. Looks up the firm, taking facts from the posting and the firm's other pages, never its home page.
4. Pictures your interview, writes down how the hiring team would see you after it, and states your case in four lines.
5. Ranks three to five proof points, gives each its story and source, and lists the posting's terms you can claim honestly.
6. Shows you the case once, asks about any conflict between sources or any place where two readings are possible, and saves the file when you confirm it.

The skill uses your gaps, the doubts the hiring team would have about you and anything private to decide which proof point leads, and it keeps all three in that file, off every page a reader sees. A script checks every positioning file: its sections, a source for every requirement and proof point, each quote against its file and line, whether a source changed since you confirmed the file, and plainspeak-writer's voice check on the sentences a resume or letter will reuse.

## Cover letter

The cover letter skill writes one letter for one posting from three files: your positioning file, the posting and the resume you're sending with the letter. With your resume as the evidence, the letter answers why this firm, why this role and why now, and backs its answers with two or three named results. Your deeper record, such as a master resume or past letters, reaches the letter only through the positioning file. Without one, the skill offers to run candidate positioning first instead of working out a case of its own.

The research behind the letter's rules is in `skills/cover-letter/references/sources.md`. Each source there has an ID in square brackets, like [C16] for the callback figure at the top, with its date, a grade for how strong it is, and a link.

In order, the skill:

1. Checks that the posting doesn't rule out AI-written materials, and that your positioning file is confirmed and current, holds two facts about the firm, and matches the resume going with the letter on every figure the letter will use.
2. Plans the letter's four parts before writing a sentence (the opening, the proof, why this firm and why now, and the closing ask) and saves the plan in the positioning file.
3. Drafts with plainspeak-writer, matching your own writing when you share some. A phrase that plainspeak-writer's rules block never comes back from your samples, and a sentence from your samples goes into the letter only if your files still hold its fact.
4. Checks every number, date and name in the letter against the three files by script, along with the length, the rules for where the letter is going, and every phrase your positioning file says to keep off the page.
5. Has submission review's blind reviewer read the draft before you see it, twice at most.
6. Hands you the letter with the results, records it in the positioning file and saves it the way it's going out: a Word file for an upload, plain text for a form's text box, or the email itself, never a PDF.

### The watermark

Current Claude models put an invisible watermark in the text they write. Because the mark is added at the model level, it's in text from Claude Code and Cowork as well as the Claude apps. The mark travels with copied text and can last through some editing, and detecting it in text is in private preview for eligible organizations [C24, C25]. So a letter this skill drafts may have the mark, and the skill never tries to remove, hide or get around it.

The skill builds each letter for you to finish, and when it hands you the letter, it points you to the two sentences only you can write: your first line and the topic you'd like to talk about. In one study of a freelance platform, more time spent editing an AI-drafted letter went with a better chance of winning the job, though the study doesn't show the editing caused it [C15].

## Submission review

Submission review has a reviewer read a finished cover letter, resume, outreach note, referral blurb, LinkedIn About section or application answer the way its real readers will: a recruiter's ten-second first look, a hiring manager reading closely, and an AI grader checking the posting's requirements. You get back findings that quote your own lines, and a verdict of Send, Fix first or Rethink.

The reviewer never sees how the piece was made. The chat that wrote your letter knows your career record, the plan behind the letter and every draft, and that knowledge fills in the holes a real reader would stop at. So the review runs in a separate helper that sees only a folder of files built for it.

### How the review stays blind

- A script builds that folder: the piece, the posting, anything the reader also sees (such as the resume sent with a letter), plainspeak-writer's check results and a list of what's included. The script has no place for notes, and it leaves the original file names out.
- The helper starts from one fixed sentence naming the folder and checks that the sentence arrived word for word. If anything was added, the helper marks the review as not blind ("blind: no").
- The helper's only tool is Read, which opens files: it opens the files on the list, can't search for others and can't edit anything.
- The helper skips project instruction files (CLAUDE.md), which helpers load by default.

**Checking against your case.** When the posting has a positioning file, Claude checks the piece against it after the report, under its own heading. The check looks at four things: whether the reviewer's first reaction matches the one line your case wants the reader to believe, whether a must-fix finding falls on one of your gaps or the hiring team's doubts, which proof points made it onto the page, and whether any phrase from the file's list of things to keep off the page shows up. The reviewer never sees that file, so the review itself stays blind.

**One limit in Cowork.** Cowork gives every helper your account's saved memory, and no setting in the plugin can turn that off. If your saved memory holds your career history, a Cowork review sees it and says "blind: no." For a fully blind review, run it in Claude Code, such as the Code tab in the Claude desktop app, which doesn't load the Claude app's saved memory.

### What the report holds

1. What the reviewer received, and whether the review was blind.
2. A first reaction in the reader's voice, two sentences at most, ending on whether you fit.
3. The verdict, set by fixed rules.
4. The findings you must fix and the ones you should, five of each in full and any more in one line each. A full finding quotes the line, names the check it fails and says what goes wrong for the reader. A finding can point toward a fix, but it doesn't supply new wording.
5. Each requirement in the posting, marked as shown, claimed without proof, or missing.
6. What the reviewer couldn't judge, since it has no career record to check facts against.

A finding is a must-fix when it's one of these: a line plainspeak-writer's checker blocks, a line its rules block that the reviewer finds by reading, a risk to the application, a missing must-have requirement when an AI grader is reading, or a piece over a hard character limit. The risks include naming a gap outright, an apology, a story about why you left a job, negative talk about an employer, and a title, date, company or figure that disagrees with your resume.

The verdict is Rethink when the first reaction sees no fit, when there are more than five must-fix findings, or when more than half the must-have requirements are missing and an AI grader is one of the readers. With one to five must-fix findings, it's Fix first. A piece with none gets Send.

## plainspeak-writer and resume-ops

Candidate positioning, cover letter and submission review are this plugin's own skills. The cover letter skill can't write without plainspeak-writer, and candidate positioning saves its file for resume-ops to read, so the plugin includes both, and one install gives you all five. Each is an exact copy of one release from its own repository: [plainspeak-writer](https://github.com/roundofschatz/plainspeak-writer) 1.7.2 and [resume-ops](https://github.com/roundofschatz/resume-ops) 2.4.4. The plugin's scripts use the plugin's own copy of plainspeak-writer even when you have another installed, because the plugin is tested with that copy.

Either tool also installs on its own from this repository's marketplace, for a leaner setup. Pick one way to install each tool, because with a separate copy beside the plugin, Claude sees two skills with the same job and may load either. Remove the separate copy when you install the plugin.

## Install

**Cowork and the Claude desktop app.**

1. Get `job-seeker-ops.zip` from the Releases page, or zip this folder yourself, leaving out `tests/`.
2. Open **Customize**, then **Plugins**, then **Add**, then **Upload plugin**, and choose the zip.
3. Start a new Cowork task. A plugin loads when a task starts.

Upload it under Plugins rather than Skills, because a skill upload drops the reviewer and the review then refuses to run. A plugin on your account also shows up in Claude Code when its next session starts.

**Claude Code.** This plugin, resume-ops and plainspeak-writer share one marketplace, called `roundofschatz`, in this repository. Add it, then install the plugin:

```
/plugin marketplace add roundofschatz/job-seeker-ops
/plugin install job-seeker-ops@roundofschatz
```

To install one tool alone, use `/plugin install resume-ops@roundofschatz` or `/plugin install plainspeak-writer@roundofschatz`. The marketplace moved here from resume-ops's repository in 0.4.4, so if you added `roundofschatz/resume-ops` as a marketplace before then, remove it before you add this one.

To try the plugin for one session, run `claude --plugin-dir ./job-seeker-ops`.

**What it needs.** Python 3.8 or newer runs the scripts. Reading a Word file also needs Python's XML parser (expat) at 2.4.1 or newer, and Python 3.9.7 and later include it. With an older one, the scripts ask you for the text instead. When LibreOffice is installed, the cover letter skill gets a real page count for the Word file, and without it the script estimates. Nothing else needs installing, because plainspeak-writer and resume-ops come inside the plugin. resume-ops's page check also uses LibreOffice and `pdftotext`, as its README lists. Chat on claude.ai doesn't run plugin helpers, so the review needs Cowork or Claude Code.

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

Claude asks once for anything missing, builds the reviewer's folder, starts the reviewer and hands back its report unchanged. A second opinion is a new review with a new folder rather than the same reviewer changing its mind. A writing skill that calls the review runs it twice at most per piece, then hands you whatever findings are still open.

## Files

```
job-seeker-ops/
├── .claude-plugin/plugin.json      name, version and description
├── .claude-plugin/marketplace.json the marketplace for the three tools
├── agents/submission-reviewer.md   the reviewer's instructions
├── skills/candidate-positioning/
│   ├── SKILL.md                    the ten steps that build a positioning file
│   ├── references/format.md        the file's format, with a full example
│   ├── references/case.md          finding what the firm is buying, and the case
│   └── scripts/check_positioning.py  checks a positioning file
├── skills/cover-letter/
│   ├── SKILL.md                    the nine steps that write a letter
│   ├── references/letter.md        the letter's shape, its plan, where it goes, a full example
│   ├── references/checks.md        every check, what runs it, and the hard fails
│   ├── references/sources.md       the research behind the rules
│   ├── scripts/check_letter.py     checks a letter against the three files
│   └── scripts/build_letter.py     writes the Word file
├── skills/submission-review/
│   ├── SKILL.md                    the steps Claude follows to start a review
│   └── scripts/build_packet.py     builds the folder the reviewer reads
├── skills/plainspeak-writer/       a copy of plainspeak-writer, never edited here
├── skills/resume-ops/              a copy of resume-ops, never edited here
├── bundled.json                    where each copy came from, with every file's hash
├── tools/sync_bundled.py           copies a release of either skill into skills/
├── tests/                          tests and test pieces, left out of the install zip
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Tests

- `python3 tests/unit/run_tests.py` runs every unit test: the tests for `build_packet.py` and `check_positioning.py`, for cover letter's two scripts and its sources, the check that `plugin.json`, the changelog and a built package agree, and the check that each bundled copy matches its release.
- `tests/RUN-TESTS.md` holds submission review's live tests: isolation, leaks, seeded flaws, repeat runs and the rest.
- `tests/RUN-TESTS-positioning.md` holds candidate positioning's live tests. Every test piece comes from made-up writers. One of them, writer H, applies to a real posting, which isn't stored here.
- `tests/RUN-TESTS-cover-letter.md` holds cover letter's live tests, with made-up writers too.

## Contributing

- Keep it general, with no personal details, clients or private work in any file.
- Build on what's here instead of replacing it.
- Log every change in `CHANGELOG.md`: what was added, changed or removed, and why.
- Run plainspeak-writer's checker on every file you change.
- Give every change to a shipped file a new version. Build the package from the release commit, so it matches the commit byte for byte: `git archive --format=zip --prefix=job-seeker-ops/ -o dist/job-seeker-ops.plugin HEAD .claude-plugin/plugin.json agents skills README.md CHANGELOG.md LICENSE`.
- Never edit `skills/plainspeak-writer/` or `skills/resume-ops/` here. Change the skill in its own repository and release it there, then copy the release in with `python tools/sync_bundled.py <name> --repo <its clone> --ref <tag>`.

**How the bundled copies stay exact.** `bundled.json` names the commit each copy came from, with a hash for every file. A unit test fails when a copy differs from those hashes, and when the skill's own repository sits beside this one, the test checks the hashes against that commit too. Each tool's own tests stay in its own repository, which runs them. The cover letter skill tells Claude to load the plainspeak-writer copy that sits beside its own folder.

## Author

Ryan Schatzman · [LinkedIn](https://www.linkedin.com/in/ryanschatzman)

## License

MIT. See `LICENSE`. plainspeak-writer and resume-ops keep their own MIT licenses, in their folders.
