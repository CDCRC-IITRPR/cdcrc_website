from django.db import models
from datetime import date

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(blank=True, null=True)
    brief = models.CharField(max_length=150, blank=True, null=True)
    url=models.URLField(null=True, blank=True)

class Events(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(blank=True, null=True)
    brief=models.CharField(max_length=100, null=True, blank=True)
    venue=models.CharField(max_length=100,blank = True,null=True)
    date = models.DateField(default=date.today)
    url=models.URLField(null=True, blank=True)