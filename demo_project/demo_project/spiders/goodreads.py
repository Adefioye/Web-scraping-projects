import scrapy

# To create a spider that will write the body of the first 10 pages in goodreads into html file

class GoodReadsSpider(scrapy.Spider):

    name = 'good_reads'

    def start_requests(self):
        urls = []
        for i in range(1, 11):
            url_string = "https://www.goodreads.com/quotes?page={}".format(i)
            urls.append(url_string)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_number = response.url.split('=')[1]
        filepath = "{}.html".format(page_number)

        with open(filepath, 'wb') as f:
            f.write(response.body)