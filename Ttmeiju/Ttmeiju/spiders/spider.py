# -*-coding:utf-8-*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# 书写要采集的网站以及分别采集各字段。

import scrapy
from Ttmeiju.items import TtmeijuItem
from scrapy.selector import Selector
from scrapy.http import Request
import sys
reload(sys) # python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

class CacthUrlSpider(scrapy.Spider):

	def __init__(self):
		self.headers = {
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept-Encoding': 'gzip, deflate',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
		}

	name = 'meiju'
	# 设置下载延时
    #download_delay = 3
	allowed_domains = ['cn163.net']
	#  start_urls = ["http://cn163.net/archives/{id}/".format(id=id) for id in ['16355', '13470', '18766', '18805']]
	start_urls = ["http://cn163.net/archives/{id}/".format(id=id) for id in ['1994']]
	# url = 'http://movie.douban.com/top250'

	def parse(self, response):
		item = TtmeijuItem()
		selector = Selector(response)
		item['name'] = response.xpath('//*[@id="content"]/div[2]/div[2]/h2/text()').extract()
		print item['name']
		# item['image_urls'] = response.xpath('//*[@id="entry"]/div[2]/img/@src').extract()
		# item['image_urls'] = response.xpath('//*[@id="entry"]/p/img/@src').extract()
		image_urls = response.xpath('//*[@id="entry"]/*/img/@src').extract()
		# print "1 spider.py image_urls: " + ','.join(image_urls)
		# if image_urls is None:
		# 	image_urls = ["http://ww1.sinaimg.cn/large/006B11Qagy1fhjh8ncz51j30b90go0um.jpg"]
		# print "2 spider.py image_urls: " + ','.join(image_urls)
		item['image_urls'] = image_urls
		# item['episode'] = response.xpath('//*[@id="entry"]/p[last()]/a/text()').extract()
		item['episode'] = response.xpath('//*[@id="entry"]/ol/li/a/text()').extract()
		# item['episode_url'] = response.xpath('//*[@id="entry"]/p[last()]/a/@href').extract()
		item['episode_url'] = response.xpath('//*[@id="entry"]/ol/li/a/@href').extract()
		yield item
		# nextLink = selector.xpath('//div[@class="relatedposts"]/ol/li/a/@href').extract()
		nextLink = selector.xpath('//div[@class="context_b"]/a/@href').extract()
		# 第10页是最后一页，没有下一页的链接
		if nextLink:
			for next in nextLink:
				# nextLink = nextLink[0]
				print next
				yield Request(next, callback=self.parse)
