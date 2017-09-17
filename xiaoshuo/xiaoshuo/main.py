# -*- coding: utf-8 -*-

from scrapy import cmdline

# cmdline.execute("scrapy crawl xxsy".split())
cmdline.execute("scrapy crawl qidian".split())
# cmdline.execute("scrapy crawl qidianmm".split())
# cmdline.execute("scrapy crawl zongheng".split())
# cmdline.execute("scrapy crawl chuangshi".split())
# cmdline.execute("scrapy crawl qidian".split())
# cmdline.execute("scrapy crawl dingdian -o dingdian.csv".split())
# from scrapy.cmdline import execute
# execute(['scrapy', 'crawl', 'dingdian'])
# 保存爬取到的数据
# cmdline.execute("scrapy crawl douban -o films.json".split())
# 保存成CSV,然后用EXCEL打开即可
# cmdline.execute("scrapy crawl douban -o items.csv -t csv".split())

