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
