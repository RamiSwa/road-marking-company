from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'category', 'author', 'publish_date')
    prepopulated_fields = {'slug': ('title_en',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_en',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
