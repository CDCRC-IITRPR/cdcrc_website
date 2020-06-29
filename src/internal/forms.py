from django import forms
from internal.models import Contact, IssueFollowUp, Issue

class ImportContactsForm(forms.Form):
    contacts_file = forms.FileField() 

class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_one', 'phone_two', 'email', 'recruiter', 'remark']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'phone_one': 'Phone #1',
            'phone_two': 'Phone #2',
            'email': 'Email',
            'recruiter': 'Recruiter',
            'remark': 'Remark',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_one': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_two': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
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
            'deadline',
        ]

        labels = {
            'title': 'Summary',
            'recruiter': 'Company',
            'student_concerned': 'Student Concerned',
            'assignees': 'Assignees',
            'priority': 'priority',
            'initial_comment': 'Comment',
            'deadline': 'Deadline'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'recruiter': forms.Select(attrs={'class': 'form-control'}),
            'student_concerned': forms.Select(attrs={'class': 'form-control'}),
            'assignees': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'initial_comment': forms.Textarea(attrs={'class': 'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }


class IssueFollowupForm(forms.ModelForm):
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
            # 'comment_is_public': forms.C(attrs={'class': 'form-control'}),
        }

