from django.db import models


class Propuesta(models.Model):
    compra = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)
    venta = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
		return "%s" % self.compra