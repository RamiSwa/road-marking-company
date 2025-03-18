from django.db import models
from django.utils.translation import gettext_lazy as _

# 1️⃣ Site Settings: Stores global site-wide settings
class SiteSettings(models.Model):
    site_name = models.CharField(_("Site Name"), max_length=200)
    contact_email = models.EmailField(_("Contact Email"))
    phone_number = models.CharField(_("Phone Number"), max_length=20)
    facebook_link = models.URLField(_("Facebook Link"), blank=True, null=True)
    instagram_link = models.URLField(_("Instagram Link"), blank=True, null=True)
    whatsapp_number = models.CharField(_("WhatsApp Number"), max_length=20, blank=True, null=True)

    def __str__(self):
        return self.site_name

# 2️⃣ Navbar Items: Manages menu items dynamically
class NavbarItem(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    url = models.CharField(_("URL Path"), max_length=200)
    order = models.PositiveIntegerField(_("Order"), default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

# 3️⃣ Hero Section: Controls the homepage banner
class HeroSection(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    subtitle = models.TextField(_("Subtitle"), blank=True, null=True)
    background_image = models.ImageField(_("Background Image"), upload_to="hero_images/")

    def __str__(self):
        return self.title

# 4️⃣ Footer Section: Manages footer content
class FooterSection(models.Model):
    company_name = models.CharField(_("Company Name"), max_length=200)
    address = models.TextField(_("Address"))
    contact_email = models.EmailField(_("Contact Email"))
    phone_number = models.CharField(_("Phone Number"), max_length=20)

    def __str__(self):
        return self.company_name

# 5️⃣ Testimonials: Stores user feedback
class Testimonial(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    feedback = models.TextField(_("Feedback"))
    image = models.ImageField(_("User Image"), upload_to="testimonials/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - Testimonial"
