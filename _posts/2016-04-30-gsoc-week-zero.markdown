---
layout: post
title:  "GSoC Week Zero!"
date:   2016-04-30 16:10:55 +0530
tags: gsoc
---
It's been an exciting week, (a bit overwhelming to be honest). Right from the GSoC results, to all the congratulations that followed, the remaining end semester exams and finally sorting out the logistics and work plan for GSoC.
This blogpost explains all the work that I've done this week, and my major plans for the week to follow.

## Treeherder Work This Week
I have been contributing to [Treeherder](https://github.com/mozilla/treeherder), the main software on which I have to carry out my work this summer, for the last 4 months. This week I tackled a couple of issues to improve the LogViewer system used by Treeherder. The first one, [Bug 1245760](https://bugzilla.mozilla.org/show_bug.cgi?id=1245760), works on highlighting errors in logs to make it easier for developers to interpret errors. The second bug, [Bug 1245760](https://bugzilla.mozilla.org/show_bug.cgi?id=1245773) improves the regex used for identification of errors in the logs.

## Pulse Actions
I have started using [Pulse Actions](https://github.com/mozilla/pulse_actions), a software which listens to Mozilla Pulse messages from Treeherder, and executes Buildbot APIs (through [Mozilla CI Tools](https://github.com/mozilla/mozilla_ci_tools)) to schedule jobs. Setting up Pulse Actions was slightly painful, due to an outdated README file (I fixed this [here](https://github.com/mozilla/pulse_actions/pull/72)) and a problem in my internet connection. My institute only allows outgoing requests for port 80, 443 (HTTP/HTTPs) and SSH. Pulse works on port 5761 and it won't be easy to run Pulse Actions with this connection. Hence, I've been given a loaner machine (via [Bug 1268068](https://bugzilla.mozilla.org/show_bug.cgi?id=1268068)) which I hope will help me when I begin hacking.
## Plans for the Upcoming Week
