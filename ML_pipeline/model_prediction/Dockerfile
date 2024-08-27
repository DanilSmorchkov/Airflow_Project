FROM python:3.12
LABEL authors="danilsmorckov"

COPY requirements.txt model_predict.py /workdir/
WORKDIR /workdir

RUN pip install -r requirements.txt