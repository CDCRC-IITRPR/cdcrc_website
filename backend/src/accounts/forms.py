from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class SignupForm(UserCreationForm):
    
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'required':True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',  }),
            'email': forms.EmailInput(attrs={'class': 'form-control',  'required':True}),
        }