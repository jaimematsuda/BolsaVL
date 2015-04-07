from django.db import models
from sectores.models import Sector

class Empresa(models.Model):
    name = models.CharField(unique=True, max_length=255)
    sector = models.ForeignKey(Sector)
    active = models.BooleanField(default=True) 

    def __unicode__(self):
		return self.name  