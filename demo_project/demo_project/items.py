# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def remove_unicode(field):
    return field.replace("\u201c", "").replace("\u201d", "").replace("\u2015", "").replace("\u2019", "").replace("\u2026", "")



class QuotesItem(scrapy.Item):
    text = scrapy.Field(
        input_processor= MapCompose(str.strip, remove_unicode),
        output_processor= TakeFirst()
        )
    author = scrapy.Field(
        input_processor= MapCompose(remove_tags, str.strip),
        output_processor= TakeFirst()
)
    tags = scrapy.Field(
        input_processor= MapCompose(remove_tags),
        out_processor=  Join()

    )

