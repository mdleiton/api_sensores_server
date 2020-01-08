from django.db import models

class Novelty(models.Model):
    date_time = models.DateTimeField()
    video = models.FileField('uploads/',null=True)
    node = models.ForeignKey(
            'Node',
            on_delete=models.PROTECT,
        )
    region = models.PositiveSmallIntegerField()

class Node(models.Model):
    location = models.ForeignKey(
            'Location',
            on_delete=models.PROTECT,
        )
    mac = models.CharField(max_length=20)
    users = models.ManyToManyField('auth.User')

class Location(models.Model):
    lat = models.DecimalField(max_digits=20, decimal_places=17)
    lon = models.DecimalField(max_digits=20, decimal_places=17)
    description = models.CharField(max_length=100)
