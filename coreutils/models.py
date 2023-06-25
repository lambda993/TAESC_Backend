from django.db import models
from django.utils import timezone

# Create your models here.


class CoreModel(models.Model):
    '''Use this model to do a full validation of the models before they get saved to the database'''

    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if self.pk == None:
            self.created = timezone.now()

        self.updated = timezone.now()

        self.full_clean()
        return super().save(args, kwargs)
