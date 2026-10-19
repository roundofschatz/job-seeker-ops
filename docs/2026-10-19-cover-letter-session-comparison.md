# What made one cover letter better than another: a comparison of two sessions

October 19, 2026. The owner ran the cover-letter skill (job-seeker-ops 0.4.7) twice in parallel for one posting, a sector marketing lead at a large engineering firm, from the same positioning file, resume and voice sample. One session ran on Opus 5.5 and one on Fable 5.1. The owner judged the Fable session's final letter much better on story, subject matter, sentence structure, tone and diction. This note says why, with the counts, and lists what changes in the skills. It leaves out the letters themselves and every personal detail, which stay in the owner's private records.

## What was compared

Five drafts, the three from session A (Opus) and the two from session B (Fable):

| Draft | When | The owner's verdict |
|---|---|---|
| A1 | First skill run | Rejected: "empty references and vague assertions, terrible sentence cadence, repetitive points," didn't fill the page |
| A2 | Rewrite to the owner's own writing sample | "Much better," but "choppy ... like a fact sheet" |
| A-final | Rewrite for flow | Judged much worse than B-final |
| B1 | First skill run | Rejected: "staccato," "sequential non sequiturs" |
| B-final | Rewrite after the owner's notes | The better letter |

The voice sample was a 3,000-word paper the owner wrote and published. Both transcripts, with every tool call and checker run, were read for the process.

## What the counts show

### Sentences

| | A1 | A2 | A-final | B1 | B-final | Sample |
|---|---|---|---|---|---|---|
| Body words | 443 | 494 | 525 | 457 | 490 | 3,054 |
| Mean sentence length | 20.1 | 23.5 | 26.2 | 19.9 | 24.6 | 24.4 |
| Spread (standard deviation) | 8.2 | 7.5 | 9.4 | 6.0 | 5.2 | 11.2 |
| Sentences of 10 words or fewer | 14% | 5% | 5% | 9% | 0% | 8% |
| Rhetorical questions in the body | 0 | 2 | 2 | 0 | 0 | 3 |

B-final matches the sample's average, but so does A2, which the owner called choppy, and A-final is closer to the sample on spread and short sentences. Matching the sample's average didn't make the better letter.

### Paragraphs

Coded by hand for each sentence after a paragraph's first, leaving out the closing ask. A tie is clear when a word points back or a connective states the relation, weak when only an incidental word is shared, and absent otherwise. A new subject is a project, employer, document or claim the paragraph's first sentence didn't set up.

| | A1 | A2 | A-final | B1 | B-final |
|---|---|---|---|---|---|
| Sentences with no tie to the one before | 2 of 16 | 4 of 15 | 0 of 14 | 6 of 17 | 2 of 15 |
| Sentences that start a new subject | 25% | 40% | 36% | 59% | 13% |
| Subjects per body paragraph | 2.0 | 2.2 | 2.2 | 3.5 | 1.5 |
| Separate claims in the letter | 7 | 7 | 9 | 7 | 1, stated 5 ways |
| Banned-pattern hits, by reading | 11 | 6 | 14 | 13 | 2 |

B-final makes one argument, taken from the owner's own paper, and four of its five paragraphs come back to it. A-final has more sentence-to-sentence ties than B-final, because its rewrite for flow added bridge sentences ("I've built that kind of plan before.", "A reputation like that pays off when it's time to win work."). Those bridges are tells: lines that point back, short flat lines after long ones, abstractions. They raised A-final's banned-pattern count above A2's.

### The checker

plainspeak-writer's checker passed every draft with no hard hit. It gave A1, the draft the owner rejected first and hardest, no warnings at all. V09 (at least 10% of a letter's sentences at 10 words or fewer, an average of 24 or less) fired on A2, A-final, B1 and B-final. The sample itself trips V09's average.

## What mattered

1. **One argument, with every paragraph answering it.** Both rejected first drafts had a claim in the map's Frame row. The better letter differed in that each paragraph's first sentence said which part of the claim, or which of the posting's asks, it answered, and proofs that answered neither came out.
2. **No cutting or splitting to meet a number.** Every draft the owner called choppy had been cut or split to meet one. A1 split sentences each time V09 fired. B1 went from 594 words to 449 over about eight passes. A2 took seven cuts to get under 500 words and onto one page. The two letters that read well stopped cutting, at 490 and 525 words.
3. **Reading the letter as the reader before the scripts.** B-final's session wrote a red-team list before any script ran and rewrote from it. Every other draft was checked first, and its fixes went to the checker's numbers.
4. **Two of the skill's own rules wrote banned lines into both first drafts.** The rule that the opening uses "the posting's own measure of the job" produced "Your posting measures this seat by..." in both. The rule that the last paragraph opens on line 4 of the case produced the same summary close in both. Two models wrote nearly the same sentences, so the cause is the instructions.

What the evidence can't settle is how much of the gap is the model. The owner's notes to the two sessions differed, and each read them differently: session A took a note about uncovered requirements as a reason to cover more ground and dropped the argument that later won, while session B took "sequential non sequiturs" as a sign there was no argument and built one. The test below splits the model from the process.

## The controlled test

Designed, not yet run.

- **Postings:** two past postings for which the owner has the letter he sent.
- **Inputs:** the same for every run of a posting: the posting, the resume, one positioning file built and confirmed once, and the same voice sample. The sent letter isn't the sample, since it's what the letters are judged against.
- **Arms:** Opus 5.5 and Fable 5.1, each with the current skill (0.5.0) and the changed one, for each posting. Eight runs.
- **Each run:** a new session, a folder holding only the inputs, the plugin pinned to the arm's version, the same first message word for word, and no feedback during the run.
- **Blind scoring:** the eight letters are shuffled and renamed L1 to L8, with headers made identical, and the owner scores them before seeing the key. A helper that sees one letter at a time codes the paragraph counts above; a script does the sentence counts.
- **Reading it:** the changed skill wins if it beats the current one in all four model-and-posting pairings, by 2 or more of 25 points in at least three. A win on one model only means the change helps that model. If one model beats the other in every pairing by more than the skill does, the model is the bigger lever. Any pairing within 2 points gets both arms run once more, since one run per cell can't separate a small effect from luck.

### Scoring sheet

| Score | Story | Subject matter | Sentence structure | Tone | Diction |
|---|---|---|---|---|---|
| 1 | A list of facts with a greeting | Proof aimed at a different job | Choppy, or long sentences glued with commas | An applicant asking, or a salesman | AI tells, coined phrases, abstractions |
| 3 | Has a point, but paragraphs wander off it | Right job, some proofs are filler | Reads fine, some sentences don't lead into the next | Professional but stiff | Plain but could be anyone's |
| 5 | One argument, and every paragraph moves it | Every proof is one this reader needs, told as what it did | Each sentence leads into the next; length fits what it says | A peer making a case to someone they respect | Plain, exact, sounds like the writer |

Each letter gets the five scores, a total out of 25 and one line on why, then the counts: body words, mean sentence length, spread, short share, questions, checker warnings, sentences with no tie, sentences that start a new subject, subjects per paragraph, separate claims, banned-pattern hits and proofs in resume order.

## The changes

The owner approved these on October 19, and they shipped in job-seeker-ops 0.6.0 and plainspeak-writer 1.8. 0.5.0 had already added a red-team step and the rule that a finding gets a rewrite instead of a patch.

### cover-letter

- **A Claim row above Frame in the map:** one sentence the letter argues, in the words of the writer's own material, never a coined phrase. Each body paragraph's row says which part of the claim, or which posting ask, it answers.
- **The Frame stops using the posting's measure of the job.** It opens on the facts the claim explains.
- **Line 4 of the case never goes in the letter as a sentence.** The close is the ask alone.
- **Proofs are ordered by the claim or the posting's asks, never by the resume.** A proof that answers neither stays out.
- **The red team moves before the scripts** and gains a heading for the claim: each paragraph's first sentence says what it answers, and every sentence after serves it.
- **No fix splits a sentence or cuts a connecting word to meet a length or short-sentence rule,** and there's no trimming pass.
- **A new upload header:** the date, the recipient on one line, a Re: line with the posting's title and its requisition number when the posting gives one, then the greeting. The sender's contact details stay on the resume.
- **The length limit:** one full page, with 350 to 450 words as a guide that never forces a cut. The 500-word cap is gone. The owner's ruling.

### plainspeak-writer (in its own repository, then copied in)

- **Confirmed:** a paragraph is one point and its evidence, and its first sentence says what the paragraph is for.
- **Changed:** every sentence after the first is about the paragraph's subject and picks up the sentence before. A bridge sentence that only points back doesn't count as a tie.
- **Dropped:** a proposed rule against rhetorical questions opening a body paragraph. The sample opens on one, and nothing tied questions to the gap.
- **Added:** state a letter's claim in the words of the writer's own material, never a coined phrase.
- **Changed in the checker, on the owner's ruling:** with 500 words or more of a writer's sample, V09's 24-word ceiling becomes the sample's own average and the 10% short floor comes off, with the default kept for writers with no sample. V04 on a letter reads only the body, as V09 does, so a letter's header and greeting no longer count as one-sentence paragraphs.
