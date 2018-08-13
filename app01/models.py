from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    wx_id = models.CharField(max_length=32, null=True, blank=True)
