# The checks

Every letter passes all of these before the person sees it. Most run by script, and the rest by reading. The scripts are `scripts/check_letter.py` in this skill and plainspeak-writer's `check_voice.py`, which `check_letter.py --voice` runs for you.

## The list

| Check | How it runs | What fails |
|---|---|---|
| The posting's rules on AI in application materials | `check_letter.py` before drafting, then the person | A posting that rules out AI-written materials, unless the person says the employer allows it |
| The first sentence is content: the reader's problem, the posting's measure or a shared world | Reading, with plainspeak-writer's opener rules by code | An announcement of what the letter will do, or the writer's name |
| The firm or the seat is named in the first two sentences, along with any referral | `check_letter.py` | Neither in the first two sentences, or a referrer the file names left out |
| Two firm facts, each put to use | Reading. candidate-positioning already kept home-page facts out | A fact listed with nothing the writer would do with it |
| Two or three results, each with a named firm or client and a number, an adopted outcome or a scale | Reading, with `check_letter.py`'s list of numbers and names | A result with no name, or one with no number, outcome or scale |
| Nothing the writer lacks, no departure story, no salary, no complaint, no sentence about how honest the letter is being | `check_letter.py` searches section 7's phrases, plainspeak-writer blocks the honesty phrases, and the rest is read | Any of them, however it's framed |
| No resume line restated [C02, C03], and every title, company, date and figure matches the resume | `check_letter.py` | A number, date or name in no file; a figure the file and the resume disagree on; a sentence that copies a resume line |
| A result the resume leaves out has its source in the positioning file | `check_letter.py` | A number found nowhere, or only in the file's working notes |
| No internal method name, only its plain description; no quote from a client or a colleague | Reading, with section 6's plain descriptions | Either one on the page |
| The last paragraph opens on line 4 in first person, and the last sentence asks for a conversation about one named thing, in the writer's own words | `check_letter.py` warns, and reading decides | A thank-you or "look forward" close, an ask with no named thing, a stock opener such as "I'd like to talk about", or an ask that opens like the writer's last letter |
| Body of 500 words or fewer, one page, one column, no letter text in a table, text box, header or footer | `check_letter.py` | Any of them |
| plainspeak-writer's checker finds no HARD hits | `check_letter.py --voice` | A HARD hit |
| Both swap tests come back no | Reading | A yes on either |
| Every sentence from the person's earlier writing states a fact the three files hold and is still true, and no sentence repeats within the letter | `check_letter.py --sample` and `--compare`, then reading | A shared sentence with a fact the files don't hold, a stale count of years, a blocked sentence, or a sentence said twice |
| submission-review says Send, or the person has the open findings after two reviews | Step 7 | A third review, or a draft shown before the review ran |

Fix every FAIL. Fix every warning from either script, or clear it with a reason in the record's checks.

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
  1. "Last year Switchgrass's forecasts missed by 24% on average..." · Switchgrass, 24%, the posting's measure
  2. "Your planning analyst will build the weekly volume forecasts for 38 terminals..." · 38 terminals
  3. "I've done that work at Brightwell Grocers Distribution since 2021." · Brightwell, 2021
```

## The two swap tests

**Could another applicant send this letter?** This is the test for a form letter [C09]. Read each paragraph and ask whether it holds something only this writer did. The Proof always does. A Frame or a Fit that any applicant could write goes back to step 3.

**Could the writer send it to another firm with the name swapped?** Put another firm's name in and read the Frame, the Fit and the Invitation again. Each one has to break: it names this firm's measure, its facts, its topic. A proof sentence the writer has used before can still pass this test, since call 5 lets it move, but those three can't.

## Sentences from earlier writing

`check_letter.py --sample FILE` lists every sentence the letter shares with a voice sample, and `--compare FILE` every sentence it shares with another letter. For each one:

1. Its fact is in the three files: a number, date or name the script finds there.
2. It's still true today: a count of years, "current", "now", "still" or a title gets checked against the dates in the files. The script flags these.
3. It's in a Proof paragraph. A shared sentence in the Frame, the Fit or the Invitation fails, since those are written for each firm.

## Warnings worth knowing

- **"Follows resume line N closely."** A proof sentence that repeats the line's numbers will trip this. Read it: when it tells the result as a story and ends on what it produced, clear it with that reason. When it copies the line, rewrite it.
- **"Names no firm, number, tool, person or posting term."** Read it. A sentence that links two named things can stay, and one that points at nothing gets cut.
- **"Is only in the positioning file's working notes."** The number sits in the map or the case but not in a proof or a firm fact. Check it against the cited source line before it stays.

## When the person edits

Their edit stands. Run both scripts on their version, export it, and tell them what the scripts found, so they decide with the facts in front of them. A hard fail in their version, like a placeholder or a wrong company name, still holds the Word file back, and the skill says which one and why. A third review runs only if they ask for one.
