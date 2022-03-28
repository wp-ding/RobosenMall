from django.db import models


class COMPANY(models.Model):
    ID = models.IntegerField(
        primary_key=True,
    )
    NAME = models.TextField(
    )
    AGE = models.IntegerField(
    )
    ADDRESS = models.CharField(
        max_length=50
    )
    SALARY = models.FloatField(

    )
    class Meta:
        verbose_name = '测试表'
        verbose_name_plural = verbose_name
        db_table = 'COMPANY'