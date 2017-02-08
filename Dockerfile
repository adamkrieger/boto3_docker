FROM python:2-alpine

WORKDIR /usr/src
COPY ./src /usr/src
VOLUME ["/usr/src"]

RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "list_buckets.py"]