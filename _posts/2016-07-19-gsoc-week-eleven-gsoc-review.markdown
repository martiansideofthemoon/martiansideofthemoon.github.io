---
layout: post
title:  "Code of GSoC 2016 - Add TaskCluster Jobs in Treeherder"
date:   2016-07-19 00:39:55 +0530
tags: gsoc
---
This blogpost has a list of all patches and pull requests that were merged for the success of the GSoC project. There is also a developer's guide on using this new feature.

## Treeherder

Treeherder is Mozilla's primary testing and sheriffing dashboard. My work here was to add UI features to show all possible TaskCluster jobs, and allow the users to select jobs they want to schedule.

This was primarily tracked on Bugzilla in [Bug 1254325](https://bugzilla.mozilla.org/show_bug.cgi?id=1254325), [Bug 1284911](https://bugzilla.mozilla.org/show_bug.cgi?id=1284911) and [Bug 1282906](https://bugzilla.mozilla.org/show_bug.cgi?id=1282906).

Here is the list of pull requests that were merged -

*[PR #1490](https://github.com/mozilla/treeherder/pull/1490) - This is the primary pull request which adds major components of the feature. This activates the APIs but does not activate the UI.
*[PR #1625](https://github.com/mozilla/treeherder/pull/1625) - This fixed a small UI regression arising from the previous PR.
*[PR #1633](https://github.com/mozilla/treeherder/pull/1633) - A follow up PR to the previous two, primarily improving the Django code.
*[PR #1688](https://github.com/mozilla/treeherder/pull/1688) - The final PR which activates the UI and fixes a UI regression which arises due to the presence of Action Tasks.

