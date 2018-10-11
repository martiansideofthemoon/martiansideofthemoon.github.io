---
layout: page
title: Research
permalink: /research/
---
My interests include Natural Language Processing, Speech Recognition and Computer Graphics.

#### **Papers**

* Revisiting the Importance of Encoding Logic Rules in Sentiment Classification  
[Kalpesh Krishna](http://martiansideofthemoon.github.io/), [Preethi Jyothi](https://www.cse.iitb.ac.in/~pjyothi/), [Mohit Iyyer](https://people.cs.umass.edu/~miyyer/)  
**EMNLP 2018** *(oral presentation, short paper)*  
\[[arxiv](https://arxiv.org/abs/1808.07733)\] \[[code + data](https://github.com/martiansideofthemoon/logic-rules-sentiment/)\]
* Hierarchical Multitask Learning for CTC-based Speech Recognition  
[Kalpesh Krishna](http://martiansideofthemoon.github.io/), [Shubham Toshniwal](http://ttic.uchicago.edu/~shtoshni/), [Karen Livescu](http://ttic.uchicago.edu/~klivescu/)  
\[[arxiv](https://arxiv.org/abs/1807.06234)\]
* A Study of All-Convolutional Encoders for Connectionist Temporal Classification  
[Kalpesh Krishna](http://martiansideofthemoon.github.io/), [Liang Lu](http://ttic.uchicago.edu/~llu/), [Kevin Gimpel](http://ttic.uchicago.edu/~kgimpel/), [Karen Livescu](http://ttic.uchicago.edu/~klivescu/)  
**ICASSP 2018** *(Awarded [SPS Travel Grant](https://signalprocessingsociety.org/events/sps-travel-grants))*  
\[[arxiv](https://arxiv.org/abs/1710.10398)\] \[[poster](https://sigport.org/sites/default/files/docs/study-convolutional-encoders.pdf)\]

#### **Bachelor's Thesis**

* Constraint Driven Learning  
*(under guidance of [Prof. Preethi Jyothi](https://www.cse.iitb.ac.in/~pjyothi/))*  
**IIT Bombay** *(2017-2018)*  
\[[pdf]({{ site.url }}/assets/btp-report.pdf)\]

#### **Research Implementations**

* [Inference Networks for Structured Prediction]() - A TensorFlow implementation for the multi-label classification experiments in [Learning Approximate Inference Networks for Structured Prediction](https://arxiv.org/abs/1803.03376). Also contains experiments on the [FIGMENT](http://cistern.cis.lmu.de/figment/) dataset and a extension to Inference Network training algorithm based on the paper [Improved Training of Wasserstein GANs](https://arxiv.org/abs/1704.00028).

* [Diversity Sampling in Machine Learning](http://github.com/martiansideofthemoon/diversity-sampling) - An implementation of [Diverse Beam Search for Neural Networks](https://arxiv.org/abs/1610.02424) in Language Modelling. Also contains the original (slightly modified code) for the interactive segmentation experiments in [Diverse M-Best Solutions in MRFs](http://ttic.uchicago.edu/~gregory/papers/MBestModes.pdf).

* [Macro Actions in Reinforcement Learning]((https://github.com/martiansideofthemoon/macro-action-rl)) - A suite of five algorithms (including ideas from "[Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning](https://arxiv.org/abs/1702.06054)") encouraging agents to repeat actions.

* [Single Image Haze Removal](https://github.com/martiansideofthemoon/blind-dehazing) - An implementation of He et al. 2009, "[Single Image Haze Removal using Dark Channel Prior](https://www.robots.ox.ac.uk/~vgg/rg/papers/hazeremoval.pdf)" and an ongoing implementation of Bahat & Irani 2016, "[Blind Dehazing using Internal Patch Recurrence](http://ieeexplore.ieee.org/document/7492870/)".

* [CNNs for Sentence Classification](https://github.com/martiansideofthemoon/tf-sentence-classification) - A TensorFlow 1.1 implementation of Kim 2014, "[Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882)".

* [Brittle Fracture Simulation](https://github.com/martiansideofthemoon/brittle-fracture-simulation) - Python implementation of O'Brien and Hodgins 1999, "[Graphical Modeling and Animation of Brittle Fracture](http://graphics.berkeley.edu/papers/Obrien-GMA-1999-08/Obrien-GMA-1999-08.pdf)".

* [ECG Signal Analysis](https://github.com/martiansideofthemoon/ecg-analysis) - Python implementation of parts of Christopher Buck, Aneesh Sampath 2013, “[ECG Signal Analysis for Myocardial Infarction Detection.](https://cnx.org/contents/VZtarYnV@2.1:WO1d4SJW@1/Introduction)”.

#### **Indian Language Datasets**

As a part of my RnD project at [IIT Bombay](http://www.iitb.ac.in/), I am releasing the dataset used to train my neural network language models. These have been mined from Wikipedia and I hope this will help further research in language modelling for Indian morphologically rich languages. The folder also contains the original PTB dataset.

* Malayalam (denoted by `ml`)
* Tamil (denoted by `ta`)
* Kannada (denoted by `kn`)
* Telugu (denoted by `te`)
* Hindi (denoted by `hi`)
* PTB (denoted by `ptb`)

All these datasets are compatible with [SRILM](http://www.speech.sri.com/projects/srilm/). Files marked with `unk` have replaced all singletons with `<unk>` tokens. Files marked with `char` are character versions. All datasets have a `train`, `valid` and `test` file. You will find the dataset [here](https://drive.google.com/file/d/0B5Y_SiDYwIObaE52dmZ0YVFXckU/view?usp=sharing).
