# coding:utf-8    

import re
import urllib
import datetime

begin_time=datetime.datetime.now()    
url = 'http://www.heibanke.com/lesson/crawler_ex00/'    
html = urllib.urlopen(url).read()    
index=re.findall(r'输入数字([0-9]{5})',html)    
print index
# while index:    
#     url='http://www.heibanke.com/lesson/crawler_ex00/%s/' % index[0]    
#     print url    
#     html=urllib.urlopen(url) .read()     
#     index=re.findall(r'数字是([0-9]{5})',html)    
    
# html=urllib.urlopen(url).read()     
# url='http://www.heibanke.com'+re.findall(r'<a href="(.*?)" class',html )[0]    
# print '最后通关的的网址是%s, 耗时%s' % (url,(datetime.datetime.now()-begin_time))    
# print 'just for test,是吧!'