from django.contrib import admin
from .models import Page, SiteSetting, NavLink

class PageAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'slug', 'order', 'created_at')
    prepopulated_fields = {'slug': ('title_en',)}
    ordering = ['order']

class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'phone', 'email', 'updated_at')

class NavLinkAdmin(admin.ModelAdmin):
    list_display = ('label_en', 'position', 'order')
    ordering = ['position', 'order']

admin.site.register(Page, PageAdmin)
admin.site.register(SiteSetting, SiteSettingAdmin)
admin.site.register(NavLink, NavLinkAdmin)
