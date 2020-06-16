from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    email=models.EmailField()
    website = models.URLField(max_length=200,null=True)
    address = models.TextField(null=True)
    logo = models.ImageField(default='someDefault.png',blank=True)
    #thumb=models.ImageField(default="default.png", blank=True) 
    categoryChoices = [
        ('Analytics','Analytics'),
        ('Consulting','Consulting'),
        ('Core (Technical)','Core (Technical)'),
        ('Finance','Finance'),
        ('I.T./Software','I.T./Software'),
        ('Management','Management'),
        ('Teaching / Research','Teaching / Research'),
        ('other','other'),
    ]
    category = models.CharField(max_length=30,choices=categoryChoices,default='other')
    OrgTypechoices = [
        ('Private Sector','Private Sector'),
        ('Start-up','Start-up'),
        ('Government','Government'),
        ('Public Sector','Public Sector'),
        ('MNC (Indian origin)','MNC (Indian origin)'),
        ('MNC (Foreign origin)','MNC (Foreign origin)'),
        ('Others','Others'),
    ]
    OrgType = models.CharField(max_length=40,choices=OrgTypechoices,default='Others')

    def __str__(self):
        return f'{self.user.username} Profile'

class JobOpportunity(models.Model):
    company = models.OneToOneField(RecruiterProfile,on_delete=models.CASCADE)
    job_designation = models.CharField(max_length=20)
    job_description = models.TextField(null=True)
    place_of_posting = models.CharField(max_length=30)
    bool_options = [
        ('Yes','Yes'),
        ('No','No'),
    ]

    #selection process
    cgpa_required = models.DecimalField(max_digits=3,decimal_places=2)
    ppt = models.CharField(max_length=10,choices=bool_options,default='Others')
    shortlist_from_resumes = models.CharField(max_length=10,choices=bool_options,default='Others')
    written_test = models.CharField(max_length=10,choices=bool_options,default='Others')
    online_test = models.CharField(max_length=10,choices=bool_options,default='Others')
    technical_test = models.CharField(max_length=10,choices=bool_options,default='Others')
    aptitude_test = models.CharField(max_length=10,choices=bool_options,default='Others')
    psychometric_test = models.CharField(max_length=10,choices=bool_options,default='Others')
    for_technicalTest_specify_likelyTopics_or_skillset = models.TextField(null=True)
    group_discussion = models.CharField(max_length=10,choices=bool_options,default='Others')
    personal_interview = models.CharField(max_length=10,choices=bool_options,default='Others')
    no_of_rounds_of_personalInterview = models.IntegerField(primary_key=False,null=False,default=1)
    no_of_offers_you_intend_to_make = models.IntegerField(primary_key=False,null=False,default=1)

    #logistics requiments
    no_of_members_required = models.IntegerField(primary_key=False,null=False,default=1)
    no_of_rooms_required_for_selection_process = models.IntegerField(primary_key=False,null=False,default=1)
    other_requirements = models.TextField(null=True)
    
    #job target disciplines
    btech_cse = models.CharField(max_length=10,choices=bool_options,default='Others')
    btech_EE = models.CharField(max_length=10,choices=bool_options,default='Others')
    btech_Mech = models.CharField(max_length=10,choices=bool_options,default='Others')
    btech_mtech_mechDual = models.CharField(max_length=10,choices=bool_options,default='Others')
    btech_civil = models.CharField(max_length=10,choices=bool_options,default='Others')
    msc_chemistry = models.CharField(max_length=10,choices=bool_options,default='Others')
    msc_mathematics = models.CharField(max_length=10,choices=bool_options,default='Others')
    msc_physics = models.CharField(max_length=10,choices=bool_options,default='Others')
    mtech_cse = models.CharField(max_length=10,choices=bool_options,default='Others')
    mtech_bioMedicalEng = models.CharField(max_length=10,choices=bool_options,default='Others')
    mtech_EE = models.CharField(max_length=10,choices=bool_options,default='Others')
    mtech_Mech = models.CharField(max_length=10,choices=bool_options,default='Others')
    msResearch_Electrical = models.CharField(max_length=10,choices=bool_options,default='Others')
    phd = models.CharField(max_length=10,choices=bool_options,default='Others')

class InternshipOpportunity(models.Model):
    company = models.OneToOneField(RecruiterProfile,on_delete=models.CASCADE)

    bool_options = [
        ('Yes','Yes'),
        ('No','No'),
    ]

    month_2 = models.CharField(max_length=10,choices=bool_options,default='Others')
    month_6 = models.CharField(max_length=10,choices=bool_options,default='Others')
    joint_master_thesis_program = models.CharField(max_length=10,choices=bool_options,default='Others')
    job_description = models.TextField(null=True)

    #selection process
    cgpa_required = models.DecimalField(max_digits=3,decimal_places=2)
    ppt = models.CharField(max_length=10,choices=bool_options,default='Others')
    shortlist_from_resumes = models.CharField(max_length=10,choices=bool_options,default='Others')
    written_test = models.CharField(max_length=10,choices=bool_options,default='Others')
    online_test = models.CharField(max_length=10,choices=bool_options,default='Others')
    technical_test = models.CharField(max_length=10,choices=bool_options,default='Others')
    aptitude_test = models.CharField(max_length=10,choices=bool_options,default='Others')
    psychometric_test = models.CharField(max_length=10,choices=bool_options,default='Others')
    for_technicalTest_specify_likelyTopics_or_skillset = models.TextField(null=True)
    group_discussion = models.CharField(max_length=10,choices=bool_options,default='Others')
    personal_interview = models.CharField(max_length=10,choices=bool_options,default='Others')
    no_of_rounds_of_personalInterview = models.IntegerField(primary_key=False,null=False,default=1)
    no_of_offers_you_intend_to_make = models.IntegerField(primary_key=False,null=False,default=1)

    #logistics requiments
    no_of_members_required = models.IntegerField(primary_key=False,null=False,default=1)
    no_of_rooms_required_for_selection_process = models.IntegerField(primary_key=False,null=False,default=1)
    other_requirements = models.TextField(null=True)

    #internship target disciplines
    btech_cse = models.CharField(max_length=10,choices=bool_options,default='Others')
    btech_EE = models.CharField(max_length=10,choices=bool_options,default='Others')
    btech_Mech = models.CharField(max_length=10,choices=bool_options,default='Others')
    btech_mtech_mechDual = models.CharField(max_length=10,choices=bool_options,default='Others')
    btech_civil = models.CharField(max_length=10,choices=bool_options,default='Others')
    msc_chemistry = models.CharField(max_length=10,choices=bool_options,default='Others')
    msc_mathematics = models.CharField(max_length=10,choices=bool_options,default='Others')
    msc_physics = models.CharField(max_length=10,choices=bool_options,default='Others')
    mtech_cse = models.CharField(max_length=10,choices=bool_options,default='Others')
    mtech_bioMedicalEng = models.CharField(max_length=10,choices=bool_options,default='Others')
    mtech_EE = models.CharField(max_length=10,choices=bool_options,default='Others')
    mtech_Mech = models.CharField(max_length=10,choices=bool_options,default='Others')