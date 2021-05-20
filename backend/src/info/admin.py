from django.contrib import admin
from .models import News,Events, Resource, ProfessionalDevelopmentActivity, ProfessionalDevelopmentBook, ProfessionalDevelopmentVideo, CorporateRelationsActivity
from .models import ResourceCategory, Department, ProfessionalDevelopmentInitiatives, ResourceImage, ContactUsResponse
# Register your models here.

def approve_resources(modeladmin, request, queryset):
    for resource in queryset:
        resource.approved = True
        resource.save()

approve_resources.short_description = "Approve resources"

class ResourceAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'author', 'approved', 'datetime')
    actions = [approve_resources]
    search_fields = ('title', 'author', 'approved', 'datetime')

admin.site.register(Resource, ResourceAdmin)

admin.site.register(News)
admin.site.register(Events)
admin.site.register(ProfessionalDevelopmentActivity)
admin.site.register(ProfessionalDevelopmentBook)
admin.site.register(ProfessionalDevelopmentVideo)
admin.site.register(CorporateRelationsActivity)
admin.site.register(ResourceCategory)
admin.site.register(ResourceImage)
admin.site.register(Department)
admin.site.register(ProfessionalDevelopmentInitiatives)
admin.site.register(ContactUsResponse)