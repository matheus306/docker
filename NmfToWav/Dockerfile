FROM ubuntu

RUN apt-get update && \
apt-get upgrade -y && \
apt-get install -y ffmpeg && \
apt-get install -y python3.6 && \
apt-get install -y python-pip && \
apt-get install -y apache2 apache2-utils libexpat1 ssl-cert python && \
apt-get install -y libapache2-mod-wsgi && \
pip install flask && \
mkdir /var/www/prod/ && \
mkdir /var/www/log && \
echo "ServerName localhost" >> /etc/apache2/apache2.conf

COPY /code /var/www/prod/
COPY /conf /etc/apache2/conf-available/

CMD a2enconf wsgi
CMD /etc/init.d/apache2 restart

MAINTAINER Matheus Melo <matheus306@gmail.com>
