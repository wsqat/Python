# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import itertools
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class XiaoshuoPipeline(object):

    def __init__(self):
        # self.csvfile = file('items.csv', 'wb')
        # self.csvfile = open('items.csv', 'wb')
        # self.csvfile = open('qdxs.csv', 'wb')
        # self.csvfile = open('qdmm.csv', 'wb')
        # self.csvfile = open('17k.csv', 'wb')
        # self.csvfile = open('xxsy.csv', 'wb')
        # self.csvfile = open('cszw.csv', 'wb') # 创世中文
        # self.csvfile = open('cszw.csv', 'ab')  # 创世中文 追加写入
        # self.csvfile = open('cszw1.csv', 'ab')  # 小说 追加写入 xxsy
        # self.csvfile = open('zongheng.csv', 'wb')  # 纵横小说网
        self.csvfile = open('novels.csv', 'ab')  # 小说 追加写入 cs
        # self.csvfile = open('test.csv', 'wb')  # 小说 追加写入 cs
        # self.csvfile = open('xxsy.csv', 'ab')  # 小说 追加写入
        self.csvfile.write(codecs.BOM_UTF8) # 防止乱码
        # self.csvwriter = csv.writer(open('items.csv', 'wb'), delimiter=',')
        # self.csvwriter = csv.writer(self.csvfile)
        self.csvwriter = csv.writer(self.csvfile,  delimiter=',') #将数据作为一系列以逗号分隔的值
        # self.csvwriter.writerow(['novel_name', 'author', 'novelurl', 'serialstatus', 'serialnumber', 'category', 'collects','reviews','month'])
        self.count = 0

    def process_item(self, item, spider):
        row = [item['novel_name'], item['author'], item['novelurl'],item['serialstatus'], item['serialnumber'], item['category'],
                    item['collect_num_total'], item['click_num_total'], item['click_num_month']]
        self.csvwriter.writerow(row)
        self.count = self.count + 1
        print "抓取起点小说网第"+str(self.count)+"条记录"
        return item
