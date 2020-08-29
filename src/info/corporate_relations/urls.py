from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('about/', views.about, name='cr_about'),
    path('activities/', views.activities, name='cr_activities'),
    path('activity_detail/<int:pk>/', views.activity_detail, name='cr_activity_detail'),
    path('hod_message/', views.hod_message, name='cr_hod_message'),
]