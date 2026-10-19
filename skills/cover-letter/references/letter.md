# The letter

The resume is the evidence. The letter is the reasoning: one claim about why this writer fits this firm's seat now, proved by two or three named results. This page covers the letter's shape, where each part takes its material from in the positioning file, the map, the three channel forms and the record. A full example from a made-up writer sits at the end, and the plugin's unit tests check it against his files.

## The shape

One claim, argued in four movements on one page [C01, C03, C08, C10]. One page is the limit, and `check_letter.py` fails a letter that runs past it. The body, the paragraphs between the salutation and the sign-off, runs about 350 to 450 words: around the 400 that one survey's hiring managers preferred on average [C18], and well past the one or two paragraphs that rarely make the case [C09]. That range is a guide for what goes in, never a reason to cut. plainspeak-writer's own floor for a cover letter is 250.

| Movement | What it does | Words | From the positioning file |
|---|---|---|---|
| Frame | Opens on the facts the claim explains, the reader's own problem told as fact, and names the firm or the seat in the first two sentences. The credential comes after the setup. A referral, when there is one, goes in the first two sentences | 60 to 90 | Section 1, the facts behind the measure of the job. Section 3's opening, on how the candidate thinks |
| Proof | Two or three results, each a named firm or client with a number, an adopted outcome or a scale, each one answering the claim or one of the posting's asks. Each sentence ends on what the work produced for the people who paid for it | 120 to 170 | Section 5, the proofs marked letter or both, told from their stories |
| Fit and why now | Two firm facts and what the writer would do with them in the seat, and the reason for the move now, said as forward motion | 100 to 150 | Section 1, the firm facts. Section 3 |
| Invitation | The ask alone: a conversation about one named thing | 20 to 50 | Section 1, the measure or a firm fact |

The word ranges are working budgets, and none of them is a reason to cut a sentence. The Proof can take two paragraphs, so the body runs four to six.

## One claim

The letter argues one claim, written in the map before any sentence. It's one sentence about what this writer does that this firm needs, built from lines 3 and 4 of the case and section 3, and stated in the words the writer's own material uses: a voice sample, an answer the person gave, a proof's story. Never a coined phrase. When the samples hold a sentence of the writer's that says it, use that sentence's words.

Every body paragraph answers part of the claim or one of the posting's asks, and its first sentence says which. Every sentence after that one stays on the paragraph's subject and picks up the sentence before it. A proof that answers neither the claim nor an ask stays out, however good it is. In a comparison of two sessions' letters, the one the writer judged better made one argument from his own paper and kept each paragraph on one subject; the drafts he rejected moved from proof to proof in resume order.

Line 4 of the case, what the reader should believe, sets the claim and never goes in the letter as a sentence. Both first drafts in that comparison closed on line 4 restated, and the writer cut it each time.

## Around the body

- **Header.** An uploaded letter opens on a business letter's header, at the body's size and never bold: the date it goes out, a blank line, the recipient on one line, then a Re: line with the posting's title as the posting writes it and its requisition number when the posting gives one, like `Re: Field Operations Manager, Req ID 20417`. A blank line, then the salutation. The recipient line is the firm and the team or the person, like `Switchgrass Freight Co., Planning Team` or `Maria Lopez, Switchgrass Freight Co.`, with no street address. The writer's name, email, phone, city and links stay off the header, since the resume on top of the stack gives them, and the name goes at the sign-off. Two guides say to format the letter like the resume [C02, C05], so it takes the resume's font, size and margins. A text box and an email have no header.
- **Salutation.** A person when the posting or the person names one, written "Dear Maria Lopez," or "Dear Ms. Lopez,". Otherwise the firm's hiring team: "Dear Switchgrass Freight hiring team," [C01, C05, C08, C18]. Never "To Whom It May Concern" [C01] and never "Dear Sir or Madam".
- **Sign-off.** One plain word and a comma ("Best," or "Sincerely,"), then the name as the resume gives it, without credentials. No thank-you line before it, since the ask is the last sentence.

## Building each movement

**Frame.** Open on something the reader already cares about: the facts the claim explains, such as the problem the firm is buying a fix for, stated as facts. Never tell the reader how their own posting sizes up the job, as in "Your posting measures this role by...", since they wrote it; both first drafts in the comparison opened that way, and the writer called it AI language. Naming what the posting asks for, so the letter can answer each ask, is fine. The first sentence is content, never an announcement of the letter's plan or the stock line naming the job and where it was posted [C06, C08]. The introduction is the part of a letter hiring managers most often say leaves the biggest impression [C18]. The writer's credential comes in the second or third sentence, once the reader is inside the problem. For a warm reader, one sentence names the referrer, the role and why they suggested writing, saying no more than the referrer agreed to, and then the problem [C06, C08, C19].

**Proof.** Pick two or three proofs marked letter or both [C01, C03], each one answering the claim or one of the posting's asks, and order them by what they answer, never by the resume. The gap and the concern in section 7 decide which proof leads: put first the proof that answers the concern without naming it. Tell each one from its story: the problem, the writer's action, the change it made. A story shows a trait that a claim only names [C09]. A proof the resume leaves out ("On the resume being sent: no") belongs here most of all, since the letter is the only place the reader meets it. Keep every title, date and figure the way the resume and the story give them.

**Fit and why now.** Use two firm facts, and use each one: say how the writer would use it in the seat, never "I admire your mission." The guides ask for the firm's own products, customers, news and challenges, then how the writer's work meets them [C04, C06]. Pick by the "Why it matters here" column. The reason for the move now is forward motion: the work this seat opens up [C11, C12]. When the person has said why they want to move, in the file or in the session, use their words. When they haven't, the why-now rests on the firm's moment (the new building, the adoption this year, the shifts added in 2026), and the letter states no reason of the person's own. Never a departure story, a complaint, a pay figure or anything from section 7 [C10].

**Invitation.** The last paragraph is the ask alone, right after the last point, with no line summing up the letter: a conversation about one named thing, taken from the measure or a firm fact, like "the lanes your forecasts miss most". "The role", "my qualifications" and "how I can contribute" aren't named things. The ask is the last sentence, a direct call to act with nothing trailing after it [C01, C10].

Write the ask the way this writer would say it to the reader, starting from the named thing: a direct question, or a plain request in the writer's words. A stock opener such as "I'd like to talk about", "I'd welcome the chance to discuss" or "I look forward to" reads as a template, and every letter in the first live runs ended on one. `check_letter.py` warns on a stock opener, and on an ask that opens with the same four words as the writer's earlier letter.

## What never goes on the page

Anything the writer lacks: a missing title, market, tool, credential, or anything they "have to learn" [C10]. The gap and the concern decide which proof leads and stay in the file. Two sources say to explain a gap or an unusual path in the letter [C07, C09]. This skill doesn't, since on a letter a gap reads as a reason to say no. Also: a reason for leaving, a complaint, salary [C10], the resume's lines restated [C02, C03, C09, C10], a sentence about how honest the letter is being, an internal method name (section 6 gives the plain description to use instead), and a quote from a client or a colleague.

## The map

Before drafting, write the map into the letter's record in section 9 of the positioning file: the claim first, then one row per movement, with what it will say, what it answers, and where that comes from. A row with nothing to say sends the work back to the positioning file, never to an old letter. The record's format is in candidate-positioning's `references/format.md`, under "9. Letters".

| Movement | What it says | From |
|---|---|---|
| Claim | A forecast misses on an input nobody has named yet, and Dmitri finds the input behind a miss and fixes it | Section 3; section 4, lines 3 and 4 |
| Frame | Last year's 24% miss and what it cost, told as fact; the analyst's job of fixing the inputs; finding the input is his work since 2021, with store promotions beside the shipper mix. Answers the claim | Section 1, measure; F1; section 3 |
| Proof | The forecast rebuilt around store promotions, 31% to 19%, answers the claim; the dashboard 14 buyers order from and the weekly note answer R10 and R11 | P1; P2 |
| Fit and why now | Lanes and terminals, and the Saturday dock shifts staffed from the weekly forecast in 2026; his warehouse years answer the freight concern; in the seat, the lanes that miss most first. Answers the claim for Switchgrass | F2; F3; P3; section 3 |
| Invitation | The ask alone: the lanes that miss most and the Saturday docks | Section 1, measure; F3 |
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
October 19, 2026

Switchgrass Freight Co., Planning Team
Re: Supply Chain Planning Analyst

Dear Switchgrass Freight hiring team,

<body paragraphs, a blank line between them>

Best,
Dmitri Okafor
```

**Text box.** The salutation, the body, the sign-off and the name, pasted as plain text [C23], with no header, since the form holds the name, email and phone. Paragraphs split by a blank line, straight quotes, no bold, no bullets, and inside the box's character limit. `check_letter.py` counts every character a person pastes.

**Email.** The letter goes in the email's body, which more readers in one survey preferred to an attachment [C20]. The first line is the subject, naming the role: `Subject: Supply Chain Planning Analyst application`. Then the salutation, the body, the sign-off and the name, with no header, and a note to attach the resume.

## The record

Before any script runs, the record gets the red-team list: every finding from reading the draft as the hiring manager, under eight fixed headings, with the paragraph each one sent back for a rewrite. `checks.md` has the headings and an example. When the letter is done, the record gets its status, its checks and its text, as `format.md` describes. The checks part lists each check with its result, and any warning cleared with its reason, so whoever opens the file later can see how the letter was checked.

## A full example

Writer B from the plugin's tests, Dmitri Okafor, writing to the made-up freight firm whose positioning file is the example at the end of candidate-positioning's `references/format.md`. The channel is an upload and the reader is cold. The unit tests run `check_letter.py` on this letter against that file and his files in `tests/writers/b-okafor/`.

```text
October 19, 2026

Switchgrass Freight Co., Planning Team
Re: Supply Chain Planning Analyst

Dear Switchgrass Freight hiring team,

Last year Switchgrass's forecasts missed by 24% on average, and a missed forecast meant idle docks one day and overtime the next. Your planning analyst will build the weekly volume forecasts for 38 terminals, find the lanes where they miss most and fix the inputs behind them. Finding the input behind a miss is the work I've done at Brightwell Grocers Distribution since 2021, where demand rises and falls with store promotions the way your volume rises and falls with the shipper mix.

Brightwell's weekly forecast used to miss by 31% across 1,900 items in three distribution centers. I rebuilt it in SQL and Excel and added store promotions as an input, since the old forecast never saw them. The first quarter after the rebuild still missed by 24%, and over 52 weeks the error came down to 19%. Brightwell's 14 buyers now set their orders every Monday from a Power BI dashboard I built for the buying team, and I write the one-page weekly note that tells them where the forecast missed that week.

Switchgrass moves less-than-truckload freight for 2,400 shippers across the Midwest and plans by lane and by terminal, so docks get staffed and trailers placed before the freight shows up. This year you added Saturday dock shifts at six terminals and staff them from the weekly forecast, so a miss now lands on a Saturday crew as well as a weekday one. Before I forecast anything, I was Brightwell's inventory coordinator, on the floor where a miss lands. I ran the cycle counts in Manhattan WMS for a Brightwell warehouse, and count variance fell from 2.8% to 0.9% once its high-value items were counted every week. In your seat I'd start the way I started at Brightwell, with the lanes that miss most and the inputs behind them, and your terminal managers would get the same kind of weekly note on what missed, written for people who don't work with data.

Could we set up a call about the lanes your forecasts miss most, and which of those lanes decide how many people you put on the Saturday docks at your six terminals?

Best,
Dmitri Okafor
```

How it meets the shape:

- **Header.** The date, the recipient line naming the firm and the planning team the posting names, and a Re: line with the posting's title. The posting gives no requisition number, so the Re: line has none.
- **Claim.** Every paragraph answers it: the miss and the work of finding its input, the input he found at Brightwell, and how that work lands at Switchgrass. Line 4 of the case set the claim and appears nowhere as a sentence.
- **Frame.** It opens on the 24% miss and what it cost, told as fact, never as what the posting says, and names Switchgrass in the first sentence. His credential comes in the third, once the job is set out, and sets Brightwell's store promotions beside Switchgrass's shipper mix, from F1.
- **Proof.** P1, told from its story, including the first quarter that still missed, which only the career record holds. P2 ends on the buyers' orders from the dashboard and the weekly note.
- **Fit and why now.** F2 and F3, each used: the forecast now staffs Saturday crews. P3's warehouse years answer the freight concern without naming it, and the why-now rests on the firm's moment, since his reason for looking is on section 7's list.
- **Invitation.** The ask alone, as a direct question about one named topic, the lanes that miss most.
- **Off the page.** No freight gap, no reorganization, no reason for looking, no pay.

`check_letter.py` gives a body of 357 words on about 0.70 of a page, and two warnings, both cleared by reading in the record: the warehouse sentence follows resume lines 14 and 15, and it tells them as a story that ends on the result rather than restating either line.
