from django import forms
from .models import ContactMessage
from django.utils.translation import gettext_lazy as _

class ContactForm(forms.ModelForm):
    """Form for users to send contact messages"""
    class Meta:
        model = ContactMessage
        fields = ["name", "phone", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": _("Your Name")}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": _("Your Phone Number")}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": _("Your Email")}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": _("Your Message")}),
        }
        labels = {
            "name": _("Full Name"),
            "phone": _("Phone Number"),
            "email": _("Email Address"),
            "message": _("Message"),
        }
