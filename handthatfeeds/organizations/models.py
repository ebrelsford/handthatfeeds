from django.db import models

from inplace.models import Place


class Organization(Place):
    email = models.EmailField(blank=True, null=True,)
    site_url = models.URLField(blank=True, null=True,)
    phone = models.CharField(max_length=15, blank=True, null=True,)
    mission = models.TextField(blank=True, null=True)
    sectors = models.ManyToManyField('Sector', blank=True, null=True,)
    types = models.ManyToManyField('Type', blank=True, null=True,)


class Sector(models.Model):
    name = models.CharField(max_length=50,)

    def __unicode__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=50,)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return self.name
