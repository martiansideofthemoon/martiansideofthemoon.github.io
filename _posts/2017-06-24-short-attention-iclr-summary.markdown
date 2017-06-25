---
layout: post
title:  "Frustratingly Short Attention Spans in NLM (ICLR 2017) - A Summary"
date:   2017-05-28 10:00:55 +0530
tags: internship ttic
---

Through this blogpost I attempt to summarise the key ideas highlighted in an [ICLR-2017](http://www.iclr.cc/doku.php?id=ICLR2017:main&redirect=1) accepted paper, Frustratingly Short Attention Spans in Neural Language Modelling, (read it [here](https://arxiv.org/abs/1702.04521)), by [Daniluk](https://www.linkedin.com/in/michaldaniluk91/?ppe=1) et al, of the University College London. You can read the official ICLR reviews on [OpenReview](https://openreview.net/forum?id=ByIAPUcee).

# Motivation

This paper is primarily motivated by the shortcomings of the traditional attention mechanism proposed in the [Bahdanau et al.](https://arxiv.org/pdf/1409.0473.pdf) ICLR-2015 paper. It tries to improve the traditional attention mechanism with a couple of improved and more meaningful models in the context of [language modelling](https://en.wikipedia.org/wiki/Language_model).  While implementing their new architecture, the authors notice a strange trend in the lengths of the attention spans (and hence the title) which motivates them to build a simple novel architecture, the "N-Gram Recurrent Neural Network", which achieves comparable performance to the more complicated attention models.

Hence, this paper ends by questioning the usefulness of complicated attention models, and tries to highlight that today's state-of-the-art architectures suffer from a long term dependency issue.

