"""
Views for the professional development section
"""

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from recruiter.models import Recruiter
from django.db.models import Q
from info.models import CorporateRelationsActivity
from config.utils import get_page_visibility_status

def about(request):
    if(get_page_visibility_status('cr_about')==False):
        return render(request, 'under_construction.html')
    context = {
        'title': 'About the Corporate Relations Department'
    }
    return render(request, 'info/corporate_relations/about.html', context=context)

def activities(request):
    if(get_page_visibility_status('cr_activities')==False):
        return render(request, 'under_construction.html')
    context = {
        'activities': CorporateRelationsActivity.objects.order_by('-date'),
        'title': 'Corporate Relations Activities',
    }
    return render(request, 'info/corporate_relations/activities.html', context=context)

def activity_detail(request, pk):
    context = {
        'activity': CorporateRelationsActivity.objects.get(pk=pk),
        'title': 'Activity Detail',
    }
    return render(request, 'info/corporate_relations/activity_detail.html', context=context)


def hod_message(request):
    if(get_page_visibility_status('cr_hod_message')==False):
        return render(request, 'under_construction.html')
    return render(request, 'info/corporate_relations/hod_message.html')