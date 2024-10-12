import json
import re

import scrapy

from scarpy_music.items import ScarpyMusicItem


class YinyueSpider(scrapy.Spider):
    name = "yinyue"
    allowed_domains = ["www.2t58.com"]


    def start_requests(self):
        name = input("请输入名称: ")
        url = 'http://www.2t58.com/so/{}/1.html'.format(name)
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        li_list = response.xpath('//div[@class="name"]/a/@href').extract()

        pattern = r"/song/(\w+)\.html"

        for li in li_list:
            result = re.search(pattern, li)

            data = {'id': result.group(1), 'type': 'music'}
            headers ={

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",

}
            url2 = 'http://www.2t58.com/js/play.php'

            print(result.group(1))
            yield scrapy.FormRequest(url=url2, formdata=data,headers=headers, callback=self.parse_music)


    def parse_music(self,response):
        src = response.text
        obj = json.loads(src)
        musicsrc = obj['url']
        name = obj['title']
        song = ScarpyMusicItem(src=musicsrc, name=name)

        yield song
        print('=============================')