# coding:utf-8

import re
import urllib
from selenium import webdriver
import time

dr = webdriver.PhantomJS()
dr.get('https://baidu.com')
data = dr.page_source
print data
time.sleep(5)
print 'Browser will close'
dr.quit()
print 'Browser closed'