from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News,Events
# Create your views here.
def home(request):
    news = News.objects.all()
    events = Events.objects.all()
    return render(request, 'info/home.html',{'news':news,'events':events})


def contacts(request):
    return render(request, 'info/contacts.html')