from modeltranslation.translator import TranslationOptions, register
from .models import Project

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')  # ✅ These fields will be translated
