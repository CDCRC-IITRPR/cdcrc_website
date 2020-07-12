from django import forms
from profiles.models import StudentProfile
from django.contrib.auth import password_validation

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('entry_number', 'phone', 'graduating_year')

        labels = {
            'entry_number': 'Entry Number',
            'phone': 'Phone',
            'graduating_year': 'Graduating Year',
        }

        widgets = {
            'entry_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'graduating_year': forms.TextInput(attrs={'class': 'form-control'}),
        }