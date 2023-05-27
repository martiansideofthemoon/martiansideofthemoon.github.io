---
layout: page
title: Other Projects
permalink: /other_projects/
order: 6
---

Outlining my non-published projects here (open source contributions, course research projects, designed homeworks). My research work can be seen [here](/research/).

#### **Other Research (Course Projects)**

[Self-supervised Learning on 3D Point Clouds](https://github.com/martiansideofthemoon/pointnet-acd-deformations): New algorithms for self-supervised learning on point clouds, where we teach models to discriminate between real and fake objects. To create fake objects, we perform global perturbations to segments of an object derived from [Approximate Convex Decomposition](https://arxiv.org/abs/2003.13834) ([report]({{ site.url }}/assets/point_cloud_discriminate.pdf)).

[MixMatch on Vision + Language Tasks (NLVR2)](https://github.com/martiansideofthemoon/mixmatch-lxmert): An attempt to integrate the [MixMatch](https://arxiv.org/abs/1905.02249) data augmentation algorithm for semi-supervised image classification to the challenging setting of [NLVR2](http://lil.nlp.cornell.edu/nlvr), where the input space has both images and text ([report](https://sumanvid97.github.io/docs/cv_report.pdf)).

[Research Exchange - A Collaborative Paper Annotation Tool](https://github.com/martiansideofthemoon/research-exchange) - A platform to collaboratively annotate scientific literature to help newcomers understand research papers, built during an Human Computer Interaction course project ([report]({{ site.url }}/assets/research-exchange.pdf)).

[Inference Networks for Structured Prediction](https://github.com/TheShadow29/infnet-spen) - A TensorFlow implementation for the multi-label classification experiments in [Learning Approximate Inference Networks for Structured Prediction](https://arxiv.org/abs/1803.03376). Also contains experiments on the [FIGMENT](http://cistern.cis.lmu.de/figment/) dataset and a extension to Inference Network training algorithm based on [Wasserstein GANs](https://arxiv.org/abs/1704.00028) ([report](https://people.cs.umass.edu/~kalpesh/infnet.pdf)).

[Diversity Sampling in Machine Learning](http://github.com/martiansideofthemoon/diversity-sampling) - An implementation of [Diverse Beam Search for Neural Networks](https://arxiv.org/abs/1610.02424) in Language Modelling. Also contains the original (slightly modified code) for the interactive segmentation experiments in [Diverse M-Best Solutions in MRFs](http://ttic.uchicago.edu/~gregory/papers/MBestModes.pdf) ([report](https://people.cs.umass.edu/~kalpesh/diversity.pdf)).

[Macro Actions in Reinforcement Learning](https://github.com/martiansideofthemoon/macro-action-rl) - A suite of five algorithms (including ideas from "[Learning to Repeat: Fine Grained Action Repetition for Deep Reinforcement Learning](https://arxiv.org/abs/1702.06054)") encouraging agents to repeat actions ([report](https://people.cs.umass.edu/~kalpesh/macro.pdf)).

[Single Image Haze Removal](https://github.com/martiansideofthemoon/blind-dehazing) - An implementation of He et al. 2009, "[Single Image Haze Removal using Dark Channel Prior](https://www.robots.ox.ac.uk/~vgg/rg/papers/hazeremoval.pdf)" and an ongoing implementation of Bahat & Irani 2016, "[Blind Dehazing using Internal Patch Recurrence](http://ieeexplore.ieee.org/document/7492870/)" ([report](https://people.cs.umass.edu/~kalpesh/dehaze.pdf)).

[CNNs for Sentence Classification](https://github.com/martiansideofthemoon/tf-sentence-classification) - A TensorFlow 1.1 implementation of Kim 2014, "[Convolutional Neural Networks for Sentence Classification](https://arxiv.org/abs/1408.5882)".  

[Brittle Fracture Simulation](https://github.com/martiansideofthemoon/brittle-fracture-simulation) - Python implementation of O'Brien and Hodgins 1999, "[Graphical Modeling and Animation of Brittle Fracture](http://graphics.berkeley.edu/papers/Obrien-GMA-1999-08/Obrien-GMA-1999-08.pdf)".  

[ECG Signal Analysis](https://github.com/martiansideofthemoon/ecg-analysis) - Python implementation of parts of Christopher Buck, Aneesh Sampath 2013, “[ECG Signal Analysis for Myocardial Infarction Detection.](https://cnx.org/contents/VZtarYnV@2.1:WO1d4SJW@1/Introduction)”.  

#### **Course Materials**

[Homework](https://github.com/martiansideofthemoon/allennlp-probe-hw) on linguistic probe tasks designed for UMass Amherst's grad NLP class using [AllenNLP](https://allennlp.org/).

#### **Open Source Contributions**

* Primary Contributor / Maintainer - [mozilla/wptview](https://github.com/mozilla/wptview)
* Significant Contributions - [mozilla/gecko-dev](https://github.com/mozilla/gecko-dev/) (Firefox), [mozilla/treeherder](https://github.com/mozilla/treeherder), [mozilla/mozilla_ci_tools](https://github.com/mozilla/mozilla_ci_tools)
* Other Contributions - [mozilla-b2g/gaia](https://github.com/mozilla-b2g/gaia/) (Firefox OS), [mozilla-bteam/bmo](https://github.com/mozilla-bteam/bmo) (Bugzilla), [rust-lang-nursery/rust-clippy](https://github.com/rust-lang-nursery/rust-clippy), [arslanbilal/git-cheat-sheet](https://github.com/arslanbilal/git-cheat-sheet), [servo/servo](https://github.com/servo/servo), [w3c/web-platform-tests](https://github.com/w3c/web-platform-tests), [sunpy/sunpy](https://github.com/sunpy/sunpy), [taskcluster/taskcluster-client](https://github.com/taskcluster/taskcluster-client.py/graphs/contributors), [saketkc/fos-proposals](https://github.com/saketkc/fos-proposals), [mozilla/geckodriver](https://github.com/mozilla/geckodriver), [mozilla/pulse_actions](https://github.com/mozilla/pulse_actions)


#### **Indian Language Datasets**

As a part of my RnD project at [IIT Bombay](http://www.iitb.ac.in/), I am releasing the dataset used to train my neural network language models. These have been mined from Wikipedia and I hope this will help further research in language modelling for Indian morphologically rich languages. The folder also contains the original PTB dataset.

* Malayalam (denoted by `ml`)
* Tamil (denoted by `ta`)
* Kannada (denoted by `kn`)
* Telugu (denoted by `te`)
* Hindi (denoted by `hi`)
* PTB (denoted by `ptb`)

All these datasets are compatible with [SRILM](http://www.speech.sri.com/projects/srilm/). Files marked with `unk` have replaced all singletons with `<unk>` tokens. Files marked with `char` are character versions. All datasets have a `train`, `valid` and `test` file. You will find the dataset [here](https://drive.google.com/file/d/0B5Y_SiDYwIObaE52dmZ0YVFXckU/view?usp=sharing).

### **Alternate PDF versions of papers**

RELiC paper: [paper](https://martiansideofthemoon.github.io/assets/relic_paper_gse.pdf)  
RankGen paper: [paper](https://martiansideofthemoon.github.io/assets/rankgen_paper_gse.pdf)  