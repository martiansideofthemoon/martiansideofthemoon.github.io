---
layout: post
title:  "ECG Analysis"
date:   2017-05-17 10:00:55 +0530
tags: ecg dsp
---

*(With inputs from [Karan Chadha](https://www.facebook.com/karanchadha005) and [Abhin Shah](https://www.facebook.com/profile.php?id=100006442563676))*.

Last semester, under the *Digital Signal Processing* course, we worked on an interesting application project. Our goal was to analyse ECG signals using DSP techniques and identify heart attacks (more precisely, Anterior [Myocardial Infractions](https://en.wikipedia.org/wiki/Myocardial_infarction)). We have hosted the project on [Github](https://github.com/martiansideofthemoon/ecg-analysis).

## Literature Survey

## Data Collection
Data was collected from a standard ECG analysis database called [Physikalisch-Technische Bundesanstalt (PTB)](https://www.physionet.org/physiobank/database/ptbdb/). We scraped Physionet using a python [script](https://github.com/martiansideofthemoon/ecg-analysis/blob/master/data/scrape.py). Each ECG waveform is accompanied with a header file with details on the diagnosis. We extracted all *Anterior Myocardial Infarction* cases in [`positive.txt`](https://github.com/martiansideofthemoon/ecg-analysis/blob/master/positive.txt) and healthy cases in [`control.txt`](https://github.com/martiansideofthemoon/ecg-analysis/blob/master/control.txt).

## Pre-Processing

## Extracting Coefficients

## Results
