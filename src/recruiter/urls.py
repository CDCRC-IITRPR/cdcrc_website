from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'recruiter'

urlpatterns = [
    # path('register/',views.registerPage,name='register'),
    # path('login/',views.loginPage,name='login')
    path('guide/',views.guide, name='guide'),
    path('jaf/', views.jaf, name='jaf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)