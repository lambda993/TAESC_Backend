from django.db import models
from django.utils.translation import gettext_lazy as _
from coreutils.models import CoreModel


class SoundCategory(CoreModel):
    sound_name = models.CharField(verbose_name=_('Sound name'), max_length=20)

    def __str__(self):
        return self.sound_name

    class Meta:
        verbose_name = _('Sound category')
        verbose_name_plural = _('Sound categories')
        ordering = ('-game_version', 'sound_name')
        unique_together = ('game_version', 'sound_name')
