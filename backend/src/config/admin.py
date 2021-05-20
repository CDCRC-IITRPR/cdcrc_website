from django.contrib import admin
from .models import PageVisibilityConfig
# Register your models here.
def make_page_visible(modeladmin, request, queryset):
    queryset.update(visible=True)
make_page_visible.short_description = "Make these pages visible"

def make_page_invisible(modeladmin, request, queryset):
    queryset.update(visible=False)
make_page_invisible.short_description = "Make these pages invisible"

class PageVisibilityConfigAdmin(admin.ModelAdmin):
    list_display = ( 'page', 'visible')
    list_filter = ('page', )
    search_fields = ['page']
    actions = [make_page_visible, make_page_invisible]


admin.site.register(PageVisibilityConfig, PageVisibilityConfigAdmin)