from django.db import models


class CoreModel(models.Model):
    '''Use this model to do a full validation of the models before they get saved to the database'''

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(args, kwargs)
