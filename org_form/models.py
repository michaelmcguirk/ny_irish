# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your databa
from __future__ import unicode_literals

from django.db import models
from cms.models.pluginmodel import CMSPlugin

class Organisation(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    address_3 = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True)
    contact_no = models.CharField(max_length=100, null=True)

    def __unicode__(self):
       return self.name

class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')

class zz_Organisation(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    address_3 = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    org_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True)
    contact_no = models.CharField(max_length=100, null=True)

class OrgPluginModel(CMSPlugin):
    Organisation = models.ForeignKey(Organisation)

    def __unicode__(self):
        return self.Organisation.name
