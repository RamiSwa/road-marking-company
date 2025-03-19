from django.shortcuts import render
from .models import SiteSettings, HeroSection, FooterSection, Testimonial

def home_view(request):
    site_settings = SiteSettings.objects.first()  # Get the first record (assuming one instance for global settings)
    hero_section = HeroSection.objects.first()  # Get homepage hero section data
    footer = FooterSection.objects.first()  # Get footer details
    testimonials = Testimonial.objects.all()  # Fetch all testimonials

    context = {
        "site_settings": site_settings,
        "hero_section": hero_section,
        "footer": footer,
        "testimonials": testimonials,
    }

    return render(request, "core/home.html", context)
