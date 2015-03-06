# -*- coding: utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy import Spider
from avaSpider.items import AvaspiderItem


class LinksSpider(Spider):
    name = "links"
    allowed_domains = ["dpchallange.com"]
    start_urls = (
            'http://www.dpchallenge.com/photo_gallery.php?GALLERY_ID=17',
            )
    base_url =  'http://www.dpchallenge.com/photo_gallery.php?GALLERY_ID=17&page=%d'

    def  start_requests(self):
    	for i in range(1,667,1):
    		yield Request(self.base_url % i , callback=self.parse)

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//table[@width="100%"]//td[@align="center"]')
        result = []
        for title in titles:
            tmp = AvaspiderItem()
            tmp ["url"] = title.select("a/@href").extract() [0] 
            result.append(tmp)
        return (result)
