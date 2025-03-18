from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    title_en = models.CharField(max_length=200, verbose_name="Title (English)")
    title_he = models.CharField(max_length=200, verbose_name="Title (Hebrew)")
    slug = models.SlugField(unique=True)

    description_en = models.TextField(verbose_name="Description (English)")
    description_he = models.TextField(verbose_name="Description (Hebrew)")

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')

    main_image = models.ImageField(upload_to="projects/main/", verbose_name="Main Image", blank=True, null=True)
    
    meta_title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Meta Title (SEO)")
    meta_description = models.TextField(blank=True, null=True, verbose_name="Meta Description (SEO)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']  # Show newest projects first

    def __str__(self):
        return self.title_en

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="projects/gallery/", verbose_name="Additional Image")
    caption = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.project.title_en}"
