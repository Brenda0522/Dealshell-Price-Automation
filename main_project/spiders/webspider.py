import scrapy
from collections import OrderedDict
from main_project.items import MainProjectItem

class WebspiderSpider(scrapy.Spider):
    name = "webspider"
    allowed_domains = ["www.nshop.com.vn"]
    start_urls = ["https://www.nshop.com.vn/collections/game-nintendo-switch?page=1"]

#go to each product in current page
    def parse(self, response):
        products = response.css('[class="product-inner product-resize"]')
        for product in products:
            curren_product_url = product.css('div a::attr(href)').get()
            products_url = ('https://www.nshop.com.vn/products')+ curren_product_url
            yield response.follow(products_url, callback = self.parse_product_page)
# change pange
# get products data:
    def parse_product_page(self, response):
        product_item = OrderedDict(MainProjectItem())
        product_item['product_names'] = response.css('div.product-heading h1::text').get()
        product_item['prices'] = response.css('div.product-price span::text').get()
        product_item['urls'] = response.url
        product_item['product_types'] = response.xpath('//*[@id="breadcrumbs"]/div/nav/ol/li[2]/a/span/text()').get()
        # product_item['condition']
        # stars
        yield product_item