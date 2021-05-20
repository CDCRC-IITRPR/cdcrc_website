from django.contrib.auth.models import User
from profiles.models import StudentProfile

def get_user_name(self):
    if self.first_name and self.last_name:
        return self.first_name + " " + self.last_name
    elif self.first_name:
        return self.first_name
    else:
        return ""

def is_team_member(self):
    return hasattr(self, 'team_profile')

def has_student_profile(self):
    return hasattr(self, 'student_profile')

def student_profile_completed(self):
    if hasattr(self, 'student_profile')==False:
        return False
    else:
        has_entry_number = True if self.student_profile.entry_number else False
        has_phone = True if self.student_profile.phone else False
        has_graduating_year = True if self.student_profile.graduating_year else False

        return has_entry_number and has_phone and has_graduating_year

User.add_to_class("get_user_name", get_user_name)
User.add_to_class("is_team_member", is_team_member)
User.add_to_class("student_profile_completed", student_profile_completed)
User.add_to_class("has_student_profile", has_student_profile)