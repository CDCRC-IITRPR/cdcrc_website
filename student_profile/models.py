from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 30)
    phone = models.CharField(max_length = 10)
    branch = models.CharField(max_length = 50)
    email =  models.CharField(max_length = 40)
    course =  models.CharField(max_length = 10)
    year =  models.CharField(max_length = 1)