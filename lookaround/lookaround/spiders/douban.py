import scrapy
from ..items import doubanItem


open('title.txt','wb')
t = open('title.txt','r')
class doubanSpider(scrapy.Spider):
    start_urls = [
        'https://www.zhihu.com/'
    ]

    name = 'douban'

    def parse(self, response):
        for href in response.xpath('//a/@href').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url,callback=self.parse_choose)

    def parse_choose(self,response):
        title = response.xpath('//title/text()').extract()
        print(title)

