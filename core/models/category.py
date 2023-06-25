from coreutils.models import CoreModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class UnitCategory(CoreModel):
    name = models.CharField(verbose_name=_('Name'), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Unit category')
        verbose_name_plural = _('Unit categories')
        ordering = ('name',)
