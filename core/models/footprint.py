from django.db import models
from django.utils.translation import gettext_lazy as _
from coreutils.models import CoreModel


class Footprint(CoreModel):
    footprint_x = models.SmallIntegerField(verbose_name=_(
        'Footprint X'), help_text=_('Unit footprint on X coordinate.'))
    footprint_z = models.SmallIntegerField(verbose_name=_(
        'Footprint Z'), help_text=_('Unit footprint on Z coordinate.'))

    def __str__(self):
        return f'{self.footprint_x}x{self.footprint_z}'

    class Meta:
        verbose_name = _('Footprint')
        verbose_name_plural = _('Footprints')
        ordering = ('-game_version', 'footprint_x', 'footprint_z')
        unique_together = ('game_version', 'footprint_x', 'footprint_z')
