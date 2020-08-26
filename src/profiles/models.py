from django.db import models
from django.contrib.auth.models import User
from utils.validators import validate_file_size, validate_file_extension
# Create your models here.
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    entry_number = models.CharField(max_length=12, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    graduating_year = models.IntegerField(null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class TeamMemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team_profile')
    level = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    domain_choices = [
        ('sde', 'Software Development'),
        ('core', 'Core'),
        ('non-core', 'Non Core'),
        ('general', 'General')
    ]
    domain = models.CharField(max_length=32, choices=domain_choices, null=True, blank=True)
    category_choices = [
        ('pg', 'Post Graduate'),
        ('ug', 'Under Graduate'),
        ('staff', 'Staff'),
        ('faculty', 'Faculty'),
    ]
    category = models.CharField(max_length=32, choices=category_choices, null=True, blank=True)
    designation = models.CharField(max_length=64, null=True, blank=True)
    photo = models.ImageField(blank=True, null=True, validators=[validate_file_size, validate_file_extension])
    visible = models.BooleanField(default=False)
    linkedin_profile = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
    
    
    