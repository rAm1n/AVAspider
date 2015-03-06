# -*- coding: utf-8 -*-

# Scrapy settings for avaSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'avaSpider'

SPIDER_MODULES = ['avaSpider.spiders']
NEWSPIDER_MODULE = 'avaSpider.spiders'

ITEM_PIPELINES = ['avaSpider.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "AVA"
MONGODB_COLLECTION = "images"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'avaSpider (+http://www.yourdomain.com)'
