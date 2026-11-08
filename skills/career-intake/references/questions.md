# The questions

This file is the one home of career-intake's questions. Claude asks them in this wording when it talks a person through, and `scripts/build_workbook.py` builds the workbook from this file, so the chat and the workbook never ask two different things.

## How these questions sound

They came from a person who helps people find their next job, written the way he asks them over coffee. Keep that voice when you ask a follow-up or add a question:

- Open with "Talk about…" or "Tell me about…", then ask the details one at a time.
- Write "you" and "your". Use everyday words: "your job", "what you did", "what changed".
- Ask for the story first and the detail after it: what happened, what was needed, what you did, what changed.
- "Be honest" and "your best estimate" are fine. They tell people a rough answer counts.
- Never a form label ("Primary responsibilities:"), and never office words a person wouldn't say out loud ("competencies", "stakeholders", "value-add").
- One question at a time. A main question can keep a short follow-up that belongs to it, such as "What happened?"

## How this file is laid out

`## Part N: Title` starts a part. The lines under it, before its first question, are what the person reads when the part starts.

`### id` starts a question. The id never changes once it ships, because records and saved answers files cite it. Retire a question by marking it `Optional: yes` rather than deleting its id, so an older answers file still opens whole. The lines under the id are the question. A line starting `Hint:` is a short note shown under the question in the workbook. `Type: count` makes the question the counting helper, which works out a total from how many at a time, how long each lasts and how many years. `Type: three` gives three boxes, one for each story. `Private: yes` marks an answer that never goes on a page someone else reads; the workbook and the answers file both say so. `Optional: yes` marks a question the person can skip; it often repeats an earlier answer for people who've already said it.

## Part 1: Talk about your current job

Start with what you do now. Short answers and bullet points are fine. You can skip a question, stop after any part, and come back later.

### work-week
Talk about a normal week at work. What did you spend your time on last week?
Hint: The everyday stuff counts. Write it the way you'd tell a friend.

### work-industry
What is your industry?

### work-title
What is your title?
Hint: Add your employer, the city, and the year you started.

### work-past-titles
What roles or titles have you held in the past?
Hint: List them with the employer and the years if you know them.

### work-credentials
What degrees, licenses, or certifications do you have?
Hint: Add the year, and when a license renews if it does.

### work-responsibilities
What are your primary responsibilities?

### work-size
How many people, how much money, or how much work do you handle in a week?
Hint: Team size, budget, cases, calls, orders, students. Your best estimate is fine.

### work-great-at
What are you really great at about your job?

### work-dislike
What don't you like about it?

### work-change
What would you change about it?
Optional: yes

### work-better-used
Is there any way your job could make better use of what you're good at?
Optional: yes

### work-tools
What tools and systems are you using?
Hint: Software, forms, records systems, phones, vehicles, anything you use to get the work done.

### work-skills
What skills do you use in your job, from running the work to the everyday tasks? List all of them.
Hint: The things you do without thinking count: calming someone down, training a new hire, keeping a schedule.

### work-others-say
What do people at work come to you for? What would your boss or your coworkers say you're best at?
Optional: yes

### work-pitch
What is your elevator pitch to someone over coffee who asks what you do, and why you do it?
Hint: Write it the way you'd say it today. Later you'll see it rewritten from your stories.

## Part 2: Tell a story about your projects or clients

This part is the heart of it. Give as much detail as you can remember, and bullet points are fine. If you need to name someone, use a first name only. Names stay in your answers: they're taken out of everything written from them.

### stories-describe
How would you describe your clients, projects, or the people your work is for?
Hint: Clients can be anyone your work is for: students, patients, customers, your crew, the orders you ship.

### stories-now
How many are you currently working on?

### stories-total
What's your best estimate of how many you've ever worked on, or how many people you've helped total?
Type: count
Hint: Fill in the three boxes and the workbook does the math. If each one takes less than a week, like a single call or shift, count how many you handle in a week and use 1 for the weeks. Change the total if you know a better number.

### best-story
Tell me a story about your best client or project experience. What happened?
Hint: Tell it start to finish. The next few questions ask for pieces of it, so there you only need to fill in what you left out.

### best-need
What was the need, or the requirement, and what did you do?

### best-why
What made this the best example?

### best-change
How did your client or project change based on your actions? What were the end results?

### worst-story
Now tell me exactly the same for your worst example. Be honest. What happened, and why is it the worst example?
Private: yes
Hint: Pick one you're okay going back to. This one stays private. It's for you and for interview practice, and it never goes on a resume. The next two questions ask for pieces of it, so fill in only what you left out.

### worst-what
What did you do, and what didn't work? What goal didn't you reach?
Private: yes

### worst-result
What was the end result?
Private: yes

### change-stories
What are your best change stories? Tell me about the times someone or something ended up in a better place because of your work.
Optional: yes

### coffee-stories
What are your three strongest stories about your professional career that you would tell a friend over coffee if they asked what you've done really well?
Type: three
Hint: Your best story can be one of the three.

### built-things
Have you built anything at work that other people still use? A form, a process, a training, a group, a tool. Who uses it, and how often?

### proof
What proof do you have of anything that you've done? Do you have any files, numbers, results, or any other types of information or data that help prove your stories and the impact you've made?
Hint: Numbers you remember count: how many a day, how many at a time, a rating. You don't need the file, and never copy anything private out of work.

### proof-looks-like
If you don't have proof yet, what do you think proof looks like for your job?
Optional: yes

### proof-praise
Do you have any reviews, awards, or notes from people you've helped or worked with? What do they say?

## Part 3: Talk about your desired position or dream job

Now look ahead. There are no wrong answers here, and "I don't know yet" is a fine place to start.

### dream-anything
If you could do anything, what do you think you would be doing? Why?

### dream-day
Tell me about what your day to day might look like, or what you would really love to spend your time doing.
Optional: yes

### dream-now
Are you getting to do any of that right now?

### dream-energy
Which parts of your work now give you energy, and which parts wear you out?
Optional: yes

### dream-titles
What roles or titles do you wish you could hold, now or in the future?
Hint: If you don't know what it's called, describe the job.

### dream-industry
Is there any type of industry you'd like to work in?

### dream-location
What location or locations would you like to work in? Are you where you want to be location-wise right now?

### dream-money
What do you make now? What's the least you can make and still be okay? How much of a pay cut, if any, could you take to make a change?
Private: yes
Hint: This stays private. It's for picking which jobs to chase, never for a resume or a letter.

### dream-limits
What can't change? Think about your schedule, your family, licenses or certifications you want to keep, how far you can drive, and whether you need to work from home.
Private: yes

### dream-roadblocks
What do you think are your biggest roadblocks?
Private: yes

### dream-skills
Are there any skills you're working to develop or would like to develop to help get you where you want to go?

### dream-people
Who do you know who works somewhere you'd like to work, or does a job you'd like to do? Who has offered to help you before?

## Part 4: Tell me about you

Last, the big picture. You've told your stories now, so use them.

### you-describe
Tell me about you. How would you describe yourself?
Optional: yes

### you-career
How would you describe what you do and your professional career?
Optional: yes

### you-superpowers
What are your superpowers?

### you-gaps
What are your gaps, shortcomings, or things you're not good at?
Private: yes
Hint: This stays private. It helps pick the right jobs, and it never goes on a page anyone else reads.

### you-wont
What are the things you won't do, or don't want to do, or don't like to do?
Private: yes
Optional: yes

### you-skills
What do you think your skills are, personally and professionally? List all of them.
Hint: Look back at your stories. Every one of them shows something you know how to do. Add the ones you didn't list before.

### you-love
What do you really love to do as a person, and what makes you happy?
