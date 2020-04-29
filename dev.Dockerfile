FROM python:3.8-slim-buster

COPY requirements.txt /app/django-server/requirements.txt

WORKDIR /app/django-server

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        # default-libmysqlclient-dev \
        # gcc \
        # python3-dev \
        # mysql-client \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get purge -y \
        # gcc \
        # python3-dev \
    && apt-get autoremove --purge -y

EXPOSE 8000
