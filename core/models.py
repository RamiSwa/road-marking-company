from django.db import models

class Page(models.Model):
    title_en = models.CharField(max_length=200, verbose_name="Title (English)")
    title_he = models.CharField(max_length=200, verbose_name="Title (Hebrew)")
    slug = models.SlugField(unique=True)
    content_en = models.TextField(verbose_name="Content (English)")
    content_he = models.TextField(verbose_name="Content (Hebrew)")

    banner_image = models.ImageField(upload_to="banners/", blank=True, null=True, verbose_name="Banner Image")
    order = models.PositiveIntegerField(default=0, verbose_name="Menu Order")

    meta_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Meta Title (SEO)")
    meta_description = models.TextField(blank=True, null=True, verbose_name="Meta Description (SEO)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']  # Ensures pages display in custom order

    def __str__(self):
        return self.title_en



class SiteSetting(models.Model):
    company_name_en = models.CharField(max_length=200, verbose_name="Company Name (English)", default="ProMark Road Marking")
    company_name_he = models.CharField(max_length=200, verbose_name="Company Name (Hebrew)", default="פרומארק סימון כבישים")

    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    location_en = models.TextField(verbose_name="Main Office Location (English)", default="123 Highway Ave, New York, NY")
    location_he = models.TextField(verbose_name="Main Office Location (Hebrew)", default="רחוב 123 היייווי, ניו יורק, ארה\"ב")

    additional_locations_en = models.TextField(blank=True, null=True, verbose_name="Additional Locations (English)")
    additional_locations_he = models.TextField(blank=True, null=True, verbose_name="Additional Locations (Hebrew)")

    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)

    footer_text_en = models.TextField(blank=True, null=True, verbose_name="Footer Text (English)", default="Precision & Safety in Every Line")
    footer_text_he = models.TextField(blank=True, null=True, verbose_name="Footer Text (Hebrew)", default="דיוק ובטיחות בכל קו")

    terms_url = models.URLField(blank=True, null=True, verbose_name="Terms & Conditions URL")
    privacy_url = models.URLField(blank=True, null=True, verbose_name="Privacy Policy URL")

    company_logo = models.ImageField(upload_to="logos/", blank=True, null=True, verbose_name="Company Logo")

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name_en


class NavLink(models.Model):
    POSITION_CHOICES = [
        ('header', 'Header'),
        ('footer', 'Footer'),
    ]
    
    label_en = models.CharField(max_length=100, verbose_name="Label (English)")
    label_he = models.CharField(max_length=100, verbose_name="Label (Hebrew)")
    url = models.URLField(verbose_name="URL")
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.label_en} ({self.position})"
