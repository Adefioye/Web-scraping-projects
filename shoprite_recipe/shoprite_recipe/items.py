# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst

class ShopriteRecipeItem(scrapy.Item):
    # name = scrapy.Field(
    #     input_processor= strip(),
    #     output_processor= TakeFirst(),
    # )
    # description = scrapy.Field(
    #     input_processor= strip(),
    #     output_processor= TakeFirst(),
    # )
    # ingredients = scrapy.Field()
    # methods = scrapy.Field()

