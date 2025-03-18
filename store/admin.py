from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'external_link', 'created_at')

admin.site.register(Product, ProductAdmin)
