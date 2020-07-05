# -*- coding: utf-8 -*-
from spiders.items import SpidersItem
from scrapy.selector import Selector
import scrapy
import lxml


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def parse(self, response):
        item = SpidersItem()
        item_list = Selector(response=response).xpath(
            '//div[@class="movie-item-hover"]')
        try:
            for items in item_list[:10]:
                name = items.xpath('./a/div/div[1]/span[1]/text()').extract()[0]
                tag = items.xpath(
                    './a/div/div[2]/text()').extract()[1].strip('\n')
                time = items.xpath(
                    './a/div/div[4]/text()').extract()[1].strip('\n')
                link = items.xpath('./a/@href').get()
                item['name'] = name
                item['link'] = "htttps://maoyan.com" + link
                item['tag'] = tag
                item['time'] = time
        except Exception as ex:
            print(ex)
            # print(item)
        finally:
            yield item

