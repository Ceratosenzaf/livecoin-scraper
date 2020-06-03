# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from shutil import which


class CoinSpiderSelenium(scrapy.Spider):
    name = 'live_coin'
    allowed_domains = ['www.livecoin.net/en'] 
    start_urls = [
        'https://www.livecoin.net/en'
    ]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')

        chrome_path = which('chromedriver')

        driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get('https://www.livecoin.net/en')

        chioce_tab = driver.find_elements_by_class_name('filterPanelItem___2z5Gb')
        chioce_tab[4].click()

        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text=self.html)
        for currency in resp.xpath('//div[contains(@class, "ReactVirtualized__Table__row tableRow___3EtiS ")]'):
            yield {
                'pair': currency.xpath('.//div[1]/div/text()').get(),
                'volume 24h': currency.xpath('.//div[2]/span/text()').get(),
                'last price': currency.xpath('.//div[3]/span/text()').get(),
                'change 24h': currency.xpath('.//div[4]/span/span/text()').get(),
                'trade link': response.urljoin(currency.xpath('.//div[8]/a/@href').get())
            }
