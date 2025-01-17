FROM python:3.8-slim-buster
WORKDIR /app/django-server

COPY requirements.txt /app/django-server/requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get purge -y \
    && apt-get autoremove --purge -y

COPY . /app/django-server

RUN chmod 755 /app/django-server/docker-entrypoint.sh

EXPOSE 8001
ENTRYPOINT ["/app/django-server/docker-entrypoint.sh"]