from django.shortcuts import render

# Create your views here.
def student_register_view(request):
    return render(request, 'accounts/student_registration.html')

def recruiter_register_view(request):
    return render(request, 'accounts/recruiter_registration.html')
