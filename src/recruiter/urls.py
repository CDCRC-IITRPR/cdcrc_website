from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'recruiter'

urlpatterns = [
    # path('register/',views.registerPage,name='register'),
    # path('login/',views.loginPage,name='login')
    # path('jaf/', views.jaf, name='jaf'),
    # path('jaf_details/<int:pk>/', views.jaf_details, name='jaf_details'),
    # path('jaf_details_pdf/<int:pk>/', views.jaf_details_pdf, name='jaf_details_pdf'),
    # path('jaf_details_simple_html/<int:pk>/', views.jaf_details_simple_html, name='jaf_details_simple_html'),
    # path('inf/', views.inf, name='inf'),
    # path('inf_details/<int:pk>/', views.inf_details, name='inf_details'),
    # path('inf_details_pdf/<int:pk>/', views.inf_details_pdf, name='inf_details_pdf'),
    # path('inf_details_simple_html/<int:pk>/', views.inf_details_simple_html, name='inf_details_simple_html'),
    path('why/',views.why_recruit, name='why'),
    path('recruiter_guide/',views.recruiter_guide, name='guide'),
    path('demographics/',views.student_demographics,name='student_demographics'), 
    path('six_month_internship/',views.six_month_internship, name='six_month_internship'), 
    path('joint_master_thesis/',views.joint_master_thesis, name='joint_master_thesis'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)