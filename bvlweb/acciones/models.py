from django.db import models
from empresas.models import Empresa 
from nemonicos.models import Nemonico 


class Accion(models.Model):
    empresa = models.ForeignKey(Empresa)
    nemonico = models.OneToOneField(Nemonico)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('empresa', 'nemonico')

    def __unicode__(self):
		return "%s, %s" % (self.empresa, self.nemonico)