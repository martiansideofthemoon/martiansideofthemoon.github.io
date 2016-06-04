---
layout: post
title:  "GSoC Week Three - Gotta Catch'em All!"
date:   2016-05-22 11:39:55 +0530
tags: gsoc
---
It's been a fun week and I'm really enjoying myself this GSoC. Quite a productive one, and I discovered an excellent new sport, cycling!

I've always loved the [Pokémon](https://en.wikipedia.org/wiki/Pok%C3%A9mon) video games and my recent completion of [HeartGold](https://en.wikipedia.org/wiki/Pok%C3%A9mon_HeartGold_and_SoulSilver) brought back these fond memories. I dedicate this week's theme to Pokémon, with my two favourite starter Pokémon engaged in a fierce battle!

![pokemon]({{ site.url }}/assets/pokemon.jpg)

Here are the technical details for the week :-

## Treeherder

I've finally gotten around the huge codebase of Treeherder and have successfully managed to produce the URL to [all_tasks.json](https://public-artifacts.taskcluster.net/Zo4UsXv_QH2VdJhSODwwWQ/0/public/all_tasks.json). I'm sending this URL to the Treeherder backend which downloads the file using [requests](http://docs.python-requests.org/en/master/) and parses it to get it in the Treeherder data structure. Treeherder has a wonderful database which gets all the extra information I need.
I send this data back and lo and behold, we have TaskCluster jobs in Treeherder!
(All the code is in this [Pull Request](https://github.com/mozilla/treeherder/pull/1490)).

Original Set of Jobs :-
![original_jobs]({{ site.url }}/assets/original.png)

"Add New Jobs" (TaskCluster only) :-
![taskcluster_jobs]({{ site.url }}/assets/tc_jobs.png)

## MozCI Tools

I set out to refactor [test_platforms.py](https://github.com/mozilla/mozilla_ci_tools/blob/9f14aebcf3255a12114076098ef6ce8b0ed5ea8d/test/test_platforms.py) by removing the irritating mock_allthethings.json file. Here is the [Pull Request](https://github.com/mozilla/mozilla_ci_tools/pull/475).

It was a fun fix, I learnt a lot about the different tools in [platforms.py](https://github.com/mozilla/mozilla_ci_tools/blob/9f14aebcf3255a12114076098ef6ce8b0ed5ea8d/mozci/platforms.py). I now download a version of allthethings.json in the [tox file](https://github.com/mozilla/mozilla_ci_tools/blob/735f5a4ffd38f6dccb40727d7985b9f8bd23e7f0/tox.ini) and use it for all testing purposes. Tests are a bit slower now, but more efficient nevertheless. This fix also increased the test coverage of the MozCI project.

## Pulse Actions

Since my last feature to duplicate talos jobs on PGO builds, we added a [small change](https://github.com/mozilla/pulse_actions/pull/80). This disables this feature on Windows 8 builds. The following picture will give you a better idea.

![talos_no_win8]({{ site.url }}/assets/talos2.png)

Like you can see, for the Windows XP PGO build, our feature is still working, but it's been disabled for Windows 8 PGO build.

## Web Platform Tests Viewer

Unrelated to GSoC, but I'm back to developing my Mozilla Quarter of Contribution Project, [wptview](https://github.com/mozilla/wptview). A few awesome contributors have agreed to refactor wptview as a part of their QoC, this summer. We have made some excellent progress over the last one week, including a [feature to edit run names](https://github.com/mozilla/wptview/commit/b2ddf8f296e376cf0da7e0e7a81d5a857fa64ec0), an important [bug fix](https://github.com/mozilla/wptview/commit/6f069c0612be7e2aec82bb9c997a121ee3a73ca7) in the SQL queries, and some checks on the Import Button, a major one [here](https://github.com/mozilla/wptview/commit/d6fbbfe5e8686583c2449aae92f8ff30f54bb57d).

I'm excited to mentor this Quarter of Contribution. You can find out more about this project [here](https://wiki.mozilla.org/Auto-tools/New_Contributor/Quarter_of_Contribution/WPTViewer_Refactor).

## Other News

I've started cycling longer distances and I'm keeping track of these workouts on [Runkeeper](https://play.google.com/store/apps/details?id=com.fitnesskeeper.runkeeper.pro&hl=en). I hope to make this an habit as I buy a new cycle next week.

## Coming up!

A lot of changes have regressed a few tests in MozCI and I hope to work on fixing some of these failing tests. I also hope to increase the code coverage of the MozCI tests. Lastly, I hope to finish the second part of the Treeherder integration.