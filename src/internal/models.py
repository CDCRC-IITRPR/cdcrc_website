from django.db import models
from profiles.models import TeamMemberProfile, StudentProfile
from recruiter.models import Recruiter
# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    suffix = models.CharField(max_length=50, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    phone_one = models.CharField(max_length=15, null=True, blank=True)
    phone_two = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    recruiter = models.ForeignKey(Recruiter, on_delete=models.SET_NULL, null=True, blank=True, related_name='recruiter_contacts')
    remark = models.CharField(max_length=512, null=True, blank=True)
    approved = models.BooleanField(default=False)
    

    def __str__(self):
        return self.first_name + " " + self.recruiter.name
    


class Issue(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    created_time = models.DateTimeField( auto_now=True) #TODO: test this out
    issue_creator = models.ForeignKey(TeamMemberProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_issues')
    recruiter = models.ForeignKey(Recruiter, null=True, blank=True, on_delete=models.SET_NULL, related_name='recruiter_issues')
    student_concerned = models.ForeignKey(StudentProfile, null=True, blank=True, on_delete=models.SET_NULL,  related_name='concerned_issues')#incase a student has raised a ticker
    issue_assignees = models.ManyToManyField(TeamMemberProfile,  blank=True,  related_name='assigned_issues')
    issue_status_choices = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]
    issue_status = models.CharField(max_length=10, choices=issue_status_choices, blank=False, null=False)
    issue_priority_choices = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    issue_priorty = models.CharField(max_length=10, choices=issue_priority_choices,  blank=False, null=False)
    initial_comment = models.TextField(blank=False, null=False)
    comment_is_public = models.BooleanField(default=False)
    next_follow_up = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title 

class IssueFollowUps(models.Model):
    issue = models.ForeignKey(Issue, null=False, blank = False, on_delete=models.CASCADE, related_name='follow_ups')
    comment = models.TextField(null=False, blank=True)
    followup_time = models.DateTimeField(auto_now=True)
    issue_assignees = models.ManyToManyField(TeamMemberProfile,  related_name='assigned_followups')
    comment_is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.comment

