from coreutils.models import CoreModel
from django.db import models


class MovementClass(CoreModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
