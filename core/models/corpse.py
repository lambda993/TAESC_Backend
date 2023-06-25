from coreutils.models import TranslatableCoreModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Corpse(TranslatableCoreModel):
    corpse_name = models.CharField(
        verbose_name=_('Corpse name'), max_length=20)

    def __str__(self):
        return self.corpse_name

    class Meta:
        verbose_name = _('Corpse')
        verbose_name_plural = _('Corpses')
        ordering = ('corpse_name',)
