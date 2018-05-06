# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PglinguaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url = scrapy.Field()
    title = scrapy.Field()
    head = scrapy.Field()
    subhead = scrapy.Field()
    date = scrapy.Field()
    body = scrapy.Field()
    author = scrapy.Field()

    images = scrapy.Field()
    image_urls = scrapy.Field()

    files = scrapy.Field()
    #file_urls = scrapy.Field()

    pass
