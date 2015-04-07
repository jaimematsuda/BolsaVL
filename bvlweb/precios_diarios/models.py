from django.db import models


class Precio_Diario(models.Model):
    anterior_fecha = models.DateField(null=True, blank=True)
    anterior = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    apertura = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    cierre = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    ex_derecho = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
		return "%s" % self.apertura