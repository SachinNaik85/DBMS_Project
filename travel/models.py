from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, primary_key = True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    phone = models.IntegerField
    password = models.CharField(max_length=20)