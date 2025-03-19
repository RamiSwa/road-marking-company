from django.contrib import admin
from .models import AboutSection, WhyChooseUs

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")

@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ("title", "icon")
    search_fields = ("title", "description")
