# coding:utf-8
import scrapy
import re
# from scrapy.http import Request
# from pip._vendor.requests.packages.urllib3 import response
from xiaoshuo.items import XiaoshuoItem
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.selector import Selector


class Qidian(scrapy.Spider):
    name = "qidian"
    allowed_domains = ["qidian.com"]
    # start_urls = ["http://a.qidian.com/?orderId=&style=1&pageSize=20&siteid=1&hiddenField=0&page="]
    start_urls = [
        "http://fin.qidian.com/?size=-1&sign=-1&tag=-1&chanId=8&subCateId=-1&orderId=&update=-1&page=" + str(
            page) + "&month=-1&style=1&vip=-1" for page in range(1, 40 / 20)
    ]
    # bash_url = "http://a.qidian.com/"
    # bashurl = '.html'
    # 起点中文网
    # baseurl = "http://a.qidian.com/?orderId=&style=1&pageSize=20&siteid=1&hiddenField=0&page="
    # url = "http://a.qidian.com/?size=-1&sign=-1&tag=-1&chanId=-1&subCateId=-1&orderId=&update=-1&month=-1&style=1&action=-1&vip=-1&page="
    # 起点女生网
    # mmurl = "http://a.qidian.com/mm?orderId=&style=1&pageSize=20&siteid=0&hiddenField=0&page="
    # qd_cookies = {'_csrfToken': 'FSLsucic5q0bH2lZs72rZCbTYKgRmEhi0I2hiiJf',
    #               'newstatisticUUID': '1504163721_596286949',
    #               'nread': '2', 'nb': '2', 'ns': '2',
    #               'e1': '%7B%22pid%22%3A%22qd_P_all%22%2C%22eid%22%3A%22qd_B18%22%2C%22l2%22%3A3%2C%22l1%22%3A4%7D',
    #               'e2': '%7B%22pid%22%3A%22qd_P_all%22%2C%22eid%22%3A%22%22%7D', 'hiijack': '0'}

    def parse(self, response):
        url = 'http://a.qidian.com/'
        # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
        headers = {'User-Agent': user_agent}
        req = urllib2.Request(url, headers=headers)  # 模拟浏览器
        myResponse = urllib2.urlopen(req)
        myPgae = myResponse.read()
        # print myPgae
        unicodePage = myPgae.decode('utf-8')
        print unicodePage
        max_num = re.findall(r'<a data-page=.*?>(.*?)</a>', unicodePage, re.S)  # 获取当前页面的页码数组
        max_num = max_num[-1]  # 取出最后一个最大页码数
        print max_num  #34748

        # novelname = re.findall(r'<h4><a href=".*?">(.*?)</a></h4>', unicodePage, re.S)
        # # print novelname.__len__()
        # urlList = re.findall(r'<h4><a href="(.*?)".*?</a></h4>', unicodePage, re.S)
        # # print urlList.__len__()
        # print "http:" + str(urlList[0])
        # info = re.findall(r'<p class="author">(.*?)</p>', unicodePage, re.S)
        # print info[1]
        # authorList = re.findall(r'<a.*?target="_blank">(.*?)</a><em>', info[1], re.S)
        # print authorList.__len__()
        # print authorList



        # // 获取每一个书的url
        # hxs = Selector(response)
        # book = hxs.select('//div[@class="book-mid-info"]/h4/a//@href').extract()
        # print book
        # hxs = HtmlXPathSelector(response)
        # // 获取每一个书的url
        # book = hxs.select('//div[@class="book-mid-info"]/h4/a//@href').extract()
        #//*[@id="article_details"]/div[1]/h1/span/a
       # print "ok"
       # print response
       # print response.body
       # print response.status
       # print "ok"
       # content = response.xpath("//div[@class='book-img-text']//ul/li/div[2]/h4/a/text()").extract()
       # if content:
       #     print(content)+"1"
       #     # print(content[0])
       # content = response.xpath("//div[@class='book-img-text']//ul/li/div[1]/h4/a/text()").extract()
       # if content:
       #     print(content) + "2"
       #
       # content = response.xpath("//div[@class='book-img-text']//ul/li/div[1]/a/@href").extract()
       # if content:
       #     print(content)+"2"
    # def start_requests(self):
        # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
        # headers = {'User-Agent': user_agent}
        # req = urllib2.Request(self.url,headers=headers)  # 模拟浏览器
        # req.meta['PhantomJS'] = True
        # myResponse = urllib2.urlopen(req)
        # myPgae = myResponse.read()
        # print myPgae
        # unicodePage = myPgae.decode('utf-8')
        # print unicodePage
        # max_num = re.findall(r'<a data-page=.*?>(.*?)</a>', unicodePage, re.S)  # 获取当前页面的页码数组
        # max_num = max_num[-1] # 取出最后一个最大页码数
        # print max_num
        # return ""
        # for num in xrange(1, int(max_num) + 1):
        # for num in xrange(1, 2):
        #     newurl = self.baseurl + str(num)
        #     yield Request(newurl, dont_filter=True, callback=self.get_name)  # 将新的页面url的内容传递给get_name函数去处理
        # 此处使用dont_filter和不使用的效果不一样，使用dont_filter就能够抓取到第一个页面的内容，不用就抓不到
        # scrapy会对request的URL去重(RFPDupeFilter)，加上dont_filter则告诉它这个URL不参与去重。



    def get_name(self, response):
        print " "
        # selector = Selector(response)
        # # print selector
        # novels = selector.xpath('//ul[@class="all-img-list cf"]')
        # print novels.__len__()
        # print novels[0]
        # for nameinfo in novels:

        # for nameinfo in response.xpath('//tr'):
        #     # print nameinfo
        #     novelurl = nameinfo.xpath('td[1]/a[1]/@href').extract_first()  # 小说地址
        #     name = nameinfo.xpath('td[1]/a[2]/text()').extract_first()  # 小说名字
        #     print (str(novelurl)+ " " +str(name))
            # if novelurl is not None:
            #     yield Request(novelurl, dont_filter=True, callback=self.get_novelcontent, meta={'name': name})
            # '''''
            # #在当前页面获取小说详情
            # #print nameinfo
            # name = nameinfo.xpath('td[1]/a/text()').extract_first()#小说名字
            # author= nameinfo.xpath('td[3]/text()').extract_first()#小说作者
            # novelurl = nameinfo.xpath('td[1]/a/@href').extract_first()#小说地址
            # serialstatus = nameinfo.xpath('td[6]/text()').extract_first()#小说状态
            # serialnumber = nameinfo.xpath('td[4]/text()').extract_first()#小说字数
            # if  novelurl:
            #     targentcontent['novel_name']=name
            #     targentcontent['author']=author
            #     targentcontent['novelurl']=novelurl
            #     targentcontent['serialstatus']=serialstatus
            #     targentcontent['serialnumber']=serialnumber
            #     #print name,author,novelurl,serialstatus,serialnumber
            #
            #     yield Request(novelurl,callback=self.get_novelcontent,meta={'targentcontent':targentcontent})
            # 小说相关的详情可以暂时不传递
            # '''

    def get_novelcontent(self, response):
        # targentcontent=response.meta['targentcontent']
        # print targentcontent['novelurl'],targentcontent['name']
        # title = response.xpath('//dd[1]/h1/text()').extract_first()
        # print title
        novel_name = response.meta['name']  # 小说名字
        author = response.xpath('//tr[1]/td[2]/text()').extract_first()  # 作者
        novelurl = response.url  # 小说地址
        serialstatus = response.xpath('//tr[1]/td[3]/text()').extract_first()  # 状态
        serialnumber = response.xpath('//tr[2]/td[2]/text()').extract_first()  # 连载字数
        category = response.xpath('//tr[1]/td[1]/a/text()').extract_first()  # 小说类别
        name_id = novelurl[-5:]  # 小说编号
        collect_num_total = response.xpath('//tr[2]/td[1]/text()').extract_first()  # 总收藏
        click_num_total = response.xpath('//tr[3]/td[1]/text()').extract_first()  # 总点击

        # chapterlistul=response.xpath('//dd[2]/div[2]/p[2]/a/text()').extract_first()
        # chapterlisturl = response.xpath('//dd[2]/div[2]/p[2]/a/@href').extract_first()
        novel_breif = response.xpath('//dd[2]/p[2]').extract_first()

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
        yield targentcontent
        # print novel_name,author,novelurl,serialstatus,serialnumber,category,name_id,collect_num_total,click_num_total,chapterlisturl

