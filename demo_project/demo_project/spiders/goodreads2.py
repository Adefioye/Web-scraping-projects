import scrapy
from demo_project.items import QuotesItem

# To create a spider that will write the body of the first 10 pages in goodreads into html file

class GoodReadsSpider(scrapy.Spider):

    name = 'good_reads_2'
    page_number = 2
    start_urls = ["https://www.goodreads.com/quotes?page=1"]

    def parse(self, response):

        items = QuotesItem()
        for quote in response.css('div.quote'):
            text = quote.css('div.quoteText::text').get()
            author = quote.css('span.authorOrTitle::text').get()
            tags = quote.css('div.greyText.smallText.left > a::text').getall()

            items['text'] = text
            items['author'] = author
            items['tags'] = tags

            yield items

        #next_page = response.css('.next_page::attr(href)').get()

        next_page = "https://www.goodreads.com/quotes?page={}".format(GoodReadsSpider.page_number)

        if GoodReadsSpider.page_number <= 10:
            GoodReadsSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

    

        #next_page = response.xpath('//a[@class="next_page"]/@href').getall()

        #if next_page is not None:
            #yield scrapy.Request(url=next_page_url, callback=self.parse)
         