# The career record and the aim file

career-intake writes two Markdown files into the person's folder. This page is their format's one home, and `scripts/check_record.py` checks both.

- `career-record.md` holds what's true about the person's work: roles, totals, stories, skills, proof, and how the work reads in other fields. candidate-positioning and resume-ops read it as a career record.
- `where-to-aim.md` holds what the person wants, what can't change, and the targets worth chasing. It's private from top to bottom.

## Writing the parts

- Dates are written `YYYY-MM-DD`.
- Every fact line ends with its source in brackets. A workbook answer is its question id, like `[best-story]`. An answer given in this session is `[A3]`, listed under "Answers in this session" at the end. A line in a file is `[resume.txt L12]`. Separate two sources with a semicolon: `[best-story; A2]`.
- Use the person's own words wherever they work. A rewrite keeps every fact they gave and adds none.
- A section with nothing in it says "None."

## People in the stories

Stories keep their full detail. They leave out names, and anything that together would tell a reader who the story is about, unless that person told the candidate directly that it's okay. In health, counseling, legal, school and social work, that also means no dates, small towns, ages, or rare details that point to one client.

Write the person as a description: "a man in his first week out of the hospital", "a family of five", "a client who'd been through three other programs". Each story ends with a `People in it:` line that says `no names` or names the people who gave their yes, with the answer where the candidate said so.

## career-record.md

```
# Career record: <first name>

Format: career-intake 1
Built: YYYY-MM-DD from <the answers file, this conversation, and any files by name>
Confirmed: not yet
```

When the person confirms it, the last line becomes `Confirmed: YYYY-MM-DD, "<their words>"`.

### 1. Work history

One block per role, most recent first: title as held, employer, city and state, years. Under it, the job in plain words and its size: how many at a time, team, budget, area, hours. Titles and dates come from the person's files when they have any, since those are what a background check compares.

### 2. Totals

Counts across the career, each with its math and a tag. `[confirmed]` means the person checked it or a record shows it. `[estimate]` means it was worked out and is only used with "about" in front of it.

```
- About 720 people served across eight years: 45 at a time, each for about 26 weeks. [estimate] [stories-total]
```

### 3. Stories

Each story gets a number and a short title in plain words, then these lines:

```
### S1. <short title>
- What happened: … [best-story]
- The need: … [best-need]
- What you did: … [best-need]
- What changed: … [best-change]
- Proof: … or "None yet; see Open questions."
- People in it: no names
```

The best story, the change stories and the three coffee stories go here. The worst story goes in section 10.

### 4. Things built that others use

What it does in plain words, where it was built, who uses it, and how often. Leave off any internal name.

### 5. Skills

Each skill in plain words, with the story or answer that shows it: `- Calms a person in crisis on the phone and gets them to a safe plan (S1, S3) [work-great-at]`. Skills the person listed with nothing behind them go under "Said, not yet shown", where they wait for a story.

### 6. In other words

How the work reads in two or three other fields. For each field: its name, the job titles it uses, and three to six lines that say the person's work in that field's words, each pointing to the story or total it rests on. Take the field's words from the live postings it was checked against, and list those postings with their links and the date checked. The person's corrections win. Note each one with its answer, like `[A5]`.

### 7. What others say

What coworkers come to them for, what a boss would say, reviews, awards and notes, each with its source.

### 8. Proof

Proof on hand: files, reports, numbers, and where each one lives. Proof to get: what would prove each story, and who could give it. In fields with private records, that means totals and outcome reports with no client names, letters from supervisors, and reviews.

### 9. How you describe it

- Before: the coffee pitch from the workbook, word for word. `[work-pitch]`
- After: the pitch and a three- or four-sentence description, written from the stories and totals in the person's words, and confirmed by them.

### 10. Private

Nothing here goes on any page someone else reads: the worst story in full, gaps, things they won't do, roadblocks, and anything they asked to keep private. Each still has its source.

### 11. Open questions

Numbers to chase, proof to find, and anything left blank, each with the question to ask.

### Answers in this session

`A1`, `A2` and on: the question and the person's answer, in their words.

## where-to-aim.md

```
# Where to aim: <first name>

Format: career-intake 1
Built: YYYY-MM-DD
Confirmed: not yet

This file is private. Nothing in it goes on a page someone else reads.
```

### 1. What you want

The kind of days they want, what gives them energy and what wears them out, the titles and industries they named, and places. Each line has its source.

### 2. What can't change

The pay floor and the pay cut they can take, schedule, family, licenses to keep, drive time, and remote work.

### 3. Targets

Two to four targets, each a job family with the standard title recruiters search for. Score each on the six points in resume-ops's `references/intake.md`, under "Choosing a target": evidence, repeatability and recency from the record, and market size, title and fit from 8 to 12 live postings. List the postings under the table with their links and the date checked.

### 4. The calls

```
- Go for: <target>. <why, in one or two sentences>
- Runner-up: <target>. <why>
- Recommend against: <target>. <why it looks strong from the inside and fails in the market>
```

### 5. People who can help

From the `dream-people` answer: who they know, where, and which target each one helps.

### 6. Next

The first postings to look at, and the step after: with a posting in hand, candidate-positioning reads the career record and works out the case.
