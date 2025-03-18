from django.db import models

class Category(models.Model):
    name_en = models.CharField(max_length=100, verbose_name="Category (English)")
    name_he = models.CharField(max_length=100, verbose_name="Category (Hebrew)")

    def __str__(self):
        return self.name_en

class Article(models.Model):
    title_en = models.CharField(max_length=200, verbose_name="Title (English)")
    title_he = models.CharField(max_length=200, verbose_name="Title (Hebrew)")
    slug = models.SlugField(unique=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="articles")

    content_en = models.TextField(verbose_name="Content (English)")
    content_he = models.TextField(verbose_name="Content (Hebrew)")

    featured_image = models.ImageField(upload_to="blog/", blank=True, null=True, verbose_name="Featured Image")

    author = models.CharField(max_length=100, verbose_name="Author", default="Admin")

    meta_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Meta Title (SEO)")
    meta_description = models.TextField(blank=True, null=True, verbose_name="Meta Description (SEO)")

    publish_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']  # Show newest articles first

    def __str__(self):
        return self.title_en
