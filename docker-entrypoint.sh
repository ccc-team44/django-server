#!/bin/bash
export COUCH_DB_USER=${COUCH_DB_USER}
export COUCH_DB_PASSWORD=${COUCH_DB_PASSWORD}
export COUCH_DB_ADDRESS=${COUCH_DB_ADDRESS}
exec python3 manage.py runserver 8001