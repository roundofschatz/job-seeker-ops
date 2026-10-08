# Cover letter test 17: the plugin's own plainspeak-writer

New in 0.4.0, when plainspeak-writer and resume-ops came with the plugin. The test checks that a cover letter run uses the copy of plainspeak-writer beside the skill, in its reading and in every script, even with another copy installed on the same computer.

## The run

- Run: cl-f1, staged again with `stage_run.py cl-f1` into `..\jso-tests\cover-letter\runs\cl-f1-040\` on 2026-10-07.
- Skill: `skills/cover-letter/` from this repository's working tree, with the plugin's other skills beside it in `skills/`, as `RUN-TESTS-cover-letter.md` now says. plainspeak-writer 1.7 was also installed on this computer as an uploaded skill in the desktop app, and job-seeker-ops 0.3.2 as a plugin.
- Replies: none. Her first message named the channel and the samples, and the skill found nothing else missing, so it drafted without asking.
- Product: Claude Code 2.1.293 in the Code tab of the Claude desktop app on Windows 11, Python 3.12.10, LibreOffice installed.
- Copies: `tests/evidence/cover-letter-runs/cl-f1-040/` holds the hand-back, the scan, the letter as text and as a Word file, and the positioning file with its record.

## What the transcript shows

`scan_transcript.py` lists 54 tool calls. Four of them read plainspeak-writer's files, and all four name the copy beside the skill:

```text
Read: file_path='C:\\Users\\<user>\\repos\\tools\\job-seeker-ops\\skills\\plainspeak-writer\\SKILL.md'
Read: file_path='C:\\Users\\<user>\\repos\\tools\\job-seeker-ops\\skills\\plainspeak-writer\\references\\voice.md'
Read: file_path='C:\\Users\\<user>\\repos\\tools\\job-seeker-ops\\skills\\plainspeak-writer\\references\\formats\\letter.md'
Read: file_path='C:\\Users\\<user>\\repos\\tools\\job-seeker-ops\\skills\\plainspeak-writer\\references\\tells.md'
```

The helper made no Skill tool call, so it never loaded the uploaded copy, and no call names a folder under the desktop app's uploads. Every voice check in the run's tool results names the same copy, as in this line from its last `check_letter.py` run:

```text
[voice] plainspeak-writer 1.7, letter surface, 0 HARD hit(s), 0 warning(s). From C:\Users\<user>\repos\tools\job-seeker-ops\skills\plainspeak-writer.
```

The two sample checks say `plainspeak-writer 1.7`, and the review packet's script printed `Voice rules from:` with the same folder. Its manifest reads `Voice rules: plainspeak-writer 1.7, in voice-rules.md`.

## What 1.7 changed in the draft

1.7's new warning for a letter whose sentences run long and flat, V09, fired on three drafts in turn: an average of 24.4 words with 7% of sentences at ten words or fewer, then 21.2 with 6%, then 20.0 with 6%. The helper split sentences until it cleared. The letter it handed over has 18 sentences, an average of 19.8 words, and 11% at ten words or fewer. The 0.3.0 letters averaged 26 words with 1% that short. The letter has none of the three constructs from the owner's review: "what the unit tests showed", "that's the coaching" and "do what ours did".

## cl-f1's key, on this run

| Test | Result | Evidence |
|---|---|---|
| 1. Three files only | Pass | No call names `master-resume.md`, and none of its 13 lines shows up in a tool result. |
| 4. Shape | Pass | A body of 357 words in five paragraphs. LibreOffice lays the Word file out on one page, `measure_page.py` measures 0.721 of a page, and the script's estimate is 0.742. |
| 5. Voice | Pass | 0 HARD hits and 0 warnings from plainspeak-writer 1.7. |
| 7. Reuse | Pass | Neither "eight years", "for the last two" nor "for five years now" is in the letter, and the record finds 0 sentences shared with the samples. |
| 8. Off the page | Pass | None of section 7's phrases is in the letter, and 61% appears where the resume has it, never 63%. |
| 9. Review limit | Pass | One blind review through the packet script, with a verdict of Send. The helper fixed two of its should-fix findings and ran the checks again. |
| 10. Channels | Pass | `Nadia_Haddad_CoverLetter_SilverLarchSchoolDistrict.docx`, with Nadia Haddad as the author, and no PDF in the folder. |
| 11. The watermark notice | Pass | The hand-over gives the line once. |
| 12. Deeper proof | Pass | P2, the sessions for 18 teachers, and P4, the 2020 committee, are told from their stories, and neither is on the resume. |
| 13. Voice samples | Pass | Before drafting, `check_letter.py --sample` set aside the note's sentence with the dash and its "not just a number, but" sentence. Neither is in the letter. |
| The record | Pass | `check_positioning.py` passes the file with the letter's record in section 9. |

## Worth a look

- The letter's ask, "Could we set up a time to talk about the common unit assessments your four middle schools will need for this year's adoption?", still opens the way the example letter's ask does, "Could we set up a call about". It names its topic, and the stock-opener warning doesn't fire, but the shape comes from the example.
- The helper wrote its fact list and a draft of the record to the session's scratch folder rather than the run folder. Neither reached the person's folder or the letter.
- After the run, six phrases of the "what the X did" kind that plainspeak-writer 1.7 now warns on were reworded in the three SKILL.md files, such as "what the writer meant" to "the writer's intent". Each instruction says what it said before, so the run stands for the released text.

## Result

Pass.
