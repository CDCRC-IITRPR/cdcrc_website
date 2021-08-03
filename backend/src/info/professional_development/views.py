"""
Views for the professional development section
"""

from django.shortcuts import render
from info.models import ProfessionalDevelopmentActivity, ProfessionalDevelopmentBook, ProfessionalDevelopmentVideo, ProfessionalDevelopmentInitiatives
from recruiter.models import Recruiter
from django.db.models import Q
from config.utils import get_page_visibility_status


def about(request):
    if(get_page_visibility_status('pd_about')==False):
        return render(request, 'under_construction.html')
    context = {
        'title': 'About the Career Development Cell'
    }
    return render(request, 'info/professional_development/about.html', context=context)

def activities(request):
    if(get_page_visibility_status('pd_activities')==False):
        return render(request, 'under_construction.html')
    context = {
        'activities': ProfessionalDevelopmentActivity.objects.order_by('-date'),
        'title': 'Career Development Activities',
    }
    return render(request, 'info/professional_development/activities.html', context=context)

def initiatives(request):
    if(get_page_visibility_status('pd_initiatives')==False):
        return render(request, 'under_construction.html')
    context = {
        'initiatives': ProfessionalDevelopmentInitiatives.objects.order_by('-date'),
        'title': 'Career Development Initiatives',
    }
    return render(request, 'info/professional_development/initiatives.html', context=context)

def activity_detail(request, pk):
    context = {
        'activity': ProfessionalDevelopmentActivity.objects.get(pk=pk),
        'title': 'Activity Detail',
    }
    return render(request, 'info/professional_development/activity_detail.html', context=context)

def initiative_detail(request, pk):
    context = {
        'initiative': ProfessionalDevelopmentInitiatives.objects.get(pk=pk),
        'title': 'Initiative Detail',
    }
    return render(request, 'info/professional_development/initiative_detail.html', context=context)

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

def pg_resources(request):
    context = {
        'title' : 'Resources for PG Students',
    }
    return render(request, 'info/professional_development/graduate_student_resources.html', context=context)