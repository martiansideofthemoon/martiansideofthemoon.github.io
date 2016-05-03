---
layout: post
title:  "GSoC Week One - Last Martian Meets Darth Vader!"
date:   2016-05-04 03:39:55 +0530
tags: gsoc
---
I've been absolutely obsessed with Star Wars this week, especially Darth Vader. I've named my [Pull Request](https://github.com/mozilla/mozilla_ci_tools/pull/469) after him, the video chat room with [Armen](https://mozillians.org/en-US/u/armenzg/) and I'm thinking of changing my IRC nickname for a day! It's probably because I just saw the awesome seventh movie in the series!

![vader]({{ site.url }}/assets/darth.png)

In any case, let's get back to how the week worked for me.

## My Development Server!

So I've officially given up on trying to set up the VPN for my loaner machine like I'd mentioned in the previous blog post. Luckily, [Dustin](https://github.com/djmitche) has given me an awesome new server to work with. It did take some time to setup, since we want to shut the server down (using `sudo halt`) when the server won't be used for prolonged periods. Dustin has a project to help turning on this server once again which can be found [here](https://github.com/djmitche/proj). I've set up this server with the [mozilla_ci_tools](https://github.com/mozilla/mozilla_ci_tools) and [pulse_actions](https://github.com/mozilla/pulse_actions) repositories and they work like a charm, overcoming the restrictions I was facing from my institute!

## Pulse Actions

I've started work on [Pulse Actions](https://github.com/mozilla/pulse_actions) on a bug to listen and identify [PGO](https://en.wikipedia.org/wiki/Profile-guided_optimization) builds on [mozilla-inbound](https://treeherder.mozilla.org/#/jobs?repo=mozilla-inbound) or [fx-team](https://treeherder.mozilla.org/#/jobs?repo=fx-team) and trigger all Talos jobs twice. More details can be found on the [bug](https://github.com/mozilla/pulse_actions/issues/70).

My work on this can be found [here](https://github.com/mozilla/pulse_actions/pull/73). Working on this has been interesting so far. I've learnt the basic workflow followed by Pulse Actions, and I discovered a [small bug](https://github.com/mozilla/mozilla_ci_tools/issues/468) in MozCI in this process. I've decided to fix this [here](https://github.com/mozilla/mozilla_ci_tools/pull/469) before I carry on with the Pulse Actions bug.

While working on MozCI I really liked [pytest](https://pytest.org) over Python [unittests](https://docs.python.org/2.7/library/unittest.html), and I hope to write a small tutorial on it soon!

## Work on mozilla-central