---
layout: post
title:  "GSoC Week Eight - LEGO Star Wars!"
date:   2016-06-25 04:39:55 +0530
tags: gsoc
---
My MozLondon trip ended on a high, when Armen gifted me a super cool Star Wars Rebels LEGO kit! I spent a complete day this week making the starships, and they are brilliant to say the least! This is what the Darth Vader ship looks like.

![lego]({{ site.url }}/assets/lego.jpg)

So I'm now having to do some in-tree work. It was an eventful week full of Action Tasks.

## Why not Pulse Actions?

So the original plan to schedule Treeherder jobs was completely using [pulse_actions](https://github.com/mozilla/pulse_actions), following an approach similar to Buildbot jobs. There are several problems here. TaskCluster has several authentication steps, and we needed to go through an RRA before I could be granted credentials to schedule TaskCluster jobs in Treeherder via Pulse Actions. TaskCluster is going through a lot of changes and it would be impossible for pulse_actions to keep up with this.
Most importantly, Dustin had done most of what I was doing in pulse_actions in-tree. The code he'd written is more effective since it was optimizing the task graph removing redundant steps.

Hence we decided NOT to go ahead with [this](https://github.com/mozilla/mozilla_ci_tools/pull/486). Nevertheless, it was fun writing a basic version of the code as it involved some graph theory. As you can see in the last blogpost, I did succeed in scheduling jobs using this approach.

## What are Action Tasks?

Action Tasks are going to be new types of jobs, which will run a new [mach command](https://dxr.mozilla.org/mozilla-central/source/mach) and schedule the jobs specified in the mach command's parameter list. When a user clicks on "Add New Jobs", a pulse message will be sent down to pulse_actions, which in turn will schedule an Action Task in that push on Treeherder.
This action task runs the new mach command and uses the in-tree code to schedule the required jobs. This is a better approach for a few reasons:

* The action task will have **all the logs regarding "Add New Jobs" failures**. There is no need to look at the PaperTrail in pulse_actions as long as the Action Task has been scheduled.
* The action task **reuses Dustin's in-tree work** and will be **easier to maintain**.
* The action task **gives users proper feedback**. A failed Action Task would mean that "Add New Jobs" has failed. In the current model, the user does not receive any feedback and is forced to file a bug, not knowing what happened.
* The **asynchronous element is slowly going away**. Since we just have one job to schedule now, once Treeherder gets its TaskCluster authentication, we could directly schedule Action Tasks using Treeherder. This would remove the need of asynchronous Pulse messages for "Add New Jobs" and slowly make "Add New Jobs" completely synchronous.

The major disadvantage of action tasks is the non-parallelism with the approach for Buildbot jobs. However, since Buildbot jobs will soon be TaskCluster jobs, it makes sense to go forward with Action Tasks.

## Are we going to kill Pulse Actions?

No, not yet. A lot of features rely on Pulse Actions. We will be using pulse_actions to schedule the Action Tasks for now. Since Treeherder is receiving a TaskCluster authentication soon, pulse_actions may not be used in the future to schedule Action Tasks, and we would do it using Treeherder directly.
We might not need pulse_actions at all in the future once Buildbot jobs have been removed completely. However, this could take a significant amount of time.

## Progress with Action Tasks

I've had an excellent week with respect to programming action tasks. It started by filing [Bug 1281062](https://bugzilla.mozilla.org/show_bug.cgi?id=1281062). As you can see, I've added patches. Yes, we have our first green action tasks! :)

So I started by creating a new mach command, `mach taskgraph action-task`. Here is what a sample command looks like -

```
./mach taskgraph action-task --task-labels="TaskLabel==A-JT3sTNQMSvayONPiHU6A,TaskLabel==AWMGHageQh-L_nkBPsQOvA" --decision-id="TADoGLV5RUWQYivg1ReyTw"
```

There are two parameters here, the very same parameters I fetch from Treeherder. The gecko decision task ID and a comma separated list of Task Labels for that decision id. I am sending exactly these two parameters down the Pulse message.

This mach command downloads the corresponding full-tasks-graph file and generates a `TaskGraph` object using it. (`TaskGraph` defined [here](https://dxr.mozilla.org/mozilla-central/source/taskcluster/taskgraph/types.py#44)). This then passes through the in-tree code to generate aritifacts, optimize the task graph and schedule the tasks.

The second part of the patch was creating an action task definition and creating it as an artifact in the decision task. This was a bit challenging, since there are a lot of contraints on the task definition schema. I did succeed after a few iterations, and I could use `action.yml` to schedule an action task in Treeherder.

The first few action tasks failed due to a timestamps issue. I'm updating all timestamps in-tree now, (in the action task mach command). I soon had my first green action task :D

![action]({{ site.url }}/assets/action.png)

In the above picture, `tc-M(dt4)` is the job I passed in the parameters, and it was successfully scheduled. Unfortunately, `optimize.py` hasn't done its magic as taskcluster-images were also scheduled. I might need to dig into what's wrong, but atleast we have an awesome start! [This](https://treeherder.mozilla.org/#/jobs?repo=try&revision=88f8d3edac627665a2dc6df5294ccd53cb53621c) is the push on Treeherder. We've tracked the task [here](https://tools.taskcluster.net/task-inspector/#dxZ73-meQ-WR4WIghphVpg/0).

## Other News

It's raining heavily in Mumbai all day, so I'm pretty much indoors. I visited the Facebook Mumbai office and it was really cool! We have started a new [Seasons of Code](http://wncc-iitb.org/soc/) project in our club named [Rattlesnake](https://github.com/ranveeraggarwal/rattlesnake) to teach people Python. I might do the same tasks in Perl!

## Coming Up

We might have to merge the Treeherder [Pull Request](https://github.com/mozilla/treeherder/pull/1490) putting some UI restrictions to help [Mike Ling](https://github.com/MikeLing) continue with his GSoC project. I hope to complete my action tasks patch and write a function in MozCI / Pulse Actions to schedule Action Tasks on receiving pulse messages.
