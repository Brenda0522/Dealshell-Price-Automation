# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MainProjectItem(scrapy.Item):
    # define the fields for your item here like:
    product_names = scrapy.Field()
    prices = scrapy.Field()
    urls = scrapy.Field()
    product_types = scrapy.Field()