FROM python:2-alpine

WORKDIR /usr/src
COPY ./requirements.txt /usr/src/
VOLUME ["/usr/src"]

RUN ["pip", "install", "-r", "requirements.txt"]
