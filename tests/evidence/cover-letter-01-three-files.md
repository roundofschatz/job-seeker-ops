# Cover letter test 1: three files only

Spec: "With a career record sitting in the same folder, the skill never opens it. The tool log shows the three files, plainspeak-writer and any voice samples the person picked, nothing else."

Runs on October 7, 2026, each in a fresh helper following `skills/cover-letter/` from this repository's working tree. The tool log is each helper's transcript, read with `tests/tools/scan_transcript.py --forbid`, which fails when a call that reads, searches or writes files names the deeper record. The scans are in `cover-letter-runs/<run>/scan.txt`.

| Run | Deeper record in the folder | Calls that name it | What the helper opened |
|---|---|---|---|
| cl-f1 | `master-resume.md` | None | The skill's files, the positioning file, `posting.txt`, `resume.txt`, the two samples she picked, plainspeak-writer and submission-review |
| cl-g1 | `linkedin.md` | None | The skill's files, the positioning file, `posting.txt`, `resume.txt`, plainspeak-writer and submission-review |
| cl-b1 | `career-record.md`, `positioning-notes.md` | None | The skill's files, the positioning file, `posting.txt`, `resume.txt`, plainspeak-writer and submission-review |

**Rechecked for 0.3.2.** The security review found that the scan only caught a call that names the file, so a search over the whole folder could read it unnoticed. The scan now also takes `--run-folder` and looks through every tool result for the deeper record's own lines, the ones no other file in the folder or the plugin holds. Run again on the three runs above, it found none of them in any result: 13 lines for cl-f1, 7 for cl-g1 and 14 for cl-b1.

The deeper record still reached the letters through the positioning file. cl-f1's letter tells three proofs only her master resume holds, and cl-g1's tells his LinkedIn text's "specifications the utility still uses" through his P1 story (test 12).

One script call touches the record's bytes: `check_positioning.py --current` hashes every stamped source to prove the case is still current. It prints no text from the record, and the owner agreed to it in the plan.

The fresh reader in cl-g1 noted that the positioning file quotes a fourth file, `linkedin.md`, treated the file as given, and opened nothing outside its message.

**Without the skill.** The same request for writer F with no skill read the master resume twice, in a loop that printed every file in the folder and in a hash of them, and its hand-over says three facts are "from your master resume".

## Result

Pass.
