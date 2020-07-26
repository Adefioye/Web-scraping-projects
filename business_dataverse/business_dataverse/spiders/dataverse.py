# -*- coding: utf-8 -*-
import scrapy


class DataverseSpider(scrapy.Spider):
    name = 'dataverse'
    page_number = 2
    start_urls = ['https://dataverse.harvard.edu/dataverse/harvard?q=business&types=dataverses%3Adatasets%3Afiles&sort=score&order=desc&page=1']

    def parse(self, response):
        items = dict()
        titles = response.css('.datasetResult .card-title-icon-block a span::text').getall()
        urls = response.css(".bg-citation a::text").getall()

        for title, url in zip(titles, urls):
            items['title'] = title
            items['url'] = url

            yield items

        #next_url = 'https://dataverse.harvard.edu/dataverse/harvard?q=business&types=dataverses%3Adatasets%3Afiles&sort=score&order=desc&page={}'.format(DataverseSpider.page_number)
        next_page = response.css('#dv-main li:nth-child(8) a').xpath('./@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
