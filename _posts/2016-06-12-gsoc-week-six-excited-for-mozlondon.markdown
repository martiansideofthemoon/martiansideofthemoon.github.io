---
layout: post
title:  "GSoC Week Six - MozLondon, Here I come!"
date:   2016-06-11 23:39:55 +0530
tags: gsoc
---
It's been the busiest week and I can proudly say I've completed a significant part of the GSoC project. I can't wait to meet my fellow Mozillians, since I'm off to London, for the Mozilla [All-Hands](https://wiki.mozilla.org/All_Hands)!

![mozlondon]({{ site.url }}/assets/mozlondon.jpg)

Let me describe last week's work :-

## MozCI Tools / Pulse Actions

Armen and Dustin had a Rapid Risk Assessment meeting and agreed to give me TaskCluster credentials for scheduling TaskCluster jobs in the try repository of Treeherder. Once the TaskCluster-Treeherder integration improves, I will be given scopes for the rest of the repositories.

I started immediately, and after a long day of hacking and pinging Dustin, I was finally able to resolve all dependencies (using Depth First Search on the task graph) and schedule some jobs. You can see my results [here](https://treeherder.mozilla.org/#/jobs?repo=try&revision=22e97582654791575c1b2027802ce3e02cc9366d). I've written it neatly in this [pull request](https://github.com/mozilla/mozilla_ci_tools/pull/486) and added some changes to [this](https://github.com/mozilla/pulse_actions/pull/82) to translate pulse messages and schedule tasks.

Having said this, we might decide to **skip** this approach since I'm having to re-write most of [optimize.py](https://dxr.mozilla.org/mozilla-central/source/taskcluster/taskgraph/optimize.py), an in-tree file written by Dustin which does pretty much the same thing and more in a much better fashion. We are going to introduce Action Tasks and schedule them in Pulse Actions, which pass on labels to optimize.py to do all the hard work.

I also fixed the two bugs I'd been given last week, [Bug 1274483](https://bugzilla.mozilla.org/show_bug.cgi?id=1274483) and [Bug 1276914](https://bugzilla.mozilla.org/show_bug.cgi?id=1276914).

## Treeherder

I had a few bits and pieces left in my main [Pull Request](https://github.com/mozilla/treeherder/pull/1490), primarily adding timestamps to pulse messages, adding a few comments, and restricting usage to the try repository. I've completed that and it's ready for final review. The bug is [1254325](https://bugzilla.mozilla.org/show_bug.cgi?id=1254325).

## Photometric Redshifts

We've made a lot of progress here, and the highlight of our work is the first working neural network! Here is the plot we've managed to produce (estimated redshift vs actual redshift) :-

![nn]({{ site.url }}/assets/first_nn.png)

There are a few points having a low estimated redshift which are distinctly off the clump of points. These are points having nearly the same value in all five photometric filters. We've isolated them in this [script](https://github.com/martiansideofthemoon/Photometric-Redshifts/blob/0d11f22d8cc58b8aeb89af2afd6ba5358cb76a91/test_codes/basic_nn_kalpesh.py) and are getting better plots on doing so. I'll describe the project in detail later on.

## Coming Up

New friends, New city, and a lot of fun! I hope to have a lot to write about next week! Till then, see you in London :)
