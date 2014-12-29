# -*- coding: utf-8 -*-

# Scrapy settings for test_project project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'xkcd'

SPIDER_MODULES = ['xkcd.spiders']
NEWSPIDER_MODULE = 'xkcd.spiders'

ITEM_PIPELINES = {'xkcd.pipelines.XKCDImagesPipeline': 1}
IMAGES_STORE = 'xkcd/images'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'test_project (+http://www.yourdomain.com)'
