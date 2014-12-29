# coding: utf-8


from xkcd.spiders.xkcd_info import XKCDSpider
from xkcd import pipelines


class XKCDDownloadSpider(XKCDSpider):
    """
    Spider like XKCDSpider, but with downloading power.
    Scrapes not only informations about images, also downloads them.

    """

    name = "xkcd_download"
    pipeline = set([pipelines.XKCDImagesPipeline, ])
