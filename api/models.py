from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

    def __str__(self):
        return self.name


class Days(models.Model):
    day_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    consumption = models.IntegerField()
    temperature = models.IntegerField()

class Months(models.Model):
    month_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    consumption = models.IntegerField()
    temperature = models.IntegerField()

