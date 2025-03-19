from django.shortcuts import render
from .models import AboutSection, WhyChooseUs

def about_view(request):
    about_section = AboutSection.objects.first()  # Get the first About section entry
    why_choose_us = WhyChooseUs.objects.all()  # Fetch all reasons
    
    context = {
        "about_section": about_section,
        "why_choose_us": why_choose_us,
    }
    return render(request, "about/about.html", context)
