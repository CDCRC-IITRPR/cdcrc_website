from django.contrib import admin

from profiles.models import StudentProfile, TeamMemberProfile

admin.site.register(StudentProfile)
admin.site.register(TeamMemberProfile)