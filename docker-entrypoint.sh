#!/bin/bash
echo "${COUCH_DB_USER}" "${COUCH_DB_PASSWORD}" "${COUCH_DB_ADDRESS}"
export COUCH_DB_USER=${COUCH_DB_USER}
export COUCH_DB_PASSWORD=${COUCH_DB_PASSWORD}
export COUCH_DB_ADDRESS=${COUCH_DB_ADDRESS}
export PYTHONUNBUFFERED=1
export DJANGO_SETTINGS_MODULE=django_server.settings
exec python manage.py runserver 0.0.0.0:8001