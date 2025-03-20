from .models import FooterSection

def footer_context(request):
    footer = FooterSection.objects.first()
    return {'footer': footer}
