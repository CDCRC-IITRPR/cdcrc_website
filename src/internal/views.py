from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from internal.forms import ImportContactsForm, AddContactForm
from utils.login_decorators import team_user_required
from internal.contacts import ContactsCSVHandler
from profiles.models import TeamMemberProfile
# Create your views here.

@team_user_required
def internal_home(request):
    team_member_profile_obj = TeamMemberProfile.objects.get(user=request.user)
    return render(request, 'internal/home.html', context={'team_member_profile_obj':team_member_profile_obj})

@team_user_required
def add_contact(request):
    if request.method=='POST':
        form = AddContactForm(request.POST)
        if form.is_valid():
            print(request.POST)
            return HttpResponse('Contact Added')
    else:
        form = AddContactForm()
    return render(request, 'internal/add_contact.html', context={'form':form})

@team_user_required
def import_contacts_from_csv(request):
    if request.method=='POST':
        form = ImportContactsForm(request.POST, request.FILES)
        if form.is_valid():
            contact_handler = ContactsCSVHandler(request.FILES['contacts_file'], request.encoding)
            contact_handler.import_from_file()
            # print(request.FILES['contacts_file'])
            return HttpResponse('Contacts Uploaded') 

    else:
        form = ImportContactsForm()
    return render(request, 'internal/import_contacts_from_csv.html', context={'form':form})