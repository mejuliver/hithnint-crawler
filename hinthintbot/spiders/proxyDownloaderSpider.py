import scrapy
import json
  
class proxyDownloaderSpider(scrapy.Spider):
    name = 'proxydownloader'
    start_urls = ["https://free-proxy-list.net"]
    proxies = []

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
            'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401
        }
    }

    def parse(self, response):
        for item in response.css(".fpl-list table tbody tr"):
            if item.css("td:nth-child(3)::text").extract_first() == "US":
                self.proxies.append(item.css("td:nth-child(1)::text").extract_first()+':'+item.css("td:nth-child(2)::text").extract_first())

        with open('proxies.json', 'w') as outfile:
            json.dump(self.proxies, outfile)
