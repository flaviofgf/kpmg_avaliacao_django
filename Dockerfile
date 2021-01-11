FROM python:3.7

ENV PYTHONUNBUFFERED=1
ENV JAVA_HOME='/usr/lib/jvm/default-java'

WORKDIR /code

RUN apt-get update
RUN apt-get install default-jdk -y

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/