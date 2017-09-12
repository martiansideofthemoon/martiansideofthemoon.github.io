---
layout: page
title: Research
permalink: /research/
---
### Code

* TensorFlow 1.1 Implementation of Kim et al. 2014, "[Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882)" - [tf-sentence-classification](https://github.com/martiansideofthemoon/tf-sentence-classification)

### Indian Language Datasets

As a part of my RnD project at [IIT Bombay](http://www.iitb.ac.in/), I am releasing the dataset used to train my neural network language models. These have been mined from Wikipedia and I hope this will help further research in language modelling for Indian morphologically rich languages. The folder also contains the original PTB dataset.

* Malayalam (denoted by `ml`)
* Tamil (denoted by `ta`)
* Kannada (denoted by `kn`)
* Telugu (denoted by `te`)
* Hindi (denoted by `hi`)
* PTB (denoted by `ptb`)

All these datasets are compatible with [SRILM](http://www.speech.sri.com/projects/srilm/). Files marked with `unk` have replaced all singletons with `<unk>` tokens. Files marked with `char` are character versions. All datasets have a `train`, `valid` and `test` file.

You will find the dataset [here](https://drive.google.com/file/d/0B5Y_SiDYwIObaE52dmZ0YVFXckU/view?usp=sharing).
 -->