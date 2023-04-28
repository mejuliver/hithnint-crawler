from shutil import which
from fake_useragent import UserAgent
import proxy

ua = UserAgent()
user_agent = ua.random

ROTATING_PROXY_LIST = []
if len(proxy.PROXIES) > 0:
    ROTATING_PROXY_LIST = proxy.PROXIES

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')

if proxy.proxy:
    SELENIUM_DRIVER_ARGUMENTS = [
        '--headless',
        f'--user-agent={user_agent}',
        f'--server-proxy={proxy.proxy}',
    ]
else:
    SELENIUM_DRIVER_ARGUMENTS = [
        '--headless',
        f'--user-agent={user_agent}',
    ]
    

# Settings for hinthintbot scrapper
# http://doc.scrapy.org/en/latest/topics/settings.html
# http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'hinthintbot'
SPIDER_MODULES = ['hinthintbot.spiders']
NEWSPIDER_MODULE = 'hinthintbot.spiders'
USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies
# COOKIES_ENABLED = True

# Disable Telnet Console
# TELNETCONSOLE_ENABLED = True

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#	'hinthintbot.CustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
	'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
    'scrapy_selenium.SeleniumMiddleware': 800
}

if len(ROTATING_PROXY_LIST) > 0:
    DOWNLOADER_MIDDLEWARES['rotating_proxies.middlewares.RotatingProxyMiddleware'] = 610
    DOWNLOADER_MIDDLEWARES['rotating_proxies.middlewares.BanDetectionMiddleware'] = 620

#EXTENSIONS = {
#	'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#	'hinthintbot.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True

# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5

# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'