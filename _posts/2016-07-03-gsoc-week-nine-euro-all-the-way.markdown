---
layout: post
title:  "GSoC Week Nine - Euro 2016 All The Way!"
date:   2016-07-03 04:39:55 +0530
tags: gsoc
---
It's been a brilliant week in every possible way. The GSoC project is coming to an end and it's fun to see four projects coming together to make one awesome feature!

This week I have been busy watching football for a change! Euro 2016! My favourite team Belgium is out unfortunately :( Nevertheless, I do hope to watch the last 5 matches.

![euro]({{ site.url }}/assets/euro.jpg)

## Treeherder

The first [Pull Request](https://github.com/mozilla/treeherder/pull/1490) has been finally merged! This allows users to use the API `runnable_jobs`, but does not add TaskCluster jobs to the UI.
This has been done as Action Tasks aren't ready and [Mike Ling](https://github.com/MikeLing) needed the `runnable_jobs` API for TaskCluster jobs too.
I've filed a followup [Bug 1282906](https://bugzilla.mozilla.org/show_bug.cgi?id=1282906) to address some code improvements which I'm doing in [this](https://github.com/mozilla/treeherder/pull/1633) PR.

Once Action Tasks are merged, we will enable "Add New Jobs" on Treeherder's UI!

## MozCI / Pulse Actions

Now the work here is a lot simpler that before. For MozCI, we need to add functions to schedule Action Tasks. This has been done in [this](https://github.com/mozilla/mozilla_ci_tools/pull/489) PR. For Pulse Actions, some code is needed to handle the new Pulse messages and call the correct MozCI functions. I continued this in an old [Pull Request](https://github.com/mozilla/pulse_actions/pull/82). We've merged a [Pull Request](https://github.com/mozilla/pulse_actions/pull/90) which accounts for the new Pulse Message format.

We have decided not to add more tests to MozCI since it ideally needs integration tests, which are not a great idea as the project won't last very long.

Besides this, I did a fix for MozCI. I corrected an issue in the TaskCluster manager of MozCI, to allow me to use credentials available in environment variables. [Here](https://github.com/mozilla/mozilla_ci_tools/pull/490) is the Pull Request.

## TaskCluster Timestamps

This is a refactor suggested by Dustin in a review of the Action Tasks patch. We have tracked the issue on [Bug 1284005](https://bugzilla.mozilla.org/show_bug.cgi?id=1284005).

The motivation behind this refactor has been the problem with timestamps in the `full-task-graph.json` file. Since tasks haven't strictly been created, it makes no sense adding timestamps here.

This has been refactored into "relative datestamps". So instead of actually putting in timestamps, we put in relative timestamps like this,

```json
created: {
	"relative-datestamp": "0 seconds"
}
expires: {
	"relative-datestamp": "7 days"
}
```

Now whenever tasks are created, a timestamp is created to represent `now`. A depth first search of the task JSON follows and all instances of these "relative datestamps" are processed and replaced with the correct timestamp with respect to the timestamp created at in the beginning.
Now tasks can be easily scheduled via Action Tasks, with proper timestamps in place!

## Action Tasks

The Action Tasks work has gone brilliantly! I managed to place in optimizations and we should be merging the patch soon. Like I said in the previous post, we are tracking the issue in [Bug 1281062](https://bugzilla.mozilla.org/show_bug.cgi?id=1281062). Here is a screenshot of the result produced,

![actionresult]({{ site.url }}/assets/actionresult.png)

Here the try syntax used is `try: -b do -p linux64 -u none -t none`. As you can see, three jobs have been scheduled by the action task. We have optimized the `linux64 opt` build and the `taskcluster-images`. Yay! :)

## Other News

I've decided to start reading A Song of Ice and Fire and have bought the first book, A Game of Thrones!

## Coming Up

It seems like the coming week might see the feature actually getting launched. I've wrapped up most of my Pull Requests, now it's all about getting them together. Let's hope it all works in the end.
