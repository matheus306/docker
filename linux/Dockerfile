FROM debian

RUN apt-get update \
&& apt-get -y upgrade \
&& apt-get install -y xfce4 \
&& apt-get install -y xfce4-goodies \
&& apt-get install -y gnome-icon-theme \
&& apt-get install -y tightvncserver \
&& apt-get install -y iceweasel \ 
&& chmod 640 /etc/shadow \ 
&& useradd -ms /bin/bash vnc \ 
&& apt-get install sudo \
&& gpasswd -a vnc sudo


MAINTAINER Matheus Melo <matheus306@gmail.com>