from django.db import models


class Nemonico(models.Model):
    name = models.CharField(unique=True, max_length=255)
    active = models.BooleanField(default=True)

    def __unicode__(self):
		return self.name