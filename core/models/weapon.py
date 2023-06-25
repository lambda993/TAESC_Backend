from coreutils.models import TranslatableCoreModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Weapon(TranslatableCoreModel):
    weapon_name = models.CharField(
        verbose_name=_('Weapon name'), max_length=20)

    def __str__(self):
        return self.weapon_name

    class Meta:
        verbose_name = _('Weapon')
        verbose_name_plural = _('Wrapons')
        ordering = ('weapon_name',)
