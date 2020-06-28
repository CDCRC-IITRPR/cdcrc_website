from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('register/',views.registerPage,name='register'),
    # path('login/',views.loginPage,name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)