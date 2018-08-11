# -*- coding: utf-8 -*-
from __future__ import absolute_import
import scrapy
import csv
from scrapy.spider import Spider
from wmscrawl.items import WmscrawlItem

csv_file = csv.reader(open('D:\\GitTest\\spidertest\\wmscrawl\\test.csv','r'))

class WmsSpider(Spider):
    name = 'wmscrawl'

    start_urls = [
        "http://baidu.com",
    ]

    def parse(self, response):
        for i in csv_file:
            item = WmscrawlItem()
            item['name'] = i[0]
            img_url = [i[1]]
            item['file_urls'] = img_url
            yield item
