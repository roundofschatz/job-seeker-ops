# Positioning test 9: gap search

Spec: "A requirement the resume misses but a deeper source covers isn't marked a gap."

- Run f1, writer F. Her resume has no line on leading professional development, which the posting requires, and her master resume has one. Files: `positioning-runs/f1/`.

## What the file says

```
| R3 | Experience leading professional development for teachers. | L16 | required | "Led monthly professional development for 18 math teachers across three Basalt Creek middle schools from 2022 to 2024". The resume being sent has no line for it. | master-resume.md L12 | strong | both |
| R7 | Experience with a curriculum adoption. | L22 | preferred | "Served on the district's math curriculum review committee for the 2020 adoption of a new 6th grade textbook, and piloted two of the three finalists in my classes". That's the choosing and piloting stage, for one grade. | master-resume.md L14 | strong | both |
```

The gaps are only the ones no source covers: the master's degree (R6), Spanish (R8) and quarterly reports to the assistant superintendent.

## Result

Pass.
