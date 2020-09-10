from django.shortcuts import render,redirect
from pymongo import MongoClient
from recruiter.models import Recruiter, JAF, INF, StudentDemographic, PastRecruiter
from django.http import HttpResponse
from utils.login_decorators import team_user_required
from bson.objectid import ObjectId
import json 
from utils.pdf_generator import render_to_pdf
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers


def guide(request):
    return render(request, 'recruiter/guide.html')

def why_recruit(request):
    return render(request, 'recruiter/why_recruit.html')

def recruiter_guide(request):
    return render(request, 'recruiter/recruiter_guide.html')

def student_demographics(request):
    demographics = StudentDemographic.objects.all()
    return render(request, 'recruiter/student_demographics.html',{'demographics': demographics})

def six_month_internship(request):
    context = {
        'title': '6 Month Internship'
    }
    return render(request, 'recruiter/six_month_internship.html', context=context)

def joint_master_thesis(request):
    context = {
        'title': 'Joint Master Thesis'
    }
    return render(request, 'recruiter/joint_master_thesis.html', context=context)

def past_recruiters(request):
    companies = PastRecruiter.objects.all()
    return render(request, 'recruiter/past_recruiters.html',{'companies':companies})


# @team_user_required
# def jaf_details_pdf(request, pk):
#     #mongo connection
#     client = MongoClient()
#     cdcrc_db = client['cdcrc']
#     jaf_collection = cdcrc_db.jaf
#     #get the jaf python object
#     jaf_obj = JAF.objects.get(pk=pk)
#     jaf_mongo_id = jaf_obj.mongo_id
#     jaf_timestamp = jaf_obj.timestamp
#     # print(jaf_mongo_id)
#     jaf_details = jaf_collection.find_one({"_id": ObjectId(jaf_mongo_id)})
#     # print(jaf_details)
#     del jaf_details['_id']
#     jaf_details['timestamp'] = jaf_timestamp
#     pdf =  render_to_pdf('recruiter/jaf_details_simple_html.html', context_dict={'jaf_details':jaf_details})
#     return HttpResponse(pdf, content_type='application/pdf')

# @team_user_required
# def jaf_details_simple_html(request, pk):
#     #mongo connection
#     client = MongoClient()
#     cdcrc_db = client['cdcrc']
#     jaf_collection = cdcrc_db.jaf
#     #get the jaf python object
#     jaf_obj = JAF.objects.get(pk=pk)
#     jaf_mongo_id = jaf_obj.mongo_id
#     jaf_timestamp = jaf_obj.timestamp
#     # print(jaf_mongo_id)
#     jaf_details = jaf_collection.find_one({"_id": ObjectId(jaf_mongo_id)})
#     # print(jaf_details)
#     del jaf_details['_id']
#     jaf_details['timestamp'] = jaf_timestamp
#     return render(request, 'recruiter/jaf_details_simple_html.html', context={'jaf_details':jaf_details})

# @team_user_required
# def jaf_details(request, pk):
#     #mongo connection
#     client = MongoClient()
#     cdcrc_db = client['cdcrc']
#     jaf_collection = cdcrc_db.jaf
#     #get the jaf python object
#     jaf_mongo_id = JAF.objects.get(pk=pk).mongo_id
#     # print(jaf_mongo_id)
#     jaf_details = jaf_collection.find_one({"_id": ObjectId(jaf_mongo_id)})
#     # print(jaf_details)
#     del jaf_details['_id']
#     return render(request, 'recruiter/jaf_details.html', context={'jaf_details':jaf_details})


# def jaf(request):
#     if request.method=='POST':
#         client = MongoClient()
#         cdcrc_db = client['cdcrc']
#         jaf_collection = cdcrc_db.jaf
#         data = request.POST.dict()
#         del data['csrfmiddlewaretoken']
#         recruiter_name = data['aboutCompanyName']
#         try:
#             recruiter = Recruiter.objects.get(name=recruiter_name)
#         except Recruiter.DoesNotExist:
#             recruiter = Recruiter(name=recruiter_name)
#             recruiter.save()

#         num_job_profiles = 0  
#         for i in range(1, 10): #TODO: no more than 9 profiles at a time
#             key = 'jobProfile' + str(i) + 'Designation'
#             if key in data.keys():
#                 num_job_profiles=i
#             else:
#                 break  

#         data_formatted = {
#             'about':{},
#             'type_is':[],
#             'sector_is':[],
#             'hr_info':{},
#             'num_job_profiles': num_job_profiles,
#             'job_profiles':{},
#             'selection_process': {},
#             'disciplines_interested_in': {}
#         }

#         for i in range(1, num_job_profiles+1):
#             data_formatted['job_profiles'][str(i)] = {}

#         for k, v in data.items():
#             if k.startswith('about'):
#                 data_formatted['about'][k] = v
#             elif k.startswith('type_is'):
#                 if len(v)>0:data_formatted['type_is'].append(v)
#             elif k.startswith('sector_is'):
#                 if len(v)>0: data_formatted['sector_is'].append(v)
#             elif k.startswith('hr_info'):
#                 data_formatted['hr_info'][k] = v
#             elif k.startswith('jobProfile'):
#                 data_formatted['job_profiles'][k[10]][k[11:]] = v
#             elif k.startswith('selection_process'):
#                 tmp = k[18:]
#                 if tmp.startswith('is'):
#                     tmp = tmp[3:]
#                 tmp = tmp.replace('_', ' ')
#                 tmp = tmp.title()
#                 data_formatted['selection_process'][tmp] = v
#             elif k=='logistics_requirements':
#                 data_formatted[k] = v
#             elif k.startswith('disciplines_interested_in'):
#                 tmp = k[26:]
#                 tmp = tmp.replace('_', ' ')
#                 data_formatted['disciplines_interested_in'][tmp] = v

#         post_id = jaf_collection.insert_one(data_formatted).inserted_id
#         jaf = JAF(recruiter=recruiter, mongo_id=str(post_id))
#         jaf.save()
#         # return HttpResponse('JAF Saved')
#         del data_formatted['_id']

#         return HttpResponse(json.dumps(data_formatted, indent=4), content_type='application/json')

#     selection_process_booleans = {
#         'selection_process_is_ppt': 'PPT',
#         'selection_process_is_shortlist_from_resumes': 'Shortlist From Resumes',
#         'selection_process_is_online_test': 'Online Test',
#         'selection_process_is_technical_test': 'Technical Test',
#         'selection_process_is_aptitude_test': 'Aptitude Test',
#         'selection_process_is_psychometric_test': 'Psychometric Test',
#         'selection_process_is_group_discussion': 'Group Discussion',
#         'selection_process_is_personal_interview': 'Personal Interview',
#     }

#     selection_process_text_inputs = {
#         'selection_process_eligibility_criteria': ['Eligibility Criteria', 'Criteria (min. CG cutoff, 0-10 scale)'],
#         'selection_process_number_of_interview_rounds': ['Number of Interview Rounds', 'Number of Personal Interview Rounds'],
#         'selection_process_period_of_recruitment': ['Preferred Period of Recruitment', 'Preferred Period of Recruitment']
#     }

#     selection_process_text_areas = {
#         'selection_process_skills_required': ['Topic/Skills Required', 'For the tests and interviews, please specify any likely topics/skill sets required', 3],
#     }

#     disciplines_interested_in = {
#         'disciplines_interested_in_BTech Computer Science & Engineering': 'B.Tech Computer Science & Engineering',
#         'disciplines_interested_in_BTech Electrical Engineering' : 'B.Tech Electrical Engineering (includes Electronics courses also)',
#         'disciplines_interested_in_BTech Mechanical Engineering': 'B.Tech Mechanical Engineering',
#     }
#     context = {
#         'disciplines_interested_in': disciplines_interested_in,
#         'selection_process_booleans': selection_process_booleans,
#         'selection_process_text_inputs': selection_process_text_inputs,
#         'selection_process_text_areas': selection_process_text_areas
#     }

#     return render(request, 'recruiter/jaf.html', context=context)

# def inf(request):
#     if request.method=='POST':
#         client = MongoClient()
#         cdcrc_db = client['cdcrc']
#         inf_collection = cdcrc_db.inf
#         data = request.POST.dict()
#         del data['csrfmiddlewaretoken']
#         recruiter_name = data['aboutCompanyName']
#         try:
#             recruiter = Recruiter.objects.get(name=recruiter_name)
#         except Recruiter.DoesNotExist:
#             recruiter = Recruiter(name=recruiter_name)
#             recruiter.save()

#         num_job_profiles = 0  
#         for i in range(1, 10): #TODO: no more than 9 profiles at a time
#             key = 'jobProfile' + str(i) + '_Designation'
#             if key in data.keys():
#                 num_job_profiles=i
#             else:
#                 break  

#         data_formatted = {
#             'about':{},
#             'type_is':[],
#             'sector_is':[],
#             'hr_info':{},
#             'num_job_profiles': num_job_profiles,
#             'job_profiles':{},
#             'selection_process': {},
#             'disciplines_interested_in': {}
#         }

#         for i in range(1, num_job_profiles+1):
#             data_formatted['job_profiles'][str(i)] = {}

#         for k, v in data.items():
#             if k.startswith('about'):
#                 data_formatted['about'][k] = v
#             elif k.startswith('type_is'):
#                 if len(v)>0:data_formatted['type_is'].append(v)
#             elif k.startswith('sector_is'):
#                 if len(v)>0: data_formatted['sector_is'].append(v)
#             elif k.startswith('hr_info'):
#                 data_formatted['hr_info'][k] = v
#             elif k.startswith('jobProfile'):
#                 tmp = k[12:]
#                 # tmp = tmp.replace('_', ' ')
#                 data_formatted['job_profiles'][k[10]][tmp] = v
#             elif k.startswith('selection_process'):
#                 tmp = k[18:]
#                 if tmp.startswith('is'):
#                     tmp = tmp[3:]
#                 tmp = tmp.replace('_', ' ')
#                 tmp = tmp.title()
#                 data_formatted['selection_process'][tmp] = v
#             elif k=='logistics_requirements':
#                 data_formatted[k] = v
#             elif k.startswith('disciplines_interested_in'):
#                 tmp = k[26:]
#                 tmp = tmp.replace('_', ' ')
#                 data_formatted['disciplines_interested_in'][tmp] = v

#         post_id = inf_collection.insert_one(data_formatted).inserted_id
#         inf = INF(recruiter=recruiter, mongo_id=str(post_id))
#         inf.save()
#         del data_formatted['_id']

#         return HttpResponse(json.dumps(data_formatted, indent=4), content_type='application/json')

#     selection_process_booleans = {
#         'selection_process_is_ppt': 'PPT',
#         'selection_process_is_shortlist_from_resumes': 'Shortlist From Resumes',
#         'selection_process_is_online_test': 'Online Test',
#         'selection_process_is_technical_test': 'Technical Test',
#         'selection_process_is_aptitude_test': 'Aptitude Test',
#         'selection_process_is_psychometric_test': 'Psychometric Test',
#         'selection_process_is_group_discussion': 'Group Discussion',
#         'selection_process_is_personal_interview': 'Personal Interview',
#     }

#     selection_process_text_inputs = {
#         'selection_process_eligibility_criteria': ['Eligibility Criteria', 'Criteria (min. CG cutoff, 0-10 scale)'],
#         'selection_process_number_of_interview_rounds': ['Number of Interview Rounds', 'Number of Personal Interview Rounds'],
#         'selection_process_period_of_recruitment': ['Preferred Period of Recruitment', 'Preferred Period of Recruitment']
#     }

#     selection_process_text_areas = {
#         'selection_process_skills_required': ['Topic/Skills Required', 'For the tests and interviews, please specify any likely topics/skill sets required', 3],
#     }

#     disciplines_interested_in = {
#         'disciplines_interested_in_BTech Computer Science & Engineering': 'B.Tech Computer Science & Engineering',
#         'disciplines_interested_in_BTech Electrical Engineering' : 'B.Tech Electrical Engineering (includes Electronics courses also)',
#         'disciplines_interested_in_BTech Mechanical Engineering': 'B.Tech Mechanical Engineering',
#     }
#     context = {
#         'disciplines_interested_in': disciplines_interested_in,
#         'selection_process_booleans': selection_process_booleans,
#         'selection_process_text_inputs': selection_process_text_inputs,
#         'selection_process_text_areas': selection_process_text_areas
#     }

#     return render(request, 'recruiter/inf.html', context=context)

# def inf_details(request, pk):
#     #mongo connection
#     client = MongoClient()
#     cdcrc_db = client['cdcrc']
#     inf_collection = cdcrc_db.inf
#     #get the jaf python object
#     inf_mongo_id = INF.objects.get(pk=pk).mongo_id
#     inf_details = inf_collection.find_one({"_id": ObjectId(inf_mongo_id)})
#     del inf_details['_id']
#     return render(request, 'recruiter/inf_details.html', context={'inf_details':inf_details})


# @team_user_required
# def inf_details_simple_html(request, pk):
#     #mongo connection
#     client = MongoClient()
#     cdcrc_db = client['cdcrc']
#     inf_collection = cdcrc_db.inf
#     #get the jaf python object
#     inf_obj = INF.objects.get(pk=pk)
#     inf_mongo_id = inf_obj.mongo_id
#     inf_timestamp = inf_obj.timestamp
#     # print(jaf_mongo_id)
#     inf_details = inf_collection.find_one({"_id": ObjectId(inf_mongo_id)})
#     # print(jaf_details)
#     del inf_details['_id']
#     inf_details['timestamp'] = inf_timestamp
#     return render(request, 'recruiter/inf_details_simple_html.html', context={'inf_details':inf_details})

# @team_user_required
# def inf_details_pdf(request, pk):
#     #mongo connection
#     client = MongoClient()
#     cdcrc_db = client['cdcrc']
#     inf_collection = cdcrc_db.inf
#     #get the jaf python object
#     inf_obj = INF.objects.get(pk=pk)
#     inf_mongo_id = inf_obj.mongo_id
#     inf_timestamp = inf_obj.timestamp
#     # print(jaf_mongo_id)
#     inf_details = inf_collection.find_one({"_id": ObjectId(inf_mongo_id)})
#     # print(jaf_details)
#     del inf_details['_id']
#     inf_details['timestamp'] = inf_timestamp
#     pdf =  render_to_pdf('recruiter/inf_details_simple_html.html', context_dict={'inf_details':inf_details})
#     return HttpResponse(pdf, content_type='application/pdf')


def why_recruit(request):
    return render(request, 'recruiter/why_recruit.html')

def recruiter_guide(request):
    return render(request, 'recruiter/recruiter_guide.html')

# def student_demographics(request):
#     student = Studentdata.objects.all()
#     return render(request, 'recruiter/student_demographics.html',{'stu': student})

def six_month_internship(request):
    context = {
        'title': '6 Month Internship'
    }
    return render(request, 'recruiter/six_month_internship.html', context=context)

def joint_master_thesis(request):
    context = {
        'title': 'Joint Master Thesis'
    }
    return render(request, 'recruiter/joint_master_thesis.html', context=context)


