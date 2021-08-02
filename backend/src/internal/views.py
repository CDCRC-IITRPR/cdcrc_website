from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from internal.forms import ImportContactsForm, ContactForm, IssueFollowupForm, IssueForm
from utils.login_decorators import team_user_required
from internal.contacts import ContactsCSVHandler
from profiles.models import TeamMemberProfile
from internal.models import Contact, Issue, IssueFollowUp
from django.urls import reverse
from utils.mailer import Mailer
import datetime
from utils.utils import render_message

# Create your views here.

@team_user_required
def internal_home(request):
    team_member_profile_obj = TeamMemberProfile.objects.get(user=request.user)
    return render(request, 'internal/home.html', context={'team_member_profile_obj':team_member_profile_obj})

@team_user_required
def update_contact(request, pk):
    contact = Contact.objects.get(pk = pk)
    if request.method=='POST':
        form = ContactForm(request.POST,  instance=contact)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('internal:approved_contacts_list'))
    else:
        form = ContactForm(instance=contact)
    return render(request, 'internal/update_contact.html', context={'form':form})

@team_user_required
def add_contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('internal:unapproved_contacts_list'))
    else:
        form = ContactForm()
    return render(request, 'internal/add_contact.html', context={'form':form})

@team_user_required
def import_contacts_from_csv(request):
    if request.method=='POST':
        form = ImportContactsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                contact_handler = ContactsCSVHandler(request.FILES['contacts_file'], request.encoding)
                contact_handler.import_from_file()
                return HttpResponseRedirect(reverse('internal:unapproved_contacts_list'))
            except:
                return render_message(request, 'Error', 'There was an error...pls check the format of your file')
        else:
            return render_message(request, 'Error', 'There was an error...pls check the format of your file')

    else:
        form = ImportContactsForm()
    return render(request, 'internal/import_contacts_from_csv.html', context={'form':form})

@team_user_required
def approved_contacts_list(request):
    approved_contacts = Contact.objects.filter(approved=True)

    context = {
        'approved_contacts': approved_contacts,
    }

    return render(request, 'internal/approved_contacts_list.html', context=context)

@team_user_required
def unapproved_contacts_list(request):
    unapproved_contacts = Contact.objects.filter(approved=False)

    context = {
        'unapproved_contacts': unapproved_contacts,
    }

    return render(request, 'internal/unapproved_contacts_list.html', context=context)


@team_user_required
def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)

    context = {
        'contact': contact,
    }

    return render(request, 'internal/contact_detail.html', context=context)

@team_user_required
def reject_contact_merge(request):
    if request.method=='POST':
        contact = Contact.objects.get(pk=int(request.POST['contact_id']))
        contact.delete()

    return HttpResponseRedirect(reverse('internal:unapproved_contacts_list'))

@team_user_required
def approve_contact_merge(request):
    if request.method=='POST':
        contact = Contact.objects.get(pk=int(request.POST['contact_id']))
        contact.approved = True
        contact.save()

    return HttpResponseRedirect(reverse('internal:unapproved_contacts_list'))

@team_user_required
def issues_list(request):
    issues = Issue.objects.all()
    context = {'issues': issues}
    return render(request, 'internal/issues_list.html', context=context)

@team_user_required
def issue_detail(request, pk):
    issue = Issue.objects.get(pk=pk)
    followups = issue.followups.all()
    context = {'issue': issue, 'followups': followups}
    return render(request, 'internal/issue_detail.html', context=context)

@team_user_required
def create_issue(request):
    if request.method=='POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue_obj =  form.save(commit=False)
            issue_obj.status = 'open'
            team_member_profile = TeamMemberProfile.objects.get(user=request.user)
            issue_obj.creator = team_member_profile
            issue_obj.save()
            for assignee in request.POST.getlist('assignees'):
                issue_obj.assignees.add(TeamMemberProfile.objects.get(pk=int(assignee)))
            issue_obj.save()

            mailer = Mailer()

            #send mail alert to the creator of this issue
            mailer.send_issue_create_alert_to_creator(
                [request.user.email],
                request.user.first_name + " " + request.user.last_name,
                'CDPC System Alert: ' +issue_obj.title,
                issue_obj.title,
                issue_obj.priority.upper(),
                issue_obj.get_detail_url(request)
            )
            #send mail alert to the assignees
            for assignee in issue_obj.assignees.all():
                mailer.send_issue_create_alert_to_assignee(
                    [assignee.user.email], 
                    assignee.user.first_name + " " + assignee.user.last_name,
                    'CDPC System Alert: ' +issue_obj.title,
                    issue_obj.title,
                    issue_obj.priority.upper(),
                    issue_obj.get_detail_url(request)
                )

            return HttpResponseRedirect(reverse('internal:issue_detail',kwargs={'pk':issue_obj.pk}))
    else:
        form = IssueForm()
    return render(request, 'internal/create_issue.html', context={'form':form})

@team_user_required
def close_issue(request):
    if request.method=='POST':
        pk = request.POST['issue_id']
        issue = Issue.objects.get(pk=pk)
        issue.status = 'closed'
        mailer = Mailer()
        mailer.send_issue_close_alert_to_creator(
            [issue.creator.user.email], 
            issue.creator.user.first_name + " " + issue.creator.user.last_name,
            request.user.first_name + " " + request.user.last_name,
            'CDPC System Alert: '+ issue.title,
            issue.title,
            issue.get_detail_url(request)
        )

        mailer.send_issue_close_alert_to_closer(
            [issue.creator.user.email], 
            request.user.first_name + " " + request.user.last_name,
            'CDPC System Alert: '+ issue.title,
            issue.title,
            issue.get_detail_url(request)
        )

        issue.save()

    return HttpResponseRedirect(reverse('internal:issue_detail', kwargs={'pk': pk}))

@team_user_required
def open_issue(request):
    if request.method=='POST':
        pk = request.POST['issue_id']
        issue = Issue.objects.get(pk=pk)
        issue.status = 'open'
        issue.save()
        mailer = Mailer()
        #send open alert to creator
        mailer.send_issue_open_alert_to_creator(
            [issue.creator.user.email], 
            issue.creator.user.first_name + " " + issue.creator.user.last_name,
            request.user.first_name + " " + request.user.last_name,
            'CDPC System Alert: '+ issue.title,
            issue.title,
            issue.get_detail_url(request)
        )

    return HttpResponseRedirect(reverse('internal:issue_detail', kwargs={'pk': pk}))

@team_user_required
def create_issue_followup(request, pk):
    if request.method=='POST':
        form = IssueFollowupForm(request.POST)
        if form.is_valid():
            next_reminder = datetime.datetime.strptime(request.POST['next_reminder'], '%m/%d/%Y %H:%M').strftime('%Y-%m-%d %H:%M')
            print(next_reminder)
            followup_obj = form.save(commit=False)
            issue_obj = Issue.objects.get(pk=pk)
            followup_obj.issue = issue_obj
            issue_obj.next_reminder = next_reminder
            issue_obj.save()
            followup_obj.save()
            for assignee in request.POST.getlist('assignees'):
                followup_obj.assignees.add(TeamMemberProfile.objects.get(pk=int(assignee)))
            followup_obj.save()

            mailer = Mailer()

            #alert the assignees
            for assignee in followup_obj.assignees.all():
                #send alert via mail to the assignees
                mailer.send_issue_followup_alert_to_assignee(
                    [assignee.user.email], 
                    assignee.user.first_name + " " + assignee.user.last_name,
                    'CDPC System Alert: '+ followup_obj.issue.title,
                    followup_obj.issue.title,
                    followup_obj.comment,
                    followup_obj.get_detail_url(request)
                )
            #alert the creator
            mailer.send_issue_followup_alert_to_creator(
                [followup_obj.issue.creator.user.email], 
                request.user.first_name + " " + request.user.last_name,
                'CDPC System Alert: '+ followup_obj.issue.title,
                followup_obj.issue.title,
                followup_obj.comment,
                followup_obj.get_detail_url(request)
            )

            mailer.send_issue_followup_alert_to_follower(
                [request.user.email], 
                request.user.first_name + " " + request.user.last_name,
                'CDPC System Alert: '+ followup_obj.issue.title,
                followup_obj.issue.title,
                followup_obj.comment,
                followup_obj.get_detail_url(request)
            )

            return HttpResponseRedirect(reverse('internal:issue_detail', kwargs={'pk':pk}))
    else:
        form = IssueFollowupForm()
    return render(request, 'internal/create_issue_followup.html', context={'form':form})