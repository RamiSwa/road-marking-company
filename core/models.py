from django.db import models
from django.utils.translation import gettext_lazy as _

class SiteSettings(models.Model):
    site_name = models.CharField(_("Site Name"), max_length=200)
    contact_email = models.EmailField(_("Contact Email"))
    phone_number = models.CharField(_("Phone Number"), max_length=20)

    def __str__(self):
        return self.site_name
