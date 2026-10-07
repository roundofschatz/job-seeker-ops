# Cover letter test 9: review limit

Spec: "submission-review runs on every draft, twice at most. After two verdicts short of Send, the person gets the draft with the open findings."

Every letter run loaded submission-review, built packets with its `build_packet.py`, and started `job-seeker-ops:submission-reviewer` with the printed line. Each transcript shows exactly two reviewers.

| Run | First verdict | Second verdict | What reached the person |
|---|---|---|---|
| cl-f1 | Send, with should-fix findings | Send | The letter, revised on six of the first review's findings, with the second report as it came back |
| cl-e1 | Fix first | Fix first | The letter with the open findings, after revising once |
| cl-g1 | Send | Send | The letter, revised on three findings, with the second report |
| cl-b1 | Send | Send | The letter, revised on six findings, with the second report |

Every reviewer wrote `blind: yes`, opened only its packet and the voice rules, and saw only the letter, the posting and the resume.

**cl-e1, two verdicts short of Send.** The posting requires an OSHA 30-hour card she doesn't have, and both reviews made it the one must-fix finding. After the second the skill stopped: "Two reviews both said 'Fix first,' and the one must-fix finding is the OSHA 30-hour card. That's something you don't have, so the letter won't mention it." Its record in section 9 reads `Status: open findings`. The hand-over lists each open finding with the reason it stays open, and asks for the facts only she has, such as start-up meetings or her part in the Fernley opening.

## Result

Pass.
