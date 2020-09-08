from django.contrib import admin
from .models import News,Events, Resource, ProfessionalDevelopmentActivity, ProfessionalDevelopmentBook, ProfessionalDevelopmentVideo, CorporateRelationsActivity
from .models import ResourceCategory, Department, ProfessionalDevelopmentInitiatives
# Register your models here.
admin.site.register(News)
admin.site.register(Events)
admin.site.register(Resource)
admin.site.register(ProfessionalDevelopmentActivity)
admin.site.register(ProfessionalDevelopmentBook)
admin.site.register(ProfessionalDevelopmentVideo)
admin.site.register(CorporateRelationsActivity)
admin.site.register(ResourceCategory)
admin.site.register(Department)
admin.site.register(ProfessionalDevelopmentInitiatives)