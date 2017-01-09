---
layout: post
title:  "Hack for Change!"
date:   2017-01-09 06:00:55 +0530
tags: hackathon
---

I took part in [Hack for Change](https://hackforchange.io) yesterday at [The Garage](http://www.thegarage.one/), Mumbai with my co-manager [Kumar Ayush](https://github.com/cheekujodhpur/). We were also co-sponsors of the hackathon and brought along our team to help out with the logistics.  It was a great day, and we ended at fourth place (tough luck!). Feels great to take part in a hackathon after 2 years!

We've hosted our app on Github - [cropforchange](https://github.com/martiansideofthemoon/cropforchange).

## The Experience

My day started early, (at about 7:00 AM). We travelled to the venue by taxi (a longish 25 km journey) and got there before anyone else! Soon people started pouring in and by 9:00 AM we were good to go! The venue was [The Garage](http://www.thegarage.one/) in Lower Parel, Mumbai.

After a sumptuous breakfast served by The Grand Hyatt hotel, we began brainstorming. We fixed on building an optimal crop allocator (based on soil properties) using Neural Networks (The theme was *Smart Villages*). We wanted to build a webapp which would allow farmers to enter data (used for training in the end-application). Our final social model was to use this software to allow farmers to pool in resources, plant crops optimally, and share profits equally. Since we did not have access to actual data, we decided to generate fake data based on a randomly generated soil yield.

We started off by working together on a greedy algorithm which would help us generate fake data. Unfortunately, we just had 7 hours to code. So we had to work *fast*. No wonder the code we wrote was so dirty. Nevertheless, we had generated our data by 1:00 PM, with 5 hours to go. [Here](https://github.com/martiansideofthemoon/cropforchange/blob/master/pictures/greedy_algo.jpg) is the algorithm we used.

After lunch, we divided the work. Ayush started working on the webapp, and I moved to implementing the neural network in TensorFlow. After an initial brainstorming and implementation of a wrong model, we finally settled on [this](https://github.com/martiansideofthemoon/cropforchange/blob/master/pictures/neural_network.jpg) feedforward neural network. It trained well enough ([loss curve](https://github.com/martiansideofthemoon/cropforchange/blob/master/pictures/training_plot.png)) and I followed up by building an evaluation script.

Ayush on the other hand build a webapp showing [distributions](https://github.com/martiansideofthemoon/cropforchange/blob/master/pictures/dist_webpage.png) and an input [interface](https://github.com/martiansideofthemoon/cropforchange/blob/master/pictures/webapp1.png). We ended the work with a communication between the evaluation script and the input webapp. The presentation followed and went pretty good!

After dinner there was an annoucement of results. We ended on fourth place (close miss!). The winners had built a web portal to help distribute leftover food from restaurants to NGOs (great idea!). As co-sponsors, we distributed t-shirts to all the winners. Feedback on our app clearly pointed to one thing - our model was *not yet* practical, since we hadn't accounted for factors like weather, crop rotation and time of the year. The hackathon expected solutions which could be applied easily to the real world. But everyone (including the winners) appreciated our work!

A great day for us and greater for our club! We are now known a lot better now across Mumbai's colleges and let's try to do better next time.

Here's a picture of the T-Shirt - (Yay! WnCC got its logo on it)

![hack]({{ site.url }}/assets/hackchange.jpg)