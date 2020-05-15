import scrapy

book_dic = dict()

class BookTitleAuthorSpider(scrapy.Spider):

    name = 'book_title_author'

    def start_requests(self):

        url = r"C:\Users\User\Desktop\Web scraping\Modern Web Scraping with Python using Scrapy and Splash\web-scraping-course-master\Section 2- Xpath Selectors Exercise\path\to\a\index.html"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        book_title = response.xpath('//h3[contains(@class, "book-title")]/text()').extract()
        raw_author = response.xpath('//h5[contains(@class,"card-title")]/text()').extract()
        raw_author = raw_author.split()
        raw_author.remove('By') # To remove By in the author_name
        author_name = " ".join(raw_author)

        book_dic[book_title] = author_name

        return book_dic
