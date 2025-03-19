from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(_("Title"), max_length=255, default="Untitled Article")  # ✅ Increased length
    slug = models.SlugField(_("Slug"), unique=True, blank=True, max_length=255)  # ✅ Increased to avoid truncation
    content = models.TextField(_("Content"), default="No content available.")
    image = models.ImageField(_("Image"), upload_to="blog/", blank=True, null=True)
    publish_date = models.DateTimeField(_("Publish Date"), default=timezone.now)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ["-publish_date"]

    def save(self, *args, **kwargs):
        """Auto-generate slug from title if it's not provided"""
        if not self.slug:
            self.slug = slugify(self.title)[:255]  # ✅ Ensure it doesn't exceed 255 characters
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
