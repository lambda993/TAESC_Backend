from coreutils.models import CoreModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class TEDClass(CoreModel):
    name = models.CharField(verbose_name=_('Name'), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('TED Class')
        verbose_name_plural = _('TED Classes')
        ordering = ('-game_version', 'name')
        unique_together = ('game_version', 'name')
