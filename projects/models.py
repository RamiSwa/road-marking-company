from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    completion_date = models.DateField(_("Completion Date"), default=timezone.now)
    featured_image = models.ImageField(_("Featured Image"), upload_to="projects/", blank=True, null=True)  # ✅ Main Image

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="gallery_images")  # ✅ Links to project
    image = models.ImageField(_("Gallery Image"), upload_to="projects/gallery/")

    def __str__(self):
        return f"{self.project.title} - Image {self.id}"
