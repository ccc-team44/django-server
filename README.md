Just testing and play around with django + react

## Setup 
1. Active virtual env

2. Install requirements.txt

3. Run

## Environment Variables
make sure you have the following variables in your environment
```
COUCH_DB_USER
COUCH_DB_PASSWORD
COUCH_DB_ADDRESS
```
eg
```
PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=django_server.settings;COUCH_DB_USER=admin;COUCH_DB_PASSWORD=1111;COUCH_DB_ADDRESS=127.0.0.1:5984
```

## Structure
django_server is the main application 


## Add new application
1. ```django-admin startapp newapp```
2. update django_server/settings.py
```
   INSTALLED_APPS = [
    ...
    'newapp.apps.NewappConfig',
    ]
    
```
3. create models and migrations, profit


## Test 
Request a sample json data for react to plot
- GET ``/snippets/1``
