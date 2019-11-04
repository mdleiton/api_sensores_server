#!/bin/bash
sleep 30
source env/bin/activate
python manage.py runserver 10.42.0.1:8081 &
