from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'timestamp')
    search_fields = ('name', 'email', 'phone')

admin.site.register(ContactMessage, ContactMessageAdmin)
