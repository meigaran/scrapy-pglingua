# -*- coding: utf-8 -*-
import scrapy

from pglingua.items import PglinguaItem

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

"""

TODOS:
 - apanhar o pé dos medias
 - apanhar o resumo das entrevistas de agal-hoje

Página principal:
 http://www.pglingua.org/index.php

Páginas de interesse:

'http://pglingua.org/noticias/informante'
'http://pglingua.org/noticias/cronicas'
'http://pglingua.org/noticias/entrevistas'
'http://pglingua.org/noticias/publicacoes'
'http://pglingua.org/noticias/eventos'
'http://pglingua.org/noticias/babel'
'http://pglingua.org/noticias/internet'
'http://pglingua.org/noticias/canal-aberto'
'http://pglingua.org/agal/agal-hoje'
'http://pglingua.org/agal/info-agal'
'http://pglingua.org/agal/atraves-editora'
'http://pglingua.org/agal/revista-agalia'
'http://pglingua.org/cursos/ops'
'http://pglingua.org/cursos/cacimbo'
'http://pglingua.org/cursos/falarmos'
'http://pglingua.org/opiniom/artigos-por-data'
'http://pglingua.org/opiniom/as-aulas-no-cinema'
'http://pglingua.org/opiniom/curiosidades'
'http://pglingua.org/opiniom/de-canones-e-canoes-ii'
'http://pglingua.org/especiais/dia-das-letras'
'http://pglingua.org/especiais/carvalho-2010'
'http://pglingua.org/especiais/aglp'
'http://pglingua.org/especiais/novas-da-galiza'
'http://pglingua.org/especiais/o-apalpador'
'http://pglingua.org/especiais/espaco-brasil'
'http://pglingua.org/especiais/espaco-brasil'

"""

class SitepointSpider(CrawlSpider):
    name = 'sitepoint'
    root = 'http://pglingua.org'

    handle_httpstatus_list = [301, 302]

    allowed_domains = [ 'pglingua.org' ]
    start_urls = ( 'http://pglingua.org/noticias/entrevistas', \
                  'http://pglingua.org/agal/agal-hoje',
                  )

    """
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
    """

    def parse(self, response):
        self.log("####### parse <"+response.url+">")

        seguinte = response.xpath('//*/a[@title="Seguinte"]')
        if len(seguinte) > 0:
            url = self.root + seguinte.xpath('@href').extract_first()
            self.log("########### Atopado SEGUINTE: <"+url+">")
            yield scrapy.Request(url, callback=self.parse)

        for artigo in response.css('div.contido_artigo_lista > h2'):
            url = self.root + artigo.xpath('a/@href').extract_first()
            self.log("########### Atopado artigo: <"+url+">")
            yield scrapy.Request(url, callback=self.parse_artigo)


    def parse_artigo(self, response):
        self.log("################ parse_artigo: <"+ response.url + ">")
        item = PglinguaItem()

        item['url'] = response.url
        item['title'] = response.xpath( '//title/text()' ).extract_first()
        item['head'] = response.xpath('//*[@id="page"]/h3/a/text()').extract_first()
        item['subhead'] = response.xpath('//*[@id="page"]/div[@class="subtitulo_artigo"]/span/p').extract_first()
        item['date'] = response.xpath('//*[@id="page"]/p[1]/span').extract_first()
        #for i in range(len(response.xpath('//*[@id="page"]/span/*'))):
        #    item['body'] = item['body'] + response.xpath('//*[@id="page"]/span/p['+str(i)+']').extract_first()
        item['body'] =  response.xpath('//*[@id="page"]/span').extract_first()

        images = []
        for multimedia in response.xpath('//*[@id="page"]/div[@class="multimedia_artigo"]'):
            #image = dict()
            #image['src'] = multimedia.xpath('img/@src').extract_first()
            #image['foot'] = multimedia.xpath('p/text()').extract_first()
            src = multimedia.xpath('img/@src').extract_first()
            if src is not None:
                if src.find('http://') < 0:
                    image_src = self.root + src
                else:
                    image_src = src
                images.append(image_src)
        item['image_urls'] =  images

        return item
