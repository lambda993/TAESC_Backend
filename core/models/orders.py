from coreutils.models import CoreModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class UnitOrder(CoreModel):
    name = models.CharField(verbose_name=_('Name'), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Unit order')
        verbose_name_plural = _('Unit orders')
        ordering = ('-game_version', 'name')
        unique_together = ('game_version', 'name')
