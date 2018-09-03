FROM ubuntu

RUN apt-get update \
&& apt-get install -y python \
&& apt-get install -y python-setuptools \
&& apt-get install -y python-pip

CMD [ "pip", "pip install -U flask-cors" ]
CMD [ "pip", "./app.py" ]

MAINTAINER Matheus Melo <matheus306@gmail.com>
