# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider


class ShopriteSpider(scrapy.Spider):
    name = 'shoprite'

    def start_requests(self):
        for offset in range(0, 180, 20):
            url = 'https://www.shoprite.com.ng/recipes.html?course=all&occasion=all&ingredient=all&offset={}'.format(offset)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if response.body is not None:
            for link in response.css('li.CardSmallRecipe').xpath('./a/@href').getall():
                yield response.follow(url=link, callback=self.parse_item)

    def parse_item(self, response):

        items = dict()
        items['recipe_name'] = response.xpath('//li[@class="breadcrumbs__item last"]/a[@class="breadcrumbs__link"]/text()').get()
        items['description'] = response.css('.type--text__card p::text').get()
        items['ingredients'] = response.css('.alt_third-col p::text').getall()
        items['methods'] = response.css('.customText li::text').getall()


 
        yield items

