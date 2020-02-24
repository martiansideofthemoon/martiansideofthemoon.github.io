---
layout: post
title:  "Model Extraction Attacks on BERT-based APIs"
date:   2020-02-10 09:00:55 +0530
tags: nlp research security model extraction stealing bert ML
image: http://martiansideofthemoon.github.io/assets/toss/extraction_sst2.png
---

### Overview

**TL;DR**: It is possible to perform distillation on BERT-based downstream NLP models without any real training data, even with nonsensical randomly sampled sequences of tokens (for example, `to way train that like be`). Commercial NLP inference APIs based on deep-learning are at the risk of being stolen via this process of zero-shot distillation.

### What are model extraction attacks?

Let's say a company hosts a publicly accessible deep learning inference API (the **victim model**), possibly behind a pay-wall allowing users to query the API with any input of their choice. A model extraction attack happens when a malicious user tries to "reverse-engineer" this black-box victim model, attempting to reconstruct a local copy of the victim model. If reconstruction is successful, the attacker has effectively stolen intellectual property and need not pay for the original API. Moreover, this process can be used to [leak information](https://arxiv.org/pdf/1609.02943.pdf) about the original training data or [construct adversarial examples](https://arxiv.org/abs/1602.02697) which will force the victim model to make incorrect predictions.

The most popular approach to carry out this attack is via distillation. First, the attacker sends a large number of queries to the API and collects the outputs received. Then, the attacker uses these query-output pairs as training data to train their local copy of the model. This process is illustrated on a BERT-based sentiment classifier below.

<style>
.mySlides {display: none}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -22px;
  color: black;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
  color: #881c1c;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
  font-weight: bold;
}

/* Number text (1/3 etc) */
.numbertext {
  /*color: #f2f2f2;*/
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .prev, .next,.text {font-size: 11px}
}
</style>

<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 8</div>
  <img src="{{ site.url }}/assets/toss/toss_blog5.svg" style="width:100%">
  <div class="text">What are model extraction attacks? This slidedeck will walkthrough a typical model extraction pipeline.</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 8</div>
  <img src="{{ site.url }}/assets/toss/toss_blog1.svg" style="width:100%">
  <div class="text">A company trains a sentiment classifier based on <a href="https://arxiv.org/abs/1810.04805">BERT</a>.</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 8</div>
  <img src="{{ site.url }}/assets/toss/toss_blog2.svg" style="width:100%">
  <div class="text">The company releases their model as a black-box API --- users can query the model but cannot look at model internals or intermediate representations. We call this API the "victim model".</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">4 / 8</div>
  <img src="{{ site.url }}/assets/toss/toss_blog3.svg" style="width:100%">
  <div class="text">A malicious user generates a large number of queries. In this paper we study queries which are randomly sampled nonsensical sequences of tokens (as shown in the figure).</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">5 / 8</div>
  <img src="{{ site.url }}/assets/toss/toss_blog4.svg" style="width:100%">
  <div class="text">The malicious user sends their queries to the API and collects the outputs produced by the model. Note that full probability distributions across labels are not necessary for model extraction.</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">6 / 8</div>
  <img src="{{ site.url }}/assets/toss/toss_blog5.svg" style="width:100%">
  <div class="text">The model trains a new model (the "extracted model") from scratch using the queries as the training data input and the API's outputs as the training data labels.</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">7 / 8</div>
  <img src="{{ site.url }}/assets/toss/toss_blog6.svg" style="width:100%">
  <div class="text">The extracted model classifies sentiment correctly on real data. We show that performance of extracted models is close to the victim model's performance.</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">8 / 8</div>
  <img src="{{ site.url }}/assets/toss/extraction_squad.png" style="width:100%">
  <div class="text">The whole model extraction pipeline being applied to victim model trained on SQuAD. Note the nonsensical nature of the paragraphs and questions.</div>
</div>

<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
<a class="next" onclick="plusSlides(1)">&#10095;</a>

</div>

<div style="text-align:center">
  <span class="dot" onclick="currentSlide(1)"></span>
  <span class="dot" onclick="currentSlide(2)"></span>
  <span class="dot" onclick="currentSlide(3)"></span>
  <span class="dot" onclick="currentSlide(4)"></span>
  <span class="dot" onclick="currentSlide(5)"></span>
  <span class="dot" onclick="currentSlide(6)"></span>
  <span class="dot" onclick="currentSlide(7)"></span>
  <span class="dot" onclick="currentSlide(8)"></span>
</div>

<script>
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
</script>

<br />

There are three important differences when comparing this process to distillation.

1. **Training Data** - Distillation usually assumes access to the original training dataset or a different dataset sampled from a distribution similar to the original training data's distribution. In model extraction settings the training data is unknown to the attacker.
2. **Access to Victim Model** - In model extraction attackers have only black-box access to the victim model (only the output labels or confidence scores for a given query). While distillation is often performed with a similar assumption, [prior work](https://arxiv.org/abs/1412.6550) has shown that distillation can be improved by using intermediate hidden representations of the teacher (which requires white-box access to the victim model).
3. **Goal** -  Distillation aims to transfer knowledge from a big model to a small model, but there is no need for compression in model extraction.

### How much do these attacks cost?

**Commercial APIs tend to be cheap.** Based on [cost estimates](https://cloud.google.com/products/calculator/) from Google Cloud APIs, it costs $62.35 to extract [SST2](https://nlp.stanford.edu/sentiment/treebank.html); $430.56 to extract a speech recognition dataset of 300 hours of telephone transcripts (the size of [Switchboard](https://catalog.ldc.upenn.edu/LDC97S62)); and $2000 to extract 1 million translation queries (each with 100 characters). Several APIs allow a limited number of free queries per IP address and it's possible to collect datasets for much lesser costs if data collection is distributed across IP addresses. This is called a [Sybil attack](https://en.wikipedia.org/wiki/Sybil_attack).

### What kind of attacks do we study in our paper?

Modern natural language processing (NLP) systems are typically based on [BERT](https://arxiv.org/abs/1810.04805), a large [transformer](https://arxiv.org/abs/1706.03762) trained using a self-supervised objective on Wikipedia. BERT produces rich natural language representations which transfer well to most downstream NLP tasks (like question answering or sentiment analysis). Modern NLP systems typically add a few task-specific layers on top of the [publicly available BERT checkpoint](https://github.com/google-research/bert/) and finetune the whole model with a small learning rate.

In our paper we perform model extraction in this modern transfer-learning setting for NLP, where the victim model is assumed to be a BERT-based classifier or question answering model. We assume that the attacker also has access to freely available large pretrained language models, but the attacker has no access to the original training data.

We use two strategies to construct attack queries. The first strategy (`RANDOM`) uses nonsensical, random sequences of tokens sampled from [Wikitext103](https://www.salesforce.com/products/einstein/ai-research/the-wikitext-dependency-language-modeling-dataset/)'s unigram distribution. The second strategy (`WIKI`) uses sentences / paragraphs from WikiText103. For tasks expecting a pair of inputs (MNLI, SQuAD), we use simple heuristics to construct the hypothesis (replace 3 words in premise with random words from Wikitext103) and question (sample words from the paragraph, prepend a Wh- word, append ? at the end) respectively. To get an idea of the kind of training data we used, look at the table below.

![extraction_dataset]({{ site.url }}/assets/toss/extraction_dataset.png)

Our key finding is that model extraction attacks are surprisingly effective with our `RANDOM` strategy and improves with the `WIKI` strategy. For instance, the victim BERT-large SQuAD model reaches a dev set performance of 90.6 F1. With our `RANDOM` strategy, the model **reaches 85.8 F1 dev performance without seeing a single grammatically valid paragraph or question during training**. With our `WIKI` strategy, **performance jumps to 89.4 F1 without seeing a single real training data point**.

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

Our results suggest that attackers who fine-tune a pretrained language models get better extracted models. If instead attackers train [QANet](https://arxiv.org/abs/1804.09541) (with full random initialization), they only achieve 43.2 F1 and 54 F1 using our `RANDOM` and `WIKI` strategy respectively, which is a significant drop in performance compared to distillation with the original training data (70.3 F1). We also show that superior pretrained language models (like XLNet) are more successful at model extraction compared to BERT.

### Is there a strategy for intelligent selection of queries?

Are some `RANDOM` / `WIKI` queries better for model extraction than others? We briefly investigated this question and found an effective strategy to select a fraction of `RANDOM` / `WIKI` queries from a much larger pool. We trained multiple copies of the victim model (each on a different random seed). We found that **queries which tend to have high agreement between the different victim models' outputs are better for model extraction**. This finding parallels [prior work](https://papers.nips.cc/paper/7219-simple-and-scalable-predictive-uncertainty-estimation-using-deep-ensembles.pdf) on out-of-distribution detection, which found that the confidence score of an ensemble of classifiers is much more effective in finding out-of-distribution inputs compared to a single over-confident classifier.

These results suggest that the closeness of the queries to the original training data's input distribution is an important factor in determining the effectiveness of distillation or model extraction.

### Is it possible to defend APIs against model extraction?

We investigated two strategies to defend APIs against model extraction --- 1) membership classification 2) API watermarking. While **both defenses were effective to some degree, they work only in limited settings** --- sophisticated adversaries might anticipate these defenses and develop simple modifications to their attacks to circumvent these defenses. Defense against model extraction is a [tricky open problem](https://arxiv.org/pdf/1909.01838.pdf#section.8), since an ideal defense should not only preserve API utility but also be undetectable to an attacker.

### Conclusions & Future Work

In this work we studied model extraction attacks in natural language processing. The attacks we discussed were quite simple and should be treated as lower bounds to more [sophisticated attacks](https://arxiv.org/abs/1811.02054) leveraging active learning. We hope that this work highlights the need for more research in the development of defense mechanisms which make model extraction impractical.

Besides work on attack-defense mechanisms, we see two other avenues for research building on this body of work.

1) **Improving Distillation** - Since distillation is possible with random sequences of tokens, this might be a good way to perform distillation in low-resource NLP settings where the original training data is not available. Random sequences (perhaps with the intelligent data selection strategy) could also be used to augment real training data for distillation. It will be interesting to check whether random sequences can be leveraged to reduce the performance gap between the original and distilled models.

2) **Closeness of Input Distributions** - Model extraction might be a good way to understand the closeness between two input distributions, where one input distribution is used to extract a model trained on another input distribution. This technique could be used as a method to tackle an important open problem in NLP ("[What is a domain?](https://twitter.com/yoavgo/status/1205989007852810244)").

### Paper, Code & Contact Information

This blogpost summarizes the results in our ICLR 2020 paper "Thieves on Sesame Street! Model Extraction of BERT-based APIs". You can find the camera ready version of the paper [here](https://arxiv.org/abs/1910.12366) and the code to reproduce experiments [here](https://github.com/google-research/language/tree/master/language/bert_extraction).

This work was done by [Kalpesh Krishna](http://martiansideofthemoon.github.io/) (during an internship at [Google AI Language](https://research.google/teams/language/)), [Gaurav Singh Tomar](https://research.google/people/GauravSinghTomar/), [Ankur P. Parikh](https://research.google/people/104995/), [Nicolas Papernot](https://www.papernot.fr/) and [Mohit Iyyer](https://people.cs.umass.edu/~miyyer/). We thank Arka Sadhu, Bhanu Teja Gullapalli and Andrew Drozdov for useful feedback on the blogpost.

We are happy to get in touch and hear feedback / questions at [kalpesh@cs.umass.edu](mailto:kalpesh@cs.umass.edu)!
