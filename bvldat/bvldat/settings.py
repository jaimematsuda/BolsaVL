# -*- coding: utf-8 -*-

# Scrapy settings for bvldat project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import sys
sys.path.insert(0, '/home/spart4kus/Proyectos/bvl/bvlweb')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'bvlweb.settings'

BOT_NAME = 'bvldat'

SPIDER_MODULES = ['bvldat.spiders']
NEWSPIDER_MODULE = 'bvldat.spiders'

ITEM_PIPELINES = {
    'bvldat.pipelines.BvldatPipeline': 1000,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bvldat (+http://www.yourdomain.com)'
