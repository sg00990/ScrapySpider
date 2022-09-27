import re
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

class KsuSpider(CrawlSpider):
    pageid = 1
    name = "ksu"
    allowed_domains = ["kennesaw.edu"]
    start_urls = [
        'https://www.kennesaw.edu/',
        'https://ccse.kennesaw.edu/',
        'https://dining.kennesaw.edu/'
    ]
    rules = (
        Rule(LinkExtractor(allow_domains=('kennesaw.edu')), callback='parse_items', follow = True),
    )
    
    DEPTH_PRIORITY = 1
    SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
    SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
    

    def parse_items(self, response):
        entry = dict.fromkeys(['pageid', 'url', 'title', 'body', 'emails'])
        
        soup = BeautifulSoup(response.text, 'html.parser')

        entry['pageid'] = KsuSpider.pageid
        entry['url'] = response.url
        entry['title'] = response.css('title::text').get()
        entry['body'] = soup.get_text()
        entry['emails'] = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', response.body.decode('utf-8'))

        # entry = {
        #     "pageid": KsuSpider.pageid,
        #     "url": response.url,
        #     "title": response.css('title::text').get(),
        #     'body': soup.get_text(),
        #     "emails": re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', response.body.decode('utf-8')),
        #     }
        
        KsuSpider.pageid += 1

        yield (entry)

# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     start_urls = [
#         'https://quotes.toscrape.com/page/1/',
#         'https://quotes.toscrape.com/page/2/',
#     ]

#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield {
#                 'text': quote.css('span.text::text').get(),
#                 'author': quote.css('small.author::text').get(),
#                 'tags': quote.css('div.tags a.tag::text').getall(),
#             }
