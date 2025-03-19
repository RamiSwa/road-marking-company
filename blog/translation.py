from modeltranslation.translator import TranslationOptions, register
from .models import Article

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ("title", "content")  # ✅ Translating the Title & Content fields
