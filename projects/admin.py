from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Allows adding images directly inside a project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'status', 'created_at')
    prepopulated_fields = {'slug': ('title_en',)}
    inlines = [ProjectImageInline]

admin.site.register(Project, ProjectAdmin)
