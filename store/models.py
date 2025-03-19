from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    """Product model for showcasing road marking equipment"""
    name = models.CharField(_("Product Name"), max_length=255, default="Unnamed Product")  # ✅ Default name
    image = models.ImageField(_("Product Image"), upload_to="store/", blank=True, null=True)  # ✅ Allow empty images
    description = models.TextField(_("Short Description"), blank=True, null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name
