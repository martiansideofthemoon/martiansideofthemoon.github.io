---
layout: page
title: Research
permalink: /research/
---
My interests include Natural Language Processing, Speech Recognition and Computer Graphics. I've primarily worked on three research projects - End-to-End Speech Recognition during my summer internship at [Toyota Technological Institute at Chicago](http://ttic.edu/), Neural Language Modelling as a part of a RnD Project at IIT Bombay and Constraint-Driven Learning for NLP applications as a part of my Bachelor's thesis at IIT Bombay.

#### **Publications**

* **Kalpesh Krishna**, Liang Lu, Kevin Gimpel, Karen Livescu  
"A Study of All-Convolutional Encoders for Connectionist Temporal Classification"  
*Accepted to ICASSP-2018*  
\[[arXiv](https://arxiv.org/abs/1710.10398)\] \[code\]

#### **Research Implementations**

* Macro Actions in Reinforcement Learning - A suite of five algorithms (including ideas from "[Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning](https://arxiv.org/abs/1702.06054)") encouraging agents to repeat actions - [macro-actions-rl](https://github.com/martiansideofthemoon/macro-action-rl)

* Single Image Haze Removal - An implementation of He et al. 2009, "[Single Image Haze Removal using Dark Channel Prior](https://www.robots.ox.ac.uk/~vgg/rg/papers/hazeremoval.pdf)" and an ongoing implementation of Bahat & Irani 2016, "[Blind Dehazing using Internal Patch Recurrence](http://ieeexplore.ieee.org/document/7492870/)" - [blind-dehazing](https://github.com/martiansideofthemoon/blind-dehazing)

* TensorFlow 1.1 implementation of Kim 2014, "[Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882)" - [tf-sentence-classification](https://github.com/martiansideofthemoon/tf-sentence-classification)

* Python implementation of O'Brien and Hodgins 1999, "[Graphical Modeling and Animation of Brittle Fracture](http://graphics.berkeley.edu/papers/Obrien-GMA-1999-08/Obrien-GMA-1999-08.pdf)" - [brittle-fracture-simulation](https://github.com/martiansideofthemoon/brittle-fracture-simulation)

* Python implementation of parts of Christopher Buck, Aneesh Sampath 2013, “[ECG Signal Analysis for Myocardial Infarction Detection.](https://cnx.org/contents/VZtarYnV@2.1:WO1d4SJW@1/Introduction)” - [ecg-analysis](https://github.com/martiansideofthemoon/ecg-analysis)

#### **Indian Language Datasets**

As a part of my RnD project at [IIT Bombay](http://www.iitb.ac.in/), I am releasing the dataset used to train my neural network language models. These have been mined from Wikipedia and I hope this will help further research in language modelling for Indian morphologically rich languages. The folder also contains the original PTB dataset.

* Malayalam (denoted by `ml`)
* Tamil (denoted by `ta`)
* Kannada (denoted by `kn`)
* Telugu (denoted by `te`)
* Hindi (denoted by `hi`)
* PTB (denoted by `ptb`)

All these datasets are compatible with [SRILM](http://www.speech.sri.com/projects/srilm/). Files marked with `unk` have replaced all singletons with `<unk>` tokens. Files marked with `char` are character versions. All datasets have a `train`, `valid` and `test` file. You will find the dataset [here](https://drive.google.com/file/d/0B5Y_SiDYwIObaE52dmZ0YVFXckU/view?usp=sharing).
