from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from profiles.models import TeamMemberProfile

def enroll_user_in_team(modeladmin, request, queryset):
    for user in queryset:
        try:
            t = TeamMemberProfile(user = user)
            t.save()
        except:
            print("User already part of team")

enroll_user_in_team.short_description = "Enroll users in team"

def unenroll_user_from_team(modeladmin, request, queryset):
    for user in queryset:
        # try:
        t = TeamMemberProfile.objects.get(user = user)
        t.delete()
        # except:
        #     print("User not part of team")
unenroll_user_from_team.short_description = "Unenroll team members from team"

def team_member(obj):
    return hasattr(obj, 'team_profile')
team_member.boolean=True
class UserAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'last_name', 'email', team_member, 'is_staff', 'is_superuser')
    # list_filter = ('is_staff', 'is_superuser', 'is_team_member')
    actions = [enroll_user_in_team, unenroll_user_from_team]
    search_fields = ('first_name', 'last_name', 'email')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

