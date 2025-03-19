from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Service

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('title',)
