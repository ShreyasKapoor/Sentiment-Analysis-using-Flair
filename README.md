# Sentiment Analysis Using Flair
Sentiment-analysis-as-a-service (SAaaS)
## Overview
In this project, I've created a kubernetes cluster that provides a REST API for sentiment analysis on sentences and records them in a database.


### Sentiment Analysis
The worker uses [open source sentiment analysis](https://github.com/flairNLP/flair) software. Our reason for turning this into a micro-service is because it takes a long time to load the sentiment analysis model.

