from django.db import models
from datetime import date
from django.contrib.auth.models import User
from utils.validators import validate_file_extension, validate_file_size
class News(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(blank=True, null=True)
    brief = models.TextField( blank=True, null=True)
    url=models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Events(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    body = models.TextField(blank=True, null=True)
    brief=models.TextField( null=True, blank=True)
    venue=models.CharField(max_length=100,blank = True,null=True)
    date = models.DateField(default=date.today)
    url=models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title 


class ResourceCategory(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class Resource(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    categories = models.ManyToManyField(ResourceCategory, related_name='resources')
    url = models.URLField(null=True, blank=True)
    brief = models.CharField(max_length=2000)
    detail = models.TextField(default='DEFAULT VALUE')
    datetime = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ResourceImage(models.Model):
    image = models.ImageField(upload_to='resources/images/')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, related_name='images', validators=[validate_file_extension, validate_file_size])

    def __str__(self):
        return str(self.file)

class Department(models.Model):
    name = models.CharField(max_length=256, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

class ProfessionalDevelopmentActivity(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    brief = models.TextField(null=False, blank=False)
    detail = models.TextField(null=True, blank=True)
    photo = models.ImageField()
    date = models.DateField()

    def __str__(self):
        return self.title

class ProfessionalDevelopmentBook(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=256)
    writer = models.CharField(max_length=100)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class ProfessionalDevelopmentVideo(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default='')
    youtube_embed_url = models.CharField(max_length=200, null=False, blank=False, default='')

    def __str__(self):
        return self.title

class CorporateRelationsActivity(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    brief = models.TextField(null=False, blank=False)
    detail = models.TextField(null=True, blank=True)
    photo = models.ImageField()
    date = models.DateField()

    def __str__(self):
        return self.title

class ProfessionalDevelopmentInitiatives(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    brief = models.TextField(null=False, blank=False)
    detail = models.TextField(null=True, blank=True)
    photo = models.ImageField()
    date = models.DateField()

    def __str__(self):
        return self.title