# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request
from settings import IMAGES_STORE


# 这里写了两个管道，一个是把下载链接保存到文件，一个是下载图片

class TtmeijuPipeline(object):
    def process_item(self, item, spider):
        return item


class WriteToFilePipeline(object):
    def process_item(self, item, spider):
        item = dict(item)
        FolderName = item['name'][0].replace('/', '')
        downloadFile = 'download_urls.txt'
        with open(os.path.join(IMAGES_STORE, FolderName, downloadFile), 'w') as file:
            for name, url in zip(item['episode'], item['episode_url']):
                file.write('{name}: {url}\n'.format(name=name, url=url))
        return item


# get_media_requests和item_completed，因为默认的图片储存路径是
# <IMAGES_STORE>/full/3afec3b4765f8f0a07b78f98c07b83f013567a0a.jpg，
# 我需要把full改成以美剧名字目录来保存，所以重写了file_path

class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            print "piplines.py image_urls: " + image_url
            yield Request(image_url, meta={'item': item})
            # yield Request(image_url, headers = {'Referer': item['header_referer']})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        FolderName = item['name'][0].replace('/', '')
        image_guid = request.url.split('/')[-1]
        filename = u'{}/{}'.format(FolderName, image_guid)
        return filename