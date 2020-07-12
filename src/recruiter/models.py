from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recruiter(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email=models.EmailField(null=True, blank=True)
    website = models.URLField(max_length=200,null=True)
    address = models.TextField(null=True)
    logo = models.ImageField(blank=True, null=True)
    domain_choices = [
        ('sde','SDE'),
        ('core','Core'),
        ('non_core','Non Core'),
    ]
    domain = models.CharField(max_length=40, choices=domain_choices, null=True, blank=True)
    visible = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class JAF(models.Model):
    recruiter = models.ForeignKey(Recruiter, null=True,  on_delete=models.SET_NULL) #TODO: check the on delete rule here later
    mongo_id = models.CharField(max_length=1000, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + " " +self.recruiter.name

class INF(models.Model):
    recruiter = models.ForeignKey(Recruiter, null=True,  on_delete=models.SET_NULL) #TODO: check the on delete rule here later
    mongo_id = models.CharField(max_length=1000, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + " " +self.recruiter.name