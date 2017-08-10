# -*- coding: utf-8 -*-

from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
# use `scrapy.spiders` instead from scrapy.spider import CrawlSpider, Rule
# import scrapy.spiders
from scrapy.linkextractors import LinkExtractor
from mzitu_scrapy.items import MzituScrapyItem


class MzituSpider(CrawlSpider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/']
    img_urls = []

    rules = (
        Rule(LinkExtractor(allow=('http://www.mzitu.com/\d{1,6}',), deny=('http://www.mzitu.com/\d{1,6}/\d{1,6}')),
             callback='parse_item', follow=True),
    )
    # img_urls = []
    # 这个列表是我们之后用来存储每个套图的全部图片的URL地址的。
    # rules中的语句是：匹配http: // www.mzitu.com / 1
    # 至6位数的的URL（\d：数字；{1, 6}
    # 匹配1至6次。就能匹配出1到6位数）
    # 但是我们会发现网页中除了http: // www.mzitu.com / XXXXXXX
    # 这种格式的URL之外；还有
    # http: // www.mzitu.com / XXXX / XXXX
    # 这个格式的URL。所以我们需要设置
    # deny来不匹配http: // www.mzitu.com / XXXX / XXXX这种格式的URL。
    # 然后将匹配到的网页交给parse_item来处理。并且持续追踪


    def parse_item(self, response):
        """
        :param response: 下载器返回的response
        :return:
        """
        print(response.url)
        item = MzituScrapyItem()
        # max_num为页面最后一张图片的位置
        max_num = response.xpath("descendant::div[@class='main']/div[@class='content']/div[@class='pagenavi']/a[last()-1]/span/text()").extract_first(default="N/A")
        item['name'] = response.xpath("./*//div[@class='main']/div[1]/h2/text()").extract_first(default="N/A")
        for num in range(1, int(max_num)):
            # page_url 为每张图片所在的页面地址
            page_url = response.url + '/' + str(num)
            print(page_url)
            yield Request(page_url, callback=self.img_url)
        item['image_urls'] = self.img_urls
        yield item


    def img_url(self, response,):
        """取出图片URL 并添加进self.img_urls列表中
        :param response:
        :param img_url 为每张图片的真实地址
        """
        img_urls = response.xpath("descendant::div[@class='main-image']/descendant::img/@src").extract()
        for img_url in img_urls:
            self.img_urls.append(img_url)



    # 重点说明！！！！不能parse函数！！这是CrawlSpider进行匹配调用的函数，你要是使用了！rules就没法进行匹配啦！！
    def parse(self, response):
        pass
