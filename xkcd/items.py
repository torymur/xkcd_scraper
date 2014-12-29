# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


from scrapy import Item, Field
from scrapy.contrib.loader.processor import MapCompose, TakeFirst
import re


def filter_empty(value):
    """ Filters empty values """
    v = value.strip()
    if v:
        return v


def filter_image_links(value):
    """
    Filters only direct image links
    Like 'http://imgs.xkcd.com/comics/canyon_small.jpg'

    """

    for link in re.findall("https?://[^\s]+.jpg|.jpeg|.gif|.png$", value):
        if link:
            return link



class XKCDItem(Item):
    url = Field(
        output_processor=TakeFirst())
    name = Field(
        output_processor=TakeFirst())
    image_urls = Field(
        input_processor=MapCompose(filter_empty, filter_image_links),)


