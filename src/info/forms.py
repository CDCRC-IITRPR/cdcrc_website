from django import forms
from info.models import Resource

class ResourceForm(forms.ModelForm):
    images = forms.ImageField( widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Resource
        fields = ['title', 'categories', 'url', 'brief', 'detail']
        labels = {
            'title': 'Title',
            'categories': 'Categories',
            'url': 'URL',
            'brief': 'Brief',
            'detail': 'Detail',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required':True}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control', 'required':True, }),
            'url': forms.TextInput(attrs={'class': 'form-control',}),
            'brief': forms.TextInput(attrs={'class': 'form-control', 'required':True, }),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }

