from scrapy.utils.project import get_project_settings
from hinthintbot.spiders.proxyDownloaderSpider import proxyDownloaderSpider
from hinthintbot.spiders.hinthintbotSpider import hinthintbotSpider
from scrapy.crawler import CrawlerProcess
from twisted.internet import defer, reactor
from scrapy.utils.project import get_project_settings

@defer.inlineCallbacks
def crawl():
    process = CrawlerProcess(get_project_settings())
    yield process.crawl(proxyDownloaderSpider)
    yield process.crawl(hinthintbotSpider)
    reactor.stop()

crawl()
reactor.run()