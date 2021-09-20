FROM python:3.8-slim

WORKDIR /usr/src/project

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY ./requirements/dev.txt ./requirements.txt
COPY ./project .

RUN pip install --upgrade pip --no-cache && \
    pip install -r requirements.txt --no-cache