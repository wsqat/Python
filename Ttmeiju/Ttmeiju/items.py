# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TtmeijuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # name是保存名字
    # image_urls和images 是爬取图片的pipeline用的，一个是保存图片URL，一个是保存图片存放信息
    # image_paths其实没什么实际作用，只是记录下载成功的图片地址
    # epiosde和episode_url是保存集数和对应下载地址
    name = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
    episode = scrapy.Field()
    episode_url = scrapy.Field()
    # pass
