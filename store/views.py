from django.shortcuts import render
from .models import Product
from django.utils.translation import gettext as _

def product_list(request):
    """View to display all products in the store."""
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products, "page_title": _("Store")})
