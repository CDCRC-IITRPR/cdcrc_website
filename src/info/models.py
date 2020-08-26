from django.db import models
from datetime import date
from utils.metadata import resource_category_choices

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


class Resource(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    category = models.CharField(max_length=256, choices=resource_category_choices, null = False, blank = False)
    url = models.URLField(null=True, blank=True)
    brief = models.TextField()

    def __str__(self):
        return self.title


class ProfessionalDevelopmentActivity(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    brief = models.TextField(null=False, blank=False)
    detail = models.TextField(null=False, blank=False)
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
    title = models.CharField(max_length=200, null=False, blank=False)
    youtube_embed_url = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.title

