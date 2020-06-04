from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'info/home.html')

def contacts(request):
    return render(request, 'info/contacts.html')