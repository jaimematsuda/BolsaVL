from django.db import models
from acciones.models import Accion 
from monedas.models import Moneda
from precios_diarios.models import Precio_Diario
from precios_historicos.models import Precio_Historico
from propuestas.models import Propuesta
from negociaciones.models import Negociacion


class Cotizacion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    accion = models.ForeignKey(Accion)
    moneda = models.ForeignKey(Moneda)
    precio_diario = models.OneToOneField(Precio_Diario)
    precio_historico = models.OneToOneField(Precio_Historico, null=True, blank=True)
    propuesta = models.OneToOneField(Propuesta)
    negociacion = models.OneToOneField(Negociacion)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('fecha', 'accion', 'precio_diario', 'propuesta', 'negociacion')

    def __unicode__(self):
        return "%s" % self.fecha