---
layout: post
title:  "OpenGL - Animation!"
date:   2016-10-30 12:00:55 +0530
tags: graphics
---

The third and final part of the assignment, and guess what! We finally have our movie ready! You can catch a glimpse here - [https://www.youtube.com/watch?v=wfe_fRxyp5E](https://www.youtube.com/watch?v=wfe_fRxyp5E).

This part of the assignment hasn't had major visual additions, but significant new features like playback and keyframes. I will go about to describe the major new changes.

## Keyframes

There is now a facility to save the state of the model at any point. This is written to a file `keyframes.txt`, which is interally a `Keyframe` object. Every time this file write happens, a `vector<Keyframe>` is updated which is a part of the `Animate` class.

There is also a facility to clear the file and `vector`.

## Playback & Interpolation

Whenever the `playback()` function is executed, a function of the `Animate` class, `play_next()` is called which generates the next frame in the scene. There is a linear interpolation between successive keyframes depending on the `FPS` global variable.

After building the scene, a `glutPostRedisplay()` is called. There is a check, `carry_on`, which checks whether any more keyframes are left to be rendered. This information is provided by the `Animate` class.
If yes, a `glutTimerFunc()` is called to `play_back()`, which executes after `1 / FPS` seconds.

## Movie

To make the final movie, there is an option to export each frame to an external `.tga` file. These files are then converted to `.png` files which are finally stitched together using `ffmpeg`.

## After Thoughts

The graphics project and course has been great to say the least! I'm really looking forward to studying Advanced Computer Graphics / Digital Geometry Processing in the future. I can finally say I know a bit about what goes into making those awesome video games.


