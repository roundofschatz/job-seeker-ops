# The checks

Every letter passes all of these before the person sees it. Most run by script, and the rest by reading. The scripts are `scripts/check_letter.py` in this skill and plainspeak-writer's `check_voice.py`, which `check_letter.py --voice` runs for you.

## The list

| Check | How it runs | What fails |
|---|---|---|
| The posting's rules on AI in application materials | `check_letter.py` before drafting, then the person | A posting that rules out AI-written materials, unless the person says the employer allows it |
| The letter argues one claim, in the words of the writer's own material, and each body paragraph's first sentence says which part of it, or which of the posting's asks, the paragraph answers | The red team, step 5 | A coined phrase for a claim, a paragraph that answers nothing, or a proof that answers neither the claim nor an ask |
| The first sentence is content: the facts the claim explains, the reader's problem or a shared world, never the reader told how their own posting sizes up the job | Reading, with plainspeak-writer's opener rules by code, and `check_letter.py` warns on the posting told back | An announcement of what the letter will do, the writer's name, or "Your posting measures this role by..." |
| The firm or the seat is named in the first two sentences, along with any referral | `check_letter.py` | Neither in the first two sentences, or a referrer the file names left out |
| Two firm facts, each put to use | Reading. candidate-positioning already kept home-page facts out | A fact listed with nothing the writer would do with it |
| Two or three results, each with a named firm or client and a number, an adopted outcome or a scale | Reading, with `check_letter.py`'s list of numbers and names | A result with no name, or one with no number, outcome or scale |
| Nothing the writer lacks, no departure story, no salary, no complaint, no sentence about how honest the letter is being | `check_letter.py` searches section 7's phrases, plainspeak-writer blocks the honesty phrases, and the rest is read | Any of them, however it's framed |
| No resume line restated [C02, C03], and every title, company, date and figure matches the resume | `check_letter.py` | A number, date or name in no file; a figure the file and the resume disagree on; a sentence that copies a resume line |
| A result the resume leaves out has its source in the positioning file | `check_letter.py` | A number found nowhere, or only in the file's working notes |
| No internal method name, only its plain description; no quote from a client or a colleague | Reading, with section 6's plain descriptions | Either one on the page |
| The last paragraph is the ask alone: a conversation about one named thing, in the writer's own words, and line 4 of the case appears nowhere as a sentence | `check_letter.py` warns, and reading decides | A summary line before the ask, line 4 restated, a thank-you or "look forward" close, an ask with no named thing, a stock opener such as "I'd like to talk about", or an ask that opens like the writer's last letter |
| One page, one column, no letter text in a table, text box, header or footer. The body's 350 to 450 words are a guide that never calls for a cut | `check_letter.py`, by estimate on the text and on the Word file, and by LibreOffice when it's installed | Any of them. A body outside the guide is only reported |
| An upload opens on the date, the recipient on one line, and a Re: line with the posting's title and its requisition number when the posting gives one | `check_letter.py` | No date, no recipient or no Re: line; the recipient on more than one line; the writer's name, email, phone, city, address or a link in the header; a number in the Re: line the posting doesn't give |
| plainspeak-writer's checker finds no HARD hits | `check_letter.py --voice` | A HARD hit |
| Both swap tests come back no | Reading | A yes on either |
| Every sentence from the person's earlier writing states a fact the three files hold and is still true, and no sentence repeats within the letter | `check_letter.py --sample` and `--compare`, then reading | A shared sentence with a fact the files don't hold, a stale count of years, a blocked sentence, or a sentence said twice |
| The red-team list is in the record under all eight headings before any script runs, and each finding was fixed by rewriting its paragraph | Step 5, with `check_positioning.py` for the headings | A missing heading, a script run before the list, or a finding fixed by a patch |
| submission-review says Send, or the person has the open findings after two reviews | Step 8 | A third review, or a draft shown before the review ran |

Fix every FAIL. Fix every warning from either script, or clear it with a reason in the record's checks. A finding in the body is fixed by rewriting its whole paragraph from the fact list, then reading the whole letter again, never by changing the words it quotes. No fix splits a sentence, or cuts the words that join one sentence to the next, to meet a length or a short-sentence rule, and there's no trimming pass: a letter past one page loses a whole proof or a point it can spare. A sentence-length warning from plainspeak-writer is cleared with a reason when the paragraphs hold together, and the writer's samples, passed with `--sample`, set what that rule expects. A finding in the header is fixed by copying the posting's title, its requisition number and the firm's name as the posting writes them, and one in the sign-off by copying the resume's name.

## Hard fails

Each of these blocks the letter until it's fixed. When only the person can fix it, they see the draft with that one item named, and the Word file waits.

| Hard fail | Caught by |
|---|---|
| No positioning file | Step 1 |
| A posting that rules out AI-written materials, with no word from the person that the employer allows it | Step 1, with `check_letter.py` before drafting |
| A sentence from earlier writing whose fact the three files don't hold, or that's no longer true | `check_letter.py --sample` and `--compare`, then reading |
| A claim with no source in the three files | `check_letter.py` for what it can count; plainspeak-writer's fresh reader for the rest |
| A wrong company, role or place name | `check_letter.py`, in the salutation and the body |
| A sentence repeated word for word within the letter, or an unfilled placeholder | `check_letter.py` |
| A PDF made by the skill | Never made. Neither script writes one |
| A Word file whose author field names a software library instead of the writer | `check_letter.py` on the Word file, which `build_letter.py` runs after writing it |

## The sentence list

List every sentence of the body beside the thing it names: a firm, a number, a tool, a person or a result. In one study, application materials with more detail and clarity drew more interviews per application [C17]. `check_letter.py --sentences` prints a first pass. A sentence with nothing beside it gets its thing or gets cut. Length isn't the test: a short sentence that names its thing stays. Write the finished list into the record's checks:

```text
- **Sentences:**
  1. "Last year Switchgrass's forecasts missed by 24% on average..." · Switchgrass, 24%
  2. "Your planning analyst will build the weekly volume forecasts for 38 terminals..." · 38 terminals
  3. "Finding the input behind a miss is the work I've done at Brightwell Grocers Distribution since 2021..." · Brightwell, 2021, store promotions
```

## The two swap tests

**Could another applicant send this letter?** This is the test for a form letter [C09]. Read each paragraph and ask whether it holds something only this writer did. The Proof always does. A Frame or a Fit that any applicant could write goes back to step 3.

**Could the writer send it to another firm with the name swapped?** Put another firm's name in and read the Frame, the Fit and the Invitation again. Each one has to break: it names this firm's measure, its facts, its topic. A proof sentence the writer has used before can still pass this test, since call 4 lets it move, but those three can't.

## Sentences from earlier writing

`check_letter.py --sample FILE` lists every sentence the letter shares with a voice sample, and `--compare FILE` every sentence it shares with another letter. For each one:

1. Its fact is in the three files: a number, date or name the script finds there.
2. It's still true today: a count of years, "current", "now", "still" or a title gets checked against the dates in the files. The script flags these.
3. It's in a Proof paragraph. A shared sentence in the Frame, the Fit or the Invitation fails, since those are written for each firm.

## The red team

Right after the draft, and before any script runs, read the whole letter once as the hiring manager at the firm: start to finish, at the pace they'd read it, with none of the draft's notes in hand. The scripts come after, so the fixes go to how the letter reads before they go to a count. Write every finding into the letter's record under `#### Red team`, with these eight headings in this order:

| Heading | What it looks for |
|---|---|
| The claim | The letter makes one argument, the map's claim, and each body paragraph's first sentence says which part of it, or which of the posting's asks, the paragraph answers. Every sentence after that one serves it. A paragraph that answers nothing, a proof that answers neither the claim nor an ask, and an opening that tells the reader what their own posting says all go here |
| Thread between paragraphs | Each paragraph picks up where the last one left off, so the reader can say why it comes next. A paragraph that could move without losing anything has no thread |
| Each sentence follows from the one before | No sentence starts a new subject without a link back, and the reader never has to look back to see what a sentence answers. The test is naming the word that ties a sentence to the one before; a bridge sentence that only points back, like "A record like that pays off", doesn't count |
| Resume restated in prose | A resume line told again as a sentence, instead of what it meant or its story. The script catches near-copies, and this catches the reworded ones |
| Abstractions, hanging references and what-clauses | An abstract word where a thing should be ("impact", "alignment", "solutions"); a "this", "that" or "it" pointing at nothing the reader can name; a what-clause, like "What I bring is" |
| Short flat lines after long ones | A short sentence that only repeats, sums up or punches the long one before it, like "It worked." A short sentence that adds a fact stays |
| Targets written as results | A goal, a plan, a forecast or a "would" written as if it happened, or a number the writer aimed for given as one they reached. A result is only what a file shows happened |
| The close | The last paragraph is the ask alone, about one named thing in the writer's words, with no summary line or line 4 before it and nothing trailing after it |

Each finding names its paragraph, quotes the words, says what's wrong and says which paragraph was rewritten. A heading with no finding reads "None." A finding can sit on its heading's line or on indented lines under it.

**The fix is a rewrite, never a patch.** Rewrite the finding's whole paragraph from the fact list of step 4, in plainspeak-writer's voice: no swapped word, no cut clause, no sentence mended where it stands. A patch fixes the words the finding quotes and leaves the paragraph's reasoning as it was, which is usually where the problem started. Re-read the whole letter as the hiring manager, then run steps 6 and 7. A finding from those steps, or a new one from reading again, goes under its heading and gets the same fix. `check_positioning.py FILE` checks that all eight headings are there, and the scripts wait until they are.

From the example letter's record, written about its first draft:

```text
#### Red team

- **The claim:** Paragraph 1 told the reader what their posting says, "your posting puts the cost plainly", and its last sentence pointed back with "that work" instead of setting up the claim. Rewrote paragraph 1 from section 1, F1 and section 3, so it opens on the 24% miss as fact and ends on finding the input behind a miss.
- **Thread between paragraphs:** Paragraph 3 went from Saturday crews to "I was Brightwell's inventory coordinator" with nothing joining them. Rewrote paragraph 3 from F3 and P3, so the warehouse years come in as the floor where a miss lands.
- **Each sentence follows from the one before:** None.
- **Resume restated in prose:** None.
- **Abstractions, hanging references and what-clauses:** None.
- **Short flat lines after long ones:** Paragraph 2, "It worked.", after the sentence on 52 weeks. Rewrote paragraph 2 from P1 and P2.
- **Targets written as results:** Paragraph 3, "your terminal managers get the same weekly note", gave a plan as if it were running. Rewrote paragraph 3 from P2 and the posting's reporting duty, as what he'd do in the seat.
- **The close:** Paragraph 4 opened on line 4 of the case, "I find the input behind a forecast miss and fix it", before the ask. Rewrote paragraph 4 as the ask alone.
```

## Warnings worth knowing

- **"Follows resume line N closely."** A proof sentence that repeats the line's numbers will trip this. Read it: when it tells the result as a story and ends on what it produced, clear it with that reason. When it copies the line, rewrite it.
- **"Names no firm, number, tool, person or posting term."** Read it. A sentence that links two named things can stay, and one that points at nothing gets cut.
- **"Is only in the positioning file's working notes."** The number sits in the map or the case but not in a proof or a firm fact. Check it against the cited source line before it stays.
- **"Says line 4 of the case."** A sentence shares most of its words with line 4. Line 4 sets the claim and never goes in the letter, so rewrite the paragraph without it; in the close, that leaves the ask alone.
- **"Tells the reader how their own posting sizes up the job."** Rewrite the opening on the facts themselves. A sentence that names what the posting asks for, so the letter can answer each ask, is fine and clears with that reason.

## When the person edits

Their edit stands, and the rewrite rule binds only the skill's own fixes, never the person's edits. Run both scripts on their version, export it, and tell them what the scripts found, so they decide with the facts in front of them. A hard fail in their version, like a placeholder or a wrong company name, still holds the Word file back, and the skill says which one and why. A third review runs only if they ask for one.
