# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 在管道管道(pipelines)里处理爬取到的数据

import json
import codecs
# import sys

# reload(sys)

# sys.setdefaultencoding('utf-8')

class DbFilmTop250Pipeline(object):
    def __init__(self):
    	# 数据存储到data.json
        # self.file = codecs.open('data.json', mode='wb', encoding='utf-8')
        # 数据存储到data.csv
        self.file = codecs.open('data.csv', mode='wb', encoding='utf_8_sig') 

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode("unicode_escape"))

        return item

	def close_spider(self, spider):
		self.file.close()