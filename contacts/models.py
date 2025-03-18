from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(verbose_name="Email Address")
    message = models.TextField(verbose_name="Message")

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
