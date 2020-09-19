from django.db import models
from django.contrib.auth.models import User
from info.models import Department
# Create your models here.

class Recruiter(models.Model):
    name = models.CharField(max_length=256, unique=True)
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
    remark = models.TextField(default='', blank=True, null=True)
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

class StudentDemographic(models.Model):
    category_choices = [
        ('ugp', 'UG for Placement'),
        ('pgp', 'PG for Placement'),
        ('ugi', 'UG for Internships'),
        ('pgi', 'PG for Internships'), 
    ]
    category = models.CharField(max_length=10, null=False, choices=category_choices)
    department = models.ForeignKey(Department, null=False, blank=False, on_delete=models.CASCADE)
    strength = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.category + " " + str(self.department)

    def get_category_display(self):
        return dict(self.category_choices)[self.category]
    def get_department_display(self):
        return str(self.department)

