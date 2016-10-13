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

I now go about to describe the basic implementation details. This article reuses the terminology in the previous [article]({% post_url 2016-09-28-opengl-cycle %}).

## The Room

The room has been made as a part of the `Assembly.cpp` classes, as a `Room` class. The `Room` class consists of six `Surface` objects, each of which produce a mesh of rectangles depending on the amount of detail needed. This has been done to ensure [Gouraud Shading](https://en.wikipedia.org/wiki/Gouraud_shading) is successful when light shines on walls.

Additionally, the room consists of a light source. The cycle has been placed at the centre of the room.

## Lighting

The first step to enable lighting needed us to change every `glColor3f` to `glMaterialfv`, and assign the same color to the object's ambient and diffused properties. We have assumed all objects are specular and reflect `(1, 1, 1)` as specular reflections.

The second step involved setting up the light sources and their properties. Two light sources have been created. One is fixed to the handle and rotates along with the handle (`GL_LIGHT1`). The second light source is present close to the centre of the ceiling (`GL_LIGHT0`).

The lighting code has been integrated with the `Assembly.cpp` classes.

## Cameras

Three cameras have been setup, a first person view, a third person view and a fixed view close to the top of the ceiling (as you saw earlier). Here are the first and third person views.

![cyclefirst]({{ site.url }}/assets/cycle_first.png)

![cyclethird]({{ site.url }}/assets/cycle_third.png)

## Textures

We developed a basic API to add textures to a certain section of any of the surfaces. Here we have added a Mona Lisa painting on the wall and a wooden floor texture on the floor.

These images were loaded from bitmap images. Very large images were causing a lot of lag while trying to move the cycle.

Additionally, a striped texture has been added to two cylinders of the frame of the cycle. Here is the texture added for reference. This is quite evident in the first person view.

![grad]({{ site.url }}/assets/RedWhiteStripe.jpg)

