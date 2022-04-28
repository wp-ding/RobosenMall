
from django.db import models


class Discount(models.Model):
    PRICE = 1
    PERCENTAGE = 2

    code = models.CharField(max_length=8, null=True)
    title = models.CharField(max_length=64)
    amount = models.BigIntegerField(null=True)
    threshold = models.BigIntegerField(default=0)
    type = models.IntegerField(default=PRICE)
    expiration = models.DateField(null=True)
    closed = models.BooleanField(default=False)
    auto = models.BooleanField(default=True)
    limit = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    creatorId = models.IntegerField(null=True)


class DiscountProduct(models.Model):
    discount = models.IntegerField(null=True)
    product = models.IntegerField(null=True)


class Coupon(models.Model):

    code = models.CharField(max_length=8, null=True)
    title = models.CharField(max_length=64)
    amount = models.BigIntegerField(null=True)
    threshold = models.BigIntegerField(default=0)
    expiration = models.DateField(null=True)
    closed = models.BooleanField(default=False)
    auto = models.BooleanField(default=True)
    limit = models.IntegerField(default=1)
    product = models.IntegerField(null=True)     # 为空全站
    created = models.DateTimeField(auto_now_add=True)
    creatorId = models.IntegerField(null=True)


class CouponRecord(models.Model):
    coupon = models.IntegerField(null=True)
    userId = models.IntegerField()
    amount = models.BigIntegerField()
    sum = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
