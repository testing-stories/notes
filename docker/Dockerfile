FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y curl \
  git \
  python3 \
  python3-pip

#Python requirements:
COPY requirements.txt /tmp/
RUN pip3 install --requirement /tmp/requirements.txt

#User:
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1001 ubuntu
USER ubuntu
WORKDIR /home/ubuntu

#Copy test content:
#COPY work/* /home/ubuntu/
RUN chown root:ubuntu /home/ubuntu
