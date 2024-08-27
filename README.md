# Airflow Example Pipeline for Machine Learning (Local Development)

This repository provides an example Apache Airflow pipeline for local development of machine learning projects. The pipeline demonstrates how to fetch news articles from an open data source and apply a zero-shot classification NLP model to classify them into predefined categories.

## Overview:
Most of this material is taken from an article on [Habr](https://habr.com/ru/amp/publications/737046/). \
In this case, we use Apache Airflow to automate the following steps:

1. Data Loader: The pipeline returns news articles from an open source and prepares them for further processing.

2. Text Classification: We use a pre-trained NLP model for zero-shot classification to assign relevant categories to the news articles.
This model can classify text into various categories without prior training on specific datasets.

3. Result Aggregation: This task focuses on aggregating the classified data.


