from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='info'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    
    path('resources/',views.resources, name='resources'),
    path('resources/create/',views.create_resource, name='create_resource'),
    path('resources/detail/<int:pk>/', views.resource_detail, name='resource_detail'),

    path('faculty_team/',views.faculty_team, name='faculty_team'),
    path('student_team/',views.student_team, name='student_team'),

    path('news/news-detail/<int:pk>',views.news_detail, name='news-detail'),
    path('events/events-detail/<int:pk>',views.events_detail, name='events-detail'),
    path('directors_message/', views.directors_message, name='directors_message'),
    path('vision_statement/', views.vision_statement, name='vision_statement'),
    path('tnp_hod_message/', views.tnp_hod_message, name='tnp_hod_message'),
    # path('cr_hod_message/', views.cr_hod_message, name='cr_hod_message'),
    # path('pd_hod_message/', views.pd_hod_message, name='pd_hod_message'),

    path('professional_development/', include('info.professional_development.urls')),
    path('corporate_relations/', include('info.corporate_relations.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
