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