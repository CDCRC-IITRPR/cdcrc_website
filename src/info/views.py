from django.shortcuts import render
from django.views.generic import ListView, DetailView
from info.models import News, Events, Resource
from recruiter.models import Recruiter
from utils.metadata import resource_category_choices
from profiles.models import TeamMemberProfile
from django.db.models import Q
# Create your views here.
def home(request):
    news = News.objects.all()
    events = Events.objects.all()
    recruiters = Recruiter.objects.filter(visible=True)
    return render(request, 'info/home.html',{'news':news,'events':events, 'recruiters': recruiters})

def contacts(request):
    return render(request, 'info/contacts.html')

def resources_by_category(request, category):
    resources = Resource.objects.filter(category=category)
    context = {'resources': resources, 'category': category}
    return render(request, 'info/resources.html', context=context)

def resource_detail(request, pk):
    resource = Resource.objects.get(pk=pk)
    context = {'resource': resource}
    return render(request, 'info/resource_detail.html', context=context)


def resources(request):
    resource_categories = resource_category_choices
    context = {'resource_categories': resource_categories}
    return render(request, 'info/resource_categories.html', context=context)

def news_detail(request, pk):    
    news = News.objects.get(pk=pk)    
    return render(request,'info/news_detail.html', {'news': news})

def events_detail(request, pk):
    events = Events.objects.get(pk=pk)
    return render(request,'info/events_detail.html',{'events':events})


def faculty_team(request):
    faculty_team_members = TeamMemberProfile.objects.filter((Q(category='faculty') | Q(category='staff')) & Q(visible=True)).order_by('-level')
    members_remainder_4 = faculty_team_members.count()
    context = {'team_members': faculty_team_members, 'team_members_remainder_4': range(1, members_remainder_4+1), 'title': 'Faculty Team'}
    return render(request, 'info/team.html', context=context)

def student_team(request):
    student_team_members = TeamMemberProfile.objects.filter((Q(category='ug') | Q(category='pg')) & Q(visible=True)).order_by('-level')
    members_remainder_4 = student_team_members.count()
    context = {'team_members': student_team_members, 'team_members_remainder_4': range(1, members_remainder_4+1), 'title': 'Student Team'}
    return render(request, 'info/team.html', context=context)

def directors_message(request):
    return render(request, 'info/directors_message.html')

def vision_statement(request):
    return render(request, 'info/vision_statement.html')

def corporate_relations_home(request):
    return render(request, 'under_construction.html')

