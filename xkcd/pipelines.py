# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline



class XKCDImagesPipeline(ImagesPipeline):
    def image_key(self, url):
        """ Returns url-name of image instead of SHA1 hash. """
        image_name = re.match(".+/(?P<name>.+.jpg|.jpeg|.gif|.png$)", url)

        return 'full/%s' % (image_name.group("name"))


    def get_media_requests(self, item, info):
        """
        Defines which spider gets normal pipeline process by
        looking at spider's pipeline attribute.
        """

        # if class isn't in the spider's pipeline, then forget about downloading
        if self.__class__ not in info.spider.pipeline:
            return

        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)


