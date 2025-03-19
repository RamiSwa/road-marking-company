from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "publish_date", "slug")
    prepopulated_fields = {"slug": ("title",)}  # ✅ Auto-fill slug field in the Admin Panel
    search_fields = ("title", "content")
    list_filter = ("publish_date",)
