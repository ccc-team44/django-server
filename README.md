Just testing and play around with django + react

## Setup 
1. Active virtual env

2. Install requirements.txt

3. Run

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
- GET ``http://127.0.0.1:8001/snippets/1``
