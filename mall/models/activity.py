from django.db import models


class Activity(models.Model):
    title           = models.CharField(max_length=256)
    # content         = models.TextField(null=True)
    # coverImage      = models.CharField(max_length=256, null=True)
    # start           = models.DateTimeField(null=True)
    # end             = models.DateTimeField(null=True)
    # inactive        = models.BooleanField(default=False)
    # status          = models.BooleanField(default=False)
    # creatorId       = models.IntegerField(null=True)
    # created         = models.DateTimeField(auto_now_add=True, null=True)
