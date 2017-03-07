# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LookaroundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    neirong = scrapy.Field()

class doubanItem(scrapy.Item):
    title = scrapy.Field()

class waibaoItem(scrapy.Item):
    name = scrapy.Field()
    renshu = scrapy.Field()
    price = scrapy.Field()