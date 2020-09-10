from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('about/', views.about, name='pd_about'),
    path('activities/', views.activities, name='pd_activities'),
    path('activity_detail/<int:pk>/', views.activity_detail, name='pd_activity_detail'),
    path('initiative_detail/<int:pk>/', views.initiative_detail, name='pd_initiative_detail'),
    path('books/', views.books, name='pd_books'),
    path('videos/', views.videos, name='pd_videos'),
    path('hod_message/', views.hod_message, name='pd_hod_message'),
    path('pg_resources/', views.pg_resources, name='pd_pg_resources'),
    path('initiatives/', views.initiatives, name='pd_initiatives'),

]