from django.db import models


class Negociacion(models.Model):
    cant_accion = models.PositiveIntegerField()
    cant_operacion = models.PositiveIntegerField()
    variacion = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    monto_negociado = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
		return "Accion %s, Operacion %s" % (self.cant_accion, self.cant_operacion)

