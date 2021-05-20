from django import forms
from profiles.models import StudentProfile, TeamMemberProfile
from django.contrib.auth import password_validation

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('entry_number', 'phone', 'graduating_year', 'linkedin_profile')

        labels = {
            'entry_number': 'Entry Number',
            'phone': 'Phone',
            'graduating_year': 'Graduating Year',
            'linkedin_profile': 'Linkedin Profile Link'
        }

        widgets = {
            'entry_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'graduating_year': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_profile': forms.URLInput(attrs={'class': 'form-control'})
        }

class TeamMemberProfileForm(forms.ModelForm):
    class Meta:
        model = TeamMemberProfile
        fields = ('level', 'phone', 'domain', 'category', 'designation', 'photo', 'linkedin_profile', 'visible')

        labels = {
            'level': 'Level',
            'phone': 'Phone',
            'domain': 'Domain',
            'category': 'Category',
            'designation': 'Designation',
            'photo':'Photo',
            'visible': 'Display on Team Page', 
            'linkedin_profile': 'Linkedin Profile Link'
        }

        widgets = {
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            # 'domain': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_profile': forms.URLInput(attrs={'class': 'form-control'})
        }