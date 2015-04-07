from django.db import models


class Precio_Historico(models.Model):
    maxima = models.DecimalField(max_digits=12, decimal_places=2)
    minima = models.DecimalField(max_digits=12, decimal_places=2)
    promedio = models.DecimalField(max_digits=12, decimal_places=2)
    active = models.BooleanField(default=True)

    def __unicode__(self):
		return "%s" % self.maxima

