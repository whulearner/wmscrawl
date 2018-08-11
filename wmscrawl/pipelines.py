# -*- coding: utf-8 -*-
import scrapy
from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WmscrawlPipeline(object):
    def process_item(self, item, spider):
        return item

class MyFilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url, meta={'item': item})
    def item_completed(self, results, item, info):
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no images")
        item['file_paths'] =  file_paths
        return item
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        path = 'full/'+ item['name'] + '.png'
        return path
