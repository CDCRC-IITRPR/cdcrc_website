from django.contrib import admin
from .models import News,Events, Resource, ProfessionalDevelopmentActivity
# Register your models here.
admin.site.register(News)
admin.site.register(Events)
admin.site.register(Resource)
admin.site.register(ProfessionalDevelopmentActivity)