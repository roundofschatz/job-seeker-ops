# The letter

The resume is the evidence. The letter is the reasoning: why this firm, why this seat, why now, proved by two or three named results. This page covers the letter's shape, where each part takes its material from in the positioning file, the map, the three channel forms and the record. A full example from a made-up writer sits at the end, and the plugin's unit tests check it against his files.

## The shape

Four movements on one page [C01, C03, C08, C10]. The body, the paragraphs between the salutation and the sign-off, runs 350 to 450 words: around the 400 that one survey's hiring managers preferred on average [C18], and well past the one or two paragraphs that rarely make the case [C09]. `check_letter.py` fails it over 500, and plainspeak-writer's own floor for a cover letter is 250.

| Movement | What it does | Words | From the positioning file |
|---|---|---|---|
| Frame | Opens inside the reader's problem or the posting's own measure of the job, and names the firm or the seat in the first two sentences. The credential comes after the setup. A referral, when there is one, goes in the first two sentences | 60 to 90 | Section 1, the measure of the job. Section 3's opening, on how the candidate thinks |
| Proof | Two or three results, each a named firm or client with a number, an adopted outcome or a scale. Each sentence ends on what the work produced for the people who paid for it | 120 to 170 | Section 5, the proofs marked letter or both, told from their stories |
| Fit and why now | Two firm facts and what the writer would do with them in the seat, and the reason for the move now, said as forward motion | 100 to 150 | Section 1, the firm facts. Section 3 |
| Invitation | What the reader should believe, in first person, then the ask: a conversation about one named thing | 40 to 70 | Section 4, line 4 |

The word ranges are working budgets, and the 500-word cap is the rule. The Proof can take two paragraphs, so the body runs four to six.

## Around the body

- **Header.** The resume's contact block, since the letter is formatted like the resume [C02, C05]: the name on its own line, then the contact line, with the same details the resume has. Then the date, written out ("October 7, 2026"). An uploaded letter has both; a text box and an email have neither.
- **Salutation.** A person when the posting or the person names one, written "Dear Maria Lopez," or "Dear Ms. Lopez,". Otherwise the firm's hiring team: "Dear Switchgrass Freight hiring team," [C01, C05, C08, C18]. Never "To Whom It May Concern" [C01] and never "Dear Sir or Madam".
- **Sign-off.** One plain word and a comma ("Best," or "Sincerely,"), then the name as the resume gives it, without credentials. No thank-you line before it, since the ask is the last sentence.

## Building each movement

**Frame.** Open on something the reader already cares about: the measure of the job in the posting's own words, or the problem the firm is buying a fix for. The first sentence is content, never an announcement of the letter's plan or the stock line naming the job and where it was posted [C06, C08]. The introduction is the part of a letter hiring managers most often say leaves the biggest impression [C18]. The writer's credential comes in the second or third sentence, once the reader is inside the problem. For a warm reader, one sentence names the referrer, the role and why they suggested writing, saying no more than the referrer agreed to, and then the problem [C06, C08, C19].

**Proof.** Pick two or three proofs marked letter or both [C01, C03], in the bank's order, unless the concern says otherwise. The gap and the concern in section 7 decide which proof leads: put first the proof that answers the concern without naming it. Tell each one from its story: the problem, the writer's action, the change it made. A story shows a trait that a claim only names [C09]. A proof the resume leaves out ("On the resume being sent: no") belongs here most of all, since the letter is the only place the reader meets it. Keep every title, date and figure the way the resume and the story give them.

**Fit and why now.** Use two firm facts, and use each one: say how the writer would use it in the seat, never "I admire your mission." The guides ask for the firm's own products, customers, news and challenges, then how the writer's work meets them [C04, C06]. Pick by the "Why it matters here" column. The reason for the move now is forward motion: the work this seat opens up [C11, C12]. When the person has said why they want to move, in the file or in the session, use their words. When they haven't, the why-now rests on the firm's moment (the new building, the adoption this year, the shifts added in 2026), and the letter states no reason of the person's own. Never a departure story, a complaint, a pay figure or anything from section 7 [C10].

**Invitation.** The last paragraph opens on section 4's line 4, said as "I". Then the ask: a conversation about one named thing, taken from the measure or a firm fact, like "the lanes your forecasts miss most". "The role", "my qualifications" and "how I can contribute" aren't named things. The ask is the last sentence, a direct call to act with nothing trailing after it [C01, C10].

Write the ask the way this writer would say it to the reader, starting from the named thing: a direct question, or a plain request in the writer's words. A stock opener such as "I'd like to talk about", "I'd welcome the chance to discuss" or "I look forward to" reads as a template, and every letter in the first live runs ended on one. `check_letter.py` warns on a stock opener, and on an ask that opens with the same four words as the writer's earlier letter.

## What never goes on the page

Anything the writer lacks: a missing title, market, tool, credential, or anything they "have to learn" [C10]. The gap and the concern decide which proof leads and stay in the file. Two sources say to explain a gap or an unusual path in the letter [C07, C09]. This skill doesn't, since on a letter a gap reads as a reason to say no. Also: a reason for leaving, a complaint, salary [C10], the resume's lines restated [C02, C03, C09, C10], a sentence about how honest the letter is being, an internal method name (section 6 gives the plain description to use instead), and a quote from a client or a colleague.

## The map

Before drafting, write the map into the letter's record in section 9 of the positioning file: one row per movement, with what it will say and where that comes from. A row with nothing to say sends the work back to the positioning file, never to an old letter. The record's format is in candidate-positioning's `references/format.md`, under "9. Letters".

| Movement | What it says | From |
|---|---|---|
| Frame | Last year's 24% miss and its cost in the posting's words; the analyst's job, the same work he's done since 2021 | Section 1, measure; section 3 |
| Proof | The forecast rebuilt around store promotions, 31% to 19%; the dashboard 14 buyers order from | P1; P2 |
| Fit and why now | Lanes and terminals, and the Saturday dock shifts staffed from the weekly forecast in 2026; his warehouse years answer the freight concern | F2; F3; P3; section 3 |
| Invitation | Line 4 in his voice, then the lanes that miss most and the Saturday docks | Section 4, line 4; F3 |
| Referral | None. The reader is cold. | Section 1, Reader |
| Off the page | The freight concern, answered by the warehouse floor in P3 without naming it; the 2020 reorganization, the reason for looking and pay stay out | Section 7 |

## Sentences from earlier writing

A sentence from an earlier letter, or other writing the person picked as a voice sample, can go into a new letter word for word when it states the same proven fact, the three files hold that fact, and it's still true today. A sentence whose fact runs on time is checked against today's dates first, and one the files have since changed doesn't move as written. A sentence plainspeak-writer's checker blocks in a sample never moves.

| From an earlier letter | Moves? |
|---|---|
| "I've mentored four student teachers from Columbia Plateau University." The resume holds it, and it's still true | Yes, into the Proof |
| "I bring eight years of classroom experience." Written in 2021; the files work out about 13 years now | No, as written. Say what the dates say now, or leave it out |
| "For the last two years I've led the department." Runs on time | No, as written |
| "I'd welcome a conversation about your coaching program." Written for another firm | No. The Frame, the Fit and the Invitation are written for each firm |

No sentence repeats word for word within one letter.

## The three channel forms

The draft is always kept as text, in the form the channel takes, and that same text goes to the review.

**Upload.** The full letter. Applicant systems fill their fields from the resume [C13], so the letter is written for the person who opens it, in a file every major system takes [C14]. `build_letter.py` turns it into the Word file, named `FirstName_LastName_CoverLetter_Company.docx`, with the resume's font, size and margins, one column, and the writer's name in the author field, plus a plain-text copy for pasting. The skill never makes a PDF, though one guide prefers it [C01]. When a posting demands one, the person exports it from the Word file.

```text
Dmitri Okafor
Kansas City, MO | (816) 555-0172 | dmitri.okafor@example.com

October 7, 2026

Dear Switchgrass Freight hiring team,

<body paragraphs, a blank line between them>

Best,
Dmitri Okafor
```

**Text box.** The salutation, the body, the sign-off and the name, pasted as plain text [C23], with no contact block or date, since the form holds those. Paragraphs split by a blank line, straight quotes, no bold, no bullets, and inside the box's character limit. `check_letter.py` counts every character a person pastes.

**Email.** The letter goes in the email's body, which more readers in one survey preferred to an attachment [C20]. The first line is the subject, naming the role: `Subject: Supply Chain Planning Analyst application`. Then the salutation, the body, the sign-off and the name, with no contact block, and a note to attach the resume.

## The record

When the letter is done, the record in section 9 gets its status, its checks and its text, as `format.md` describes. The checks part lists each check with its result, and any warning cleared with its reason, so whoever opens the file later can see how the letter was checked.

## A full example

Writer B from the plugin's tests, Dmitri Okafor, writing to the made-up freight firm whose positioning file is the example at the end of candidate-positioning's `references/format.md`. The channel is an upload and the reader is cold. The unit tests run `check_letter.py` on this letter against that file and his files in `tests/writers/b-okafor/`.

```text
Dmitri Okafor
Kansas City, MO | (816) 555-0172 | dmitri.okafor@example.com

October 7, 2026

Dear Switchgrass Freight hiring team,

Last year Switchgrass's forecasts missed by 24% on average, and your posting puts the cost plainly: idle docks one day and overtime the next. Your planning analyst will build the weekly volume forecasts for 38 terminals, find the lanes where they miss most and fix the inputs. I've done that work at Brightwell Grocers Distribution since 2021.

Brightwell's weekly forecast used to miss by 31% across 1,900 items in three distribution centers. I rebuilt it in SQL and Excel and added store promotions as an input, since the old forecast never saw them. The first quarter after the rebuild still missed by 24%, and over 52 weeks the error came down to 19%. Brightwell's 14 buyers now set their orders every Monday from a Power BI dashboard I built for the buying team, and I write the one-page weekly note that tells them where the forecast missed that week.

Switchgrass moves less-than-truckload freight for 2,400 shippers across the Midwest and plans by lane and by terminal, so docks get staffed and trailers placed before the freight shows up. This year you added Saturday dock shifts at six terminals and staff them from the weekly forecast, so a miss now lands on a Saturday crew as well as a weekday one. Before I forecast anything, I was Brightwell's inventory coordinator, on the floor where a miss lands. I ran the cycle counts in Manhattan WMS for a Brightwell warehouse, and count variance fell from 2.8% to 0.9% once its high-value items were counted every week. In your seat I'd start the way I started at Brightwell, with the lanes that miss most and the inputs behind them, and your terminal managers would get the same kind of weekly note on what missed, written for people who don't work with data.

I find the input behind a forecast miss and fix it, and I can do that for Switchgrass's lanes. Could we set up a call about the lanes your forecasts miss most, and which of those lanes decide how many people you put on the Saturday docks at your six terminals?

Best,
Dmitri Okafor
```

How it meets the shape:

- **Frame.** It opens on the posting's own measure, the 24% miss and what it costs, and names Switchgrass in the first sentence. His credential comes in the third, in ten words, once the job is set out.
- **Proof.** P1, told from its story, including the first quarter that still missed, which only the career record holds. P2 ends on the buyers' orders from the dashboard.
- **Fit and why now.** F2 and F3, each used: the forecast now staffs Saturday crews. P3's warehouse years answer the freight concern without naming it, and the why-now rests on the firm's moment, since his reason for looking is on section 7's list.
- **Invitation.** Line 4 in his voice, then the ask as a direct question about one named topic, the lanes that miss most.
- **Off the page.** No freight gap, no reorganization, no reason for looking, no pay.

`check_letter.py` gives a body of 350 words and two warnings, both cleared by reading in the record: the warehouse sentence follows resume lines 14 and 15, and it tells them as a story that ends on the result rather than restating either line.
