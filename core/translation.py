from modeltranslation.translator import register, TranslationOptions
from .models import SiteSettings, NavbarItem, HeroSection, FooterSection, Testimonial

@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ('site_name',)

@register(NavbarItem)
class NavbarItemTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(HeroSection)
class HeroSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')

@register(FooterSection)
class FooterSectionTranslationOptions(TranslationOptions):
    fields = ('company_name', 'address')

@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('name', 'feedback')
