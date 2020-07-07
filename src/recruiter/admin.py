from django.contrib import admin
from .models import Recruiter, JAF, INF #,JobOpportunity,InternshipOpportunity
# Register your models here.
admin.site.register(Recruiter)
admin.site.register(JAF)
admin.site.register(INF)

# admin.site.register(JobOpportunity)
# admin.site.register(InternshipOpportunity)