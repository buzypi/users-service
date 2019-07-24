FROM ubuntu:18.04

RUN apt-get update \
  && apt-get -y install python3 python3-pip \
  && apt-get -y autoremove \
  && rm -rf /var/lib/apt/lists/*
