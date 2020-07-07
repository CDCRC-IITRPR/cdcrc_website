from django.contrib import admin
from .models import News,Events, Resource
# Register your models here.
admin.site.register(News)
admin.site.register(Events)
admin.site.register(Resource)