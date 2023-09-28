import scrapy
from collections import OrderedDict
from main_project.items import MainProjectItem
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
        # response.follow(self.parse_next_page,meta={'data': data})
    
    # change to next page
    # def parse_next_page(self, response)(not use):
        data = response.meta.get('data')
        dynamic_website = data.get("dynamic_website")
        if dynamic_website == False:
            # Change to the next page if available
            next_page = response.css(data.get("next_page")).get()
            if next_page is not None:
                next_page_url = response.urljoin(next_page)
            # Follow the link to the next page and continue parsing with the same metadata
            yield response.follow(next_page_url, callback=self.parse, meta={'data': data})
        else:
            with open("/Users/quangpham/Documents/my_project_aug_2023/project/main_project/main_project/automation/selenium/click_next_page/next_page_url.json", "r") as dynamic_url_file:
                dynamic_url_data = json.load(dynamic_url_file)
            for entry in dynamic_url_data:
                next_page_urls = entry.get("next_url")
                for next_page_url in next_page_urls:
                    yield response.follow(next_page_url, callback=self.parse, meta={'data': data})
    def parse_product_page(self, response):
        data = response.meta.get('data')
        product_item = OrderedDict(MainProjectItem())
        # Extract 'product_names' data using CSS selector
        product_item['web_name'] = data.get('web_name')
        if not product_item['web_name']:
            self.logger.error("No 'web_name' found in list_data.json")
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


## at the moment iam able to fo inside the clicking function but for some reason the programm doesn run
## i have able to call Page_clicker().automate_clicking_through_pages() by using __init__.py
## i have able to finish the work today inclue connect the click next page to the spider, how ever i run in to little problem that is when i import Page_clicker it automaticly dellete the whole next_page_url.json file befor pulling any data from it so i have to turn that off and fix it later 
## at the moment i choose to seprate the Page_clicker into a seprate function so that the clients could it by them self and don have to run page_clicker every thing scraping which would minimize the time running but instead all i need to do is ask the client if they want to run page_clicker or not.