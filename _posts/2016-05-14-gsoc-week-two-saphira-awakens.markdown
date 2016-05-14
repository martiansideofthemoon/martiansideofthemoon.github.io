---
layout: post
title:  "GSoC Week Two - Saphira Awakens!"
date:   2016-05-14 11:39:55 +0530
tags: gsoc
---
It's been a really hectic week, and unfortunately I could not do too much GSoC work, but I hope I'm on track. At the end of this week, I gifted a friend my favourite fantasy story, [Eragon](http://www.alagaesia.com/books_detail.php?book=eragon), the first book of the Inheritance Cycle. With sweet memories, I'll dedicate this week's theme to Saphira, the main dragon in the Inheritance Cycle.

![saphira]({{ site.url }}/assets/saphira.jpg)

Getting back to work, this is how it's been last week :-

## Pulse Actions

Yes! We have finally merged the [Pull Request](https://github.com/mozilla/pulse_actions/pull/73) which now schedules two Talos jobs for completed PGO builds in mozilla-inbound and fx-team. I got to learn a bit a [Heroku](https://dashboard.heroku.com/apps) and PaperTrail, so it was a great week in this repsect. Here is a screenshot from Treeherder showing what I achieved :-

![talos]({{ site.url }}/assets/talos.png)

As you can see, all Talos jobs (marked with a **T**) have been completed twice. This has been done to reduce the time taken to get Talos alerts to half. We listen to build completions on a Pulse exchange, and trigger Talos downstream jobs accordingly.

## Work on mozilla-central

[Bug 1232005](https://bugzilla.mozilla.org/show_bug.cgi?id=1232005) has been re-opened to allow us to generate all_tasks.json in all branches, not just [try](treeherder.mozilla.org/#/jobs?repo=try). There is some ongoing discussion about the best way to do this.