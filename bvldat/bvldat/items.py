# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field

from sectores.models import Sector
from empresas.models import Empresa

class BvldatItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class SectorItem(DjangoItem):
    django_model = Sector

class EmpresaItem(DjangoItem):
	django_model = Empresa