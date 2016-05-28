---
layout: post
title:  "GSoC Week Four - He Held the Door! :'("
date:   2016-05-28 11:39:55 +0530
tags: gsoc
---
It's been a busy week. I've been busy with college work and I did a bit of GSoC work too this week.

So this week's theme HAS to be [Game of Thrones](http://www.imdb.com/title/tt0944947/), because they've just produced the most heartbreaking twist in the story, and keeping some other theme would just dirrespect brilliant television show (since I follow it actively).

I dedicate this week to [Hodor](http://gameofthrones.wikia.com/wiki/Hodor), who had one task (to Hold the Door - "Ho-Dor"), and he held on, sacrificing himself, bringing tears to millions of fans.

![hodor]({{ site.url }}/assets/hodor.png)

Getting back to work, here are the technical details for the week :-

## Treeherder

This week started with Dustin making some changes to Taskcluster. We now have a [full-tasks.json](https://public-artifacts.taskcluster.net/SQas-oGSQaWoyFIPLeLBdg/0/public/full-task-graph.json) file due to the big-graph changes. This made my work slightly easier, and I've completed this Pull Request. On clicking "Add New Jobs", Treeherder sends "Task Labels" as buildernames for TaskCluster jobs, through Pulse. The PR will be merged once I prepare MozCI for this change. [Pull Request](https://github.com/mozilla/treeherder/pull/1490)).

## MozCI Tools

Armen had landed a a major change in MozCI Tools to account for PGO builds. There were a few errors in the code along with a couple of failing tests which I fixed in this [Pull Request](https://github.com/mozilla/mozilla_ci_tools/pull/477).

## Web Platform Tests Viewer

I landed a change this week which accounts for path filters where the path column does not have entries starting with a forward slash (/). The official dates for Quarter of Contribution have been added [here](https://wiki.mozilla.org/Auto-tools/New_Contributor/Quarter_of_Contribution/Summer_2016). Hoping to get some awesome contributors!

## Other News

I've started watching some videos to learn Digital Image Processing from this [channel](https://www.youtube.com/playlist?list=PLuh62Q4Sv7BUf60vkjePfcOQc8sHxmnDX). I hope I can use this knowledge to do an exciting project later this summer!

## Coming Up

This week I intend to start preparing MozCI Tools to perform various tasks with the Task Labels that Treeherder will produce. These would include, getting the latest full-tasks.json file, understanding dependencies, scheduling all these jobs in TaskCluster. This work might be a little diffficult, and I hope to spend more time this week working on the project. I also need to fine tune my Treeherder Pull Request so that it is good enough to be deployed.
