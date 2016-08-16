---
layout: post
title:  "OpenGL - A Cool Paint Tool!"
date:   2016-08-16 17:00:55 +0530
tags: graphics
---

It's been a long time since my GSoC blog series, and I've had an exciting week thanks to a Computer Graphics assignment on OpenGL. The assignment involved creating a Paint application which can save / load images in a vector like custom format. This blog describes the algorithms used along with a few screenshots of the results.

The entire project has been hosted on a private repository on Github for now. All features requested for in the assignment have been completed.

## Features

All drawings are done on a 512 x 512 black canvas.
This program can draw **lines**, **triangles**, of **any color and thickness**. It has an **eraser** function which paints in the background color. There is a **fill** feature, which emulates any drawing software's Paint Bucket function. Lastly, there is a feature to save your current drawing. This is saved in a vector format, and can be loaded back into the software to reproduce the painting.

Here's a painting of stars on a blue backdrop

![stars]({{ site.url }}/assets/stars.png)

