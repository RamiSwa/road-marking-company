from django.db import models
from django.utils.translation import gettext_lazy as _

class Service(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    icon = models.CharField(_("Icon Class"), max_length=100, help_text=_("FontAwesome or Bootstrap Icons class"))

    def __str__(self):
        return self.title
