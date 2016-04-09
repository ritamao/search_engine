# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PageItem(scrapy.Item):
    title = scrapy.Field();
    url = scrapy.Field();
    content = scrapy.Field();
    links = scrapy.Field();
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
