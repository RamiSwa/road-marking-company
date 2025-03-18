from django.shortcuts import render
from django.utils.translation import get_language
from .models import SiteSettings

def home(request):
    lang = get_language()  # Detects current language
    settings = SiteSettings.objects.first()

    return render(request, 'base.html', {
        'site_name': settings.site_name,  # Auto-detects translation
    })
