---
layout: post
title:  "GSoC Week Ten - Songs of ICE & FIRE!"
date:   2016-07-10 00:39:55 +0530
tags: gsoc
---
A disappointing week, but that's probably because I'd raised my expectations too much. There have been several weird merge conflicts on the [mozilla-central](https://github.com/mozilla/gecko-dev) which have delayed Dustin and my development process.
Thankfully, we saw a merge on Friday. Dustin has filed these anomalies in this in [Bug 1285259](https://bugzilla.mozilla.org/show_bug.cgi?id=1285259).

The most pleasant thing this week was a wonderful story book I've been reading, the first song of Ice and Fire, Game of Thrones!

![asoiaf]({{ site.url }}/assets/asoiaf.png)

## Treeherder

Lots of activity here! We merged the follow up [Pull Request](https://github.com/mozilla/treeherder/pull/1633) improving the code used to schedule TaskCluster jobs. I did some other unrelated work for Treeherder in my spare time.

* [PR #1645](https://github.com/mozilla/treeherder/pull/1645) - A feature to improve the "Cancel All Jobs" UI. This improved the tooltips and added an important use-case. The button doesn't strictly "Cancel All Jobs" now!
* [PR #1646](https://github.com/mozilla/treeherder/pull/1646) - My first Perfherder fix! This fix adds an option for any viewer to copy alert summary to his clipboard. Boy, adding stuff to the clipboard is harder than I thought!
* [PR #1661](https://github.com/mozilla/treeherder/pull/1661) (Open) - This is a feature to improve to eliminate a very irritating issue in the Sherrif panel of Treeherder. I doubt this is going to be an easy fix though!

## MozCI / Pulse Actions

The [PR](https://github.com/mozilla/mozilla_ci_tools/pull/489) to schedule Action Tasks has been merged! I did a short [refactoring](https://github.com/mozilla/mozilla_ci_tools/pull/491) to help the pulse_actions PR. We should be merging that on Monday. All in all, the work in these two repositories seems to be getting over.

## TaskCluster

[Bug 1284005](https://bugzilla.mozilla.org/show_bug.cgi?id=1284005) has been a major source of irritation this week. It was stuck in a merge conflict and took nearly the entire week to get merged.

Another feature I have been desperately waiting for is module finder which Dustin's working on in this [revision](https://reviewboard.mozilla.org/r/61882/diff/2#index_header). Again, this was backed out due to a weird merge conflict and it hasn't landed yet! Action Tasks need this to function.

The Action Task work in [Bug 1281062](https://bugzilla.mozilla.org/show_bug.cgi?id=1281062) has been split up into two patches, with the second patch adding all the `from_json` code for `TaskGraph`. I've filed that in [Bug 1285755](https://bugzilla.mozilla.org/show_bug.cgi?id=1285755). This code is more or less ready, and should be good to go this week.

I had a hard time with Mercurial while splitting up the patches. I really need to start using Mercurial bookmarks.

## Bugzilla

I've been exploring the Bugzilla code in Perl with Dylan and I've gotten my first bug to solve! This patch hopes to speed up things a certain "Enter Bug" page (for Firefox Core bugs). It's tracked in [1021795](https://bugzilla.mozilla.org/show_bug.cgi?id=1021795).

## Other News

Well nothing here this week. I just hope France win the Euro 2016 final!

## Coming Up

Code Reviews, those **r+** I've been desperately waiting for, some testing and QA (hopefully) and yes, a fifth semester of Electrical Engineering!
