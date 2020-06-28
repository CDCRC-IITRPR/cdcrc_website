from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import student_register_view, recruiter_register_view
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('student_registration/', student_register_view, name='student_registration'),
    path('recruiter_registration/', recruiter_register_view, name='recruiter_registration'),

]
