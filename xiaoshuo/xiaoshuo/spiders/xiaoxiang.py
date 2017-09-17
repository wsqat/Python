# coding:utf-8
import scrapy
import re
from scrapy.http import Request
from xiaoshuo.items import XiaoshuoItem
import urllib2
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 潇湘书院
class XXSY(scrapy.Spider):
    name = "xxsy"
    allowed_domains = ["xxsy.net"]
    bash_url = "http://www.xxsy.net/search"
    baseurl = 'http://www.xxsy.net'
    # http: // www.xxsy.net / search?s_wd = & s_type = 1 & sort = 9 & pn = 3
    # 类别 1 - 17
    query = '?s_wd=&sort=1&s_type='

    def start_requests(self):
        # for i in range(1, 2):
        for i in range(1, 18):
            url = self.bash_url + self.query + str(i)
            yield Request(url, self.parse)

    def parse(self, response):
        baseurl = response.url  # 此处得到的url为http://www.x23us.com/class/*_1.html
        # max_num = response.xpath('//*[@id="pagelink"]/a[14]/text()').extract_first()  # 获取当前页面的最大页码数
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(baseurl, headers=headers)  # 模拟浏览器
        myResponse = urllib2.urlopen(req)
        myPgae = myResponse.read()
        unicodePage = myPgae.decode('utf-8')
        # print  myPgae
        # 根据正则表达式拿到所有的内容
        max_num = re.findall(r'type="text/javascript">.*?"pagecount":(.*?)}', unicodePage, re.S) # 获取当前页面的最大页码数
        print "max_num: "+ str(max_num[0])

        # for num in xrange(1, 2):
        for num in xrange(1, int(max_num[0]) + 1):
            newurl = baseurl + "&pn=" + str(num)
            print newurl
            # 此处使用dont_filter和不使用的效果不一样，使用dont_filter就能够抓取到第一个页面的内容，不用就抓不到
            # scrapy会对request的URL去重(RFPDupeFilter)，加上dont_filter则告诉它这个URL不参与去重。
            if newurl is not None:
                yield Request(newurl, dont_filter=True, callback=self.get_name)  # 将新的页面url的内容传递给get_name函数去处理

    def get_name(self, response):
        selector = Selector(response)
        # print selector
        novels = selector.xpath('//ul[@class="con_ord_2"]')
        # print novels
        # nameinfo = novels[0]
        for nameinfo in novels:
            novel_name = nameinfo.xpath('li[2]/a/text()').extract()[0]
            # print novel_name
            novelurl = nameinfo.xpath('li[2]/a/@href').extract()[0]
            novelurl = self.baseurl + novelurl
            author = nameinfo.xpath('li[2]/span[1]/text()').extract()[0]
            # print author
            serialstatus = nameinfo.xpath('li[2]/span[2]/text()').extract()[0]
            # print serialstatus
            category = nameinfo.xpath('li[2]/span[3]/text()').extract()[0]
            # print category
            # 总点击： 350040464 月点击：4370 月票：0 订阅人气：0 更新：2013-04-04 字数：
            click_num_total = nameinfo.xpath('li[4]/span[1]/text()').extract()[0]
            click_num_total = int(click_num_total.split("：")[1])
            collect_num_total = nameinfo.xpath('li[4]/span[4]/text()').extract()[0]
            collect_num_total = int(collect_num_total.split("：")[1])
            serialnumber = nameinfo.xpath('li[4]/span[6]/text()').extract()[0]
            serialnumber = int(serialnumber.split("：")[1])
            targentcontent = XiaoshuoItem()
            targentcontent['novel_name'] = novel_name
            targentcontent['author'] = author
            targentcontent['novelurl'] = novelurl
            targentcontent['serialstatus'] = serialstatus
            targentcontent['serialnumber'] = serialnumber
            targentcontent['category'] = category
            targentcontent['collect_num_total'] = int(collect_num_total)
            targentcontent['click_num_total'] = int(click_num_total)
            # targentcontent['name_id'] = name_id
            # targentcontent['novel_breif'] = novel_breif
            # yield targentcontent
            if novelurl is not None:
                yield Request(str(novelurl), dont_filter=True, callback=self.get_novelcontent, meta={'targentcontent': targentcontent})


    def get_novelcontent(self, response):
        # print response.body
        selector = Selector(response)
        # print selector
        click_num_total = selector.xpath('//span[@id="b-info-click"]/text()').extract()[0]
        # print click_num_total
        collect_num_total = selector.xpath('//span[@id="b-info-shoucang"]/text()').extract()[0]
        # print collect_num_total
        click_num_month = selector.xpath('//span[@id="b-info-monthpiao"]/text()').extract()[0]
        # print click_num_month
        targentcontent = response.meta['targentcontent']
        author = targentcontent['author']  # 小说作者
        novelurl = response.url  # 小说地址
        # print author+" "+novelurl
        targentcontent['click_num_total'] = int(click_num_total)
        targentcontent['collect_num_total'] = int(collect_num_total)
        targentcontent['click_num_month'] = int(click_num_month)
        # return ""
        yield targentcontent




