
import scrapy
from test_scrapy.items import DemoItem

class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["zhiboba.com"]
    start_urls = [
        "https://www.zhiboba.com/" 
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

          #model= DataModel()
        #model['url'] = response.url
        #model['name'] = response.xpath("//*[@id='soccer']/a[1]").extract() 
        #return model
        model=DemoItem()
        model['url'] = response.url
        model['name'] = response.xpath("//*[@id='soccer']/a[1]").extract() 
        yield model
       