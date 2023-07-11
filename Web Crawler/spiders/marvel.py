
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import sys
from scrapy import Request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class LkSpider(CrawlSpider):
    name = 'multi_spider'

    # read csv with just url per line
    # with open('urls.csv') as file:
    #     start_urls = [line.strip() for line in file]
    def __init__(self, url=None,domain=None, *args, **kwargs):
        super(LkSpider, self).__init__(*args, **kwargs)
        self.urls=url.strip('\'')
        self.start_urls=[self.urls]
        print(self.start_urls)
        self.allowed_domains = [domain.strip('\'')]
        print(self.allowed_domains)
    
    # allowed_domains=['everybodyeating.com']
    def start_request(self):
        request = Request(url = self.start_urls, callback=self.parse)
        yield request
 

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        # get the domain for the file name
        domain = response.request.url
        soup=BeautifulSoup(response.text,features="lxml")
        l=[]
        for i in soup.get_text().split('\n'):
                  if i.strip()=='':
                       continue
                  l.append(i.strip())
        yield {
             'url':domain,
             'text':l
        }

# # main driver
# if __name__ == "__main__":
#     process = CrawlerProcess()
#     process.crawl(LkSpider)
#     process.start()