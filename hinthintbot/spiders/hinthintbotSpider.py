import scrapy
from scrapy_selenium import SeleniumRequest
import json
from urllib.parse import urlparse
import os
from pydispatch import dispatcher
  
class hinthintbotSpider(scrapy.Spider):
    name = 'hinthintbot'

    def __init__(self,url="", **kwargs):
        self.url = url
        domain = urlparse(url).netloc.replace('www.','')
        self.domain_settings = False

        if os.path.isfile("settings.json"):
            f = open('settings.json')
            scrap_sites_settings = json.load(f)
            f.close()

            domain_settings_arr  = list(filter(lambda x:x["domain"]==domain,scrap_sites_settings))
            if len(domain_settings_arr) > 0:
                self.domain_settings = domain_settings_arr[0]

        super().__init__(**kwargs)
        
    def start_requests(self):
        print(self.domain_settings)
        print(self.url)

        if self.url != "":
            yield SeleniumRequest(
                url = self.url,
                wait_time = 30,
                screenshot = False,
                callback = self.parse,
                dont_filter = True
            )
  
    def parse(self, response):
        # with open('page.html', 'wb') as html_file:
        #     html_file.write(response.body)

        # scrap product name, price, thumbnails, currency

        settings_single = self.domain_settings["single_item"]

        product = {}

        product["title"] = response.css(settings_single["parent_el"]+' '+settings_single["title"]+'::text').extract_first()
        if len(product["title"]) > 0:
            product["title"] = product["title"].strip()
            
        product["currency"] = response.css(settings_single["parent_el"]+' '+settings_single["currency"]+'::text').extract_first()
        product["price"] = response.css(settings_single["parent_el"]+' '+settings_single["price"]+'::text').extract_first()
        product["price_fraction"] = response.css(settings_single["parent_el"]+' '+settings_single["price_fraction"]+'::text').extract_first()
        product["thumbnails"] = response.css(settings_single["parent_el"]+' '+settings_single["thumbnails"]).xpath('@src').getall()

        # store to json
        with open('product.json', 'w') as outfile:
            json.dump(product, outfile)

        return product
