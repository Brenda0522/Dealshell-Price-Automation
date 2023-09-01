import scrapy


class WebspiderSpider(scrapy.Spider):
    name = "webspider"
    allowed_domains = ["www.nshop.com.vn"]
    start_urls = ["https://www.nshop.com.vn/collections/game-nintendo-switch?page=1"]

#go to each product in current page
    def parse(self, response):
        products = products.css('[class="product-inner product-resize"]')
        pass
# change pang
# get products data:
    def parse_product_page(self, response):
        # product names = response.css('div.product-heading h1::text').get()
        # prices = response.css('div.product-price span::text').get()
        # urls = response.url
        # product types = response.xpath('//*[@id="breadcrumbs"]/div/nav/ol/li[2]/a/span/text()').get()
        # condition
        # stars
        pass