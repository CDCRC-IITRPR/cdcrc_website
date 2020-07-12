from django.urls import path
from django.contrib.auth import views as auth_views
from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('view_profile/', views.view_profile, name='view_profile'),
    path('update_student_profile/', views.update_student_profile, name='update_student_profile'),
]
