#!/bin/bash

export PYTHONPATH="${PYTHONPATH}:/app/postorius_standalone:/app"
export DJANGO_SETTINGS_MODULE='settings_local'


start (){
    python /app/postorius_standalone/manage.py migrate --noinput
    python /app/postorius_standalone/manage.py collectstatic --noinput
    python /app/create_admin.py

    uwsgi --ini /app/app.ini --logto /app/app.log  &
    tail -f /var/log/nginx/error.log & 
    tail -f /var/log/nginx/access.log & 
    nginx
}

stop (){
    killall uwsgi
    killall nginx
}

trap stop SIGINT SIGKILL SIGTERM

start
