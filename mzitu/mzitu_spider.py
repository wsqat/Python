# -*- coding: utf-8 -*-
# 多进程+多线程的下载代码

from download import request
from mongodb_queue import MogoQueue
from bs4 import BeautifulSoup
import sys
reload(sys) # python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')

spider_queue = MogoQueue('meinvxiezhenji', 'crawl_queue')
def start(url):
    response = request.get(url, 3)
    Soup = BeautifulSoup(response.text, 'lxml')
    all_a = Soup.find('div', class_='all').find_all('a')
    for a in all_a:
        title = a.get_text()
        url = a['href']
        spider_queue.push(url, title)
        print(u'已经把 href: '+ url + ' 加入队列')
    """上面这个调用就是把URL写入MongoDB的队列了"""

if __name__ == "__main__":
    start('http://www.mzitu.com/all')

"""这一段儿就不解释了哦！超级简单的"""