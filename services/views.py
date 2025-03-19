from django.shortcuts import render
from django.utils.translation import gettext as _
from .models import Service

def services_view(request):
    """ Render the services page with translated content """
    services = Service.objects.all()
    return render(request, "services/services.html", {"services": services})
