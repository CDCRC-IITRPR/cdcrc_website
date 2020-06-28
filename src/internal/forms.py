from django import forms
from internal.models import Contact

class ImportContactsForm(forms.Form):
    contacts_file = forms.FileField() 

class AddContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_one', 'phone_two', 'email', 'recruiter', 'remark']