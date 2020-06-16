from django.contrib import admin
from .models import RecruiterProfile,JobOpportunity,InternshipOpportunity
# Register your models here.
admin.site.register(RecruiterProfile)
admin.site.register(JobOpportunity)
admin.site.register(InternshipOpportunity)