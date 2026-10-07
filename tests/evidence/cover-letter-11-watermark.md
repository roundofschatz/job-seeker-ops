# Cover letter test 11: the watermark notice

Spec: "The watermark notice appears once in the README and once at hand-over, and nothing in the skill tries to remove the mark."

**The hand-overs.** Every run that handed over a letter gave the line once, in the words SKILL.md step 9 sets:

| Run | Times the line appears | The line as given |
|---|---|---|
| cl-f1 | 1 | "Current Claude models put an invisible watermark in the text they write, which stays with copied text, so this letter's text may carry one [C24]." |
| cl-e1 | 1 | The same, with "[C24]" |
| cl-g1 | 1 | The same, without "[C24]" |
| cl-b1 | 1 | The same, with "[C24]" |
| cl-f2 | 1 | The same, without "[C24]" |

The runs that stop before a letter, cl-n1, cl-n2 and cl-e2, hand over no letter and give no line. Neither run without the skill mentions the mark. The counts come from `grep -o "invisible watermark"` on each `cover-letter-runs/<run>/handback.md`.

**The README.** "Current Claude models put an invisible watermark in the text they write" appears once, in the paragraph under "### The watermark", with its sources [C24, C25].

**Nothing removes or hides the mark.** In the five letter runs' transcripts, the only tool calls that name the watermark are the hand-overs themselves and one search in cl-e1 for rows C24 and C25 of `sources.md`. No file in any run folder mentions the mark. SKILL.md step 9 tells the skill never to remove, hide or get around the mark, or suggest a way to, and the README says the same.

## A fix this test led to

Three of the hand-overs gave "[C24]" inside the line. That source ID means something to the skill's files but not to the person reading the letter. SKILL.md now gives the line without the ID and keeps the citation in the sentence after it, which only Claude reads. cl-g1 gave the line without it before the change, and cl-f2, which ran after it, gave the line without it too.

## Result

Pass.
