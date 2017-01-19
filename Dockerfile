FROM ubuntu:xenial

MAINTAINER Marcin Matląg <marcin.matlag@gmail.com>

ENV APPHOME /app
ENV DATADIR /data

ARG user=app
ARG group=app
ARG uid=999
ARG gid=999

RUN groupadd -g ${gid} ${group} \
    && useradd -d "${APPHOME}" -u ${uid} -g ${gid} -m -s /bin/bash ${user}

RUN apt-get update;  apt-get --no-install-recommends -y install nginx  bzr uwsgi uwsgi-plugin-python python-pip python-setuptools supervisor

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR ${APPHOME}
RUN bzr branch --revision=14 lp:~mailman-coders/postorius/postorius_standalone 

RUN mkdir ${DATADIR}
COPY settings_local.py /app
COPY create_admin.py /app
COPY postorius_app.wsgi /app

COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY nginx_supervisord.conf /etc/supervisor/conf.d/
COPY postorius_supervisord.conf /etc/supervisor/conf.d/


COPY run.sh /
COPY app.ini /app/
RUN chmod 750 /run.sh 
RUN chown ${user}:${group} /run.sh
RUN chown -R ${user}:${group} /var/lib/nginx/ /var/log/nginx 

RUN chown -R ${user}:${group} . /data
USER ${user}

COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8000

CMD /run.sh

