from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
