from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import SiteSettings

@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    list_display = ('site_name',)
