# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy import Item,Field

# class DbFilmTop250Item(scrapy.Item):
class DbFilmTop250Item(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 名称（name）
	# 描述（movieInfo）
	# 评分（star)
	# 格言（quote）
    title = Field()
    movieInfo = Field()
    star = Field()
    quote = Field()
    # pass
