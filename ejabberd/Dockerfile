FROM ubuntu

COPY ./init.sh /home

RUN apt-get update && \
    apt-get install -y ejabberd && \
    apt-get install -y wget && \
    apt-get install -y git && \
    apt-get install -y make && \
    apt-get install -y gcc && \
    apt-get install -y libexpat1-dev && \
    apt-get install -y libyaml-dev && \
    apt-get install -y automake && \
    apt-get install -y libssl-dev && \
    apt-get install -y erlang && \
    apt-get install -y build-essential && \
    apt-get install -y libncurses5-dev && \
    apt-get install -y openssl && \
    apt-get install -y zlib1g-dev && \
    apt-get install -y libgd-dev && \
    apt-get install -y libwebp-dev && \
    apt-get install -y fop && \
    apt-get install -y xsltproc && \
    apt-get install -y unixodbc-dev && \
    cd /opt && \
    wget -O ejab.tgz https://www.process-one.net/downloads/downloads-action.php?file=/ejabberd/18.01/ejabberd-18.01.tgz && \
    tar -xvzf ejab.tgz && \
    cd ejabberd-18.01/ && \
    ./configure --enable-mysql && \
    make && \
    make install && \
    sh /home/init.sh


