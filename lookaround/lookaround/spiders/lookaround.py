import scrapy
from ..items import LookaroundItem


class lookaroundSpider(scrapy.Spider):
    start_urls = [
        "http://www.qiushibaike.com"
    ]
    name = 'lookaround'
    allowed_domains = ['qiushibaike.com']

    def parse(self, response):
        for href in response.xpath("//a[@class='contentHerf']/@href"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)
            print(href)

    def parse_dir_contents(self, response):
        item = LookaroundItem()
        item['neirong'] = response.xpath("//*[@id='single-next-link']/div/text()").extract()
        yield item