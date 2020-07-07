# -*- coding: utf-8 -*-

# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class WebcrawlerhaPipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):

    def __init__(self):
        self.pages_seen = set()

    def process_item(self, item, spider):
        if item['page'] in self.pages_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.pages_seen.add(item['page'])
            return item