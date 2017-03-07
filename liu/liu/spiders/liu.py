#enccoding = utf- 8
import scrapy

class spiderss(scrapy.Spider):
    name = 'liu'
    start_urls = [
        'https://book.douban.com/top250?start=0'
    ]
    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "cookie":"bdshare_firstime=1468914886146; uuid_tt_dd=-5001253189475811181_20160719; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1484900806,1486973876,1487066845; UN=qq_36241746; UE=""; BT=1483491398883; __utma=17226283.24061182.1481007320.1481007320.1481007320.1; __utmz=17226283.1481007320.1.1.utmcsr=download.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/download/davidleefulan/8423803; uuid=65bd9422-450e-4425-a07c-73621923d9a0; avh=34631291; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1487066845; dc_tos=old04g; dc_session_id=1487066848544"
    }

    def parse(self, response):
        name = response.xpath('td/div[0]/a/text').extract()
        rating = response.xpath('span[@class = rating_nums]/text').extract()
        yield {
            'name': name,
            'rating': rating
        }
        next_page = response.xpath('span[@class = next]/a/[href]')
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse)

