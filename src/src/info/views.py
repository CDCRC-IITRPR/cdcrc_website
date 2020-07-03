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

def for_recruiters(request):
    return render(request, 'info/for_recruiters.html')

def news_detail(request, pk):    
    news = News.objects.get(pk=pk)    
    return render(request,'info/news_detail.html', {'news': news})

def events_detail(request, pk):
    events = Events.objects.get(pk=pk)
    return render(request,'info/events_detail.html',{'events':events})
