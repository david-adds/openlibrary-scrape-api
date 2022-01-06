import scrapy
from scrapy.http import FormRequest

class OpenlibraryLoginSpider(scrapy.Spider):
    name = 'openlibrary_login'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/account/login']

    def parse(self, response):
        yield FormRequest.from_response(
            response,
            formid = 'register',
            formdata = {
                'username': 'david.adds@gmail.com',
                'password': '1234',
                'redirect': '/account/loans',
                'debug_token': '',
                'login': 'Log In'
                


            },
            callback = self.after_login
        )
    def after_login(self,response):
        print('LOGGED IN!!!')
        
        
