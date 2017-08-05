# -*- coding: utf-8 -*-  
  
from scrapy.spiders import CrawlSpider  
from scrapy.selector import Selector  
from db_film_top250.items import DbFilmTop250Item  
from scrapy.http import Request  
  
class Douban(CrawlSpider):  
    name = "douban"  
    start_urls = ['http://movie.douban.com/top250']  
  
    url = 'http://movie.douban.com/top250'  
  
    def parse(self,response):  
        #print response.body  
        item = DbFilmTop250Item()  
        selector = Selector(response)  
        #print selector  
        Movies = selector.xpath('//div[@class="info"]')  
        #print Movies  
        for eachMoive in Movies:  
            title = eachMoive.xpath('div[@class="hd"]/a/span/text()').extract()[0]
            # 把两个名称合起来  
            fullTitle = ''  
            for each in title:  
                fullTitle += each  
            star = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]  
            quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            # .strip()  去除空格
            movieInfo = eachMoive.xpath('div[@class="bd"]/p/text()').extract()[0].strip()
            # quote可能为空，因此需要先进行判断  
            if quote:  
                quote = quote[0]  
            else:  
                quote = ''  
            #print fullTitle  
            #print movieInfo  
            #print star  
            #print quote  
            # item['movieInfo'] = ';'.join(movieInfo)  
            item['star'] = star  
            item['quote'] = quote
            item['title'] = fullTitle    
            item['movieInfo'] = movieInfo
            yield item  
            nextLink = selector.xpath('//span[@class="next"]/link/@href').extract() 
            # 第10页是最后一页，没有下一页的链接  
            if nextLink:  
                nextLink = nextLink[0]  
                print nextLink  
                yield Request(self.url + nextLink, callback=self.parse)