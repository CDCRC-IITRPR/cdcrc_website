from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    email=models.EmailField()
    website = models.URLField(max_length=200,null=True)
    address = models.TextField(null=True)
    logo = models.ImageField(default='someDefault.png',blank=True)
    organisation_type_choices = [
        ('Private Sector','Private Sector'),
        ('Start-up','Start-up'),
        ('Government','Government'),
        ('Public Sector','Public Sector'),
        ('MNC (Indian origin)','MNC (Indian origin)'),
        ('MNC (Foreign origin)','MNC (Foreign origin)'),
        ('Others','Others'),
    ]
    organisation_type = models.CharField(max_length=40, choices= organisation_type_choices)

    def __str__(self):
        return self.name

