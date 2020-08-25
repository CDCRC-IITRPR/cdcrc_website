"""
Views for the professional development section
"""

from django.shortcuts import render
from info.models import ProfessionalDevelopmentActivity, ProfessionalDevelopmentBook, ProfessionalDevelopmentVideo
from recruiter.models import Recruiter
from utils.metadata import resource_category_choices
from django.db.models import Q



def about(request):
    context = {
        'title': 'About the Professional Development Department'
    }
    return render(request, 'info/professional_development/about.html', context=context)

def activities(request):
    context = {
        'activities': ProfessionalDevelopmentActivity.objects.order_by('-date'),
        'title': 'Professional Development Activities',
    }
    return render(request, 'info/professional_development/activities.html', context=context)

def activity_detail(request, pk):
    context = {
        'activity': ProfessionalDevelopmentActivity.objects.get(pk=pk),
        'title': 'Activity Detail',
    }
    return render(request, 'info/professional_development/activity_detail.html', context=context)

def books(request):
    context = {
        'title' : 'Library',
        'books': ProfessionalDevelopmentBook.objects.all()
    }
    return render(request, 'info/professional_development/books.html', context=context)

def videos(request):
    context = {
        'title' : 'Resources for UG Students',
        'videos' : ProfessionalDevelopmentVideo.objects.all()
    }
    return render(request, 'info/professional_development/videos.html', context=context)