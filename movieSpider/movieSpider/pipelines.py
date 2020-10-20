# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MoviespiderPipeline:
    def open_spider(self,spider):
        self.fp = open("movieDetail.csv",mode='a',encoding='utf-8')

    def process_item(self, item, spider):
        detail = item['detail']
        self.fp.write(detail)
        self.fp.write('\n')
        return item

    def close_spider(self,spider):
        self.fp.close()
