---
layout: post
title:  "Model Extraction Attacks on BERT-based APIs"
date:   2020-02-10 09:00:55 +0530
tags: nlp research security model extraction stealing bert ML
image: http://martiansideofthemoon.github.io/assets/extraction_squad.png
---

### Overview

This blogpost summarizes the results in our ICLR 2020 paper "Thieves on Sesame Street! Model Extraction of BERT-based APIs". You can find the camera ready version of the paper [here](https://arxiv.org/abs/1910.12366) and the code to reproduce experiments [here](https://github.com/google-research/language/tree/master/language/bert_extraction).

**TL;DR**: It is possible to perform distillation on BERT-based downstream NLP models without any real training data, even with nonsensical randomly sampled sequences of tokens. Commercial NLP inference APIs based on deep-learning are at the risk of being stolen via this process of zero-shot distillation.

### What are model extraction attacks?

Let's say a company hosts a publicly accessible deep learning inference API (the **victim model**), possibly behind a pay-wall allowing users to query the API with any input of their choice. A model extraction attack happens when a malicious user tries to "reverse-engineer" this black-box victim model, attempting to reconstruct a local copy of the victim model. If reconstruction is successful, the attacker has effectively stolen intellectual property and need not pay for the original API. Moreover, this process can be used to [leak information](https://arxiv.org/pdf/1609.02943.pdf) about the original training data or [construct adversarial examples](https://arxiv.org/abs/1602.02697) which work on the victim model.

The most popular approach to carry out this attack is via distillation. First, the attacker sends a large number of queries to the API and collects the outputs received. Then, the attacker uses these query-output pairs as training data to train their local copy of the model. This process is illustrated on a BERT-based SQuAD question answering model below.

![extraction_squad]({{ site.url }}/assets/extraction_squad.png)

There are three important differences when comparing this process to distillation.

1. **Training Data** - Distillation usually assumes access to the original training dataset. In model extraction settings the training data is generally unknown to the attacker.
2. **Access to Victim Model** - Distillation assumes (and often leverages) full white-box access to the internals of the model. On the other hand, model extraction has only black-box access to the victim model with only the output labels and/or the model’s confidence scores.
3. **Goal** -  Distillation aims to transfers knowledge from a big model to a small model, but there is no such requirement in model extraction.

### How much do these attacks cost?

Commercial APIs tend to be cheap. Based on [cost estimates](https://cloud.google.com/products/calculator/) from Google Cloud APIs, it costs $62.35 to extract SST2; $430.56 to extract a speech recognition dataset of the size Switchboard; and $2000 to extract 1 million translation queries (each with 100 characters). Several APIs allow a limited number of free queries per IP address and it's possible to collect datasets for much lesser costs if data collection is distributed across IP addresses.

### What kind of attacks do we study in our paper?

In our paper we focus on modern transfer learning settings in NLP, where the victim model is assumed to be a BERT-based classifier or question answering model. We assume that the attacker also has access to freely availablel large pretrained language models, but the attacker has no access to the original training data.

We use two strategies to construct attack queries. The first strategy (`RANDOM`) uses nonsensical, random sequences of tokens sampled from Wikitext103's unigram distribution. The second strategy (`WIKI`) uses sentences / paragraphs from WikiText103. For tasks expecting a pair of inputs (MNLI, SQuAD), we use simple heuristics to construct the hypothesis (replace 3 words in premise with random words from Wikitext103) and question (sample words from the paragraph, prepend a Wh- word, append ? at the end) respectively. To get an idea of the kind of training data we used, look at the table below.

![extraction_dataset]({{ site.url }}/assets/extraction_dataset.png)

Our key finding is that model extraction attacks are surprisingly effective with our RANDOM strategy and improves with the WIKI strategy. For instance, the original BERT-large SQuAD model reaches a dev set performance of 90.6 F1. With our RANDOM strategy, we can reach up to 85.8 F1 without the model seeing a single grammatically valid paragraph or question during training. With our WIKI strategy, performance jumps to 89.4 F1 without seeing a single real training data point.

<style>
table {
	border-collapse: collapse;
    width:100%;
    border-spacing: 0;
    border: 1px solid;
    padding: 1px;
}
th{
    border:1px solid #000000;
    text-align: center;
}
td{
    border:1px solid;
    text-align: center;
}
</style>

|                     | Number of Queries | SST2 (%) | MNLI (%) | SQuAD (F1) |
|---------------------|-------------------|----------|----------|------------|
| API / Victim Model  | 1x                | 93.1     | 85.8     | 90.6       |
| `RANDOM`            | 1x                | 90.1     | 76.3     | 79.1       |
| `RANDOM`            | upto 10x          | 90.5     | 78.5     | 85.8       |
| `WIKI`              | 1x                | 91.4     | 77.8     | 86.1       |
| `WIKI`              | upto 10x          | 91.7     | 79.3     | 89.4       |

<br/>

### Did language model pre-training make model extraction easier?

Our results suggest that a pretrained model simplified the process of model extraction. QANet models (with full random initialization) is able to achieve 43.2 F1 and 54 F1 using our `RANDOM` and `WIKI` strategy, which is a significant drop in performance compared to distillation with the original training data (70.3 F1). In general we found that superior pretrained language models are more successful at model extraction controlling for the number of queries and the query strategy.

### Is there a strategy for intelligent selection of queries?

Are some `RANDOM` / `WIKI` queries better for model extraction than others? We briefly investigated this question and found an effective strategy to select a fraction of `RANDOM` / `WIKI` queries from a much larger pool. We trained multiple copies of the victim model (each on a different random seed). We found that queries which tend to have high agreement between the different victim models are better for model extraction. This finding parallels [prior work](https://papers.nips.cc/paper/7219-simple-and-scalable-predictive-uncertainty-estimation-using-deep-ensembles.pdf) on out-of-distribution detection, which found that the confidence score of an ensemble of classifiers is much more effective in finding out-of-distribution inputs compared to a single over-confident classifier.

These results suggest that the closeness of the queries to the original training data's input distribution is an important factor in determining the effectiveness of distillation or model extraction.

### Is it possible to defend APIs against model extraction?

We investigated two strategies to defend APIs against model extraction --- 1) membership classification 2) API watermarking. While both defenses were effective to some degree, they work only in limited settings --- sophisticated adversaries might anticipate these defenses and develop simple modifications to their attacks to circumvent these defenses. Defense against model extraction is a tricky open problem, since an ideal defense should not only preserve API utility but also be undetectable to an attacker.

### Conclusions & Future Work

In this work we studied model extraction attacks in natural language processing. The attacks we discussed were quite simple and should be treated as lower bounds to more sophisticated attacks leveraging active learning. We hope that this work highlights the dangers of model extraction and fuels research in the development of defense mechanisms which slow down or prevent model extraction.

Besides work on attack-defense mechanisms, we see two other avenues for research building on this body of work.

1) **Improving Distillation** - Since distillation is possible with random sequences of tokens, this might be a good way to perform distillation in low-resource NLP settings where the original training data is not available. Random sequences (perhaps with the intelligent data selection strategy) could also be used to augment real training data for distillation. It will be interesting to check whether random sequences can be leveraged to reduce the performance gap between the original and distilled models.

2) **Closeness of Input Distributions** - Model extraction might be a good way to understand the closeness between two input distributions, where one input distribution is used to extract a model trained on another input distribution. This technique could be used as a method to tackle an important open problem in NLP ("[What is a domain?](https://twitter.com/yoavgo/status/1205989007852810244)").

### Contact

This work was done by [Kalpesh Krishna](http://martiansideofthemoon.github.io/) (during an internship at [Google AI Language](https://research.google/teams/language/)), [Gaurav Singh Tomar](https://research.google/people/GauravSinghTomar/), [Ankur P. Parikh](https://research.google/people/104995/), [Nicolas Papernot](https://www.papernot.fr/) and [Mohit Iyyer](https://people.cs.umass.edu/~miyyer/). We are happy to get in touch and hear feedback / questions at [kalpesh@cs.umass.edu](mailto:kalpesh@cs.umass.edu)!
