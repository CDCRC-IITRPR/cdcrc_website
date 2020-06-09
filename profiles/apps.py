from django.apps import AppConfig
from . models import Profile
from django.contrib import admin


class ProfilesConfig(AppConfig):
    name = 'profiles'

admin.site.register(Profile)
