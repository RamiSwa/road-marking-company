from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from .models import Article

def blog_list(request):
    """ View to list all blog articles """
    articles = Article.objects.all()
    return render(request, "blog/blog_list.html", {"articles": articles})

def blog_detail(request, slug):
    """ View for a single blog article """
    article = get_object_or_404(Article, slug=slug)
    return render(request, "blog/blog_detail.html", {"article": article})
