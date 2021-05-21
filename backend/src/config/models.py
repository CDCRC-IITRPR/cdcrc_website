from django.db import models

class PageVisibilityConfig(models.Model):
    CHOICES = (
        ('pd_about', 'pd_about'),
        ('pd_activities', 'pd_activities'),
        ('pd_library', 'pd_library'),
        ('pd_videos', 'pd_videos'),
        ('cr_about', 'cr_about'), 
        ('cr_activities', 'cr_activities'),
        ('cr_hod_message', 'cr_hod_message'),
        ('pd_hod_message', 'pd_hod_message'),
        ('tnp_hod_message', 'tnp_hod_message'),
        ('pd_initiatives', 'pd_initiatives'),
    )
    page = models.CharField(max_length=128, null=False, blank=False, unique=True, choices=CHOICES)
    visible = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.page
