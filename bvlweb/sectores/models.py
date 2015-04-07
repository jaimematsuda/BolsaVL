from django.db import models


class Sector(models.Model):
    name = models.CharField(unique=True, max_length=100)
    active = models.BooleanField(default=True)    

    def __unicode__(self):
		return self.name