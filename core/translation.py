from core.models import Unit
from modeltranslation.translator import TranslationOptions, register


@register(Unit)
class UnitTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
