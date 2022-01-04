import scrapy


class EbooksSpider(scrapy.Spider):
    name = 'ebooks'
    allowed_domains = ['openlibrary.org/subjects/picture_books.json?limit=12&offset=12']
    start_urls = ['http://openlibrary.org/subjects/picture_books.json?limit=12&offset=12/']

    def parse(self, response):
        pass
