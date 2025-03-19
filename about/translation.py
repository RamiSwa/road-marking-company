from modeltranslation.translator import TranslationOptions, register
from .models import AboutSection, WhyChooseUs

@register(AboutSection)
class AboutSectionTranslationOptions(TranslationOptions):
    fields = ("title", "description")

@register(WhyChooseUs)
class WhyChooseUsTranslationOptions(TranslationOptions):
    fields = ("title", "description")
