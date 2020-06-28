from django.contrib import admin
from internal.models import Issue, IssueFollowUps, Contact
# Register your models here.
admin.site.register(Issue)
admin.site.register(IssueFollowUps)
admin.site.register(Contact)