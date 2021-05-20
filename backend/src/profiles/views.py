from django.shortcuts import render
from profiles.forms import StudentProfileForm, TeamMemberProfileForm
from utils.utils import render_message
from profiles.models import StudentProfile
from django.contrib.auth.decorators import login_required
from utils.login_decorators import team_user_required
from .models import TeamMemberProfile
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

@login_required
def view_profile(request):
    return render(request, 'profiles/view_profile.html')

# @login_required
# def update_student_profile(request):
#     if request.method=='POST':
#         if request.user.has_student_profile():#is_valid() returns false because there is a unique constrain on the entry_number
#             form = StudentProfileForm(request.POST)
#             # if form.is_valid():
#             student_profile = request.user.student_profile
#             student_profile.entry_number = form.data.get('entry_number')
#             student_profile.phone = form.data.get('phone')
#             student_profile.graduating_year = form.data.get('graduating_year')
#             student_profile.save()
#         else:
#             form = StudentProfileForm(request.POST)
#             if form.is_valid():
#                 student_profile = form.save(commit=False)
#                 student_profile.user = request.user
#                 try:
#                     student_profile.save()
#                 except:
#                     return render_message(request, 'Error', 'Could not update student profile')
#         return render_message(request, 'Profile Updated', 'Your profile was successfully updated!')
#     else:
#         form = StudentProfileForm()
#         context = {'form': form}
#         return render(request, 'profiles/student_profile_form.html', context=context)

@login_required
def update_student_profile(request):
    if request.user.has_student_profile():
        student_profile = StudentProfile.objects.get(user = request.user)
        if request.method=='POST':
            form = StudentProfileForm(request.POST,  instance=student_profile)
            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect(reverse('profiles:view_profile'))
        else:
            form = StudentProfileForm(instance=student_profile)
            context = {'form': form}
            return render(request, 'profiles/student_profile_form.html', context=context)
    else:
        if request.method=='POST':
            form = StudentProfileForm(request.POST)
            if form.is_valid():
                sp = form.save(commit=False)
                sp.user = request.user
                sp.save()
                return HttpResponseRedirect(reverse('profiles:view_profile'))
        else:
            form = StudentProfileForm()
            context = {'form': form}
            return render(request, 'profiles/student_profile_form.html', context=context)

@login_required
@team_user_required
def update_team_profile(request):
    team_profile = TeamMemberProfile.objects.get(user = request.user)
    if request.method=='POST':
        form = TeamMemberProfileForm(request.POST, request.FILES, instance=team_profile)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponseRedirect(reverse('profiles:view_profile'))
    else:
        form = TeamMemberProfileForm(instance=team_profile)
        context = {'form': form}
        return render(request, 'profiles/team_profile_form.html', context=context)