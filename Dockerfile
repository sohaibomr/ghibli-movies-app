FROM python:3.7-slim-buster

RUN mkdir /movies-server

WORKDIR /movies-server

# first, copy module requirements and install so that code changes do not affect the cache of this layer
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY app app

COPY templates templates

RUN ls

ENTRYPOINT uvicorn app.server:APP --host 127.0.0.1