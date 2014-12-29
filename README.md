xkcd Scraper
============

Pretty small Scrapy project that helps enjoy http://xkcd.com locally. 

Was made mostly for cursory examination Scrapy as a tool and brief diving in web scraping in general.

Spiders
=========
Project contains:
* xkcd_info - collects main information about every comic image: url, name, image_url
* xkcd_download - not only collects information like 'xkcd_info' spider, also downloads all comic images

How-To
======
How to tame [Scrapy](http://doc.scrapy.org/en/latest/intro/tutorial.html)

For running spiders and store the scraped data in json (for example):

```scrapy crawl xkcd_info -o xkcd_data.json``` - collects image info

```scrapy crawl xkcd_download -o xkcd_data.json``` - collects info + downloads images

