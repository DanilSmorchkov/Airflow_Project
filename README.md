# Airflow Example Pipeline for Machine Learning (Local Development)

This repository provides an example Apache Airflow pipeline for local development of machine learning projects. The pipeline demonstrates how to fetch news articles from an open data source and apply a zero-shot classification NLP model to classify them into predefined categories.

## Overview:
Most of this material is taken from an article on [Habr](https://habr.com/ru/amp/publications/737046/). \
In this case, we use Apache Airflow to automate the following steps:

1. Data Loader: The pipeline returns news articles from an open source and prepares them for further processing.

2. Text Classification: We use a pre-trained NLP model for zero-shot classification to assign relevant categories to the news articles.
This model can classify text into various categories without prior training on specific datasets.

3. Result Aggregation: This task focuses on aggregating the classified data.

## Usage:
To use this pipeline for local development, follow the steps below:
1. Check that Docker Engine has sufficient memory allocated.
2. Before the first Airflow run, prepare your environment:
- if you are working on Linux, specify the AIRFLOW_UID by running the command:
```zsh
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
- Perform the database migration and create the initial user account:
```zsh
 docker compose up airflow-init
```
The created user account will have the login airflow and the password `airflow`.
3. Start Airflow and build custom images to run tasks in Docker-containers:
```zsh
docker compose up --build
```
4. Access the Airflow web interface in your browser at http://localhost:8080.
5. Trigger the DAG financial_news to initiate the pipeline execution.
6. When you are finished working and want to clean up your environment, run:
```zsh
docker compose down --volume --rmi all
```
