from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.translation import gettext as _
from django.conf import settings
from .models import ContactMessage, ContactInfo
from .forms import ContactForm

def contact_view(request):
    """Handles the contact form submission and sends an email notification."""
    contact_info = ContactInfo.objects.first()  # Fetch contact details
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()

            # Send email notification
            subject = _("New Contact Message from") + f" {contact_message.name}"
            message = _(
                f"New message from {contact_message.name} ({contact_message.email}):\n\n"
                f"Phone: {contact_message.phone}\n"
                f"Message:\n{contact_message.message}"
            )
            recipient_list = [contact_info.email] if contact_info else [settings.EMAIL_HOST_USER]

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                recipient_list,
                fail_silently=False,
            )

            messages.success(request, _("Your message has been sent successfully!"))
            return redirect("contact")

    return render(request, "contacts/contact.html", {"form": form, "contact_info": contact_info})
