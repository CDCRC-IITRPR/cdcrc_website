from django.contrib import admin

from profiles.models import StudentProfile, TeamMemberProfile


def name(obj):
    return obj.user.first_name+" "+obj.user.last_name

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ( 'id', name, 'entry_number', 'phone')
    # list_filter = ('is_staff', 'is_superuser', 'is_team_member')
    # actions = [enroll_user_in_team, unenroll_user_from_team]
    search_fields = ('id', 'entry_number', 'phone',  'user__first_name', 'user__last_name')


admin.site.register(StudentProfile, StudentProfileAdmin)



class TeamMemberProfileAdmin(admin.ModelAdmin):
    list_display = ( 'id', name, 'phone', 'domain', 'designation', 'visible')
    # list_filter = ('is_staff', 'is_superuser', 'is_team_member')
    # actions = [enroll_user_in_team, unenroll_user_from_team]
    search_fields = ('id', 'phone', 'domain', 'user__first_name', 'user__last_name')


admin.site.register(TeamMemberProfile, TeamMemberProfileAdmin)