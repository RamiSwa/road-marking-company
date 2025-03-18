from django.contrib import admin
from .models import Page, SiteSetting, NavLink
from django.utils.html import format_html


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('company_name_en', 'phone', 'email', 'logo_preview', 'updated_at')
    readonly_fields = ('logo_preview', 'updated_at')

    fieldsets = (
        ("Company Details", {
            "fields": (
                "company_name_en", "company_name_he",
                "company_logo", "logo_preview",
                "phone", "email",
                "location_en", "location_he",
                "additional_locations_en", "additional_locations_he"
            ),
        }),
        ("Social Media Links", {
            "fields": ("facebook", "instagram", "linkedin", "whatsapp"),
        }),
        ("Footer Settings", {
            "fields": ("footer_text_en", "footer_text_he", "terms_url", "privacy_url"),
        }),
    )

    def logo_preview(self, obj):
        if obj.company_logo:
            return format_html('<img src="{}" width="100" height="auto" style="border-radius:5px;" />', obj.company_logo.url)
        return "No Logo Uploaded"
    
    logo_preview.short_description = "Logo Preview"
    
    

class PageAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'slug', 'order', 'created_at')
    prepopulated_fields = {'slug': ('title_en',)}
    ordering = ['order']



class NavLinkAdmin(admin.ModelAdmin):
    list_display = ('label_en', 'position', 'order')
    ordering = ['position', 'order']

admin.site.register(Page, PageAdmin)
admin.site.register(SiteSetting, SiteSettingAdmin)
admin.site.register(NavLink, NavLinkAdmin)
