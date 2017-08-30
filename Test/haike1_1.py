#!/usr/bin/python  
# coding:utf-8  
#通过urllib 的方法获取网页内容，通过正则表达式获取所需的字符  
import requests  
import re  
import datetime,sys  
reload(sys)  
sys.setdefaultencoding('utf-8')  
begin_time=datetime.datetime.now()  
  
url = r'http://www.heibanke.com/lesson/crawler_ex00/'  
new_url = url  
num_re = re.compile(r'<h3>[^\d<]*?(\d+)[^\d<]*?</h3')  
while True:  
    print '正在读取网址 ',new_url  
    html = requests.get(new_url).text  
    num = num_re.findall(html)  
    if len(num) == 0:  
        new_url='http://www.heibanke.com'+re.findall(r'<a href="(.*?)" class',html )[0]  
        break;  
    else:  
        new_url = url+num[0]  
print '最后通关的的网址是%s, 耗时%s' % (new_url,(datetime.datetime.now()-begin_time)) 