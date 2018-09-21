FROM ubuntu

RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y ffmpeg && \
apt-get install -y python3.6 && \
apt-get install -y python-pip && \
apt-get install -y apache2 apache2-utils libexpat1 ssl-cert python && \
apt-get install -y libapache2-mod-wsgi && \
pip install flask && \
mkdir /var/www/prod && \
mkdir /var/www/log && \
echo "ServerName localhost" >> /etc/apache2/apache2.conf

COPY /code /var/www/prod/
COPY /conf /etc/apache2/conf-available/

RUN chmod +x /etc/apache2/conf-available/entrypoint.sh

ENTRYPOINT ["/etc/apache2/conf-available/entrypoint.sh"]

MAINTAINER Matheus Melo <matheus306@gmail.com>
