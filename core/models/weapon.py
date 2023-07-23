from django.db import models
from django.utils.translation import gettext_lazy as _
from coreutils.models import CoreModel


class Weapon(CoreModel):
    weapon_name = models.CharField(
        verbose_name=_('Weapon name'), max_length=20)

    def __str__(self):
        return self.weapon_name

    class Meta:
        verbose_name = _('Weapon')
        verbose_name_plural = _('Wrapons')
        ordering = ('-game_version', 'weapon_name')
        unique_together = ('game_version', 'weapon_name')
