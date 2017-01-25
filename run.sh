#!/bin/bash

export PYTHONPATH="${PYTHONPATH}:/app/postorius_standalone:/app"
export DJANGO_SETTINGS_MODULE='settings_local'


python /app/postorius_standalone/manage.py migrate --noinput
python /app/postorius_standalone/manage.py collectstatic --noinput
python /app/create_admin.py
chown app:app -R ${DATADIR}

/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
