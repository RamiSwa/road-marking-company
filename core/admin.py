from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.html import format_html
from .models import SiteSettings, HeroSection, FooterSection, Testimonial

@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    list_display = ("site_name", "logo_preview", "contact_email", "phone_number")

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:10px;" />', obj.logo.url)
        return "-"
    logo_preview.short_description = "Logo Preview"

@admin.register(HeroSection)
class HeroSectionAdmin(TranslationAdmin):
    list_display = ("title", "background_image")

@admin.register(FooterSection)
class FooterSectionAdmin(TranslationAdmin):
    list_display = ("company_name", "address", "contact_email", "phone_number")

@admin.register(Testimonial)
class TestimonialAdmin(TranslationAdmin):
    list_display = ("name", "feedback")
