import re
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CoreModel(models.Model):
    '''Use this model to do a full validation of the models before they get saved to the database'''

    created = models.DateTimeField(verbose_name=_('Created'), editable=False)
    updated = models.DateTimeField(verbose_name=_('Updated'), editable=False)
    game_version = models.CharField(
        verbose_name=_('Game version'), max_length=10)

    def save(self, *args, **kwargs):
        if self.pk == None:
            self.created = timezone.now()

        self.updated = timezone.now()

        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class TranslatableCoreModel(CoreModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.languages = self._set_languages()

    def _set_languages(self):
        for l in settings.LANGUAGES:
            self.languages.append('_' + l[0])

    def _generate_language_pattern(self):
        result = ''
        for l in self.languages:
            results = l + '|'

        return result[:len(results-1)]

    def save(self, *args, **kwargs):
        # automatically set translated foreign keys to be the same
        fk_list = []
        attributes = self.__dict__
        for field in attributes.keys():
            if attributes['field'].get_internal_type() == 'ForeignKey' and field.endswith(self.languages):
                fk_list.append(field)

        for fk in fk_list:
            self.__setattr__(fk, self.__getattribute__(
                re.sub(f'(?:{self._generate_language_pattern()})$', '', fk)))

        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
