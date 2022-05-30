"""

fsc_contact/admin.py: Admin models for contactAdmin.

"""

# - - - - - Django Imports - - - - - - - - -
from django.contrib import admin

# - - - - - Internal imports - - - - - - - -
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Admin class to display email subject and message
    """
    list_display = (
        'email',
        'subject',
        'message'
    )


admin.site.register(Contact, ContactAdmin)
