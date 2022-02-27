from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Days(models.Model):
    day_id = models.AutoField(primary_key=True, blank=True)
    user_id = models.IntegerField()
    timestamp = models.TextField()
    consumption = models.IntegerField()
    temperature = models.IntegerField()


class Months(models.Model):
    month_id = models.AutoField(primary_key=True, blank=True)
    user_id = models.IntegerField()
    timestamp = models.TextField()
    consumption = models.IntegerField()
    temperature = models.IntegerField()

