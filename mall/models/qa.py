
from django.db import models


class QA(models.Model):
    question           = models.CharField(max_length=256)
    answer             = models.TextField(null=True)
    inactive           = models.BooleanField(default=False)
    creatorId          = models.IntegerField(null=True)
    created            = models.DateTimeField(auto_now_add=True)