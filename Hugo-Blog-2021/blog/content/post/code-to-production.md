{
 "title": "Software Engineers Rush to Write Bad Code",
 "date": "2022-04-18T13:52:11+02:00",
 "draft": false,
 "topics": ["writing"],
 "description": "Engineers are pushed to write code quickly and the quality suffers because of it. How can you move quickly while maintaining a high level of quality?",
 "preview_image": "/image/code-to-production/preview_image.jpg"
}

([Originally posted on the DEPT® Engineering Blog](https://engineering.deptagency.com/software-engineers-rush-to-write-bad-code))

Software engineers are often forced to deliver value quickly for the customer. They move fast. What they create is a mixture of researching, brainstorming, learning, prototyping, and final drafting.

It is an absolute mess.

Software engineers must separate the mixture of activities. Do one activity. Do it well. Focus on getting your final draft into production and nothing else.

### How does an engineering mess happen?

You are tasked with implementing some new library, `lib-foo`, into your codebase.

You install the package and immediately get faced with bugs. You play the game of whack-a-mole, solving one bug after the next. Are you learning anything about this new library?

After days of banging your head against the wall, you get something that compiles and does what you want. Was that the best way to do it?

You create a pull request and take a look over your code. What a mess. Will you be able to understand it six months in the future?

Two years later, you're at a new job and are again tasked with implementing `lib-foo`. Do you remember anything about the library? Probably not.

If this sounds familiar, it's time to make a change.

### There is a Better Way

Engineers face a lot of frustrating situations.

Of all of these situations, though, nothing is more effective at killing enthusiasm and motivation than troubleshooting several bugs at the same time. When you're learning something new, you should focus on that one thing and nothing else. Everything else should get out of the way.

I do a lot of work with React. When I wanted to learn something new with React, I'd copy an old project, gut it, and use that to start.

At some point, I learned of [Cookiecutter](https://github.com/cookiecutter/cookiecutter). It is a Python tool for generating a project's boilerplate from a template. No Python experience required. Tired of copying, pasting, and gutting, I wrote myself a [React Cookiecutter](https://github.com/TravisBumgarner/cookiecutter-react) to speed things up. I know the code well. Now, with a simple Python command, I've got a sandbox to start learning about a new React library.

Folks familiar with [Create React App](https://create-react-app.dev/) might be wondering: why not just use that? Well, I have been maintaining my React Cookiecutter for several years now and it is very familiar for me. If Create React App is a tool you know well, use it.

**Pick the tools that work best for you so you can focus only on your learning**.

Now that I have an environment to play around in, it is time to start learning.

My process is usually the following:

1. Use one of my Cookiecutters to spin up a sandbox to play in.
2. Follow along with a tutorial and the documentation to learn the basics of the library.
3. Explore the library's ideas and concepts.
4. When I'm content with my learnings I'll add it to my [Learning Repo](https://github.com/TravisBumgarner/learning/tree/master/archives). When possible, I will add notes in Markdown or comments to supplement the artifact.

For more complicated tasks, I'll create a folder in my [Proof of Concepts Repo](https://github.com/TravisBumgarner/proof-of-concepts). An example of such a task would be connecting two libraries I don't know with each other. I'll start by exploring each separately in the Learning Repo. Then I'll use those two explorations as references to integrate the two together.

Some might say that I'm writing throwaway code and it is a waste of time. Bad code is a liability. I'm throwing away code but it is only so that I can focus on writing a final draft of code for production. Furthermore, it is reference code. I have a place to look if I need to use that technology in a different codebase in the future. Finally, the majority of the code I write in a sandbox gets copied into the codebase.

As I start working in the actual codebase, I might get stuck on something. In this situation, I can jump back into any of my reference code and troubleshoot in isolation. I can figure out if the issue is from the new libraries or from pre-existing code.

Now imagine, you're two years down the road and you need to implement `lib-foo` again. You could try and take a look at where you originally implemented it, but maybe you don't have access to that codebase anymore. **The great thing about creating a repository of references is that you can carry it with you throughout your career**.

Over time, the collection of references grows. You can share them with others who are learning what you've learned. You can implement those technologies more easily the second time around. You're moving at a better pace!

### Fast Forward Two Years

You sit down to begin a new project integrating `lib-foo`, `lib-bar`, and `lib-buzz` into an existing code base. Will you rush to get a pull request open that is, at best, a rough draft?

Or will you have learning repos for `lib-foo` and `lib-bar`? A proof of concept on how the two connect together? Where you can build a solution more easily, elegantly, and quickly?

The choice is yours.