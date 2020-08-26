from django.db import models
from profiles.models import TeamMemberProfile, StudentProfile
from recruiter.models import Recruiter
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    suffix = models.CharField(max_length=254, null=True, blank=True)
    job_title = models.CharField(max_length=254, null=True, blank=True)
    phone_one = models.CharField(max_length=15, null=True, blank=True)
    phone_two = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    recruiter = models.CharField(max_length=254, null=True, blank=True)
    remark = models.CharField(max_length=512, null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    

    def __str__(self):
        return self.first_name + " " + str(self.recruiter)
    


class Issue(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    created_time = models.DateTimeField( auto_now=True) #TODO: test this out
    creator = models.ForeignKey(TeamMemberProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='created_issues')
    recruiter = models.ForeignKey(Recruiter, null=True, blank=True, on_delete=models.SET_NULL, related_name='recruiter_issues')
    student_concerned = models.ForeignKey(StudentProfile, null=True, blank=True, on_delete=models.SET_NULL,  related_name='concerned_issues')#incase a student has raised a ticker
    assignees = models.ManyToManyField(TeamMemberProfile,  blank=True,  related_name='assigned_issues')
    issue_status_choices = [
        ('open', 'Open'),
        ('closed', 'Closed'),
    ]
    status = models.CharField(max_length=10, choices=issue_status_choices, blank=False, null=False)
    issue_priority_choices = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    priority = models.CharField(max_length=10, choices=issue_priority_choices,  blank=False, null=False)
    initial_comment = models.TextField(blank=False, null=False)
    next_reminder = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_detail_url(self, request):
        curr_site = get_current_site(request)
        full_url = "http://"+curr_site.domain+str(reverse('internal:issue_detail', kwargs={'pk': self.pk}))
        return full_url

class IssueFollowUp(models.Model):
    issue = models.ForeignKey(Issue, null=False, blank = False, on_delete=models.CASCADE, related_name='followups')
    comment = models.TextField(null=False, blank=True)
    followup_time = models.DateTimeField(auto_now=True)
    assignees = models.ManyToManyField(TeamMemberProfile,  related_name='assigned_followups')
    

    def get_detail_url(self, request):
        curr_site = get_current_site(request)
        full_url = "http://"+curr_site.domain+str(reverse('internal:issue_detail', kwargs={'pk': self.issue.pk}))
        print(full_url)
        return full_url

    def __str__(self):
        return self.comment

