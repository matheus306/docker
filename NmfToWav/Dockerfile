FROM ubuntu

RUN apt-get update && \
apt-get install -y ffmpeg && \
apt-get install -y python3.6 && \
apt-get install -y python-pip && \
apt-get install -y libapache2-mod-wsgi python-dev && \
pip install flask

 
EXPOSE 5000

COPY /code /code
WORKDIR /code

CMD python app.py

MAINTAINER Matheus Melo <matheus306@gmail.com>
