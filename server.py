from http.server import BaseHTTPRequestHandler, HTTPServer
from scrapy.utils.project import get_project_settings
from hinthintbot.spiders.proxyDownloaderSpider import proxyDownloaderSpider
from hinthintbot.spiders.hinthintbotSpider import hinthintbotSpider
from scrapy.crawler import CrawlerProcess
from twisted.internet import defer, reactor
from scrapy.utils.project import get_project_settings
from urllib import parse
import json

hostName = "localhost"
serverPort = 8080

class HinthintScrapyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()        
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        
    def do_POST(self):
        length = int(self.headers.get('content-length'))
        field_data = self.rfile.read(length)
        fields = parse.parse_qs(str(field_data,"UTF-8"))
        query = {}

        url =  fields["url"][0]

        with open('url.json', 'w') as outfile:
            json.dump([url], outfile)
        
        # for response in self.crawl():
        #     print(response.name)
            # if response["name"] == "hinthintbot":
            #     query = response["data"]

        self.crawl()

        f = open('product.json')
        query = json.load(f)
        f.close()

        reactor.run()
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(query).encode())

    @defer.inlineCallbacks
    def crawl(self):
        process = CrawlerProcess(get_project_settings())
    
        yield process.crawl(proxyDownloaderSpider)
        yield process.crawl(hinthintbotSpider)
        reactor.stop()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), HinthintScrapyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")