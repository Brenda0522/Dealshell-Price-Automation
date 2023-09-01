import scrapy


class WebspiderSpider(scrapy.Spider):
    name = "webspider"
    allowed_domains = ["www.nshop.com.vn"]
    start_urls = ["https://www.nshop.com.vn/collections/game-nintendo-switch?page=1"]

#go to each product in current page
    def parse(self, response):
        products = products.get('div.col-md-3 col-sm-4 col-xs-6 product-loop')
        pass
# change pang
# get products data:
    def parse_product_page(self, response):
        # product names = response.css('div.product-heading h1::text').get()
        # prices = response.css('div.product-price span::text').get()
        # urls
        # product types
        # condition
        # stars
        pass