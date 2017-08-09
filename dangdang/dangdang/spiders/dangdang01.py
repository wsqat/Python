# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request

class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.com"]
    start_urls = [
        'http://category.dangdang.com/cp01.54.06.00.00.00-srsort_score_desc-f0%7C0%7C0%7C0%7C0%7C1%7C0%7C0%7C0%7C0%7C0%7C0%7C0-shlist.html']

    def parse(self, response):

        title = response.xpath("//p[@class='name']/a/text()").extract()
        link = response.xpath("//a[@class='pic']/@href").extract()
        comment = response.xpath("//a[@class='search_comment_num']/text()").extract()

        for i in range(0,len(title)):
            dd = DangdangItem()
            dd["title"] = ''.join(title[i]).strip()
            dd["link"] = link[i]
            dd["comment"] = comment[i]
            # print  "len(title): "+str(len(title))
            # print  "len(link): " + str(len(link))
            # print  "len(comment): " + str(len(comment))
            # print(dd["title"])
            # print(dd["link"])
            # print(dd["comment"])
            yield dd
        for i in range(1, 101):
            url = "http://category.dangdang.com/pg" + str(
                i) + "-cp01.54.06.00.00.00-srsort_score_desc-f0%7C0%7C0%7C0%7C0%7C1%7C0%7C0%7C0%7C0%7C0%7C0%7C0-shlist.html"
            yield Request(url, callback=self.parse)
