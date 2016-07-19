---
layout: post
title:  "GSoC Week Eleven - Go, Go, Go!"
date:   2016-07-19 00:39:55 +0530
tags: gsoc
---
All the code's been merged and the feature works! Hurrah!

Of course, there are a few issues here and there which we will fix over the due time. This will be my last blog of the series. After this, I'll have one blog having a list of all the work I did for GSoC. I'll also make one more blogpost where I introduce this wonderful new feature.

This week has been a fitness week, thanks to Pokemon Go! You just can't stop walking :)

![go]({{ site.url }}/assets/go.jpg)

## TaskCluster

This week we saw the successful merge of [Bug 1285755](https://bugzilla.mozilla.org/show_bug.cgi?id=1285755) followed by [Bug 1281062](https://bugzilla.mozilla.org/show_bug.cgi?id=1281062). This was tested in four important use cases by us and Armen has documented it in [Bug 1284911](https://bugzilla.mozilla.org/show_bug.cgi?id=1284911).

I have filed a follow up bug, [Bug 1286813](https://bugzilla.mozilla.org/show_bug.cgi?id=1286813). This fix will provide additional optimizations when there are multiple Action Tasks.

## MozCI / Pulse Actions

All the MozCI / Pulse Actions work has been merged. TaskCluster has granted Pulse Actions additional scopes to allow it to schedule jobs to Treeherder's `try` repository.

## Treeherder

A couple of commits were merged under [Bug 1284911](https://bugzilla.mozilla.org/show_bug.cgi?id=1284911). These commits activate new runnable TaskCluster jobs in the UI and fix a filtering issue in my main Treeherder patch. Once these were merged, the project was complete.

I've filed two follow up bugs. A good-first-bug for newcomers, [Bug 1286897](https://bugzilla.mozilla.org/show_bug.cgi?id=1286897) and another simple bug after Pulse Actions is granted more scopes, [Bug 1286894](https://bugzilla.mozilla.org/show_bug.cgi?id=1286894).

[PR #1661](https://github.com/mozilla/treeherder/pull/1661) has made some substantial progress, and I've been successful in solving most of the issue and adding the corresponding unittest. However, we still have some performance concerns.

It might take a while before we can merge this Pull Request.

## Bugzilla

I did some work for the Bugzilla issue in this [Pull Request](https://github.com/mozilla-bteam/bmo/pull/14). I need to continue this with a database call optimization.

Setting up Bugzilla has been a tough task to be honest!

## Other News

College has started, and lots of new things to explore!

## Coming Up

Like I said this is my last blogpost in the weekly series. There will be two more blogs, one having a complete list of commits to Mozilla for GSoC, and the second introducing the feature for developers.

I do hope you found my weekly blog series interesting :)
