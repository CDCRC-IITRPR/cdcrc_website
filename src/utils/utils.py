from django.template.loader import render_to_string
from django.shortcuts import render

def render_message(request, title , message):
    return render(request, 'message.html', context={'title': title, 'message': message})