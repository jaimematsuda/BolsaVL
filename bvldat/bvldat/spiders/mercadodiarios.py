# -*- coding: utf-8 -*-
import scrapy
from bvldat.items import SectorItem
import datetime
import time

import django
django.setup()
from sectores.models import Sector
from empresas.models import Empresa
from nemonicos.models import Nemonico 
from acciones.models import Accion
from negociaciones.models import Negociacion
from monedas.models import Moneda
from precios_diarios.models import Precio_Diario 
from propuestas.models import Propuesta
from cotizaciones.models import Cotizacion 


class MercadodiariosSpider(scrapy.Spider):
    name = "mercadodiarios"
    allowed_domains = ["bvl.com.pe"]
    start_urls = (
        'http://www.bvl.com.pe/includes/cotizaciones_todas.dat',
    )

    def parse(self, response):

        for sel in response.xpath('//tr') :

            sect = sel.xpath('td[4]/text()').extract()
            nemo = sel.xpath('td[3]/text()').extract()
            ante = sel.xpath('td[5]/text()').extract()
            anfe = sel.xpath('td[6]/text()').extract()
            apet = sel.xpath('td[7]/text()').extract()
            exde = sel.xpath('td[8]/text()').extract()
            cier = sel.xpath('td[9]/text()').extract()
            comp = sel.xpath('td[10]/text()').extract()
            vent = sel.xpath('td[11]/text()').extract()
            cacc = sel.xpath('td[12]/text()').extract()
            cope = sel.xpath('td[13]/text()').extract()
            vari = sel.xpath('td[14]/text()').extract()
            mone = sel.xpath('td[15]/text()').extract()
            nego = sel.xpath('td[16]/text()').extract()

            for n in nego:

                numero = n

                if not numero == u'\xa0':

                    if len(sel.xpath('td[2]/text()').extract()) == 0:
                        empr = sel.xpath('td[2]/a/text()').extract()
                    else:
                        empr = sel.xpath('td[2]/text()').extract()

                    for se, ne, em, an, af, ap, ex, \
                        ci, co, ve, ca, cp, va, mo, ng in \
                        zip(sect, nemo, empr, ante, anfe, apet, exde, \
                            cier, comp, vent, cacc, cope, vari, mone, nego):

                        sector = se.encode('utf-8')
                        nemonico = ne.encode('utf-8')
                        empresa = em.encode('utf-8')
                        anterior = an.encode('utf-8')
                        an_fe = af.encode('utf-8')
                        for afw in anfe:
                            if not afw ==  u'\xa0':
                                anterior_fecha = time.strftime(
                                    "%Y-%m-%d", time.strptime(an_fe, "%d/%m/%Y"
                                        ))
                        apertura = ap.encode('utf-8')
                        ex_derecho = ex.encode('utf-8')
                        cierre = ci.encode('utf-8')
                        compra = co.encode('utf-8')
                        venta = ve.encode('utf-8')
                        canacc = ca.encode('utf-8')
                        cant_accion = canacc.replace(",", "")
                        canope = cp.encode('utf-8')
                        cant_operacion = canope.replace(",", "")
                        variacion = va.encode('utf-8')
                        moneda = mo.encode('utf-8')
                        monneg = ng.encode('utf-8')
                        monto_negociado = monneg.replace(",", "")

                        print empresa

                        if len(Sector.objects.filter(name=sector).values()) == 0:
                            if len(sector) == 0:
                                sectorsv = Sector()
                                sectorsv.name = 'N/A'
                            else:
                                sectorsv = Sector()
                                sectorsv.name = sector
                            sectorsv.save()
                        sectorid = Sector.objects.get(name=sector)

                        if len(Nemonico.objects.filter(name=nemonico).values()) == 0:
                            if len(nemonico) == 0:
                                nemonicosv = Nemonico()
                                nemonicosv.name = 'N/A'
                            else:
                                nemonicosv = Nemonico()
                                nemonicosv.name = nemonico
                            nemonicosv.save()      
                        nemonicoid = Nemonico.objects.get(name=nemonico)

                        if len(Empresa.objects.filter(name=empresa).values()) == 0:
                            empresasv = Empresa()
                            empresasv.name = empresa
                            empresasv.sector = sectorid
                            empresasv.save()
                        empresaid = Empresa.objects.get(name=empresa)

                        if len(Accion.objects.filter(empresa=empresaid, 
                                                     nemonico=nemonicoid
                                                     ).values()) == 0:
                            accionsv = Accion()
                            accionsv.empresa = empresaid
                            accionsv.nemonico = nemonicoid
                            accionsv.save()
                        accionid = Accion.objects.get(empresa=empresaid, 
                                                      nemonico=nemonicoid)
                        
                        if len(Moneda.objects.filter(simbolo=moneda).values()) == 0:
                            monedasv = Moneda()
                            monedasv.simbolo = moneda
                            monedasv.save()
                        monedaid = Moneda.objects.get(simbolo=moneda)

                        precio_diariosv = Precio_Diario()
                        for afx in anfe:
                            if not afx ==  u'\xa0':
                                precio_diariosv.anterior_fecha = anterior_fecha
                        for anx in ante:
                            if not anx ==  u'\xa0':
                                precio_diariosv.anterior = anterior
                        for apx in apet:
                            if not apx ==  u'\xa0':
                                precio_diariosv.apertura = apertura
                        for cix in cier:
                            if not cix ==  u'\xa0':        
                                precio_diariosv.cierre = cierre
                        for edx in exde:
                            if not edx == u'\xa0':
                                precio_diariosv.ex_derecho = ex_derecho
                        precio_diariosv.save()
                        precio_diarioid = Precio_Diario.objects.get(
                            id=precio_diariosv.id) 

                        propuestasv = Propuesta()
                        for cx in comp:
                            if not cx == u'\xa0':
                                propuestasv.compra = compra
                        for vx in vent: 
                            if not vx == u'\xa0':
                                propuestasv.venta = venta            
                        propuestasv.save()
                        propuestaid = Propuesta.objects.get(id=propuestasv.id)

                        negociacionsv = Negociacion()
                        negociacionsv.cant_accion = cant_accion
                        negociacionsv.cant_operacion = cant_operacion
                        for vrx in vari:
                            if not vrx ==  u'\xa0':
                                negociacionsv.variacion = variacion
                        negociacionsv.monto_negociado = monto_negociado
                        negociacionsv.save()
                        negociacionid = Negociacion.objects.get(id=negociacionsv.id)

                        cotizacionsv = Cotizacion()
                        cotizacionsv.accion = accionid
                        cotizacionsv.moneda = monedaid
                        cotizacionsv.precio_diario = precio_diarioid
                        cotizacionsv.propuesta = propuestaid
                        cotizacionsv.negociacion = negociacionid
                        cotizacionsv.save()
                        










        


                
            
    

