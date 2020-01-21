import os
import sys
import django
import datetime
import json
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_server.settings')
django.setup()

from django.contrib.auth.models import User
from novelty.models import *

admin_1 = User.objects.create_superuser(username="admin1", password="adminadmin")
admin_1.save()

admin_2 = User.objects.create_superuser(username="admin2", password="adminadmin")
admin_2.save()

location_guayaquil = Location(lat=-2.203816, lon=-79.897453, description="Ubicación del nodo 1")
location_guayaquil.save()

location_quito = Location(lat=-0.180653, lon=-78.467834, description="Ubicación del nodo 2")
location_quito.save()

nodo_guayaquil = Node(location=location_guayaquil, mac=" 91:75:1a:ec:9a:c7")
nodo_guayaquil.save()
nodo_guayaquil.users.add(admin_1, admin_2)
nodo_guayaquil.save()

nodo_quito = Node(location=location_quito, mac=" 91:75:1a:ec:9a:c8")
nodo_quito.save()
nodo_quito.users.add(admin_1, admin_2)
nodo_quito.save()