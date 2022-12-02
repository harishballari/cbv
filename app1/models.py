from django.db import models

# Create your models here.

class Course(models.Model):
    cname = models.CharField(max_length=40)
    dur = models.IntegerField()
    fee = models.IntegerField()

    