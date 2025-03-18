from django.db import models
from django.utils.translation import gettext_lazy as _

# ✅ 1️⃣ Site Settings: Stores global site-wide settings
class SiteSettings(models.Model):
    site_name = models.CharField(_("Site Name"), max_length=200)
    logo = models.ImageField(_("Company Logo"), upload_to="logos/", blank=True, null=True)
    contact_email = models.EmailField(_("Contact Email"))
    phone_number = models.CharField(_("Phone Number"), max_length=20)
    facebook_link = models.URLField(_("Facebook Link"), blank=True, null=True)
    instagram_link = models.URLField(_("Instagram Link"), blank=True, null=True)
    whatsapp_number = models.CharField(_("WhatsApp Number"), max_length=20, blank=True, null=True)
    company_location = models.CharField(_("Company Location"), max_length=255, blank=True, null=True)

    def __str__(self):
        return self.site_name


# ✅ 2️⃣ Hero Section: Homepage banner content
class HeroSection(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    subtitle = models.TextField(_("Subtitle"), blank=True, null=True)
    background_image = models.ImageField(_("Background Image"), upload_to="hero_images/")

    def __str__(self):
        return self.title


# ✅ 3️⃣ Footer Section: Editable company details for the footer
class FooterSection(models.Model):
    company_name = models.CharField(_("Company Name"), max_length=200)
    address = models.TextField(_("Address"))
    contact_email = models.EmailField(_("Contact Email"))
    phone_number = models.CharField(_("Phone Number"), max_length=20)

    def __str__(self):
        return self.company_name


# ✅ 4️⃣ Testimonials: Customer reviews stored dynamically
class Testimonial(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    feedback = models.TextField(_("Feedback"))
    image = models.ImageField(_("User Image"), upload_to="testimonials/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - Testimonial"
