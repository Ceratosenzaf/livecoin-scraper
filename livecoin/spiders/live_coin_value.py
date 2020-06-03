# -*- coding: utf-8 -*-
import scrapy

class LiveCoinValueSpider(scrapy.Spider):
    name = 'live_coin_value'
    allowed_domains = ['www.livecoin.net']
    start_urls = ['https://www.livecoin.net/en/']

    def parse(self, response):
        pass
