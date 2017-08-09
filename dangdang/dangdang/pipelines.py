# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import sys

class DangdangPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    def __init__(self):
        # load(sys)
        self.conn = pymysql.connect(host="127.0.0.1", user="root", password="WSQwsq1314", db="python_db")
        self.conn.set_charset("utf8")

    def process_item(self, item, spider):
        title = item["title"]
        link = item["link"]
        comment = item["comment"]

        print(item["title"])
        print(item["link"])
        print(item["comment"])
        # return item
        sql = "insert into book(title,link,comment) values ('" + title + "','" + link + "','" + comment + "');"
        print(sql)

        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
            # pass

    def close_spider(self):
        self.conn.close()
