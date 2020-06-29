from django.contrib import admin
from internal.models import Issue, IssueFollowUp, Contact
# Register your models here.
admin.site.register(Issue)
admin.site.register(IssueFollowUp)
admin.site.register(Contact)