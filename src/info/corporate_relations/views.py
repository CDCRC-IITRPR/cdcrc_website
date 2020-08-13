"""
Views for the professional development section
"""

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from recruiter.models import Recruiter
from utils.metadata import resource_category_choices
from django.db.models import Q



def about(request):
    return render(request, 'under_construction.html')