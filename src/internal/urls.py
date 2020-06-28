from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from internal import views

app_name = 'internal'

urlpatterns = [
    path('', views.internal_home, name='home'),
    path('add_contact/', views.add_contact, name='add_contact'),
    path('import_contacts_from_csv', views.import_contacts_from_csv, name='import_contacts_from_csv'),
] 