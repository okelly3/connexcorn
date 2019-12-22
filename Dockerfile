FROM python:3.6-slim-buster
MAINTAINER Ofir Kelly (okelly3@gmail.com)

COPY . /
WORKDIR /

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#CMD ["gunicorn"  , "-b", "0.0.0.0:9090", "hello"]
CMD ["gunicorn"  , "-b", "0.0.0.0:9090", "-w", "4", "hello"]