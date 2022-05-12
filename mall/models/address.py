
from django.db import models


class Address(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=20, null=True)
    receiver = models.CharField(max_length=20)
    province = models.BigIntegerField(null=True, max_length=12)
    city = models.BigIntegerField(null=True, max_length=12)
    district = models.BigIntegerField(null=True, max_length=12)
    place = models.CharField(max_length=64, null=True)
    mobile = models.CharField(max_length=11, null=True)
    tel = models.CharField(max_length=20, null=True)
    isDefault = models.BooleanField(default=False)
    inactive = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


class Area(models.Model):
    code = models.BigIntegerField(default=None, max_length=12)
    parent_id = models.BigIntegerField(default=None, max_length=12)
    name = models.CharField(default=None, max_length=40)
    level_id = models.CharField(default=None, max_length=40)



