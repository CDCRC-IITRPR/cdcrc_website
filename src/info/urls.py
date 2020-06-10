from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('for_recruiters/',views.for_recruiters, name='for_recruiters'),
    path('news/news-detail/<int:pk>',views.news_detail, name='news-detail'),
    path('events/events-detail/<int:pk>',views.events_detail, name='events-detail'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
