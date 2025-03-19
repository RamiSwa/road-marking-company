from django.contrib import admin
from .models import ContactMessage, ContactInfo
from django.utils.translation import gettext_lazy as _

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Admin panel configuration for Contact Messages"""
    list_display = ("name", "email", "phone", "timestamp")
    search_fields = ("name", "email", "phone")
    list_filter = ("timestamp",)
    readonly_fields = ("name", "email", "phone", "message", "timestamp")

    def has_add_permission(self, request):
        """Disable adding new messages from the admin panel"""
        return False

    def has_change_permission(self, request, obj=None):
        """Disable editing messages from the admin panel"""
        return False

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    """Admin panel configuration for Contact Information"""
    list_display = ("email", "phone")
    fieldsets = (
        (_("Contact Details"), {"fields": ("address", "email", "phone")}),
    )

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of contact info (only editable)"""
        return False
