# Key: Writer C (tests 10 and 11)

Packet: `c-abernathy/letter.txt` with no target, no companion and no channel.

**Test 10, no target.** The manifest says no target was given. The report says it used a general reader for a cover letter, skips the requirement check, and writes "None." or a note about the missing target under Requirements. The skill asked for the posting once and no more. The expected verdict is Send, since the checker finds only list-of-three warnings: two in plainspeak-writer 1.3, one for the whole piece in 1.4. Listing them as should-fix or clearing them with a reason both count.

**Test 11, no voice rules.** Built with `--no-voice`, the manifest says the voice rules weren't found. The report writes `Voice: unchecked`, makes no voice findings, and the verdict comes from the other checks, which gives Send.
