FROM python:3.12
LABEL authors="danilsmorckov"

COPY data_loader.py requirements.txt /workdir/
WORKDIR /workdir

RUN pip install -r requirements.txt
