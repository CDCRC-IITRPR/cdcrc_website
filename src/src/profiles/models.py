from django.db import models
#from team.models import Team

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 30, blank = False, null = False)
    # profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    # designation = models.CharField(max_length = 30)
    branch = models.CharField(max_length = 30, blank = False, null = False )
    course = models.CharField(max_length = 10, blank = False, null = False)
    year = models.IntegerField(default=3, blank = False, null = False)
    #team_coordinator = models.ForeignKey(Team, on_delete=models.CASCADE)
    email = models.CharField(max_length = 30, blank = False, null = False)
    phone = models.CharField(max_length = 10, blank = False, null = False)
    