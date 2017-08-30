# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from dingdian2 import settings
import os
import urllib2
from dingdian2.items import Dingdian2Item

from bs4 import BeautifulSoup as bs
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Dingdian2Pipeline(object):
    def process_item(self, item, spider):
        dir_path = "%s/%s" % (settings.PAGE_STORGE, spider.name)

        if not os.path.exists(dir_path):
            #   print "dir_path is %s",dir_path
            os.makedirs(dir_path)
        if isinstance(item, Dingdian2Item):
            novelpath = dir_path + '/' + item['novel_name']
            print novelpath
            if not os.path.exists(novelpath):
                os.makedirs(novelpath)
            novelbreif = item['novel_name'] + "_简介"
            novelbreifpath = novelpath + '/' + novelbreif + '.txt'
            if not os.path.exists(novelbreifpath):
                with open(novelbreifpath, 'wb') as novel_write:
                    novel_write.write(item['novel_name'])
                    novel_write.write('\t|\t')
                    novel_write.write(item['author'])
                    novel_write.write('\t|\t')
                    novel_write.write(item['novelurl'])
                    novel_write.write('\n')
                    novel_write.write(item['serialstatus'])
                    novel_write.write('\t|\t')
                    novel_write.write(item['serialnumber'])
                    novel_write.write('\t|\t')
                    novel_write.write(item['category'])
                    novel_write.write('\n')
                    novel_write.write(item['name_id'])
                    novel_write.write('\t|\t')
                    novel_write.write(item['collect_num_total'])
                    novel_write.write('\t|\t')
                    novel_write.write(item['click_num_total'])
                    novel_write.write('\n')
                    novel_write.write(item['novel_breif'])
                    novel_write.close

            titlename = item['chaptername']
            # titlenamepath = novelpath + '/' + titlename + '.txt'
            novel_name_path = novelpath + '/' + str(item['novel_name']) + '.txt'
            print novel_name_path
            chapterurl = item['chapterurl']
            html = urllib2.urlopen(chapterurl).read()
            soup1 = bs(html, 'lxml')
            # if not os.path.exists(novel_name_path):
                # with open(novel_name_path, 'wb') as file_write:
            # 以追加模式打开
            with open(novel_name_path, 'a') as file_write:
                cont = soup1.find("dd", attrs={"id": "contents"}).getText()
                # print cont
                file_write.write(titlename)
                file_write.write('\n')
                file_write.write(cont)
                file_write.write('\n')
                file_write.close()

        return item

        # -o books.csv 参数的意思是将抓取的Item集合输出到csv文件。
        # 除了CSV格式，Scrapy还支持JSON，XML的格式输入
