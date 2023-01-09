FROM ubuntu:20.04
MAINTAINER Francesco Andronico <andronico.francesco@gmail.com>
LABEL Description="Auto Installer" \
    License="Innonation"    \
    Usage="docker build -t pymap . && docker run -v path1:/tmp/pymap/report --name pymap pymap" \
    Version="0.1"

ENV TZ=Europe/Rome \
    DEBIAN_FRONTEND=noninteractive


#installo tutto
RUN apt-get update
RUN apt-get install -y \
              git \
              python3\
              python3-pip

RUN pip3 install \
    termcolor \
    pyfiglet \
    pygments \
    json2html


#creo la cartella report
RUN mkdir /tmp/inno

#copio main
COPY main.py /tmp/inno

#espongo il volume
VOLUME /tmp/inno





