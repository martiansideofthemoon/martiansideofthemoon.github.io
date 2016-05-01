---
layout: post
title:  "Selected for GSoC-2016!"
date:   2016-04-30 14:10:55 +0530
tags: gsoc
---

This is my first blogpost and I'm extremely happy to announce that "The Last Martian" (yes that's me) has been selected for [GSoC](https://summerofcode.withgoogle.com/) this year!

## But, What is GSoC?

GSoC, standing for Google Summer of Code, is a program happening once a year between the months of May and August. It's meant to promote open source development. Google funds a number of open source projects under some open source organizations, for everyone's benefit. There is a lot of money involved, and not to forget the awesome goodies!

## So, Where am I going to work?

I will be working from home for the organization I've been selected for, which is [Mozilla](https://www.mozilla.org/en-US/), the brilliant workforce behind the popular browser [Firefox](https://www.mozilla.org/en-US/firefox/new/).
More specifically, I will be working with the [Engineering Productivity](https://wiki.mozilla.org/EngineeringProductivity) team. Our major goal is to improve the testing infrastructure for Firefox and other Mozilla products through several tools and services aimed at improving the overall productivity of engineers in Mozilla.
![firefox]({{ site.url }}/assets/firefox.jpg)

## What's my Project?

Like every open source project, Mozilla's products have a solid infrastructure for testing. There are tens of thousands of tests which have to be run for each and every change that is made to the Mozilla codebase. You can get an idea by looking at [Treeherder](https://treeherder.mozilla.org/#/jobs?repo=mozilla-central), the user interface for all these tests. To run these tests efficiently on the server farm, Mozilla uses a test scheduler, which schedules builds and the corresponding tests in a logical fashion. This entire process is termed as **Continuous Integration**.
Mozilla has been using [Buildbot](http://buildbot.net) for all the job scheduling in the past. Now, a new software, [TaskCluster](http://docs.taskcluster.net/) has been developed to take over Mozilla's CI and is slowly being integrated into Mozilla's testing infrastructure.

My project involves improving the TaskCluster-Treeherder integration by adding an option to manually schedule TaskCluster jobs. This would primarily involve understanding the TaskCluster APIs and authentication system it follows, along with Mozilla's [Pulse](https://wiki.mozilla.org/Auto-tools/Projects/Pulse) system which is used for communication between the different Engineering Productivity tools. This project will involve work in Python and Javascript.

I will be mentored by [Armen Zambrano](https://mozillians.org/en-US/u/armenzg/) and [Joel Maher](https://mozillians.org/en-US/u/jmaher/) for this project. Hoping to do a good job!

You can read more about my project in my proposal [here](http://home.iitb.ac.in/~kalpesh1729/gsoc.pdf).

## What am I expecting from GSoC?

This is going to be exciting 3 months for me. Through this GSoC, I hope to understand Mozilla's CI system through and through. I hope to make some great new friends and guides. I handle a repository in Mozilla (a test results filtering system, [Web Platform Tests Results Viewer](https://github.com/mozilla/wptview)) and I hope to get some newcomers involved in this project, and take it forward.

In short, I hope to use this platform to establish myself as an awesome **a-teamer** (a-team is the nickname for Mozilla's Engineering Productivity).