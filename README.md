# API server for Android and sensors app

Simple API rest for Sensors project using django and django-rest-api

## Installation

just run:

```bash
pip install -r requirements.txt
```

## First time Run project

follow next commands:

```bash
python manage.py migrate
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: whateverYouWant
Password (again): whateverYouWantAgain
Superuser created successfully.
```

and continue with steps in Run Project.


## Run project

just:

```bash
python manage runserver
```

by default project will server at http://127.0.0.1:8000/

## urls

availables urls:

    admin/
    ^api-auth/
    ^users/$ [name='user-list']
    ^users\.(?P<format>[a-z0-9]+)/?$ [name='user-list']
    ^users/(?P<pk>[^/.]+)/$ [name='user-detail']
    ^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='user-detail']
    ^groups/$ [name='group-list']
    ^groups\.(?P<format>[a-z0-9]+)/?$ [name='group-list']
    ^groups/(?P<pk>[^/.]+)/$ [name='group-detail']
    ^groups/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='group-detail']
    ^novelties/$ [name='novelty-list']
    ^novelties\.(?P<format>[a-z0-9]+)/?$ [name='novelty-list']
    ^novelties/(?P<pk>[^/.]+)/$ [name='novelty-detail']
    ^novelties/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='novelty-detail']
    ^nodes/$ [name='node-list']
    ^nodes\.(?P<format>[a-z0-9]+)/?$ [name='node-list']
    ^nodes/(?P<pk>[^/.]+)/$ [name='node-detail']
    ^nodes/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='node-detail']
    ^locations/$ [name='location-list']
    ^locations\.(?P<format>[a-z0-9]+)/?$ [name='location-list']
    ^locations/(?P<pk>[^/.]+)/$ [name='location-detail']
    ^locations/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='location-detail']
    ^$ [name='api-root']
    ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']

## API login

To get a valid token, you should make a post to http://127.0.0.1:8000/api-token-auth/ providing a valid username and password. the response will be a JSON with the nex format:

{ 'token' : '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' }

this token value will be used to validate access to the API. Next request should have Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b in header.

