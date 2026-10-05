# Positioning test 5: reuse

Spec: "A second request for the same posting reads the existing file and doesn't rebuild it."

- Run f-reuse, on October 5, 2026: a new helper got writer F's first message again, in the folder that already held her confirmed file from run f1.
- File: `positioning-silver-larch-school-district-math-curriculum-coordinator-grades-6-to-8.md`.

## What happened

The helper looked for the file by its name, ran `check_positioning.py --current`, and used the file as it was. Its whole reply is in `positioning-runs/f-reuse/conversation.md`. It begins: "Your case is already worked out." Then it says none of her four files had changed and every quote still matched its source, "So I'm using it as it is instead of building it again."

| | Before | After |
|---|---|---|
| SHA-256 | 76dbaf9268fa31e0ca3254be56af571ba2354c5462b59d70364e170659930cf3 | The same |
| Modified | 2026-10-05 15:44:01 | The same |
| Files in the folder | Five | The same five |

The reuse took one message, 145 seconds and 121,048 tokens. The first build took 1,136 seconds.

## Result

Pass.
