import scrapy

book_dic = dict()

class BookTitleAuthorSpider(scrapy.Spider):

    name = 'booktitleandauthor'

    def start_requests(self):

        url = 'file:///C:/Users/User/Desktop/Web%20scraping/Modern%20Web%20Scraping%20with%20Python%20using%20Scrapy%20and%20Splash/web-scraping-course-master/Section%202-%20Xpath%20Selectors%20Exercise/index.html.html'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        book_title = response.xpath('//h3[contains(@class, "book-title")]/text()').extract()
        raw_author = response.xpath('//h5[contains(@class,"card-title")]/text()').extract()
        raw_author = raw_author.split()
        raw_author.remove('By') # To remove By in the author_name
        author_name = " ".join(raw_author)

        book_dic[book_title] = author_name

        return book_dic