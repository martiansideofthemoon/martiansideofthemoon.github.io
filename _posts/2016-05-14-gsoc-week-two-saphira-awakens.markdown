---
layout: post
title:  "GSoC Week Two - Saphira Awakens!"
date:   2016-05-14 11:39:55 +0530
tags: gsoc
---
It's been a really hectic week, and unfortunately I could not do too much GSoC work, but I guess I'm on track. At the end of this week, I gifted a friend my favourite fantasy story, [Eragon](http://www.alagaesia.com/books_detail.php?book=eragon), the first book of the Inheritance Cycle. With sweet memories, I'll dedicate this week's theme to Saphira, the main dragon in the Inheritance Cycle.

![saphira]({{ site.url }}/assets/saphira.jpg)

Getting back to work, this is how it's been last week :-

## Pulse Actions

Yes! We have finally merged the [Pull Request](https://github.com/mozilla/pulse_actions/pull/73) which now schedules two Talos jobs for completed PGO builds in mozilla-inbound and fx-team. I got to learn a bit of [Heroku](https://dashboard.heroku.com/apps) and PaperTrail, so it was a great week in this repsect. Here is a screenshot from Treeherder showing what I achieved :-

![talos]({{ site.url }}/assets/talos.png)

As you can see, all Talos jobs (marked with a **T** and **T-e10s**) have been completed twice. This has been done to reduce the time taken to get Talos alerts to half. We listen to build completions on a Pulse exchange, and trigger Talos downstream jobs accordingly.

## Work on mozilla-central

[Bug 1232005](https://bugzilla.mozilla.org/show_bug.cgi?id=1232005) has been re-opened to allow us to generate all_tasks.json in all branches, not just [try](treeherder.mozilla.org/#/jobs?repo=try). There is some ongoing discussion about the best way to do this.

## Work on Treeherder

Now that we've generated **all_tasks.json** it's time to use it in Treeherder! I've been working this week to begin integrating this with Treeherder and it's been a daunting task due to Treeherder's huge codebase!
You can track my progress in this [Pull Request](https://github.com/mozilla/treeherder/pull/1490).

So far, I've managed to procure the correct URL to **all_tasks.json** in the Treeherder UI on pressing "Add New Jobs". I'm sending this data to Treeherder's [runnable_jobs](https://treeherder.mozilla.org/docs/#!/project/Runnable_Jobs_list) API which will fetch the file subsequently.
I'm having a hard time setting up Treeherder's vagrant environment, but I hope to achieve some success in the beginning of next week. Once this is done, I can start hacking the Django APIs.

## Other News

I had a great interview, and I've been selected for the [Cargill Scholarship](http://cargillglobalscholars.com)!

We have decided to launch a third [Quarter of Contribution](https://wiki.mozilla.org/Auto-tools/New_Contributor/Quarter_of_Contribution) and I've found five excellent contributors from my college for this program. This QoC, we hope to achieve major refactoring of [WPT Results Viewer](https://github.com/mozilla/wptview) and [Perfherder](https://wiki.mozilla.org/EngineeringProductivity/Projects/Perfherder) improvements. Hackers are invited!

## Coming up!

Besides Pull Requests named after dragons in the Inheritance Cycle, I hope to complete my Treeherder Pull Request and get a review by the end of the next week. This patch will download and parse all_tasks.json and return a list of all TaskCluster jobs that can be scheduled in the repository.

I also intend to do extensive work on MozCI, where I will refactor the unit tests and remove the mock allthethings.json file. We have filed an [issue](https://github.com/mozilla/mozilla_ci_tools/issues/474) for this.
