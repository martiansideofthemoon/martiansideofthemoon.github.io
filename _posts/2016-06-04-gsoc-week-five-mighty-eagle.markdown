---
layout: post
title:  "GSoC Week Five - Mighty Mighty Eagle!"
date:   2016-06-04 11:39:55 +0530
tags: gsoc
---
A month has elapsed since I started my GSoC project. It's been a great learning experience and I've learnt several aspects about Mozilla's Testing infrastructure.
This week I saw the new [Angry Birds Movie](https://en.wikipedia.org/wiki/The_Angry_Birds_Movie), and I can't seem to get Peter Dinklage's [Mighty Eagle](https://www.youtube.com/watch?v=hxBsM1QOZbE) song out of my head. So I had very little choice while I chose my theme.

![eagle]({{ site.url }}/assets/eagle.jpg)

Getting back to work, this is how it's been last week :-

## MozCI Tools / Pulse Actions

Now that I'm done with the first two parts of my GSoC project, I need to prepare MozCI Tools to receive the modified Pulse messages and parse them appropriately.
This is seeming difficult since I don't have the required TaskCluster scopes to publish to Treeherder. Armen might need to make a [Rapid Risk Assessment](https://wiki.mozilla.org/Security/Risk_management/Rapid_Risk_Assessment) before I can make any progress.

In the meantime, I've done some preparatory work in [this](https://github.com/mozilla/mozilla_ci_tools/pull/480) Pull Request to download the latest full-tasks-graph.json file from the TC Index. I've also started work on parsing the new Pulse Messages in [this](https://github.com/mozilla/pulse_actions/pull/82) Pull Request.

Armen has assigned two bugs to me, related to MozCI. In the [first one](https://bugzilla.mozilla.org/show_bug.cgi?id=1274483) I need to handle nightly builders in MozCI. I also need to check some special properties of the Android nightly builds. In the [second one](https://bugzilla.mozilla.org/show_bug.cgi?id=1276914) I need to remove the MozCIError which is raised when a non existing builder is passed.

## Photometric Redshifts

I've started a [project](https://github.com/martiansideofthemoon/Photometric-Redshifts) where I will estimate redshifts of galaxies in the [SDSS database](www.sdss.org) using machine learning. I've implemented the [kNN regression](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm#k-NN_regression) algorithm and got a fairly decent result. I hope to move to a Neural Network soon.

![knn]({{ site.url }}/assets/knn_regression.png)

## Other News

We are starting the third [Quarter of Contribution](https://wiki.mozilla.org/Auto-tools/New_Contributor/Quarter_of_Contribution/Summer_2016) on Monday, 4th June. [nihal111](https://github.com/nihal111) and [arpan98](https://github.com/arpan98) will be helping [jgraham](https://github.com/jgraham) and me hack [wptview](https://github.com/mozilla/wptview). Congratulations!

## Coming Up!

This week I hope to address the issues pointed out on my Treeherder [pull request](https://github.com/mozilla/treeherder/pull/1490). I also hope to solve the two bugs assigned to me Armen. If the security issue is resolved, I will proceed with scheduling TC jobs. I may not be able to blog next week, since I'm off to [#mozlondon](https://twitter.com/hashtag/mozlondon)!
