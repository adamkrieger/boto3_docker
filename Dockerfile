FROM python:2-alpine

ENV PATH /usr/src:$PATH
COPY ./src /usr/src

WORKDIR /usr/vol
VOLUME ["/usr/vol"]

RUN ["pip", "install", "-r", "/usr/src/requirements.txt"]

CMD ["python", "list_buckets.py"]