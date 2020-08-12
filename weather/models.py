from django.db import models


class City(models.Model):
    code = models.BigIntegerField(blank=False, null=False, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=2, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)

