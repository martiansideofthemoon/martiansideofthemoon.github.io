---
layout: post
title:  "OpenGL - A 3D Cycle!"
date:   2016-09-28 17:00:55 +0530
tags: graphics
---

As the paint tool was wrapped up, up came the task of modelling a 3D cycle. I'd never modelled anything from scratch in 3-D before this, and it's been a wonderful experience!

Here's how our final product looks like -

![cycle]({{ site.url }}/assets/cycle.png)

Without going into the gory details, here's how this task was achieved -

## Base Object

There is a base class `BaseObject` that contains the basic format of all objects. Every object has children ([hierarchial modelling](http://www.gamedev.net/page/resources/_/technical/opengl/opengl-object-hierarchy-r1267)), and a specific render sequence. It is customary to render all children first and apply all the transformations on the parent to the children.

This is implemented using the `glPushMatrix()` and `glPopMatrix()` pair.

## Parts

Each individual part of the cycle is inherited from the `BaseObject` along with suitable parameters. An example is the `Wheel` part, which has parameters like `wheel_radius`, `spokes`, `wheel_center`, `wheel_normal` and `wheel_color[2]`. The rotate function is suitable constrained to prevent rotation on non normal axes.

## Assembly

A `Cycle` class has been written which assembles the entire cycle. It reads parameters from a file and makes objects of the various part classes. Parent-Children relationships are correctly established in this function.

The `Cycle` class also handles the rotations and motions of the cycle. On executing the `pedal()` function, it is ensure that only the angle of the wheels, pedal, rider and chain change by the same amount. A similar procedure is followed for the handle.

## Bonus Parts

In this assignment, the chain and the rider were the bonus parts. You can see them clearly here.

![cycle2]({{ site.url }}/assets/cycle2.png)

* `Chain` - The `Chain` has been built up using small cylinders of the identical radius and arranged in the correct form touching each other. While moving the chain, for each link the straight distance travelled and circular angle covered is calculated and superimposed accordingly.

* *Ghost* `Rider` - The `Rider`, (a ghost, since he just has legs), is characterised by two angles, the thigh angle and the calf angle. Using the cosine rule, the correct position of the foot has been calculated after taking the pedal position as an input.
