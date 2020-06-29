from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('for_recruiters/0',views.for_recruiters0, name='for_recruiters/0'),
    path('for_recruiters/1',views.for_recruiters1, name='for_recruiters/1'),
    path('for_recruiters/2',views.for_recruiters2, name='for_recruiters/2'),
    path('for_recruiters/3',views.for_recruiters3, name='for_recruiters/3'),
    path('resources/',views.resources, name='resources'),
    path('team/',views.team, name='team_list'),
    path('news/news-detail/<int:pk>',views.news_detail, name='news-detail'),
    path('events/events-detail/<int:pk>',views.events_detail, name='events-detail'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
