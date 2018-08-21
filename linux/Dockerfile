FROM debian

MAINTAINER Matheus Melo <matheus306@gmail.com>

RUN apt-get update && apt-get install -y apache2 && apt-get clean

ENV APACHE_LOCK_DIR="/var/lock"
ENV APACHE_PID_FILE="/var/run/apache2.pid"
ENV APACHE_RUN_USER="www-data"
ENV APACHE_RUN_GROUP="www-data"
ENV APACHE_LOG_DIR="/var/log/apache2"

LABEL Description="Apache WebService - Debian"

EXPOSE 80

ADD http://www.proredetelecom.com.br/docker/logo.jpg /var/www/html/
ADD http://www.proredetelecom.com.br/docker/index.html /var/www/html/
ADD http://www.proredetelecom.com.br/docker/styles.css /var/www/html/
ADD https://www.google.com.br/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png /var/www/html/

RUN chown -R www-data: /var/www/html/.
CMD /etc/init.d/apache2 start && /bin/bash