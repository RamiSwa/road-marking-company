from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):  
    model = ProjectImage
    extra = 1  # ✅ Allow adding multiple images in project admin panel

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "completion_date", "featured_image")
    search_fields = ("title", "description")
    list_filter = ("completion_date",)
    inlines = [ProjectImageInline]  # ✅ Enables adding multiple images inside project

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ("project", "image")
