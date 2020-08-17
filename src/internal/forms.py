from django import forms
from internal.models import Contact, IssueFollowUp, Issue
from bootstrap_datepicker_plus import DateTimePickerInput


class ImportContactsForm(forms.Form):
    contacts_file = forms.FileField() 

class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_one', 'phone_two', 'email', 'recruiter', 'linkedin_url', 'remark']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_one': 'Phone #1',
            'phone_two': 'Phone #2',
            'email': 'Email',
            'recruiter': 'Recruiter',
            'linkedin_url': 'Linkedin URL', 
            'remark': 'Remark',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_one': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_two': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
            'recruiter': forms.Select(attrs={'class': 'form-control'}),
            'remark': forms.Textarea(attrs={'class': 'form-control'}),
        }

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title',
            'recruiter',
            'student_concerned',
            'assignees',
            'priority',
            'initial_comment',
            'next_reminder',
        ]

        labels = {
            'title': 'Summary',
            'recruiter': 'Company',
            'student_concerned': 'Student Concerned',
            'assignees': 'Assignees',
            'priority': 'priority',
            'initial_comment': 'Comment',
            'next_reminder': 'Reminder'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'recruiter': forms.Select(attrs={'class': 'form-control'}),
            'student_concerned': forms.Select(attrs={'class': 'form-control'}),
            'assignees': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'initial_comment': forms.Textarea(attrs={'class': 'form-control'}),
            'next_reminder': DateTimePickerInput(),
        }


class IssueFollowupForm(forms.ModelForm):
    next_reminder = forms.DateTimeField(
        # label="Next Reminder",
        widget=DateTimePickerInput(),
        # help_text=password_validation.password_validators_help_text_html(),
        # localize=True
    )
    class Meta:
        model = IssueFollowUp
        fields = [
            'comment',
            'assignees',
        ]
        labels = {
            'comment': 'Comment',
            'assignees': 'Assignees',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'assignees': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

