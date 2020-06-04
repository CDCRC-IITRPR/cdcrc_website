from django.shortcuts import render

# Create your views here.
def team_list(request):
    return render(request, 'team/team_list.html')