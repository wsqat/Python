# -*- coding: utf-8 -*-

from scrapy import cmdline

cmdline.execute("scrapy crawl douban".split())
# 保存爬取到的数据
# cmdline.execute("scrapy crawl douban -o films.json".split())
# 保存成CSV,然后用EXCEL打开即可
# cmdline.execute("scrapy crawl douban -o items.csv -t csv".split())