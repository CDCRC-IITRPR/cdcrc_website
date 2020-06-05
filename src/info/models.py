from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created=models.DateField(auto_now_add=True)
    brief=models.CharField(max_length=150)

class Events(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created=models.DateField(auto_now_add=True)
    brief=models.CharField(max_length=150)