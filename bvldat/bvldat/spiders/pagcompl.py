# -*- coding: utf-8 -*-
import scrapy


class PagcomplSpider(scrapy.Spider):
    name = "pagcompl"
    allowed_domains = ["bvl.com.pe"]
    start_urls = (
        'http://www.bvl.com.pe/includes/cotizaciones_todas.dat',
    )

    def parse(self, response):
        filename = 'prueba' #response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
