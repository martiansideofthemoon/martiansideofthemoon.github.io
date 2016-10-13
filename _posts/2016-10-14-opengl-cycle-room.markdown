---
layout: post
title:  "OpenGL - Cycle All Lit Up!"
date:   2016-10-14 17:00:55 +0530
tags: graphics
---

The next part of the assignment involved adding lighting, textures, motion and cameras to our scene. It has been pretty interesting. The best part is the added realism to the whole scene.

Here is the final output produced in fixed camera mode.

![cycle3]({{ site.url }}/assets/cycle3.png)

## ANNNNDDD, Lights OFF!

![cycle4]({{ site.url }}/assets/cycle4.png)

I now go about to describe the basic implementation details. This article reuses the terminology in the previous [article]({% post_url 2016-09-28-opengl-cycle.markdown %}).

## The Room

The room has been made as a part of the `Assembly.cpp` classes, as a `Room` class. The `Room` class consists of six `Surface` objects, each of which produce a mesh of rectangles depending on the amount of detail needed. This has been done to ensure [Gouraud Shading](https://en.wikipedia.org/wiki/Gouraud_shading) is successful when light shines on walls.

Additionally, the room consists of a light source. The cycle has been placed at the centre of the room.


