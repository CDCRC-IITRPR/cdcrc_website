from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length = 30)
    designation = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length = 30)

