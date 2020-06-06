from django.db import models
from datetime import date

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    brief=models.CharField(max_length=150)
    url=models.URLField(null=True)

class Events(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    brief=models.CharField(max_length=150)
    venue=models.CharField(max_length=50,blank = True,null=True)
    date = models.DateField(default=date.today)
    url=models.URLField(null=True)