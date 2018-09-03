FROM ubuntu

RUN apt-get update \
&& apt-get install -y python \
&& apt-get install -y python-setuptools \
&& apt-get install -y python-pip \
&& pip install flask \
&& pip install -U flask-cors


EXPOSE 5000

MAINTAINER Matheus Melo <matheus306@gmail.com>
