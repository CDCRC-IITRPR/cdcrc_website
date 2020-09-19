"""
Views for the professional development section
"""

from django.shortcuts import render
from recruiter.models import Recruiter
from django.db.models import Q
from config.utils import get_page_visibility_status

def past_recruiters(request):
    companies = Recruiter.objects.filter(visible=True).order_by('name')
    companies_remainder_4 = companies.count()
    context = {'companies': companies, 'companies_remainder_4': range(1, companies_remainder_4+1), 'title': 'Past Recruiters'}
    return render(request, 'recruiter/past_recruiters.html',{'companies':companies})
