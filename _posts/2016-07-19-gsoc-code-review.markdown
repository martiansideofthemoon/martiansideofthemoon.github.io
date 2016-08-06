---
layout: post
title:  "Code of GSoC 2016 - Add TaskCluster Jobs in Treeherder"
date:   2016-07-20 00:39:55 +0530
tags: gsoc
---
This blogpost has a list of all patches and pull requests that were merged for the success of the GSoC project. There is also a [developer's guide](https://wiki.mozilla.org/ReleaseEngineering/TryServer#How_to_push_to_try) on using this new feature. Besides this, a [technical blog]({% post_url 2016-07-20-how-i-added-tc-jobs %}) has been added.

This feature is **COMPLETE** and **WORKING**. There are a few follow up bugs which I will mention in this blogpost and were not strictly a part of the project.

## TaskCluster

TaskCluster is a graph based test scheduler which is at the heart of Mozilla's Continuous Integration. My major work in this GSoC project was in the `taskcluster` part of [mozilla-central](https://dxr.mozilla.org/mozilla-central/source/).

My job was to implement Action Tasks which will do the job of scheduling new jobs. I also needed to improve the TaskGraph optimization that was being used.

All my TaskCluster work was recorded in [Bug 1281062](https://bugzilla.mozilla.org/show_bug.cgi?id=1281062). This was broken down into four different patches finally -

* [Bug 1284005](https://bugzilla.mozilla.org/show_bug.cgi?id=1284005) ([Patch](https://hg.mozilla.org/mozilla-central/rev/7e73e9581bca)) - This is the first bug. This refactors the timestamp mechanism used in `TaskGraph` generation. Now instead of actual timestamps, `relative-datestamps` are used which are replaced with actual timestamps when the tasks are actually created.
* [Bug 1285755](https://bugzilla.mozilla.org/show_bug.cgi?id=1285755) ([Patch](https://hg.mozilla.org/mozilla-central/rev/b1a86b2b81ff)) - This is the second bug. This adds a feature to build a `TaskGraph` object from a corresponding JSON file, taking care of the special cases for various `Task` subclasses. This feature also utilized [Dustin](https://github.com/djmitche)'s [patch](https://hg.mozilla.org/mozilla-central/rev/2393f903d0a7) to find python modules.
* [Bug 1281062](https://bugzilla.mozilla.org/show_bug.cgi?id=1281062) ([Patch](https://hg.mozilla.org/mozilla-central/rev/d223b3cdee66)) - The final piece of the puzzle which adds action tasks.
* [Bug 1288220](https://bugzilla.mozilla.org/show_bug.cgi?id=1288220) ([Patch](https://hg.mozilla.org/integration/autoland/rev/d05aa8ecdb0b)) - Adding a `from_json` implementation for `TestTask`, fixing a regression.


## Treeherder

Treeherder is Mozilla's primary testing dashboard. My work here was to enchance the APIs to show TaskCluster jobs, allow the users to select jobs they want to schedule, and finally send these TaskCluster jobs through a Pulse message.

This was primarily tracked on Bugzilla in [Bug 1254325](https://bugzilla.mozilla.org/show_bug.cgi?id=1254325), [Bug 1284911](https://bugzilla.mozilla.org/show_bug.cgi?id=1284911), [Bug 1282906](https://bugzilla.mozilla.org/show_bug.cgi?id=1282906) and [Bug 1288053](https://bugzilla.mozilla.org/show_bug.cgi?id=1288053)

Here is the list of pull requests that were merged -

* [PR #1490](https://github.com/mozilla/treeherder/pull/1490) - This is the primary pull request which adds major components of the feature. This activates the APIs but does not activate the UI.
* [PR #1625](https://github.com/mozilla/treeherder/pull/1625) - This fixed a small UI regression arising from the previous PR.
* [PR #1633](https://github.com/mozilla/treeherder/pull/1633) - A follow up PR to the previous two, primarily improving the Django code.
* [PR #1688](https://github.com/mozilla/treeherder/pull/1688) - The final PR which activates the UI and fixes a UI regression which arises due to the presence of Action Tasks.
* [PR #1710](https://github.com/mozilla/treeherder/pull/1710) - Fixing a regression caused by the new `full-task-graph.json` format.

## MozCI

MozCI is a python package that's utilizes the different parts of Mozilla's Continuous Integration and connects them together via APIs. Originally, my work here was to add functions to schedule all TaskCluster jobs requested, resolving dependencies and fixing task references.

However, since we decided to use Action Tasks, the work here reduced substantially.

Here is the list of pull requests we used -

* [PR #480](https://github.com/mozilla/mozilla_ci_tools/pull/480) - Fetching the full tasks file. We backed out these changes in a latter PR.
* [PR #486](https://github.com/mozilla/mozilla_ci_tools/pull/486) (CLOSED) - This Pull Request contains the method originally proposed in the GSoC proposal. We didn't merge this due to less reliability and sustainability.
* [PR #489](https://github.com/mozilla/mozilla_ci_tools/pull/489) - This patch allows us to schedule action tasks, which perform all the magic in-tree.
* [PR #490](https://github.com/mozilla/mozilla_ci_tools/pull/490) - A small fix to removing an old TODO.
* [PR #491](https://github.com/mozilla/mozilla_ci_tools/pull/491) - A final refactoring of "schedule_action_task", to allow it to have a `dry_run` feature.
* [PR #495](https://github.com/mozilla/mozilla_ci_tools/pull/495) - Fixing a regression caused by the new `full-task-graph.json` format.

## Pulse Actions

Pulse Actions is a project which utilizes the MozCI functions on RabbitMQ based Pulse messages. My work here was to identify the TaskCluster requests in the pulse messages and utilize the MozCI library to schedule the action tasks.

Here is the list of pull requests we used -

* [PR #82](https://github.com/mozilla/pulse_actions/pull/82) - The primary patch here, which reads pulse messages and sends the data over to MozCI.
* [PR #104](https://github.com/mozilla/pulse_actions/pull/104) - Fixing a spelling mistake in the Pulse message.
* [PR #107](https://github.com/mozilla/pulse_actions/pull/107) - Fixing a regression caused by the new `full-task-graph.json` format.

Having done this, Pulse Actions was granted the correct scopes through [Bug 1286843](https://bugzilla.mozilla.org/show_bug.cgi?id=1286843).

## TaskCluster Scheduler Experiments

Here is the list of pull requests we used -

This is mostly an experimental repository which was used for all the experimentation and testing. It was an important part of the project as it has python scripts to quickly schedule action tasks.

* [PR #2](https://github.com/armenzg/TC_developer_scheduling_experiments/pull/2) - The original implementation which was backed out due to less reliability and sustainability.
* [PR #3](https://github.com/armenzg/TC_developer_scheduling_experiments/pull/3) - The logic actually used in MozCI to schedule Action Tasks.
* [PR #4](https://github.com/armenzg/TC_developer_scheduling_experiments/pull/4) - Adding command line arguments to the schedule_action_task.py script.

## Follow-Up Bugs

Here are the bugs that have been filed as a follow up. None of them are necessary for the feature to work, but will improve the code and speed.

* [Bug 1288028](https://bugzilla.mozilla.org/show_bug.cgi?id=1288028) - We need to speed up the first step where we get a list of all possible jobs by clicking "Add New Jobs".
* [Bug 1286894](https://bugzilla.mozilla.org/show_bug.cgi?id=1286894) - The current feature only works for the try repository (where it is really needed). This bug hopes to assess the risks involved with extending this feature to non-try repositories. It should be fairly straightforward to fix.
* [Bug 1286813](https://bugzilla.mozilla.org/show_bug.cgi?id=1286813) - This is the bug to improve the `TaskGraph` optimizations when more than one Action Task is scheduled.
* [Bug 1286897](https://bugzilla.mozilla.org/show_bug.cgi?id=1286897) - This is the bug to fix a wrong naming convention in Treeherder's python files. This is a good-first-bug for beginners.

## Non GSoC Work

I added a number of features outside of the GSoC project during the GSoC period. I will hyperlink them below.

* **Treeherder** - [PR #1645](https://github.com/mozilla/treeherder/pull/1645), [PR #1646](https://github.com/mozilla/treeherder/pull/1646) and [PR #1661](https://github.com/mozilla/treeherder/pull/1661).
* **MozCI** - [PR #469](https://github.com/mozilla/mozilla_ci_tools/pull/469), [PR #470](https://github.com/mozilla/mozilla_ci_tools/pull/470), [PR #473](https://github.com/mozilla/mozilla_ci_tools/pull/473), [PR #475](https://github.com/mozilla/mozilla_ci_tools/pull/475), [PR #477](https://github.com/mozilla/mozilla_ci_tools/pull/477), [PR #482](https://github.com/mozilla/mozilla_ci_tools/pull/482), [PR #483](https://github.com/mozilla/mozilla_ci_tools/pull/483), [PR #484](https://github.com/mozilla/mozilla_ci_tools/pull/484) and [PR #485](https://github.com/mozilla/mozilla_ci_tools/pull/485)
* **Pulse Actions** - [PR #73](https://github.com/mozilla/pulse_actions/pull/73), [PR #75](https://github.com/mozilla/pulse_actions/pull/75), [PR #80](https://github.com/mozilla/pulse_actions/pull/80), [PR #84](https://github.com/mozilla/pulse_actions/pull/84) and [PR #90](https://github.com/mozilla/pulse_actions/pull/90).
* **Bugzilla** - [PR #14](https://github.com/mozilla-bteam/bmo/pull/14)
* **WPT Viewer** - [PR #130](https://github.com/mozilla/wptview/pull/130), [PR #131](https://github.com/mozilla/wptview/pull/131), [PR #133](https://github.com/mozilla/wptview/pull/133), [PR #139](https://github.com/mozilla/wptview/pull/139), [PR #140](https://github.com/mozilla/wptview/pull/140) and a lot of code review since I'm the maintainer of this project.
