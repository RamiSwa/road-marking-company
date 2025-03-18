from modeltranslation.translator import register, TranslationOptions
from .models import SiteSettings, HeroSection, FooterSection, Testimonial

@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('site_name', 'company_location')  # ✅ Translatable fields

@register(HeroSection)
class HeroSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')  # ✅ Translatable fields

@register(FooterSection)
class FooterSectionTranslationOptions(TranslationOptions):
    fields = ('company_name', 'address')  # ✅ Translatable fields

@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('name', 'feedback')  # ✅ Translatable fields
