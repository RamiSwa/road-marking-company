from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactMessage(models.Model):
    """Stores contact form messages from users."""
    name = models.CharField(_("Full Name"), max_length=100)
    phone = models.CharField(_("Phone Number"), max_length=15)
    email = models.EmailField(_("Email Address"))
    message = models.TextField(_("Message"))
    timestamp = models.DateTimeField(_("Sent At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Contact Message")
        verbose_name_plural = _("Contact Messages")
        ordering = ["-timestamp"]

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class ContactInfo(models.Model):
    """Editable company contact details for the contact page."""
    address = models.TextField(_("Address"))
    email = models.EmailField(_("Contact Email"))
    phone = models.CharField(_("Phone Number"), max_length=20)

    class Meta:
        verbose_name = _("Contact Information")
        verbose_name_plural = _("Contact Information")

    def __str__(self):
        return str(_("Company Contact Details"))  # ✅ Fix: Ensure it returns a proper string
