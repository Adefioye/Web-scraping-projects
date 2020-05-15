import scrapy
from scrapy.loader import ItemLoader
from demo_project.items import QuotesItem

#To create a spider that will write the body of the first 10 pages in goodreads into html file

class GoodReadsSpider(scrapy.Spider):

    name = 'good_reads_3'
    page_number = 2
    start_urls = ["https://www.goodreads.com/quotes?page=1"]


    def parse(self, response):

        for quote in response.css('div.quote'):
            loader = ItemLoader(item=QuotesItem(), selector=quote, response=response)

            loader.add_css('text', 'div.quoteText::text')
            loader.add_css('author', 'span.authorOrTitle')
            loader.add_css('tags', 'div.greyText.smallText.left > a')
            yield loader.load_item()

        next_page = "https://www.goodreads.com/quotes?page={}".format(GoodReadsSpider.page_number)

        if GoodReadsSpider.page_number <= 10:
            GoodReadsSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)


