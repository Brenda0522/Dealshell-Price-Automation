import scrapy
from collections import OrderedDict
from main_project.items import MainProjectItem
from automation.selenium.click_nex_page.next_page_click import Page_clicker
import json

class WebspiderSpider(scrapy.Spider):
    name = "webspider"

    # Load JSON data from 'list_data.json' file
    with open('list_data.json', 'r') as json_file:
        json_data = json.load(json_file)
            
    def start_requests(self):
        # Iterate through the JSON data to start scraping from each specified URL
        for data in self.json_data:
            start_url = data.get("start_url")  # Extract the start URL
            allowed_domain = data.get("allowed_domain")  # Extract allowed domain
            self.logger.debug(f"Start URL: {start_url}, Allowed Domain: {allowed_domain}")
            
            # Start a new request for each URL and provide metadata
            yield scrapy.Request(start_url, callback=self.parse, meta={'data': data, 'allowed_domain': allowed_domain})

    def parse(self, response):
        data = response.meta.get('data')
        
        # Extract product elements from the current page using CSS selectors
        products = response.css(data.get("products"))
        for product in products:
            # Extract the URL of the current product
            current_product_url = product.css(data.get("current_product_url")).get()
            
            # Construct the full product URL
            products_url = data.get('products_url') + current_product_url
            
            # Follow the product URL and call the parse_product_page callback with metadata
            yield response.follow(products_url, callback=self.parse_product_page, meta={'data': data})
    def parse_next_page(self,response):
        dynamic_website = response.css(data.get("dynamic_website"))
        if dynamic_website == False:
            data = response.meta.get('data')
            # Change to the next page if available
            next_page = response.css(data.get("next_page")).get()
            if next_page is not None:
                next_page_url = response.urljoin(next_page)
            # Follow the link to the next page and continue parsing with the same metadata
            yield response.follow(next_page_url, callback=self.parse, meta={'data': data})
        elif dynamic_website == True:
            Page_clicker.automate_clicking_through_pages()
            
            pass

    def parse_product_page(self, response):
        data = response.meta.get('data')
        product_item = OrderedDict(MainProjectItem())

        # Extract 'product_names' data using CSS selector
        product_item['product_names'] = response.css(data.get('product_names')).get()
        if not product_item['product_names']:
            self.logger.error("No 'product_names' found in response.meta")

        # Extract 'prices' data using CSS selector
        product_item['prices'] = response.css(data.get('prices')).get()
        if not product_item['prices']:
            self.logger.error("No 'prices' found in response.meta")

        # Extract 'product_types' data using XPath
        product_item['product_types'] = response.xpath(data.get('product_types')).get()
        if not product_item['product_types']:
            self.logger.error("No 'product_types' found in response.meta")

        # Always set the 'urls' data to the current page's URL
        product_item['urls'] = response.url

        # Yield the product item
        yield product_item