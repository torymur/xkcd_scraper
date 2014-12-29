# coding: utf-8

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.loader import ItemLoader

from xkcd.items import XKCDItem


class XKCDSpider(CrawlSpider):
    """
    Defines spider's name, extractor's rules, domains,
    urls for start crawling xkcd.com
    """

    name = "xkcd_info"
    allowed_domains = ["xkcd.com"]
    start_urls = ["http://xkcd.com/1"]
    rules = [
        Rule(LinkExtractor(allow=["/\d+/"],
                        restrict_xpaths=["//ul[@class='comicNav']/li"]),
            callback="parse_xkcd",
            follow=True)]


    pipeline = set([])

    def parse_xkcd(self, response):
        """ Scrapes 'url', 'name', 'image_urls' """

        xkcdLoader = ItemLoader(item=XKCDItem(), response=response)
        xkcdLoader.add_value("url", response.url)
        xkcdLoader.add_xpath("name", "//div[@id='ctitle']/text()")
        xkcdLoader.add_xpath("image_urls", "//div[@id='middleContainer']/text()")

        return xkcdLoader.load_item()

