from django.contrib import admin
from .models import Recruiter, JAF, INF #,JobOpportunity,InternshipOpportunity
# Register your models here.

def make_recruiter_visible(modeladmin, request, queryset):
    queryset.update(visible=True)
make_recruiter_visible.short_description = "Make recruiters visible in past recruiters on home page"

class RecruiterAdmin(admin.ModelAdmin):
    empty_value_display = "NA"
    list_display = ( 'name', 'visible')
    list_filter = ('visible', )
    search_fields = ['name']
    actions = [make_recruiter_visible]


admin.site.register(Recruiter, RecruiterAdmin)
admin.site.register(JAF)
admin.site.register(INF)
