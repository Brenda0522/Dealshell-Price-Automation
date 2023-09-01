import scrapy


class WebspiderSpider(scrapy.Spider):
    name = "webspider"
    allowed_domains = ["www.nshop.com.vn"]
    start_urls = ["https://www.nshop.com.vn/collections/game-nintendo-switch?page=1"]

#go to each product in current page
    def parse(self, response):
# change pange
        pass
# get products data:
    def parse_product_page(self, response):
        # product names
        # prices
        # urls
        # product types
        # condition
        # stars
        pass