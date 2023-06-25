from coreutils.models import CoreModel
from django.db import models


class UnitSide(CoreModel):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
