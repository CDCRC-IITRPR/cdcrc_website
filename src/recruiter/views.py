from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate,login,logout
# # from .forms import CreateRecruiterForm
# from django.contrib import messages
# # Create your views here.
# def registerPage(request):
#     form=CreateRecruiterForm
#     if request.method == 'POST':
#         form=CreateRecruiterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user=form.cleaned_data.get('username')
#             messages.success(request,'Account was created for'+user)
#             return redirect('login')
#     context = {'form':form}
#     return render(request,'recruiter/register.html',context)

# def loginPage(request):

#     if request.method=='POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username, password=password)

#     return render(request,'recruiter/login.html',{})

def jaf(request):
    if request=='POST':
        print("Data Fetched")

    selection_process_booleans = {
        'is_ppt': 'PPT',
        'is_shortlist_from_resumes': 'Shortlist From Resumes',
        'is_online_test': 'Online Test',
        'is_technical_test': 'Technical Test',
        'is_aptitude_test': 'Aptitude Test',
        'is_psychometric_test': 'Psychometric Test',
        'is_group_discussion': 'Group Discussion',
        'is_personal_interview': 'Personal Interview',
    }

    selection_process_text_inputs = {
        'eligibility_criteria': ['Eligibility Criteria', 'Criteria (min. CG cutoff, 0-10 scale)'],
        'number_of_interview_rounds': ['Number of Interview Rounds', 'Number of Personal Interview Rounds'],
        'period_of_recruitment': ['Preferred Period of Recruitment', 'Preferred Period of Recruitment']
    }

    selection_process_text_areas = {
        'skills_required': ['Topic/Skills Required', 'For the tests and interviews, please specify any likely topics/skill sets required', 3],
    }

    disciplines_interested_in = {
        'btech_cse': 'B.Tech Computer Science & Engineering',
        'btech_ee' : 'B.Tech Electrical Engineering (includes Electronics courses also)',
        'btech_me': 'B.Tech Mechanical Engineering',
    }
    context = {
        'disciplines_interested_in': disciplines_interested_in,
        'selection_process_booleans': selection_process_booleans,
        'selection_process_text_inputs': selection_process_text_inputs,
        'selection_process_text_areas': selection_process_text_areas
    }

    return render(request, 'recruiter/jaf.html', context=context)