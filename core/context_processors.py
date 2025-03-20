from .models import FooterSection
from .models import SiteSettings


def footer_context(request):
    footer = FooterSection.objects.first()
    return {'footer': footer}

def site_settings_context(request):
    return {'site_settings': SiteSettings.objects.first()}