from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='info'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    
    path('resources/',views.resources, name='resources'),
    path('resources/<str:category>/', views.resources_by_category, name='resources_by_category'),
    path('resource_detail/<int:pk>/', views.resource_detail, name='resource_detail'),

    path('faculty_team/',views.faculty_team, name='faculty_team'),
    path('student_team/',views.student_team, name='student_team'),

    path('news/news-detail/<int:pk>',views.news_detail, name='news-detail'),
    path('events/events-detail/<int:pk>',views.events_detail, name='events-detail'),
    path('directors_message/', views.directors_message, name='directors_message'),
    path('vision_statement/', views.vision_statement, name='vision_statement'),

    path('professional_development', views.professional_development_home, name="pd_home"),
    path('corporate_relations_development', views.corporate_relations_home, name="cr_home"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
