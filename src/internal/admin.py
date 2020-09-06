from django.contrib import admin
from internal.models import Issue, IssueFollowUp, Contact
# Register your models here.
admin.site.register(Issue)
admin.site.register(IssueFollowUp)


def approve_contacts(modeladmin, request, queryset):
    for contact in queryset:
        contact.approve = True
        contact.save()

approve_contacts.short_description = "Approve contacts"

class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'first_name', 'last_name', 'phone_one', 'email', 'recruiter', 'approved')
    actions = [approve_contacts]
    search_fields = ('first_name', 'last_name', 'email', 'phone_one', 'recruiter' )

admin.site.register(Contact, ContactAdmin)
