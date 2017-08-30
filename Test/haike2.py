# coding:utf-8

import re
import urllib
import sys
reload(sys)
sys.setdefaultencoding("utf8")

url = 'http://www.heibanke.com/lesson/crawler_ex01/'
data = {'username':'sagewang'}

for x in xrange(1,31):
	data['password'] = x
	data['csrfmiddlewaretoken'] = 'qJcWyLWxfti4VCCVkifQJYElUE6aO9gr'
	post_data=urllib.urlencode(data)
	print post_data
	html = urllib.urlopen(url,post_data).read()
	result = re.findall('密码错误',html)
	if not result:
		print "闯关成功,下一关网址是：http://www.heibanke.com" + re.findall(r'<a href="(.*?)" class',html)[0]
		break