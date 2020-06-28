# from django.shortcuts import render,redirect
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