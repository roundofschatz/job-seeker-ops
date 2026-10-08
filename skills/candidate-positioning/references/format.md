# The positioning file

One Markdown file per posting holds the case for one candidate. This page is the format's one home. resume-ops and cover-letter read files written to it, and `scripts/check_positioning.py` checks them. A full example from a made-up writer sits at the end.

## The file name

The file is named `positioning-<company>-<role>.md` and saved in the folder that holds the person's resume. The company and the role go in lowercase with hyphens between the words, and a legal ending such as "Inc." or "Co." comes off. This command reads them from a saved draft's heading and prints the name, so the posting's words never go into a command:

```
python scripts/check_positioning.py --name-from positioning-draft.md
```

For a draft that opens `# Positioning: Switchgrass Freight Co. · Supply Chain Planning Analyst`, it gives `positioning-switchgrass-freight-supply-chain-planning-analyst.md`.

## How the file starts

```
# Positioning: <Company> · <Role>

Format: candidate-positioning 1
```

The format line lets a reader refuse a version of the file it doesn't know.

## Writing the parts

- Dates are written `YYYY-MM-DD`.
- A source is a file and a line, like `resume.txt L12`, a range of lines, like `resume.txt L8-L9`, or the ID of an answer the person gave in the session, like `A2`. Separate two sources with a semicolon.
- A quote holds the words that state the fact, in double quotes, exactly as the source has them. From a past letter, a whole sentence can move when it states the same proven fact and is still true. Any number, title or date in it is checked against the resume and the dates first.
- A pipe character inside a cell is written `\|`, so the cell doesn't split.
- A section with nothing in it says "None."

## The sections

There are eight, in this order, each with its number. A ninth belongs to cover-letter, which adds a record there for each letter it writes, in the shape under "9. Letters" below. A rebuild keeps section 9 exactly as it was.

### 1. Target

Labelled lines, then the firm facts.

- `- **Company:**` and `- **Role:**`, as the posting names them.
- `- **Posting:**` gives the saved file, the date it was read and the link, or "none".
- `- **Measure of the job:**` quotes the posting's own measure of success, with its line: `"..." (posting.txt L4)`.
- `- **Channel:**` reads upload, text box with its character limit, email, or not given.
- `- **Reader:**` reads cold, warm with the referrer's name and what they agreed to, or not given.
- `- **What matters to the person:**` gives what to lead with, what to avoid and any limits on the search, with its source, or not given.

Under `### Firm facts`, each fact gets a row with these columns: `#` (F1, F2 and on), `Fact`, `Why it matters here`, `Source` and `Checked`. A fact comes from the posting or from the firm's other pages, never from the home page, since every applicant reads the home page. The source is the page's address. When the person saved the page, the saved file and line follow in brackets, like `https://www.example.org/news/plan (firm-pages.md L11)`, so the fact can be checked both ways. When the saved pages include the home page, `check_positioning.py --sources` fails a fact that shares a number with it, such as a store count or a founding year, whichever page the fact cites. A fact from the posting gives the posting's file and line. A fact the person told you gives the answer's ID, after their link when they gave one. Two facts is the floor and there's no ceiling. Each one says in a line why it matters to this case, so whoever writes the letter can pick by relevance. With fewer than two, write the ones there are, or "None.", and say so to the person.

### 2. Requirement map

Every required qualification, preferred qualification and responsibility in the posting gets a row, with these columns:

| Column | Holds |
|---|---|
| `#` | R1, R2 and on |
| `Requirement` | The posting's words, as written |
| `Line` | The posting line it comes from, like `L13` |
| `Kind` | required, preferred or responsibility |
| `Evidence` | The quoted words that answer it, with a short note when one helps, such as years worked out from the dates |
| `Source` | Where each quote sits. For a gap, `searched` and the files searched, then the answer's ID when the person confirmed the gap, like `searched resume.txt; A2` |
| `Strength` | strong, partial, or gap with its owner: `gap, owned by the role` or `gap, shared with <team>` |
| `Show on` | resume, letter, both, or `off` for a gap |

A partial row says in its note which part the evidence covers. A gap row's evidence reads "None." and can name the nearest true fact, so nobody mistakes it for a match.

A posting line that doesn't belong to this role gets no row, such as another unit's requirement in a posting several units share, or a heading over the duties. List those lines once, under the map, with the reason:

```
Not mapped: L34 to L37 and L41 to L45, requirements for other units; L49 and L60, headings over the duties.
```

Every other line that names a requirement or a duty gets a row.

### 3. The hiring team's view

About 150 to 250 words in the hiring team's voice, after the interview. It opens on how the candidate thinks, turns to why that fits this moment, raises the fair concern and what answered it, and ends on an honest summary. It recites no numbers and has no urgency line. `references/case.md` says how to write it.

### 4. The case in four lines

Four numbered lines with these labels, in order:

```
1. **What they want:** ...
2. **Where the candidate stands** (a working note, never on a page): ...
3. **The story the evidence tells:** ...
4. **What the reader should believe:** ...
```

resume-ops takes the summary's direction from them, and cover-letter ends on the fourth.

### 5. Proof bank

Three to five proofs, best first for this posting, each under `### P1. <short name>` with these lines:

- `- **Result:**` names a firm or client and gives a number or an outcome.
- `- **Story:**` gives the problem, what the candidate did and what changed, from the source and in the file's own words.
- `- **Source:**` gives each file and line with its date, like `career-record.md L6 (2026-09-20)`.
- `- **On the resume being sent:**` reads yes or no.
- `- **Use on:**` reads resume, letter or both. A result the resume leaves out can still go on the letter.
- `- **Answers:**` lists the requirement IDs it proves.

### 6. Words to use

The posting's terms the candidate can claim honestly, each with the requirement or proof that backs it, in two columns: `Posting term` and `Claim it with`. Then `### Plain descriptions`, with `Internal name` and `Plain description` columns, or "None." A page uses the plain description, never the internal name.

### 7. Keep off the page

One bullet per item, starting with its kind:

- `- **Gap (R7):**` for each gap row in the map.
- `- **Concern:**` for the concern from section 3. There's one.
- `- **Sensitive:**` for anything the person keeps private, such as a reason for leaving or a pay figure.

A gap and the concern each end with `Watch for:` and the phrases that would put them on a page, in quotes. Pick phrases an honest page about this person would never need, since a script searches finished pieces for them.

### 8. Stamp

A row per source file, with these columns: `File`, `Role`, `Date` and `SHA-256`. The role is one of posting, resume being sent, deeper record, past letter, notes, firm pages, rulings or other. The date is the one written in the file, the one the person gave, or the file's own date, marked as such. The SHA-256 is the first 12 characters of the file's hash, which `check_positioning.py --current` compares to tell whether a source changed. Text files are hashed with their line endings read as plain newlines, so a copy saved on another system matches.

Then three labelled lines:

- `- **Built:**` gives the date and the skill's version.
- `- **Voice check:**` gives plainspeak-writer's version and result, or why it didn't run.
- `- **Confirmed:**` reads `not yet` until step 10, then the date and the person's words in quotes.

Last, `### Answers in this session` lists each answer the file cites, with its ID, the person's words in quotes, and the date, or reads "None."

### 9. Letters

cover-letter adds this section, headed `## 9. Letters`, the first time it writes a letter for the posting, and one record under it for each letter. candidate-positioning never writes here.

Each record starts `### Letter 1 · <Role> · YYYY-MM-DD`, with the letters numbered in the order they were written and the date the record started. These labelled lines come next:

- `- **Role:**` the role, as section 1 names it.
- `- **Date:**` the date the letter was written.
- `- **Channel:**` upload, text box with its character limit, or email.
- `- **Reader:**` cold, or warm with the referrer's name and what they agreed to.
- `- **Resume:**` the resume that goes with the letter, by file name.
- `- **Voice samples:**` the person's own writing that set the letter's sound, by file name, or none.
- `- **Status:**` one of draft, ready, open findings, not reviewed, or sent with its date, like `sent 2026-10-09`.
- `- **Built:**` the skill and its version, like `cover-letter 0.3.0`.

A record is a draft while the map stands and the letter isn't finished. It's ready when the review said Send, or when the person took the letter as it stood. It reads open findings when two reviews still found something to fix, not reviewed when no reviewer was available, and sent once the person says the letter went out.

Three parts follow, each under its own `####` heading:

- `#### Map`, a table with the columns `Movement`, `What it says` and `From`, and a row each for Frame, Proof, Fit and why now, Invitation, Referral and Off the page. `From` names the parts of this file the row draws on, such as `P1; P3` or `F2; section 3`. The Referral row reads "None." for a cold reader. The Off the page row names the concern and the proof that answers it without naming it.
- `#### Checks`, one line for each check with its result: the voice check, the body's word count, `check_letter.py`, the sentence list, the two swap tests, any sentence from the person's earlier writing, each review's verdict, what the posting says about AI, and the watermark notice given at hand-over.
- `#### Text`, the letter as the person got it, word for word, in a fenced block that opens with three backticks and `text`.

A draft record needs its labelled lines and its map. Past draft, it also needs its checks and its text. `check_positioning.py` checks both, and a heading inside the fenced text never counts as a record.

## A full example

Writer B from the plugin's tests, Dmitri Okafor, applying to a made-up freight firm. The quotes point at the files in `tests/writers/b-okafor/`, and the unit tests check every one of them.

```markdown
# Positioning: Switchgrass Freight Co. · Supply Chain Planning Analyst

Format: candidate-positioning 1

## 1. Target

- **Company:** Switchgrass Freight Co.
- **Role:** Supply Chain Planning Analyst
- **Posting:** posting.txt, read 2026-10-05. Link: none, since the person pasted the text.
- **Measure of the job:** "Last year our forecasts missed by 24% on average, and a missed forecast means idle docks one day and overtime the next." (posting.txt L4)
- **Channel:** upload
- **Reader:** cold
- **What matters to the person:** lead with the forecast-error result, and keep the 2020 reorganization and pay out of everything (positioning-notes.md L3, L5, L7).

### Firm facts

| # | Fact | Why it matters here | Source | Checked |
|---|---|---|---|---|
| F1 | Switchgrass moves less-than-truckload freight for 2,400 shippers across the Midwest. | Volume rises and falls with the shipper mix, the way Brightwell's demand moved with store promotions. | posting.txt L4 | 2026-10-05 |
| F2 | The planning team forecasts by lane and by terminal, so docks are staffed and trailers placed before the freight shows up. | A miss lands on dock staffing, and Dmitri ran warehouse cycle counts before he moved to forecasting. | posting.txt L4 | 2026-10-05 |
| F3 | Switchgrass added Saturday dock shifts at six terminals in 2026 and staffs them from the weekly forecast. | Saturday staffing now rides on a forecast that's right by terminal. | https://www.switchgrass-freight.example/news/saturday-dock-shifts | 2026-10-05 |

## 2. Requirement map

| # | Requirement | Line | Kind | Evidence | Source | Strength | Show on |
|---|---|---|---|---|---|---|---|
| R1 | Bachelor's degree in supply chain, business, analytics or a related field. | L13 | required | "Bachelor of Science in Supply Chain Management, Prairie Bluff University, 2018" | resume.txt L18 | strong | resume |
| R2 | Three or more years in demand planning, supply planning or forecasting. | L14 | required | "Planning Analyst \| Aug 2021 - Present"; about five years of forecasting to October 2026, worked out from the dates. The career record gives the formal title, "Planning Analyst II", and the resume's title stands (A1). | resume.txt L7; career-record.md L4; A1 | strong | both |
| R3 | Advanced Excel, including pivot tables and lookups, and working SQL. | L15 | required | "rebuilding the forecast in SQL and Excel"; "Excel (pivot tables, XLOOKUP, Power Query), SQL" | resume.txt L9; resume.txt L21 | strong | resume |
| R4 | Experience with a transportation or warehouse management system. | L16 | required | "Ran cycle counts in Manhattan WMS" | resume.txt L14 | strong | both |
| R5 | Clear written updates for people who don't work with data. | L17 | required | "Write a one-page weekly note on forecast misses for the buying team." | resume.txt L11 | strong | both |
| R6 | Power BI or Tableau. | L20 | preferred | "Built a Power BI dashboard that 14 buyers use every Monday to set orders." | resume.txt L10 | strong | resume |
| R7 | Experience in less-than-truckload or other freight. | L21 | preferred | None. His forecasting has been for grocery items. | searched resume.txt, career-record.md, positioning-notes.md | gap, owned by the role | off |
| R8 | Build and run weekly volume forecasts for 38 terminals. | L7 | responsibility | "Forecast weekly demand for 1,900 items across three distribution centers." Weekly forecasts at scale, by item and distribution center rather than by terminal. | resume.txt L8 | partial | both |
| R9 | Find the lanes where forecasts miss most, and fix the inputs. | L8 | responsibility | "by rebuilding the forecast in SQL and Excel with store promotions as an input"; "The first quarter after the rebuild was still at 24%." | resume.txt L9; career-record.md L6 | strong | both |
| R10 | Turn forecasts into dock staffing and trailer plans with the operations team. | L9 | responsibility | "Built a Power BI dashboard that 14 buyers use every Monday to set orders." His forecasts became buying plans, not staffing plans. | resume.txt L10 | partial | letter |
| R11 | Report forecast accuracy every week to terminal managers. | L10 | responsibility | "Write a one-page weekly note on forecast misses for the buying team." | resume.txt L11 | strong | both |

## 3. The hiring team's view

We came away thinking Dmitri treats a forecast miss as a question with an answer. At Brightwell he went looking for the input the old forecast never saw, found it in store promotions, and rebuilt the forecast around it. Our planning team needs that habit, because our misses come from inputs nobody has named yet, lane by lane.

Our concern was freight. He has planned grocery demand, not trailers, and our volume moves with shippers rather than shelves. What answered it was his time on the warehouse side. He ran cycle counts on a warehouse floor before he built a single forecast, so he has worked where a bad forecast lands. He also writes the kind of weekly note our terminal managers would want.

He'd learn our lanes quickly, because he starts with the misses. We'd hire him for the way he finds the cause of a miss, and we'd expect his first months to go into learning which inputs move our volume.

## 4. The case in four lines

1. **What they want:** A planner who finds why Switchgrass's lane forecasts miss and fixes the inputs, so docks get staffed and trailers placed before the freight arrives.
2. **Where the candidate stands** (a working note, never on a page): Strong on finding the input behind a miss, rebuilding a forecast in SQL and Excel, and weekly written reporting. No freight or terminal work, since his planning has been for groceries.
3. **The story the evidence tells:** At Brightwell he found the input the old forecast missed, rebuilt the forecast around store promotions, and cut its error from 31% to 19%.
4. **What the reader should believe:** Dmitri finds the input behind a forecast miss and fixes it, and he can do that for Switchgrass's lanes.

## 5. Proof bank

### P1. Forecast error cut at Brightwell Grocers Distribution

- **Result:** Brightwell Grocers Distribution's weekly forecast error fell from 31% to 19% over 52 weeks.
- **Story:** Brightwell's weekly forecast missed by 31% across 1,900 items in three distribution centers. Dmitri rebuilt it in SQL and Excel and added store promotions as an input. The first quarter after the rebuild still missed by 24%, and over 52 weeks the error came down to 19%.
- **Source:** resume.txt L8-L9 (2026-10-02); career-record.md L6 (2026-10-02)
- **On the resume being sent:** yes
- **Use on:** both
- **Answers:** R2, R3, R9

### P2. The dashboard Brightwell's buyers order from

- **Result:** At Brightwell, 14 buyers set their orders every Monday from a Power BI dashboard Dmitri built.
- **Story:** Dmitri built a Power BI dashboard for Brightwell's buying team. All 14 buyers now use it every Monday to decide what to order.
- **Source:** resume.txt L10 (2026-10-02)
- **On the resume being sent:** yes
- **Use on:** both
- **Answers:** R6, R10

### P3. Count variance cut in Manhattan WMS

- **Result:** In a 410,000-square-foot Brightwell warehouse, cycle-count variance fell from 2.8% to 0.9%.
- **Story:** As an inventory coordinator, Dmitri ran cycle counts in Manhattan WMS for a 410,000-square-foot warehouse. He moved high-value items to weekly counts, and count variance fell from 2.8% to 0.9%.
- **Source:** resume.txt L13-L15 (2026-10-02)
- **On the resume being sent:** yes
- **Use on:** letter
- **Answers:** R4

## 6. Words to use

| Posting term | Claim it with |
|---|---|
| forecasting | R2, P1 |
| demand planning | R2 |
| SQL | R3, P1 |
| pivot tables | R3 |
| warehouse management system | R4, P3 |
| Power BI | R6, P2 |
| forecast accuracy | R11, P1 |
| written updates | R5 |

### Plain descriptions

None.

## 7. Keep off the page

- **Gap (R7):** no less-than-truckload or other freight work. Watch for: "new to freight", "no freight experience", "learning freight"
- **Concern:** he has planned grocery demand, not freight volume, so the hiring team may doubt how fast he learns lanes. Watch for: "different industry", "learning curve", "outside freight"
- **Sensitive:** the 2020 reorganization and the night shifts it brought (career-record.md L5; positioning-notes.md L5). Watch for: "reorganization", "night shift"
- **Sensitive:** the reason for looking (career-record.md L7). Watch for: "no path", "senior analyst"
- **Sensitive:** pay, both the salary floor and the target (career-record.md L13; positioning-notes.md L7). Watch for: "salary", "$85,000", "top of the range"

## 8. Stamp

| File | Role | Date | SHA-256 |
|---|---|---|---|
| posting.txt | posting | 2026-10-05 (read) | 5bc4bf94f8b5 |
| resume.txt | resume being sent | 2026-10-02 (file date) | 8d312d2052e2 |
| career-record.md | deeper record | 2026-10-02 (file date) | 14935e046b70 |
| positioning-notes.md | notes | 2026-10-02 (file date) | 7a4cbb96790b |

- **Built:** 2026-10-05 by candidate-positioning 0.2.0
- **Voice check:** plainspeak-writer 1.6.2, letter surface, no HARD hits
- **Confirmed:** 2026-10-05, "Yes, that's my case. Keep Planning Analyst, and keep freight off everything."

### Answers in this session

| # | Answer | Date |
|---|---|---|
| A1 | "Keep Planning Analyst on the page. HR has it as Planning Analyst II." | 2026-10-05 |
```
