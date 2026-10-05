# Positioning test 7: one confirmation

Spec: "The skill stops once, at step 9, and an ambiguous case reaches the person as a question with a recommendation."

As agreed on October 5, the skill may also ask once at step 2, in one message, when something's missing. Every run's conversation is in `positioning-runs/<run>/conversation.md`, word for word.

## Stops in each run

| Run | Writer | Step 2 message | Step 9 confirmation | Other stops |
|---|---|---|---|---|
| e1 | E, resume only | One: what matters, a longer record and the channel | One | None |
| f1 | F, who sent everything | None | One | None |
| g1 | G, with no web access | One: what matters, two firm facts and the channel | One | None |
| h1 | H, resume only | One: what matters, a longer record, the channel and a referral | One | None |
| e2 | E, round two | One: what matters, a longer record, the channel and a referral | One | None |
| h2 | H, round two | One: what matters, a longer record, the channel and a referral | One | None |

## The ambiguous case

Writer G's posting names two programs and says the role will fit the person. His step 9 message asked which program the resume and letter should lead with, and gave each case in one line. Then it recommended one: "I recommend the lining group. Your record there matches the job nearly point for point, and you've already lined more than their first target, 14 miles against their ten." It closed the question with what happens on no answer: "If you don't answer, I'll keep the lining group." He took the recommendation, and the file records his answer as A5.

## Without the skill

With no skill, the same prompts for writers E and F asked several questions at once and then saved a case without showing it for confirmation. For writer G, it came back with new questions three times before it settled.

## Result

Pass.
