![](UTA-DataScience-Logo.png)

# Tabular Playground Series - Apr 2022

* **One Sentence Summary** Ex: This repository holds an attempt to apply LSTMs to arbitrary action time series data from
Tabular Playground Series - Apr 2022 challenge on Kaggle. (https://www.kaggle.com/competitions/tabular-playground-series-apr-2022)


## Overview

  * **Definition of the tasks / challenge**  The task, as defined by the Kaggle challenge is to use a time series of 12 features, in time steps of 1 sec. for a overall total sequence of 1 minute to predict the action that best fits that sequence. The classification problem is rather arbitrary in discussing the actual actions thus we name them action 0 and action 1. The goal is to provide the best possible area under the curve for the ROC curve.
  * **Your approach** The approach in this repository formulates the problem as classification task, using deep recurrent neural networks as the model with the full time series of features as input. The goal is to use LSTM to allow us to create an accurate model with the use of dropoff to achieve the best metric.
  * **Summary of the performance achieved** Ex: Our best model was able to predict the next day stock price within 23%, 90% of the time. At the time of writing, the best performance on Kaggle of this metric is 18%.

## Summary of Workdone

### Data

* Data:
  * Type: 
    * Input: CSV file of 12 features, output: 0 or 1 for the sequence state.
  * The training set: Comprising ~26,000 60-second recordings of thirteen biological sensors for almost one thousand experimental participants.
  * The test set: For each of the ~12,000 sequences, you should predict a value for that sequence's state
 
#### Preprocessing / Clean up

* The only preprocessing needed was to format the data that would allow it to be processed by the LSTM layer. THe data has a row for each time step and each time step has 12 features thus with the 60 time steps per sequence. We end up with a sample of 720 variables.

#### Data Visualization

Show a few visualization of the data and say a few words about what you see.

### Problem Formulation

* Define:
  * Input / Output: 
  * Models
    * The only model that I tried this round was the LSTM model under the RNN. The reason I used this model is because LSTM is good at being able to lear and remember over long sequences of input data. The model learns to extract features from sequences of observations and how to map the internal features to different action types. Also with the added benefit of not needing to engineer extra features.
  * Loss, Optimizer, other Hyperparameters.

### Training

* Describe the training:
  * How you trained: software and hardware.
  * How did training take.
  * Training curves (loss vs epoch for test/train).
  * How did you decide to stop training.
  * Any difficulties? How did you resolve them?

### Performance Comparison

* The performance metric that we are going to be using is the Area under the ROC curve.
* Show/compare results in one table.
* Show one (or few) visualization(s) of results, for example ROC curves.

### Conclusions

* State any conclusions you can infer from your work. Example: LSTM work better than GRU.

### Future Work

* The next next thing that I would love to try is using a CNN to handle classification of time series data.
* What are some other studies that can be done starting from here.

## How to reproduce results

* In this section, provide instructions at least one of the following:
   * Reproduce your results fully, including training.
   * Apply this package to other data. For example, how to use the model you trained.
   * Use this package to perform their own study.
* Also describe what resources to use for this package, if appropirate. For example, point them to Collab and TPUs.

### Overview of files in repository

* Kaggle Competition: This is the journal used to both train the model and run the evaluation of the metrics. Lastly also to take a small look at some visuals.

### Software Setup
* The only software required to perform a similar task would be to install matplotlib, numpy, keras, and tensorflow onto python.
* All these packages and documentation can be found on their own websites.
* These packages can be downloaded through the terminal with pip3 install "package"

### Data

* The data used in this project can be found on the Kaggle competition site. (https://www.kaggle.com/competitions/tabular-playground-series-apr-2022/data)

### Training

* Describe how to train the model

#### Performance Evaluation

* Describe how to run the performance evaluation.








