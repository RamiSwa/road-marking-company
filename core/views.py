from django.shortcuts import render
from .models import SiteSettings, HeroSection, FooterSection, Testimonial
from about.models import AboutSection, WhyChooseUs
from services.models import Service
from projects.models import Project
from store.models import Product
from blog.models import Article
from contacts.models import ContactInfo

def home_view(request):
    site_settings = SiteSettings.objects.first()  # Get the first record (assuming one instance for global settings)
    hero_section = HeroSection.objects.first()  # Get homepage hero section data
    footer = FooterSection.objects.first()  # Get footer details
    testimonials = Testimonial.objects.all()  # Fetch all testimonials
    about_section = AboutSection.objects.first()  
    services = Service.objects.all()[:3]
    projects = Project.objects.all()[:3]
    products = Product.objects.all()[:3]
    blog_posts = Article.objects.all()[:3]
    contact_info = ContactInfo.objects.first()

    context = {
        "site_settings": site_settings,
        "hero_section": hero_section,
        "footer": footer,
        "testimonials": testimonials,
        "about_section": about_section,
        "services": services,
        "projects": projects,
        "products": products,
        "blog_posts": blog_posts,
        "contact_info": ContactInfo
    }

    return render(request, "core/home.html", context)
