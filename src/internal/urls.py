from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from internal import views

app_name = 'internal'

urlpatterns = [
    path('', views.internal_home, name='home'),
    path('approved_contacts_list/', views.approved_contacts_list, name='approved_contacts_list'),
    path('unapproved_contacts_list/', views.unapproved_contacts_list, name='unapproved_contacts_list'),
    path('contact_detail/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('import_contacts_from_csv/', views.import_contacts_from_csv, name='import_contacts_from_csv'),
    path('reject_contact_merge/', views.reject_contact_merge, name='reject_contact_merge'),
    path('approve_contact_merge/', views.approve_contact_merge, name='approve_contact_merge'),
    path('issues_list/', views.issues_list, name='issues_list'),
    path('issue_detail/<int:pk>/', views.issue_detail, name='issue_detail'),
    path('create_issue/', views.create_issue, name='create_issue'),
    path('close_issue/', views.close_issue, name='close_issue'),
    path('open_issue/', views.open_issue, name='open_issue'),

    path('create_issue_followup/<int:pk>/', views.create_issue_followup, name='create_issue_followup'),
] 