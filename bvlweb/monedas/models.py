from django.db import models


class Moneda(models.Model):
    name = models.CharField(max_length=255, blank=True)
    simbolo = models.CharField(max_length=45)
    active = models.BooleanField(default=True)

    def __unicode__(self):
		return self.simbolo
