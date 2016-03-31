FROM ubuntu:14.04
MAINTAINER "Ryuta Koide"

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y python python-pip python-dev

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

EXPOSE 5000

CMD ["/bin/bash", "-c", "tail -f /dev/null"]
