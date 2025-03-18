from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import SiteSettings, NavbarItem, HeroSection, FooterSection, Testimonial

@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    list_display = ("site_name", "contact_email", "phone_number")

@admin.register(NavbarItem)
class NavbarItemAdmin(TranslationAdmin):
    list_display = ("title", "url", "order")
    list_editable = ("order",)

@admin.register(HeroSection)
class HeroSectionAdmin(TranslationAdmin):
    list_display = ("title", "background_image")

@admin.register(FooterSection)
class FooterSectionAdmin(TranslationAdmin):
    list_display = ("company_name", "address", "contact_email")

@admin.register(Testimonial)
class TestimonialAdmin(TranslationAdmin):
    list_display = ("name", "feedback")
