# coding:utf-8    
#注意事项：在linux平台上，前面两句注释是这样写的，尤其是第一句没有空格。    
#本程序是用于python爬虫练习，用于在黑板客上闯关所用。    
#程序分析：打开黑板客首页：http://www.heibanke.com/lesson/crawler_ex00/    
#发现第一关就是让你不停的更换域名，然后打开新的网页    
# 那思路如下：    
# 1.网页打开模块    
# 2.在打开的网页中通过bs4或者正则表达式获取网页中的数字串，然后组成新的网页地址再次打开，然后一直重复。    
    
import re
import urllib
from datetime import datetime

begin_time = datetime.now()
url = 'http://www.heibanke.com/lesson/crawler_ex00/'
html = urllib.urlopen(url).read()
# print html
# index=re.findall(r'输入数字[0-9]{5}',html)
index=re.findall(r'输入数字([0-9]{5})',html)
print index

while index:
	url = 'http://www.heibanke.com/lesson/crawler_ex00/%s/' % index[0]
	print url
	html = urllib.urlopen(url).read()
	# index=re.findall(r'输入数字([0-9]{5})',html)
	index=re.findall(r'数字是([0-9]{5})',html)    

html = urllib.urlopen(url).read()
# url = 'http://www.heibanke.com'+re.findall(r'<a href=".*?" class',html)[0]
url='http://www.heibanke.com'+re.findall(r'<a href="(.*?)" class',html )[0]    
print '最后通关的的网址是%s, 耗时%s' % (url,(datetime.now()-begin_time))    
print 'just for test,是吧!'