---
layout: post
title:  "OpenGL - A Cool Paint Tool!"
date:   2016-08-16 17:00:55 +0530
tags: graphics
---

It's been a long time since my GSoC blog series, and I've had an exciting week thanks to a Computer Graphics assignment on OpenGL. The assignment involved creating a Paint application which can save / load images in a vector like custom format, without using any of the in-built functionality that OpenGL gives us. This blog describes the algorithms used along with a few screenshots of the results.

The entire project has been hosted on a private repository on Github for now. **All features requested for in the assignment have been completed.**

## Features

All drawings are done on a 1024 x 640 black canvas.
This program can draw **lines**, **triangles**, of **any color and thickness**. It has an **eraser** function which paints in the background color. There is a **fill** feature, which emulates any drawing software's Paint Bucket function. Lastly, there is a feature to save your current drawing. This is saved in a vector format, and can be loaded back into the software to reproduce the painting.

Here's a painting of stars on a blue backdrop

![stars]({{ site.url }}/assets/stars.png)

## Plotting Points

To plot a single point at `(x, y)`, a `point_t` object was created having color same as the attribute in `pen_t`. This point was then extrapolated depending on the size provided by `pen_t`. For `size = 1`, a single pixel was plotted. For `size = 2`, a `3 x 3` grid was plotted with `(x, y)` as the centre of the square. In general, for `size = i`, a `2i-1 x 2i-1` square was plotted centred at `(x,y)`.

## Lines and Triangles

To draw lines, the [Brensenham Algorithm](https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm) was used and implemented in all eight octants. Each desired pixel was drawn individually after an adjustment on size and color, depending on the attributes of the `pen_t` class. All pixels were first added to a 2D array and plotted on the screen at the end of the whole operation.

To draw triangles, three lines were drawn in succession.

## Fill Algorithm

To fill a certain section on the image, first a seed pixel is provided by the user. The color of that pixel is called the target color, and all pixels which are connected (horizontal and vertical connections only) to this pixel by a series of target colored pixels are colored by the fill color.

The fill algorithm implemented is the second algorithm in the [alternative implementations](https://en.wikipedia.org/wiki/Flood_fill#Alternative_implementations) mentioned on the Wikipedia page. The first alternative implementation was extremely slow, forcing us to use the faster and more practical approach of filling the east-west direction first.

## Loading / Saving from Files

The program maintains a list of operations performed on the canvas from the start. The operations supported are drawing lines (code `'L'`), drawing triangles (code `'T'`), changing pen configuration, (code `'C'`) and filling figures (code `'F'`). Each of the corresponding classes have a pair of functions, `to_string` and `from_string`.

Each time one of the above operations happen, the `to_string` converts relevant information about the object to a string and stores it in the list along with the `op_code`. On pressing Save, the list is read out and written down into a file.

On pressing `Load`, the file is read and divided into op_codes and inputs. The input strings are fed into empty objects via the `from_string` function, which populates the object's parameters (for example, the endpoints of a `line_t` object). This object is then drawn to the canvas.

## Future Improvements

* There is a need to have an UNDO function. This is easy to implement due to the list structure that has been used to store operations.
* There should be a function to draw circles and ellipses.
* The eraser is not very useful in the current implementation.

## Finally, an ode to Rio 2016!

![rio]({{ site.url }}/assets/rio.png)
