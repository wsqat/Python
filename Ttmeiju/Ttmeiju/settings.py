# -*- coding: utf-8 -*-

# Scrapy settings for Ttmeiju project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os # add by sagewang

BOT_NAME = 'Ttmeiju'

SPIDER_MODULES = ['Ttmeiju.spiders']
NEWSPIDER_MODULE = 'Ttmeiju.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Ttmeiju (+http://www.yourdomain.com)'
# add by sagewang begin
# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
# IPPOOL=[
#     {"ipaddr":"61.129.70.131:8080"},
#     {"ipaddr":"61.152.81.193:9100"},
#     {"ipaddr":"120.204.85.29:3128"},
#     {"ipaddr":"219.228.126.86:8123"},
#     {"ipaddr":"61.152.81.193:9100"},
#     {"ipaddr":"218.82.33.225:53853"},
#     {"ipaddr":"223.167.190.17:42789"}
# ]

# add by sagewang end

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
# modify by sagewang 让scrapy不要遵守robot协议，之后就能正常爬取了
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# modified by sagewang 爬取间隔
# DOWNLOAD_DELAY = 3
DOWNLOAD_DELAY = 1

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# modified by sagewang 用cookie
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# modified by sagewang 重写默认请求头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html, application/xhtml+xml, application/xml',
#   'Accept-Language': 'zh-CN,zh;q=0.8',
#   'Host':'cn163.net',
#   'Referer':'http://cn163.net/',
#   'X-XHR-Referer':'http://cn163.net/'
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Ttmeiju.middlewares.TtmeijuSpiderMiddleware': 543,
#}

# modified by sagewang for add IPPOOL
# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

# modified by sagewang 激活自定义UserAgent和代理IP
DOWNLOADER_MIDDLEWARES = {
   # 'Ttmeiju.middlewares.MyCustomDownloaderMiddleware': 553,
   #  'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 543,
   #  'Ttmeiju.middlewares.MyproxiesSpiderMiddleware': 125
   #  'Ttmeiju.useragent.UserAgent': 1,
   #  'Ttmeiju.proxymiddlewares.ProxyMiddleware': 100,
   #  'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Ttmeiju.pipelines.TtmeijuPipeline': 300,
#}

# add by sagewang
ITEM_PIPELINES = {
    # 'Ttmeiju.pipelines.IpProxyPoolPipeline': 300,
    'Ttmeiju.pipelines.WriteToFilePipeline': 3,
    'Ttmeiju.pipelines.MyImagesPipeline': 1,
}
# 图片存储路径
IMAGES_STORE = os.path.join(os.getcwd(), 'image')
#自定义存储imageurl的字段,item["image_urls"]
# IMAGES_URL_FILED = "image_urls"

IMAGES_EXPIRES = 90
IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
