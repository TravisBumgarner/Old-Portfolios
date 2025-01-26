{
    "title": "Finish What You Start",
    "date": "2018-11-23T17:39:21-07:00",
    "draft": false,
    "topics": ["writing"],
    "description": "I love starting hobby projects. However, I seem to hate finishing them. Let's figure out how to finish things.",
        "preview_image": "/image/finish-what-you-start/preview_image.jpg"
}

### Introduction

I love starting hobby projects. However, I seem to hate finishing them. The GitHub description for one of my personal projects from over a year ago reads “Work in Progress: I swear I’ll finally finish this project.”

It’s thrilling to set out to build something new. The initial momentum is exhilarating. Functionality starts sprouting up everywhere, progress is made, the end is in sight. Until it isn’t. Somewhere along the way, something happens, the momentum is lost, and the project is either abandoned - or the finish point becomes a perpetually dangling carrot.

At the start of 2018, in pursuit of becoming a better programmer, I set out to find the root cause of my struggle to take a project across the finish line. Over the last 11 months, I have come to the conclusion that there are two culprits. The first is a lack of balance between time spent planning, exploring and coding. The second is the difficulty of staying focused on the task at hand. How can these issues be addressed? I propose a variety of solutions, split out into the three stages of a project: exploring, doing, and finishing. In the exploring phase, a track is created to move the project in the right direction. In the doing phase we keep ourselves on that track, and in the finishing phase, we reach our destination.

### Explore

Before a single line of polished code is written, it’s important to chunk out time to explore the problem, identify solutions, and set out on a path to finishing. Or to give an analogy, you can think of polished code as the final draft and the exploration phase as the research and outline.

Shortly into my career as a software engineer, I was given the reigns to pick my first project at a new job. I was working on a fitness website and noticed that the profile photos for our users were squashed vertically which had the unfortunate result of making them appear larger than they were in reality. In my mind, this was unacceptable and required me to pull out all the stops. Without much thought, I threw myself into the code. Surely the problem would be solved with the perfect image cropper, built from scratch. Or so I thought.

Three days later, images could be cropped, rotated, or scaled – but my code couldn’t do all three of these things at the same time without weird issues. I panicked and decided to start looking for prebuilt solutions for React. Except I still barely knew React. Another day and a half later, I stopped, took a break, and reached out to my boss for help.

#### Know Your Resources

I realized that what I had set out to build was too ambitious. A larger company, with tens or hundreds of engineers, could commit more resources to solving such an issue. However, we were a team of two engineers working on a website barely out of its infancy. During the post-mortem, we had a discussion that could be summed up by the Agile Manifesto Principle of Simplicity which states, “The art of maximizing the amount of work not done–is essential” [1]. The more realistic and much more easily achievable goal was a solution discovered after a short period of research. It saved us a ton of time, satisfied the majority of users’ profile photos, made the code simpler and easier to maintain, and bought us time to return to the issue later and focus on other more pressing issues.

#### Know What You’re Building

When I set out to build the image cropper, I headed in completely the wrong direction without giving consideration to the multiple different ways the problem could have been solved. It is important to know what might be needed in the journey to being done. Spend time researching alternatives, reading articles, discussing the issue, etc. This process will help you to realize all of the aspects that go into a potential solution.

#### Test the Various Solutions

When I first started coding, when creating new features, I’d start trying to write the solution alongside the rest of my fully functioning code. Sometimes, I’d get into a weird state and decide to revert all changes since I would foresee more time fixing the mess I had just written.

I realized my issue was that I didn’t know exactly what I was building. I was trying to write production code to solve a problem I still didn’t quite understand or know what the solution would look like. In this case, I found it best to create a branch or separate scratch file, set a timer, and get to coding alternative solutions to aspects of the problem. Don’t write tests, worry about the quality of code, or spend too much time coding; just write. When the timer is up, ask yourself “Is this enough to make a decision or do I need more time”. When you’re satisfied with your research, start fresh (or better yet, write tests - more to come on that in a bit).

### Do

Have you ever found yourself setting out to solve some problem, getting side tracked on a bit of refactoring or solving a minor bug you noticed and two hours later you’ve edited 20 different files and you can’t even remember what you set out to solve in the first place? I’ve been there too many times. Luckily, following the advice I’ve proposed ahead, in my last personal project, only once did I make a commit in which I added a bunch of code for which I couldn’t write a concise summary of its changes. (For the curious, the first commit read “What have I done?” followed by “…what have I done, seriously”.)

#### Set Tangible Goals and Track Them

I saw a to-do list once that contained such well-defined items as “Find a new apartment.” How does one do that? Perhaps better put would be items such as “Get in contact with a real estate agent” and “Check out one apartment a week”.

The same applies for coding projects such as “add a new page to app X”. I used to jump in and just start typing until the new page was implemented. Except that involved a ton of moving parts and I never really knew if some aspect of the page that I was working on was ever really done. I might spend days working on some script that could have been implemented in minutes with a quick Google search or spend hours tweaking some CSS, never really making actual progress. It feels like a never-ending game of whack-a-mole in which nothing ever really feels done, no milestones passed, just a start and finish with nothing in between.

This method just doesn’t work for larger tasks and over time I’ve transitioned to a more methodical approach. Continuing with the new page example, I break down the various tasks that go into finishing the page and order them so that one task leads into the next. I start by wiring up the page into the rest of the app and getting ‘Hello World!’ printed on the screen. Then I’ll start tackling each individual section of the page. Sometimes I’ll break tasks down further until I can grok the scope of work required for each one. For example, if this page has a contact form, the steps I might take include building out the structure of the form with HTML, adding logic for checking proper inputs with JavaScript, making it pretty with CSS and connecting it to the API. Each step, signifies a milestone, a task completed, and a step closer to being done.

#### Design with Test Driven Development

Before I learned what TDD was, I made assumptions based off of the three words that make up the acronym. I believed that the whole idea was that instead of writing tests after writing the code, that tests would be written before the code. But it is much more than that.

I had an aha moment while reading Growing Object-Oriented Software, Guided by Tests which states that “TDD turns testing into a design activity”[2]. Furthermore, it states that “writing a test first forces us to clarify our intentions, and we don’t start the next piece of work until we have an unambiguous description of what it should do”[2]. By writing a test first, a test that fails since we don’t have code, we have an indicator of something we are working towards, a test that once successful, marks our work as done.

Building on top of this is the idea of double loop testing. Double loop testing consists of a larger picture test, such as “Build a widget that can submit text”, and contained within that test, are several smaller tests that make up the various functionality of that widget. Together, bite sized tasks and their associated tests can pass in the pursuit of making the larger outer loop test pass.

#### Stay Focused

As mentioned in the intro to this section, I have historically been notoriously bad at staying focused on the task at hand. Over time, I have discovered a few methods that help me to stay on track.

##### Queue It

One solution to this is that I’ll put out a scrap piece of paper (an issue tracker works as well) and write down what I’m working on. If I notice some other bit of code in need of repair or improvement, I’ll note it on my queue and go back to what I was working on. Once done with the current issue, I can decide whether to address those issues or track them somewhere else to address in the future.

##### Avoid Feature Creep

Keep the question in the back of your mind “Is this what I should be working on right now?” If it’s not, queue it, or scrap it.

Commit Bite Sized Functionality and do it Often
Keep focus on never straying far from a functioning state of code. Incrementally add functionality and commit it. Combine this with a queue and constantly work towards passing tests.

### Finish

#### Wrapping it Up

At this point, there should be indicators that you’re done. Tests are passing. To-do items are being crossed off of lists. Awesome! You’re finished.

#### But Do These Methods Work?

As I was trying to conclude this post I realized that you might be wondering, “interesting stuff, does it actually work for you?” To answer this question, I decided to take a look at my GitHub history starting at the point that I decided to prioritize getting better at finishing tasks. Of the 13 projects I started, only one turned into a perpetually dangling carrot that I abandoned. Nine projects ended after a successful exploration phase in which I decided not to continue working. Three large projects were completed. My proudest of the three was finally completing the project with the description “I swear I’ll finally finish this project” mentioned in the introductory paragraph.

My most recent project is about a week old at this point. I can clearly see the impacts of the techniques I’ve described in this article. I have overcome unknowns by spending time researching, avoided getting side tracked by queueing issues as they arise, and committed bite sized functionality so that my code is always in a working state. This will be my most ambitious project yet and I have the confidence that I’ll be able to see it through to the end by keeping myself on the correct path of exploring, doing, and finishing.

### Reference
[1] [Agile Manifesto in English](http://agilemanifesto.org/iso/en/principles.html)

[2] [Growing Object-Oriented Software Guided by Tests](http://www.growing-object-oriented-software.com/)
