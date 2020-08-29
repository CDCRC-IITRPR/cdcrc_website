"""
Views for the professional development section
"""

from django.shortcuts import render
from info.models import ProfessionalDevelopmentActivity, ProfessionalDevelopmentBook, ProfessionalDevelopmentVideo
from recruiter.models import Recruiter
from utils.metadata import resource_category_choices
from django.db.models import Q
from config.utils import get_page_visibility_status


def about(request):
    if(get_page_visibility_status('pd_about')==False):
        return render(request, 'under_construction.html')
    context = {
        'title': 'About the Professional Development Department'
    }
    return render(request, 'info/professional_development/about.html', context=context)

def activities(request):
    if(get_page_visibility_status('pd_activities')==False):
        return render(request, 'under_construction.html')
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
    if(get_page_visibility_status('pd_library')==False):
        return render(request, 'under_construction.html')
    context = {
        'title' : 'Library',
        'books': ProfessionalDevelopmentBook.objects.all()
    }
    return render(request, 'info/professional_development/books.html', context=context)

def videos(request):
    if(get_page_visibility_status('pd_videos')==False):
        return render(request, 'under_construction.html')
    context = {
        'title' : 'Video Resources for Students',
        'videos' : ProfessionalDevelopmentVideo.objects.all()
    }
    return render(request, 'info/professional_development/videos.html', context=context)

def hod_message(request):
    if(get_page_visibility_status('pd_hod_message')==False):
        return render(request, 'under_construction.html')
    return render(request, 'info/professional_development/hod_message.html')