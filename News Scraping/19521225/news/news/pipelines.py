# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv

class csvWriterPipeline:
    def open_spider(self, spider):
        self.file = csv.writer(open('data.csv', 'a'), lineterminator='\n')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.writerow(item.values())
        return item

class NewsPipeline:
    def process_item(self, item, spider):
        return item
