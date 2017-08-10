# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup
import json

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/']
    # 定义请求头
    header = {
        # 使用手机的User-Agent
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
        'Host': 'www.zhihu.com',
        "Referer": "https://www.zhihu.com/",
    }

    # def parse(self, response):
    #     all_urls = response.css('a::attr(href)').extract()
    #     all_urls = [parse.urljoin(response.url, url) for url in all_urls]
    #     all_urls = filter(lambda x : True if x.startswith('https') else False, all_urls)
    #     pass

    # spider入口方法
    def start_requests(self):
        # 访问https://www.zhihu.com/login/phone_num登录页面,在do_login回调中处理
        return [scrapy.Request('https://www.zhihu.com/login/email', headers=self.header, callback=self.do_login)]
        # return [scrapy.Request('https://www.zhihu.com/login/phone_num', headers=self.header, callback=self.do_login)]

    def do_login(self, response):
        response_text = response.text
        # soup = BeautifulSoup(response.text)
        soup = BeautifulSoup(response.text,"lxml")

        # 解析获取xsrf
        xsrf = soup.select('input[name="_xsrf"]')[0]['value']
        if xsrf:
            login_data = {
                '_xsrf': xsrf,
                # 'phone_num': '手机号',
                # 'password': '密码',
                'email': '786607676@qq.com',
                'password': 'wsqali1314',
                'captcha': ''
            }
            # 由于登录需要验证码,因此需要先获取验证码,在do_login_after_captcha回调获取验证码,封装传递的login_data参数
            import time
            t = str(int(time.time() * 1000))
            captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
            yield scrapy.Request(captcha_url, headers=self.header, meta={'login_data': login_data},
                                 callback=self.do_login_after_captcha)

    def do_login_after_captcha(self, response):
        # 获取验证码操作
        with open('captcha.gif', 'wb') as f:
            f.write(response.body)
            # print "--------"
            # print (response.body)
            f.close()
        from PIL import Image
        try:
            im = Image.open('captcha.gif')
            im.show()
            # im.close()
        except:
            pass

        # print ('请输入验证码: ')
        # raw_input()函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）
        captcha = raw_input('请输入验证码: ')
        # print captcha

        # 登录
        login_data = response.meta.get("login_data", {})
        login_data['captcha'] = captcha
        # login_url = 'https://www.zhihu.com/login/phone_num'
        login_url = 'https://www.zhihu.com/login/email'
        # FormRequest可以完成表单提交,在check_login回调中验证登录是否成功
        return [scrapy.FormRequest(
            url=login_url,
            formdata=login_data,
            headers=self.header,
            callback=self.check_login
        )]

    def check_login(self, response):
        # 验证登录是否成功
        text_json = json.loads(response.text)
        print (text_json["msg"])
        if "msg" in text_json and text_json["msg"] == "登录成功".decode("utf-8"):
            print "login success!"
            yield response.text
            print (response.text)
            for url in self.start_urls:
                yield scrapy.Request('http://www.zhihu.com', dont_filter=True, callback=self.page_content, headers=self.header)
        else:
            print "login fail!"

    # def check_login(self, response):
    #     if json.loads(response.body)['r'] == 0:
    #         yield scrapy.Request(
    #             'http://www.zhihu.com',
    #             headers=self.headers,
    #             callback=self.page_content,
    #             dont_filter=True,
    #         )

    def page_content(self, response):
        with open('first_page.html', 'wb') as f:
            f.write(response.body)
        print 'done'
