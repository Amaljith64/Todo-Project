import datetime

from django.db import models


# Create your models here.
class task(models.Model):
    def __str__(self):
        return self.name  # TO change name to added task

    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    date=models.DateField(default=datetime.date.today)

