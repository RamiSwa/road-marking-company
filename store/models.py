from django.db import models

class Product(models.Model):
    title_en = models.CharField(max_length=200, verbose_name="Title (English)")
    title_he = models.CharField(max_length=200, verbose_name="Title (Hebrew)")

    short_description_en = models.TextField(verbose_name="Short Description (English)")
    short_description_he = models.TextField(verbose_name="Short Description (Hebrew)")

    external_link = models.URLField(verbose_name="Contact or Purchase Link")

    image = models.ImageField(upload_to="store/", blank=True, null=True, verbose_name="Product Image")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_en
