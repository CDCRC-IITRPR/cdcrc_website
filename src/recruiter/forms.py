from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateRecruiterForm(UserCreationForm):
    company=forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ['company','username','email','password1','password2']