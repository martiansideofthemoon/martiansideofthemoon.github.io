---
layout: post
title:  "Code of GSoC 2016 - Add TaskCluster Jobs in Treeherder"
date:   2016-07-19 00:39:55 +0530
tags: gsoc
---
This blogpost has a list of all patches and pull requests that were merged for the success of the GSoC project. There is also a developer's guide on using this new feature.

This feature is **COMPLETE** and **WORKING**. There are a few follow up bugs which I will mention in this blogpost and were not strictly a part of the project.

## TaskCluster

TaskCluster is a graph based test scheduler which is at the heart of Mozilla's Continuous Integration. My major work in this GSoC project was in the `taskcluster` part of [mozilla-central](https://dxr.mozilla.org/mozilla-central/source/).

My job was to implement Action Tasks which will do the job of scheduling new jobs. I also needed to improve the TaskGraph optimization that was being used.

All my TaskCluster work was recorded in [Bug 1281062](https://bugzilla.mozilla.org/show_bug.cgi?id=1281062). This was broken down into three different patches finally -

* [Bug 1284005](https://bugzilla.mozilla.org/show_bug.cgi?id=1284005) ([Patch](https://hg.mozilla.org/mozilla-central/rev/7e73e9581bca)) - This is the first bug. This refactors the timestamp mechanism used in `TaskGraph` generation. Now instead of actual timestamps, `relative-datestamps` are used which are replaced with actual timestamps when the tasks are actually created.
* [Bug 1285755](https://bugzilla.mozilla.org/show_bug.cgi?id=1285755) ([Patch](https://hg.mozilla.org/mozilla-central/rev/b1a86b2b81ff)) - This is the second bug. This adds a feature to build a `TaskGraph` object from a corresponding JSON file, taking care of the special cases for various `Task` subclasses.
* [Bug 1281062](https://bugzilla.mozilla.org/show_bug.cgi?id=1281062) ([Patch](https://hg.mozilla.org/mozilla-central/rev/d223b3cdee66)) - The final piece of the puzzle which adds action tasks. This feature also utilized [Dustin](https://github.com/djmitche)'s [patch](https://hg.mozilla.org/mozilla-central/rev/2393f903d0a7) to find python modules.



## Treeherder

Treeherder is Mozilla's primary testing dashboard. My work here was to add UI features to show all possible TaskCluster jobs, and allow the users to select jobs they want to schedule.

This was primarily tracked on Bugzilla in [Bug 1254325](https://bugzilla.mozilla.org/show_bug.cgi?id=1254325), [Bug 1284911](https://bugzilla.mozilla.org/show_bug.cgi?id=1284911) and [Bug 1282906](https://bugzilla.mozilla.org/show_bug.cgi?id=1282906).

Here is the list of pull requests that were merged -

* [PR #1490](https://github.com/mozilla/treeherder/pull/1490) - This is the primary pull request which adds major components of the feature. This activates the APIs but does not activate the UI.
* [PR #1625](https://github.com/mozilla/treeherder/pull/1625) - This fixed a small UI regression arising from the previous PR.
* [PR #1633](https://github.com/mozilla/treeherder/pull/1633) - A follow up PR to the previous two, primarily improving the Django code.
* [PR #1688](https://github.com/mozilla/treeherder/pull/1688) - The final PR which activates the UI and fixes a UI regression which arises due to the presence of Action Tasks.

## MozCI

MozCI is a python package that's utilizes the different parts of Mozilla's Continuous Integration and connects them together via APIs. Originally, my work here was to add functions to schedule all TaskCluster jobs requested, resolving dependencies and fixing task references.

However, since we decided to use Action Tasks, the work here reduced substantially.

Here is the list of pull requests we used -

* [PR #480](https://github.com/mozilla/mozilla_ci_tools/pull/480) - Fetching the full tasks file. We backed out these changes in a latter PR.
* [PR #486](https://github.com/mozilla/mozilla_ci_tools/pull/486) (CLOSED) - This Pull Request contains the method originally proposed in the GSoC proposal. We didn't merge this due to less reliability and sustainability.
* [PR #489](https://github.com/mozilla/mozilla_ci_tools/pull/489) - This patch allows us to schedule action tasks, which perform all the magic in-tree.
* [PR #490](https://github.com/mozilla/mozilla_ci_tools/pull/490) - A small fix to removing an old TODO.
* [PR #491](https://github.com/mozilla/mozilla_ci_tools/pull/491) - A final refactoring of "schedule_action_task", to allow it to have a `dry_run` feature.

## Pulse Actions

Pulse Actions is a project which utilizes the MozCI functions on RabbitMQ based Pulse messages. My work here was to identify the TaskCluster requests in the pulse messages and utilize the MozCI library to schedule the action tasks.

* [PR #82](https://github.com/mozilla/pulse_actions/pull/82) - The primary patch here, which reads pulse messages and sends the data over to MozCI.
* [PR #104](https://github.com/mozilla/pulse_actions/pull/104) - Fixing a spelling mistake in the Pulse message.


