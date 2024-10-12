# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScarpyMusicPipeline:
    def process_item(self, item, spider):


        url =  item.get('src')
        filename = './song/'+item.get('name')+'.mp3'
        urllib.request.urlretrieve(url=url,filename=filename)

        return item

